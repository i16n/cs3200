import numpy as np
import matplotlib.pyplot as plt
from forwardEulerMPL import forwardEuler
from trapezoidalEuler import trapezoidal_predictor_corrector

# Parameters
Ts = 19
Tc = 84
r = 0.025
total_time = 300

# this is just newtons method
def analytical_solution(t, Ts, Tc, r):
    return Ts + (Tc - Ts) * np.exp(-r * t)

# really simple, just uses np arange to plot everything at the step size points
def plot_analytical(step_size):
    t = np.arange(0, total_time + step_size, step_size)
    Tc_analytical = analytical_solution(t, Ts, Tc, r)

    plt.plot(t, Tc_analytical, color='red')

    # TOGGLE THIS ON TO PLOT IT
    # plt.plot(t, forwardEuler(step_size))
    plt.plot(t, trapezoidal_predictor_corrector(Tc, Ts, r, step_size, total_time))

    # simple inner functionality to find biggest error point
    biggest_error = 0
    for i in range(len(t)):
        current_error = abs(Tc_analytical[i] - trapezoidal_predictor_corrector(Tc, Ts, r, step_size, total_time)[i])
        if current_error > biggest_error:
            biggest_error = current_error
            biggest_error_index = i
    print(f'Biggest error: {biggest_error} at step {t[biggest_error_index]} seconds')

    plt.xlabel('time in secs (red line is analytical solution computed at the step size points)')
    plt.ylabel('temp in celcsius')
    plt.title(f'Coffee Problem: \nStep Size = {step_size} s')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_analytical(0.25)
