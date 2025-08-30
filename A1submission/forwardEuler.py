# this version allows you to interactively select a step size and see the forward euler plot in the terminal.
# It works on mac
# This file isn't necessarily part of my submission.

import subprocess
# notes
# recursive calc:
# y1 = y0 + hy0' = y0 + h * f(y0,t0)
# f(y0,t0) = -r(Tc-Ts), where r = 0.025 per second, Tc is 84, Ts is 19
# we will do forward euler iteratively because it's much easier to append to an array iteratively

# note for the TA or teacher: i wrote this for  youplot and then realized that's a bad idea

# vars and inputs

Ts = 19 # temperature of surrounding celsius
r = 0.025 # rate of cooling PER SECOND
t = 300 # 5 minutes in seconds
plot_values = []

# iterative forward euler calculation
def forwardEuler(h: int):
    print(type(h))
    Tc = 80 # temperature of cup celsius
    plot_values.append((0, Tc)) # Y0
    current_step = 0
    total_steps = t/h
    while current_step < total_steps:
        current_step += 1
        Tc = Tc+calculateTd(Tc, h)
        plot_values.append((current_step*h, Tc))

# "explicit euler" but for simplicity I put h here. It doesn't really matter if it's here or in forwardEuler function.
def calculateTd(cupTemp: float, h: int):
    return (-r*h)*(cupTemp-Ts)

# a subprocess acts like a terminal command, so we call youplot and give it some params
def plot_from_tuples(data):

    # convert the data array into a csv format
    csv_data = "x,y\n" + "\n".join(f"{x},{y}" for x, y in data)

    process = subprocess.Popen(
    ['youplot', 'line', '-d', ',', '-H', '--width', '100', '--height', '50'],
    stdin=subprocess.PIPE
)
    process.communicate(input=csv_data.encode())


h = input("input step size in seconds (perhaps one of: 30, 15, 10, 5, 1, 0.5, 0.25): ")
h_as_int = float(h)
forwardEuler(h_as_int)
plot_from_tuples(plot_values)



