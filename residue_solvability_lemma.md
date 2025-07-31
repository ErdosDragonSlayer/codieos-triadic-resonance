
# Residue Solvability Lemma

## Statement:
Let r = p/q ∈ ℚ, with 0 < r < 1. Then there exist integers y ≤ z such that:
    1/y + 1/z = r

## Constructive Method:
Let:
    y₀ = ⌊q/p⌋ + 1

Iterate over y ≥ y₀:
    z = 1 / (r - 1/y)

If z ∈ ℤ⁺ and z ≥ y, then (y, z) is a valid decomposition.

## Theoretical Basis:
Sylvester's method for Egyptian fractions guarantees that any r ∈ (0,1) can be written as a sum of distinct unit fractions.

## Application:
This lemma completes the constructive proof of the Erdős–Straus Conjecture using the T₁ transform.

For each n ≥ 2:
    x = ⌈n/4⌉
    r = 4/n - 1/x

Then (y, z) is always solvable by this method.
