import numpy as np
import numpy.testing as npt

from src import matrix_utils

# 中文提示：这些测试展示矩阵加法的典型场景与异常情况。


def test_add_matrices_basic():
    """Ensure two 2x2 matrices add element-wise."""

    left = [[1, 2], [3, 4]]
    right = [[5, 6], [7, 8]]
    result = matrix_utils.add_matrices(left, right)

    # 中文断言：预期结果为逐元素相加后的矩阵。
    npt.assert_array_equal(result, np.array([[6, 8], [10, 12]], dtype=np.float64))


def test_add_matrices_accepts_numpy_arrays():
    """Verify function works with ndarray inputs."""

    left = np.array([[12.0, 23.3], [7.1, 14.9]])
    right = np.ones((2, 2))
    result = matrix_utils.add_matrices(left, right) # type: ignore
    print(result)
    npt.assert_array_equal(result, np.array([[2.0, 2.0], [2.0, 2.0]]))


def test_add_matrices_shape_mismatch():
    """Expect ValueError when shapes differ."""

    left = [[1, 2]]
    right = [[1, 2], [3, 4]]

    try:
        matrix_utils.add_matrices(left, right)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for mismatched shapes.")
