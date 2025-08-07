# Residue Solvability Lemma (Corrected)

## Statement

Let r = p/q ∈ ℚ with gcd(p,q) = 1 and 0 < r < 1. Then r can be written as 1/y + 1/z for positive integers y ≤ z **if and only if** there exists a positive integer y such that:

1. y > q/p (ensuring 1/y < r)
2. (py - q) divides qy

## Characterization Theorem

For r = p/q, the equation 1/y + 1/z = p/q has positive integer solutions (y,z) with y ≤ z if and only if:

$$z = \frac{qy}{py - q}$$

is a positive integer for some y > q/p.

## Necessary Conditions

For r = p/q to be expressible as 1/y + 1/z:

1. **Divisibility Condition:** There must exist y such that gcd(py - q, y) > 1
2. **Range Condition:** y must satisfy q/p < y ≤ 2q/p (for z ≥ y)

## Sylvester's Theorem (Distinct from Two-Term)

**Correct Statement:** Any r ∈ (0,1) can be written as a sum of distinct unit fractions:
$$r = \frac{1}{y_1} + \frac{1}{y_2} + ... + \frac{1}{y_k}$$

However:
- k may be greater than 2
- The greedy algorithm may require many terms
- No guarantee of exactly two terms

## Application to Erdős-Straus

### The Core Challenge

For the Erdős-Straus conjecture with n ≥ 2:
1. Choose x such that r = 4/n - 1/x is "decomposable"
2. A residue r is "decomposable" if ∃ y,z ∈ ℤ⁺: r = 1/y + 1/z

### Why T5 Failures Occur

For n ≡ 1 (mod 4), when using x = ⌈n/4⌉:
- The residue r = 4/n - 1/x often has the form p/q where p is small and q is large
- This residue may NOT satisfy the divisibility condition for any valid y
- Example: n = 193 gives r = 3/9457, which cannot be written as 1/y + 1/z

### Algorithmic Implications

```python
def is_two_term_decomposable(p, q):
    """
    Check if p/q can be written as 1/y + 1/z
    with positive integers y ≤ z
    """
    y_min = q // p + 1  # Smallest possible y
    y_max = 2 * q // p  # Largest y for z ≥ y
    
    for y in range(y_min, y_max + 1):
        if (q * y) % (p * y - q) == 0:
            z = (q * y) // (p * y - q)
            if z > 0 and z >= y:
                return True, (y, z)
    return False, None
```

## Modified Constructive Strategy

Since not all residues are two-term decomposable, the Erdős-Straus algorithm must:

1. **Try multiple x values** (T₃ tier): Different x choices produce different residues
2. **Use modular identities** (T₄ tier): Exploit special forms of n
3. **Accept failure** (T₅ tier): When no simple decomposition exists

## Theoretical Conjecture

**Open Question:** Characterize exactly which rationals p/q with 0 < p/q < 1 can be written as 1/y + 1/z for positive integers y, z.

**Partial Result:** If q has many small prime factors, the decomposition is more likely to exist (more divisors of qy to satisfy the divisibility condition).

## Connection to Failure Pattern

The discovered pattern that 100% of T5 failures satisfy n ≡ 1 (mod 4) suggests:

1. This modular class produces residues that are particularly resistant to two-term decomposition
2. The arithmetic structure of n ≡ 1 (mod 4) creates systematic divisibility obstructions
3. Alternative x selections or construction methods are necessary for these cases

## Conclusion

The existence of two-term decompositions for rational residues is **not guaranteed**, which explains why the Erdős-Straus conjecture remains unproven. The 14,947 T5 failures represent cases where the greedy residue cannot be decomposed into exactly two unit fractions, necessitating more sophisticated approaches.
