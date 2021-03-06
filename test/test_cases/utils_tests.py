import unittest
import numpy as np
import pycuda.gpuarray
from src.utils.cuda import *
from src.utils.activations import *

class CudaTestCase(unittest.TestCase):

    def test_matmul_gpu(self):
        a = np.random.uniform(0, 10, (10, 5))
        b = np.random.uniform(0, 10, (5, 4))
        c = np.random.uniform(0, 10, (10, 4))

        A = pycuda.gpuarray.to_gpu(a)
        B = pycuda.gpuarray.to_gpu(b)
        C = pycuda.gpuarray.to_gpu(c)
        Y = modified_gemm_gpu(A, B, C)

        y = np.matmul(a, b) + c

        y_gpu = Y.get()

        self.assertListEqual(y_gpu.tolist(), y.tolist())

    def test_tanh_gpu(self):
        shape = (4, 1)
        a = np.random.uniform(-100, 100, shape)
        A = pycuda.gpuarray.to_gpu(a)
        x_gpu = tanh_gpu(A).get()
        x = tanh(a)

        for i in range(shape[0]):
            self.assertLessEqual(abs(x_gpu[i] - x[i]), 1e-5)

    def test_sigmoid_gpu(self):
        shape = (4, 1)
        a = np.random.uniform(-100, 100, shape)
        A = pycuda.gpuarray.to_gpu(a)
        x_gpu = sigmoid_gpu(A).get()
        x = sigmoid(a)

        for i in range(shape[0]):
            self.assertLessEqual(abs(x_gpu[i] - x[i]), 1e-5)

    def test_softmax_gpu(self):
        shape = (4, 1)
        a = np.random.uniform(-100, 100, shape)
        A = pycuda.gpuarray.to_gpu(a)
        x_gpu = softmax_gpu(A).get()
        x = softmax(a)

        for i in range(shape[0]):
            self.assertLessEqual(abs(x_gpu[i] - x[i]), 1e-5)