import math
import numpy as np
from sklearn.utils import extmath


def sigmoid(X):
    func = np.vectorize(lambda x: 1 / (1 + math.exp(-x)))
    return func(X)


def tanh(X):
    func = np.vectorize(lambda x: math.tanh(x))
    return func(X)


def softmax(X):
    return extmath.softmax(X)