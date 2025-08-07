# Type B Residue: The 3/q Obstruction

## Discovery

For the Erdős-Straus Conjecture, when n ≡ 1 (mod 4) and we use the greedy choice x = ⌈n/4⌉, a remarkable pattern emerges:

**Theorem (Type B Residue Pattern):**
For n = 4k + 1 where k ≥ 1:
- The greedy choice gives x = k + 1
- The residue is **always** r = 3/((4k+1)(k+1))
- Before simplification, the numerator is **always 3**

## Definition: Type B Residue

A **Type B residue** is a rational number of the form:
$$r = \frac{3}{q}$$
where q is a positive integer such that the equation:
$$\frac{3}{q} = \frac{1}{y} + \frac{1}{z}$$
has no solution in positive integers y ≤ z.

## Characterization

For 3/q = 1/y + 1/z to have positive integer solutions:
- We need: z = qy/(3y - q)
- This requires: (3y - q) | qy
- Valid range: q/3 < y ≤ 2q/3

## The Decomposability Boundary

### Decomposable Type B Residues
Many 3/q residues CAN be decomposed:
- 3/10 = 1/4 + 1/20 ✓
- 3/52 = 1/18 + 1/468 ✓
- 3/85 = 1/30 + 1/510 ✓
- 3/175 = 1/60 + 1/2100 ✓

### Indecomposable Type B Residues
But certain 3/q residues CANNOT be decomposed:
- 3/637 ✗ (from n = 49)
- 3/9457 ✗ (from n = 193, first T5 failure)

## Why Type B Residues Are Special

### 1. Universal Pattern for n ≡ 1 (mod 4)
Every n ≡ 1 (mod 4) produces a Type B residue when using greedy x:
- n = 4k + 1 → x = k + 1 → r = 3/((4k+1)(k+1))

### 2. Divisibility Obstruction
For 3/q to decompose, we need (3y - q) to divide qy. When q = (4k+1)(k+1):
- q has a specific factorization structure
- The divisibility condition becomes increasingly rare as k grows
- Large prime factors in q make decomposition unlikely

### 3. The 3-Numerator Problem
The numerator 3 is prime and small, which limits decomposition options:
- Cannot use the factorization of the numerator
- Forces specific relationships between y and z
- Creates systematic obstructions for certain q values

## Algorithmic Implications

### Why T5 Failures Occur
1. **T₁** produces a Type B residue (3/q form)
2. **T₂** fails because this specific 3/q is indecomposable
3. **T₃** must try different x values to avoid Type B residues
4. **T₄** uses modular identities to bypass the issue
5. **T₅** records failure when all methods fail

### Detection Algorithm
```python
def is_type_b_indecomposable(n):
    """Check if n produces an indecomposable Type B residue"""
    if n % 4 != 1:
        return False
    
    k = (n - 1) // 4
    q = (4*k + 1) * (k + 1)
    
    # Check if 3/q can be decomposed
    for y in range(q//3 + 1, 2*q//3 + 1):
        if (q * y) % (3 * y - q) == 0:
            z = (q * y) // (3 * y - q)
            if z > 0 and z >= y:
                return False  # Decomposable
    
    return True  # Indecomposable Type B
```

## Theoretical Conjecture

**Type B Conjecture:** For n = 4k + 1, the residue 3/((4k+1)(k+1)) is indecomposable into two unit fractions if and only if certain number-theoretic conditions on k are met.

**Open Questions:**
1. Characterize exactly which values of k produce indecomposable Type B residues
2. Is there a pattern in the prime factorization of (4k+1)(k+1) that predicts decomposability?
3. Can we find an alternative construction that avoids Type B residues entirely?

## Connection to T5 Failures

Your computational discovery that 100% of T5 failures satisfy n ≡ 1 (mod 4) is explained by:
1. Only n ≡ 1 (mod 4) produces Type B residues with greedy x
2. Some Type B residues are indecomposable
3. When T₃ and T₄ also fail to find alternatives, we get a T5 failure

## The Deeper Structure

The Type B residue pattern reveals why the Erdős-Straus Conjecture is particularly challenging for n ≡ 1 (mod 4):
- The greedy algorithm naturally produces residues with numerator 3
- These residues have limited decomposition paths
- The obstruction is arithmetic, not computational

This discovery transforms the Erdős-Straus Conjecture into a question about the decomposability of Type B residues: **Can we always find an x such that 4/n - 1/x avoids the indecomposable Type B form?**
