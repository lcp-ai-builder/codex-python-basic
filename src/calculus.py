"""Utility helpers for basic calculus operations.

中文说明：包含一些基础微积分函数，方便初学者练习，例如数值求导。
"""

from __future__ import annotations

from typing import Callable


def numerical_derivative(
    func: Callable[[float], float],
    x: float,
    h: float = 1e-6,
) -> float:
    """Approximate the derivative of `func` at `x`.

    中文说明：使用对称差分公式求导，h 越小结果越精确，但过小会受浮点误差影响。
    """

    if h <= 0:
        raise ValueError("Step size h must be positive.")

    # 中文提示：中心差分公式 (f(x+h) - f(x-h)) / (2h) 具有较好的精度与稳定性。
    return (func(x + h) - func(x - h)) / (2 * h)
