# this is just forward euler but using matplotlib
import matplotlib.pyplot as plt


# iterative forward euler calculation
def forwardEuler(h: int):
    t = 300 # 5 minutes in seconds
    plot_values = []
    Tc = 84 # temperature of cup celsius
    plot_values.append(Tc) # Y0
    current_step = 0
    total_steps = t/h
    while current_step < total_steps:
        
        current_step += 1
        Tc = Tc+calculateTd(Tc, h)
        plot_values.append(Tc)
    return plot_values

def calculateTd(cupTemp: float, h: int):
    Ts = 19.0 # temperature of surrounding celsius
    r = 0.025 # rate of cooling PER SECOND
    return (-r*h)*(cupTemp-Ts)




