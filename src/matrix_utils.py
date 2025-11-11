"""Matrix utilities built on top of NumPy.

中文说明：示例函数展示如何用 NumPy 进行矩阵加法，便于学习数组运算。
"""

from __future__ import annotations

from typing import Sequence

import numpy as np


def add_matrices(
    left: Sequence[Sequence[float]],
    right: Sequence[Sequence[float]],
) -> np.ndarray:
    """Return element-wise sum of two matrices.

    中文说明：接收可迭代的二维序列（列表/元组/NumPy 数组都可以），内部转换成 ndarray 并逐元素相加。
    """

    # 中文提示：np.asarray 不会强制复制数据，可兼容列表或 ndarray。
    left_arr = np.asarray(left, dtype=np.float64)
    right_arr = np.asarray(right, dtype=np.float64)

    if left_arr.shape != right_arr.shape:
        raise ValueError("Matrices must share the same shape for addition.")

    # 中文提示：NumPy 支持广播加法，这里通过 shape 校验确保是标准矩阵逐元素相加。
    return left_arr + right_arr
