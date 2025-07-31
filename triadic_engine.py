
from fractions import Fraction
from math import ceil

def determine_band(n):
    return 0 if n == 2 else (n + 1) // 4

ELEMENTAL_GLYPHS = {0: "🜀", 1: "🜁", 2: "🜂", 3: "🜃"}

def codieos_triadic_resonance_engine(n):
    try:
        x = ceil(n / 4)
        residue = Fraction(4, n) - Fraction(1, x)
        if residue <= 0:
            return None
        min_y = max(x, int(1 / float(residue)) + 1)
        max_y = 10 * x * x
        for y in range(min_y, max_y):
            remaining = residue - Fraction(1, y)
            if remaining <= 0:
                continue
            z_num = remaining.denominator
            z_den = remaining.numerator
            if z_den > 0 and z_num % z_den == 0:
                z = z_num // z_den
                if z >= y:
                    verification = Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                    if verification == Fraction(4, n):
                        return {
                            "n": n,
                            "x": x,
                            "y": y,
                            "z": z,
                            "mod_4": n % 4,
                            "glyph": ELEMENTAL_GLYPHS[n % 4],
                            "band": determine_band(n)
                        }
    except:
        pass
    return None
