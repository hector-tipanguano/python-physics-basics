# Free Fall Simulation (Python)

This project simulates the motion of an object in **free fall** using Python.

The object is released from an initial height and falls under the influence of gravity.  
The program computes the position as a function of time and plots the trajectory.

## Physical Model

The height of the object as a function of time is given by

h(t) = h₀ - (1/2) g t²

where

- h₀ = initial height
- g = gravitational acceleration (9.81 m/s²)
- t = time

The simulation runs from t = 0 until the object reaches the ground.

## Parameters used in the simulation

- Initial height: 100 m
- Gravitational acceleration: 9.81 m/s²
- Time resolution: 100 points

## Libraries used

- NumPy
- Matplotlib

## Output

The program generates a graph showing the **height of the object as a function of time** until it reaches the ground.

## Author

Hector Gabriel Tipanguano  
Physics student at Escuela Politécnica Nacional
