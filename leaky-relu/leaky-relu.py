import numpy as np

def leaky_relu(x, alpha=0.1):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    
    result = np.where(np.array(x)>=0 , x , alpha * np.array(x))
    return result
    
        
   