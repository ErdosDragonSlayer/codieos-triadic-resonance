# CodieOS Triadic Resonance Engine v2
# Author: Robbie Robertson + CodieOS AI Collaboration
# Description: A verified constructive engine (not a proof) for the Erdős-Straus Conjecture

from fractions import Fraction
import csv
import math


def is_unit_fraction(x):
    return x.denominator == 1 and x.numerator == 1


def solve_erdos_straus(n, max_x_shift=100):
    for shift in range(max_x_shift):
        x = math.ceil(n / 4) + shift
        r = Fraction(4, n) - Fraction(1, x)

        if r <= 0:
            continue  # skip invalid residue

        # Try to decompose r into two unit fractions
        y = math.ceil(1 / r)
        r2 = r - Fraction(1, y)
        if r2 <= 0:
            continue

        z = math.ceil(1 / r2)

        # Check solution validity
        total = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        if total == Fraction(4, n):
            tier = "T1" if shift == 0 else "T3"
            return {
                "n": n,
                "x": x,
                "y": y,
                "z": z,
                "tier": tier,
                "method": "T1 + Sylvester" if shift == 0 else f"Iterative fallback (x_shift={shift})",
                "status": "success"
            }

    # T4: Apply known modular identities
    # Identity for n ≡ 3 (mod 4)
    if n % 4 == 3:
        x = (n + 1) // 4
        y = n * (n + 1) // 2
        z = y
        total = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        if total == Fraction(4, n):
            return {
                "n": n,
                "x": x,
                "y": y,
                "z": z,
                "tier": "T4",
                "method": "Modular identity (n ≡ 3 mod 4)",
                "status": "success"
            }

    # Identity for n ≡ 1 (mod 2)
    if n % 2 == 1:
        x = (n + 1) // 2
        y = n * (n + 1) // 2
        z = y
        total = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        if total == Fraction(4, n):
            return {
                "n": n,
                "x": x,
                "y": y,
                "z": z,
                "tier": "T4",
                "method": "Modular identity (n ≡ 1 mod 2)",
                "status": "success"
            }

    # T5: Failure logging with diagnostic info
    return {
        "n": n,
        "x": None,
        "y": None,
        "z": None,
        "tier": "T5",
        "method": "Failed (rational residue or no matching identity)",
        "status": "failure"
    }


# Run batch and export CSV
def run_batch(start, end, filename="triadic_results_v2.csv"):
    tier_stats = {"T1": 0, "T3": 0, "T4": 0, "T5": 0}
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["n", "x", "y", "z", "tier", "method", "status"])
        writer.writeheader()
        for n in range(start, end + 1):
            result = solve_erdos_straus(n)
            tier_stats[result["tier"]] += 1
            writer.writerow(result)
    print("Batch completed: results saved to triadic_results_v2.csv")
    print("Tier Summary:")
    for tier, count in tier_stats.items():
        print(f"  {tier}: {count} cases")


# Example test run
if __name__ == "__main__":
    run_batch(2, 10000000)
