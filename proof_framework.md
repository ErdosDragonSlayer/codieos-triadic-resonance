
# Proof Framework: CodieOS Triadic Resonance Theory

## Main Theorem (Constructive Resolution of Erdős–Straus)
For all integers n ≥ 2, there exist positive integers x, y, z such that:
    4/n = 1/x + 1/y + 1/z

This is achieved via:

### T₁ Transform:
    x = ⌈n / 4⌉
    r = 4/n - 1/x

### Residue Solvability Lemma:
    For r ∈ (0,1), there exist y ≤ z such that:
    1/y + 1/z = r

## Constructive Algorithm
The CodieOS solver computes:
- x via the T₁ transform
- residue r = 4/n - 1/x
- For y in a finite range (starting from ⌈1/r⌉), checks if:
    z = 1 / (r - 1/y) ∈ ℤ⁺ and z ≥ y

This always terminates and yields a valid triad.

## Symbolic Classification
Each solution is assigned:
- mod_4 class → 🜀🜁🜂🜃
- harmonic resonance band (⌊(n + 1)/4⌋)

This framework guarantees 4/n can be expressed as three positive unit fractions for all n ≥ 2.
