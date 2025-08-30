# this is just forward euler but using matplotlib instead of youplot
import matplotlib.pyplot as plt

Ts = 19 # temperature of surrounding celsius
r = 0.025 # rate of cooling PER SECOND
t = 300 # 5 minutes in seconds


# iterative forward euler calculation
def forwardEuler(h: int):
    Tc = 80 # temperature of cup celsius
    plot_values.append((0, Tc)) # Y0
    current_step = 0
    total_steps = t/h
    while current_step < total_steps:
        current_step += 1
        Tc = Tc+calculateTd(Tc, h)
        plot_values.append((current_step*h, Tc))

def calculateTd(cupTemp: float, h: int):
    return (-r*h)*(cupTemp-Ts)


# h = input("input step size in seconds (perhaps one of: 30, 15, 10, 5, 1, 0.5, 0.25): ")
# h_as_int = float(h)

steps = [30,15,10,5,1,0.5,0.25]

graphs = []

plot_values = []
for step_size in steps:
    forwardEuler(step_size)
    a, b = zip(*plot_values)
    x = list(a)
    y = list(b)
    fig, ax = plt.subplots()
    ax.plot(a, b)
    plt.show()
    # plot_values = []
    # graphs.append(x)
    # graphs.append(y)
    # plot_values = []

# now graphs contains all the data we want to plot




