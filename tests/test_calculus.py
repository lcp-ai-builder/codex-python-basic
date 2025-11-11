import math

from src import calculus

# 中文提示：这些测试验证 numerical_derivative 在常见函数上表现正常。


def test_derivative_of_square():
    """f(x) = x^2 的导数是 2x，x=3 时应为 6。"""

    result = calculus.numerical_derivative(lambda x: x**2, 3.0)
    assert math.isclose(result, 6.0, rel_tol=1e-5)


def test_derivative_of_sine():
    """f(x)=sin(x) 的导数是 cos(x)，x=0 时应为 1。"""

    result = calculus.numerical_derivative(math.sin, 0.0)
    assert math.isclose(result, 1.0, rel_tol=1e-5)


def test_invalid_step_size():
    """h 必须为正数，否则抛出 ValueError。"""

    try:
        calculus.numerical_derivative(math.sin, 0.0, h=-1.0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for non-positive h.")
