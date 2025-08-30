# Instructions to run

I initially wrote this program to use youplot, but realized matplotlib might work better for this. The file of interest for problem 2.A is `forwardEulerMPL.py`, and requires that you download matplotlib. I did this in a venv for simplicity. That's the only dependency.

If you want to try the interactive youplot version:
It can be downloaded via homebrew: `brew install youplot`
It can also be downloaded in some linux distros just via `apt install youplot`

## General structure

To run the comparisons, I use a comment-toggle structure and I import forward euler and trapezoidal euler into my analytical plotter so you can see them side by side.
In other words, to switch between viewing trapezoidal euler or forward euler compared with the analytical solution at the same step size points, just comment one out.
To run these comparisons, go to plotAnalytical.py

## Other notes

There is a print statement in the code that will tell you in the console what the biggest error is and where it occurred between the analytical solution computed at the same step sizes as either the forward or trapezoidal method.
