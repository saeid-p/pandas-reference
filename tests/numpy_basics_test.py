import numpy as np  # https://numpy.org/doc/stable/user/quickstart.html


def random_numbers_test():
    random_array = np.random.rand(5)
    assert len(random_array) == 5


def array_processing_test():
    # https://numpy.org/doc/stable/user/basics.creation.html
    a1D = np.array([1, 2, 3, 4])
    b1D = np.array([3, 1, 2, 5])
    c1D = a1D + b1D
    np.testing.assert_array_equal(np.array(c1D), [4, 3, 5, 9])

    a2D = np.array([[1, 2], [3, 4]])
    assert len(a2D) == 2

    a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    assert len(a3D) == 2

    array_range = np.arange(10)
    assert len(array_range) == 10
