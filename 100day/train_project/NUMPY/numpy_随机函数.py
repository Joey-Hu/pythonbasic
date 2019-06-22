#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: numpy_随机函数.py
# @time: 2019/6/7 15:57
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np

# 1.全1数列
nd = np.ones(shape=(5, 4), dtype=np.int8)
'''
 Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: C
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.

    Returns
    -------
    out : ndarray
        Array of ones with the given shape, dtype, and order.

'''
print(nd)

'''
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
'''
# 2. 全0数列
nd2 = np.zeros(shape=(2, 3, 4), dtype=np.float16)
'''
Parameters
        ----------
        shape : int or tuple of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.
        order : {'C', 'F'}, optional, default: 'C'
            Whether to store multi-dimensional data in row-major
            (C-style) or column-major (Fortran-style) order in
            memory.
    
        Returns
        -------
        out : ndarray
            Array of zeros with the given shape, dtype, and order.
'''
print(nd2)
'''
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
'''
# 3. 全值（给定）数列
nd3 = np.full(shape=(3, 5), fill_value=np.inf)
'''
def full(shape, fill_value, dtype=None, order='C'):
    """
    Return a new array of given shape and type, filled with `fill_value`.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    fill_value : scalar
        Fill value.
    dtype : data-type, optional
        The desired data-type for the array  The default, `None`, means
         `np.array(fill_value).dtype`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.

    Returns
    -------
    out : ndarray
        Array of `fill_value` with the given shape, dtype, and order.

'''
print(nd3)
'''
[[inf inf inf inf inf]
 [inf inf inf inf inf]
 [inf inf inf inf inf]]

'''
# 4. 对角数列
nd4 = np.eye(N=5, k=-1)
'''
def eye(N, M=None, k=0, dtype=float, order='C'):
    """
    Return a 2-D array with ones on the diagonal and zeros elsewhere.

    Parameters
    ----------
    N : int
      Number of rows in the output.
    M : int, optional
      Number of columns in the output. If None, defaults to `N`.
    k : int, optional
      Index of the diagonal: 0 (the default) refers to the main diagonal,
      a positive value refers to an upper diagonal, and a negative value
      to a lower diagonal.
    dtype : data-type, optional
      Data-type of the returned array.
    order : {'C', 'F'}, optional
        Whether the output should be stored in row-major (C-style) or
        column-major (Fortran-style) order in memory.

        .. versionadded:: 1.14.0

    Returns
    -------
    I : ndarray of shape (N,M)
      An array where all elements are equal to zero, except for the `k`-th
      diagonal, whose values are equal to one.
'''
print(nd4)
'''
[[0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]]
'''
# 5. 等差数列
nd5 = np.linspace(0, 100, num=21, )
'''
def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,
             axis=0):
    """
    Return evenly spaced numbers over a specified interval.

    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop`].

    The endpoint of the interval can optionally be excluded.

    .. versionchanged:: 1.16.0
        Non-scalar `start` and `stop` are now supported.

    Parameters
    ----------
    start : array_like
        The starting value of the sequence.
    stop : array_like
        The end value of the sequence, unless `endpoint` is set to False.
        In that case, the sequence consists of all but the last of ``num + 1``
        evenly spaced samples, so that `stop` is excluded.  Note that the step
        size changes when `endpoint` is False.
    num : int, optional
        Number of samples to generate. Default is 50. Must be non-negative.
    endpoint : bool, optional
        If True, `stop` is the last sample. Otherwise, it is not included.
        Default is True.
    retstep : bool, optional
        If True, return (`samples`, `step`), where `step` is the spacing
        between samples.
    dtype : dtype, optional
        The type of the output array.  If `dtype` is not given, infer the data
        type from the other input arguments.

        .. versionadded:: 1.9.0

    axis : int, optional
        The axis in the result to store the samples.  Relevant only if start
        or stop are array-like.  By default (0), the samples will be along a
        new axis inserted at the beginning. Use -1 to get an axis at the end.

        .. versionadded:: 1.16.0

    Returns
    -------
    samples : ndarray
        There are `num` equally spaced samples in the closed interval
        ``[start, stop]`` or the half-open interval ``[start, stop)``
        (depending on whether `endpoint` is True or False).
    step : float, optional
        Only returned if `retstep` is True

        Size of spacing between samples.

'''
print(nd5)
'''
[  0.   5.  10.  15.  20.  25.  30.  35.  40.  45.  50.  55.  60.  65.
  70.  75.  80.  85.  90.  95. 100.]
'''

# 6. arrange数列
nd6 = np.arange(1, 101, 2)
'''
def arange(start=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    arange([start,] stop[, step,], dtype=None)
    
        Return evenly spaced values within a given interval.
    
        Values are generated within the half-open interval ``[start, stop)``
        (in other words, the interval including `start` but excluding `stop`).
        For integer arguments the function is equivalent to the Python built-in
        `range` function, but returns an ndarray rather than a list.
    
        When using a non-integer step, such as 0.1, the results will often not
        be consistent.  It is better to use `numpy.linspace` for these cases.
    
        Parameters
        ----------
        start : number, optional
            Start of interval.  The interval includes this value.  The default
            start value is 0.
        stop : number
            End of interval.  The interval does not include this value, except
            in some cases where `step` is not an integer and floating point
            round-off affects the length of `out`.
        step : number, optional
            Spacing between values.  For any output `out`, this is the distance
            between two adjacent values, ``out[i+1] - out[i]``.  The default
            step size is 1.  If `step` is specified as a position argument,
            `start` must also be given.
        dtype : dtype
            The type of the output array.  If `dtype` is not given, infer the data
            type from the other input arguments.
    
        Returns
        -------
        arange : ndarray
            Array of evenly spaced values.
    
            For floating point arguments, the length of the result is
            ``ceil((stop - start)/step)``.  Because of floating point overflow,
            this rule may result in the last element of `out` being greater
            than `stop`.
'''
print(nd6)
'''
[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47
 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95
 97 99]
'''

# 7. 随机数数列
nd7 = np.random.randint(0, 101, (5, 5))
'''
def randint(low, high=None, size=None, dtype='l'): # real signature unknown; restored from __doc__
    """
    randint(low, high=None, size=None, dtype='l')
    
            Return random integers from `low` (inclusive) to `high` (exclusive).
    
            Return random integers from the "discrete uniform" distribution of
            the specified dtype in the "half-open" interval [`low`, `high`). If
            `high` is None (the default), then results are from [0, `low`).
    
            Parameters
            ----------
            low : int
                Lowest (signed) integer to be drawn from the distribution (unless
                ``high=None``, in which case this parameter is one above the
                *highest* such integer).
            high : int, optional
                If provided, one above the largest (signed) integer to be drawn
                from the distribution (see above for behavior if ``high=None``).
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
            dtype : dtype, optional
                Desired dtype of the result. All dtypes are determined by their
                name, i.e., 'int64', 'int', etc, so byteorder is not available
                and a specific precision may have different C types depending
                on the platform. The default value is 'np.int'.
    
                .. versionadded:: 1.11.0
    
            Returns
            -------
            out : int or ndarray of ints
                `size`-shaped array of random integers from the appropriate
                distribution, or a single such random int if `size` not provided.
'''
print(nd7)
'''
[[20 72 85 73 48]
 [ 8 37 84 18  2]
 [30 79 42 91 89]
 [69  9 14 22 78]
 [69 10 28 43  0]]
'''

# 8. 标准正态分布（平均值=0，方差=1）
nd8 = np.random.randn(4, 5)
'''
def randn(*dn): # known case of numpy.random.mtrand.randn
    """
    randn(d0, d1, ..., dn)
    
            Return a sample (or samples) from the "standard normal" distribution.
    
            If positive, int_like or int-convertible arguments are provided,
            `randn` generates an array of shape ``(d0, d1, ..., dn)``, filled
            with random floats sampled from a univariate "normal" (Gaussian)
            distribution of mean 0 and variance 1 (if any of the :math:`d_i` are
            floats, they are first converted to integers by truncation). A single
            float randomly sampled from the distribution is returned if no
            argument is provided.
    
            This is a convenience function.  If you want an interface that takes a
            tuple as the first argument, use `numpy.random.standard_normal` instead.
    
            Parameters
            ----------
            d0, d1, ..., dn : int, optional
                The dimensions of the returned array, should be all positive.
                If no argument is given a single Python float is returned.
    
            Returns
            -------
            Z : ndarray or float
                A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from
                the standard normal distribution, or a single such float if
                no parameters were supplied.
'''
print(nd8)
'''
[[ 1.22185765  2.09986219 -0.71872626 -0.57921484 -1.50102062]
 [-0.08401382 -0.48772752  0.79623061 -0.68759613  1.7718497 ]
 [ 1.29784392 -0.41479959  0.05062391  0.48360525 -0.58117937]
 [ 1.45247897  0.34181505  0.76010842 -1.41076809  1.41382421]]
'''
# 9. 正态分布   .round(n) 结果保留n位小数
nd9 = np.random.normal(loc=10, scale=10, size=(5, 5)).round(2)
'''
def normal(loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    normal(loc=0.0, scale=1.0, size=None)
    
            Draw random samples from a normal (Gaussian) distribution.
    
            The probability density function of the normal distribution, first
            derived by De Moivre and 200 years later by both Gauss and Laplace
            independently [2]_, is often called the bell curve because of
            its characteristic shape (see the example below).
    
            The normal distributions occurs often in nature.  For example, it
            describes the commonly occurring distribution of samples influenced
            by a large number of tiny, random disturbances, each with its own
            unique distribution [2]_.
    
            Parameters
            ----------
            loc : float or array_like of floats
                Mean ("centre") of the distribution.
            scale : float or array_like of floats
                Standard deviation (spread or "width") of the distribution.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``loc`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized normal distribution.

'''
print("nd9 = ", nd9)
'''
[[34.32  3.04 20.39 -1.19  8.43]
 [14.93 19.39 -3.32 10.19 21.48]
 [24.56 25.48  8.25 12.69  9.5 ]
 [ 0.99 29.73 -1.34 -1.45 23.15]
 [28.62 18.99  8.14 17.54  2.55]]
'''
print(nd9.ndim)     # 输出维度 2
print(nd9.shape)    # 输出形状 (5, 5)
print(nd9.size)     # 总长度 = row * col
print(nd9.dtype)    # 数据类型  float64
