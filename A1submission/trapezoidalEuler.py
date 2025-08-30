
# this is the explicit euler function, same as from forwardEuler file.
def f(t, y, k, T_ambient):
    return -k * (y - T_ambient)

# this is the predictor-correct algorithm (trapezoidal method from euler) like we saw in class
def trapezoidal_predictor_corrector(y0, T_ambient, k, h, t_total):
    steps = int(t_total / h)
    y = y0
    t = 0
    ys = [y]
    ts = [t]

    # nested loop
    for n in range(steps):
        # this is "explicit euler"
        y_pred = y + h * f(t, y, k, T_ambient)
        # i chose to do this iteratively
        error = 1e-6
        y_corr = y_pred

        # inner loop for error solving. I arbitrarily chose 100 as my stopping point
        for _ in range(100):
            y_next = y + h/2 * (f(t, y, k, T_ambient) + f(t+h, y_corr, k, T_ambient))

            # the error is extremely small. We exit loop when error is met
            if abs(y_next - y_corr) < error:
                break
            y_corr = y_next # update value
        y = y_corr
        t += h
        ys.append(y)
    return ys



# ts, ys = trapezoidal_predictor_corrector(initial_temp, surrounding_temp, k, h, t_total)
