def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for i in range(steps):
        g = 2 * a * x0 + b 
        x0 = x0 - lr * g
    return x0
    