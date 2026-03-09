import numpy as np
def gru_cell_forward(x, h_prev, params):
    Wz, Uz, bz = params["Wz"], params["Uz"], params["bz"]
    Wr, Ur, br = params["Wr"], params["Ur"], params["br"]
    Wh, Uh, bh = params["Wh"], params["Uh"], params["bh"]

    D = Wz.shape[0]
    H = Uz.shape[0]

    x, x_was_1d = _as2d(x, D)
    h_prev, h_was_1d = _as2d(h_prev, H)

    z = _sigmoid(x @ Wz + h_prev @ Uz + bz)


    r = _sigmoid(x @ Wr + h_prev @ Ur + br)

    h_tilde = np.tanh(x @ Wh + (r * h_prev) @ Uh + bh)

    h = (1 - z) * h_prev + z * h_tilde

    if x_was_1d:
        return h.reshape(-1)

    return h