from __future__ import annotations

import math

# 中文提示：这里导入未来注解特性，保证类型注解在 Python 3.11+ 中更灵活。


def get_message(name: str) -> str:
    """Return a friendly greeting.

    中文说明：返回一条友好的问候语，输入名字为空时会自动替换为默认值。
    """

    # 中文提示：strip 去掉字符串两端的空白；若结果为空字符串，则用 "there" 作为兜底。
    cleaned = name.strip() or "there"
    # 中文提示：使用 f-string 拼接最终消息，更易读也更高效。
    return f"Hello, {cleaned}! Welcome to your Python project."


def calculate_sine(angle_radians: float) -> float:
    """Return the sine value of a radian angle.

    中文说明：接收弧度制角度，利用 math.sin 计算其正弦值。
    """

    # 中文提示：math.sin 需要弧度输入，若用户有角度制可先用 math.radians 转换。
    return math.sin(angle_radians)


def degrees_to_radians(angle_degrees: float) -> float:
    """Convert degrees to radians.

    中文说明：角度制转弧度制，内部调用 math.radians，方便和三角函数配合使用。
    """

    return math.radians(angle_degrees)


def radians_to_degrees(angle_radians: float) -> float:
    """Convert radians to degrees.

    中文说明：弧度制转角度制，内部使用 math.degrees，便于输出更直观的角度数值。
    """

    return math.degrees(angle_radians)


def main() -> None:
    # 中文提示：main 函数作为程序入口，示范如何调用 get_message。
    print(get_message("Codex"))
    # 中文提示：演示计算 90 度（π/2 弧度）的正弦值，结果应接近 1。
    print(f"sin(pi/2) = {calculate_sine(math.pi / 2):.2f}")
    # 中文提示：展示角度与弧度之间的转换。
    print(f"90° -> {degrees_to_radians(90):.2f} rad")
    print(f"π/2 rad -> {radians_to_degrees(math.pi / 2):.1f}°")


if __name__ == "__main__":
    # 中文提示：仅在直接运行本文件时才执行 main，便于测试与复用。
    main()
