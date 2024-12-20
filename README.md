# Mercury-Venus-Earth-Alignment-Simulator
This program simulates the orbital positions of three planets (Mercury, Venus, and Earth) and determines the first day on which they align relative to the Sun within a specified tolerance. The program considers two types of alignments:

Same-side alignment: All planets are on the same side of the Sun.
Opposite-side alignment: One planet is nearly opposite the other two.
Key Steps
## Angular Velocity Calculation: 
Calculate the angular velocity (degrees per day) for each planet based on its orbital period.

## Daily Simulation: 
Starting from day 1, calculate the current angular position of each planet every day.

## Alignment Check: 
Check whether the planets are in a same-side or opposite-side alignment:

### Same-side alignment:
 All angles are within the specified tolerance (e.g., 1 degree).
### Opposite-side alignment: 
One angle difference is close to 0 degrees, while the other two are close to 180 degrees, within the tolerance.
## Termination Condition: 
When the first day of each alignment type (same-side and opposite-side) is found, record the results and terminate the simulation.

