import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(x, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    n , d = x.shape
    w = np.zeros(d)
    b = 0 
    for i in range(steps):
         z = x @ w + b 
         p = _sigmoid(z)
         error = p - y
         grad_w  = x.T @ error / n 
         grad_b = np.mean(error)
         w = w - lr * grad_w 
         b = b - lr * grad_b 
    return (w,b)
 