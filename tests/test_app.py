import math

from src import app

# 中文提示：测试文件命名以 test_ 开头，pytest 会自动发现并运行。


def test_get_message_default():
    """Verify fallback behavior when blank input is provided."""

    # 中文断言：传入空字符串时应得到默认问候语。
    assert app.get_message("") == "Hello, there! Welcome to your Python project."


def test_get_message_strips_whitespace():
    """Ensure leading and trailing whitespace is cleaned up."""

    # 中文断言：前后带空格的名字会被 strip，最终问候语中只保留核心名字。
    assert (
        app.get_message("  Codex  ")
        == "Hello, Codex! Welcome to your Python project."
    )


def test_calculate_sine_pi_over_two():
    """Check that sine calculation matches math.sin for pi/2."""

    # 中文断言：π/2 的正弦值应该接近 1，使用 math.isclose 处理浮点误差。
    assert math.isclose(app.calculate_sine(math.pi / 2), 1.0, rel_tol=1e-9)


def test_degrees_to_radians():
    """Ensure degree-to-radian conversion follows math.radians."""

    # 中文断言：180 度应该等于 π 弧度。
    assert math.isclose(app.degrees_to_radians(180.0), math.pi, rel_tol=1e-9)


def test_radians_to_degrees():
    """Ensure radian-to-degree conversion follows math.degrees."""

    # 中文断言：π/2 弧度应转换成 90 度。
    assert math.isclose(
        app.radians_to_degrees(math.pi / 2),
        90.0,
        rel_tol=1e-9,
    )
