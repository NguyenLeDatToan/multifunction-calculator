from __future__ import annotations
from fractions import Fraction
from decimal import Decimal, getcontext
from typing import Tuple, List, Union

import sympy as sp

# Set higher precision for Decimal operations
getcontext().prec = 28

NumberLike = Union[int, float, str, Decimal]


def _to_decimal(x: NumberLike) -> Decimal:
    if isinstance(x, Decimal):
        return x
    if isinstance(x, str):
        return Decimal(x)
    return Decimal(str(x))


def _to_fraction(x: NumberLike) -> Fraction:
    if isinstance(x, Fraction):
        return x
    if isinstance(x, str):
        return Fraction(x)
    # Use string to avoid float binary issues
    return Fraction(str(x)).limit_denominator()


# 1) Giải tỷ lệ: a/b = c/x -> x

def solve_proportion(a: NumberLike, b: NumberLike, c: NumberLike) -> Fraction:
    """Giải tỉ lệ a/b = c/x và trả về x là Fraction tối giản.

    x = (b * c) / a
    """
    a_f = _to_fraction(a)
    b_f = _to_fraction(b)
    c_f = _to_fraction(c)
    if a_f == 0:
        raise ZeroDivisionError("a must not be 0 in proportion a/b = c/x")
    x = (b_f * c_f) / a_f
    return Fraction(x.numerator, x.denominator)


# 2) Giải phương trình tìm x từ chuỗi, ví dụ: "2x + 3 = 11"

def solve_for_x(equation_str: str) -> List[sp.Expr]:
    """Giải phương trình một ẩn x từ chuỗi.

    Hỗ trợ dạng "expr = expr" hoặc nếu không có '=', hiểu là expr = 0.
    Trả về danh sách nghiệm (có thể rỗng).
    """
    x = sp.symbols('x')
    if '=' in equation_str:
        left, right = equation_str.split('=', 1)
        left_expr = sp.sympify(left)
        right_expr = sp.sympify(right)
        eq = sp.Eq(left_expr, right_expr)
    else:
        eq = sp.Eq(sp.sympify(equation_str), 0)
    solutions = sp.solve(eq, x)
    return solutions


# 3) Nhân tử / rút gọn căn bậc hai

def simplify_sqrt(n: NumberLike) -> sp.Expr:
    """Rút gọn căn bậc hai, ví dụ: 8 -> 2*sqrt(2)."""
    expr = sp.sqrt(sp.Integer(n) if isinstance(n, int) else sp.sympify(n))
    return sp.simplify(expr)


def multiply_square_roots(a: NumberLike, b: NumberLike) -> sp.Expr:
    """Tính và rút gọn sqrt(a) * sqrt(b) = sqrt(a*b)."""
    expr = sp.sqrt(sp.sympify(a)) * sp.sqrt(sp.sympify(b))
    return sp.simplify(expr)


# 4) Chuyển đổi số thập phân ⇄ phân số ⇄ phần trăm

def decimal_to_fraction_and_percent(x: NumberLike) -> Tuple[Fraction, Decimal]:
    """Từ thập phân -> (phân số, phần trăm)

    Trả về:
      - Fraction tối giản
      - Decimal phần trăm (ví dụ 12.5 nghĩa là 12.5%)
    """
    dec = _to_decimal(x)
    frac = _to_fraction(dec)
    percent = (dec * Decimal(100))
    return frac.limit_denominator(), +percent  # unary + to apply context


def fraction_to_decimal_and_percent(numer: NumberLike, denom: NumberLike) -> Tuple[Decimal, Decimal]:
    """Từ phân số -> (thập phân, phần trăm)."""
    numer_d = _to_decimal(numer)
    denom_d = _to_decimal(denom)
    if denom_d == 0:
        raise ZeroDivisionError("denominator must not be 0")
    dec = numer_d / denom_d
    percent = dec * Decimal(100)
    return +dec, +percent


def percent_to_decimal_and_fraction(pct: NumberLike) -> Tuple[Decimal, Fraction]:
    """Từ phần trăm -> (thập phân, phân số). Chấp nhận chuỗi như '12.5%' hoặc '12.5'."""
    if isinstance(pct, str) and pct.strip().endswith('%'):
        value = pct.strip()[:-1]
    else:
        value = pct
    dec = _to_decimal(value) / Decimal(100)
    frac = _to_fraction(dec)
    return +dec, frac.limit_denominator()


__all__ = [
    'solve_proportion',
    'solve_for_x',
    'simplify_sqrt',
    'multiply_square_roots',
    'decimal_to_fraction_and_percent',
    'fraction_to_decimal_and_percent',
    'percent_to_decimal_and_fraction',
]
