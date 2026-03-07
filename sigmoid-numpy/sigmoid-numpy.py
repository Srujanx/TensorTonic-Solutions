import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray( x , dtype = float)
    x = (1 / ( 1 + np.exp(-x)) )
    return x
    