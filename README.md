# TSP-Simulated-Annealing
Solving the Traveling Salesman Problem using Simulated Annealing and the 2-opt heuristic in Python

---

## TSP Solver using Simulated Annealing

This project implements the **Travelling Salesman Problem (TSP)** optimization using the **Simulated Annealing** metaheuristic.  
It was developed as part of my academic work in *Microwave & RF Electronics (ETF Belgrade)*, subject: _Optimization Algorithms in Engineering_, to explore algorithmic optimization techniques.  
The task was to find the shortest path between 263 cities, whose coordinates are provided in the file `_in263 (4).txt`, without returning to the original city, and display the resulting shortest path.  
The search space consisted of **263! possible permutations**, representing all possible city visit orders, making brute-force search computationally infeasible.

---

## Overview

The **Travelling Salesman Problem (TSP)** is a classic optimization problem aiming to find the shortest possible route that visits each city exactly once and returns to the starting point.  
The **Simulated Annealing (SA)** algorithm mimics the physical process of annealing — gradually cooling a material to reach a state of minimal energy.

---

## Algorithm Summary

- **Initial Solution**: A random path through all cities.  
- **Neighbor Function**: 2-opt swap to slightly modify the route. Two random indices `i` and `j` are selected along the path, and the segment between them is reversed:  
  ```python
  putanja[i:j+1] = reversed(putanja[i:j+1])
  ```
  This effectively removes two edges and reconnects the path in a new way, potentially shortening the total distance while keeping the route valid.  
  Repeating this operation introduces small variations in the path, allowing the annealing process to search locally and globally for better solutions.  
  In this case, it achieved significantly better results than a basic random swap.

- **Acceptance Criterion**:  
  The new solution is accepted if it improves the total distance, or with probability  
  **P(accept) = exp(−ΔE / T)**,  
  where ΔE is the increase in path length (difference between the new and current solution), and T is the current temperature.  
  This stochastic acceptance helps the algorithm explore the solution space more freely during higher temperatures and gradually focus as T decreases (by allowing acceptance of “worse” solutions, the algorithm avoids getting stuck in local minima).

- **Cooling Schedule**:  
  The temperature decreases according to an exponential cooling scheme, following  
  **T = T₀ × αⁿ**,  
  where T₀ is the initial temperature, α ∈ (0,1) is the cooling rate, and n is the iteration number.

The process continues until the system “cools” below a threshold temperature.

---

## Key Parameters

| Parameter | Description | Example |
|------------|--------------|----------|
| `temperaturne_vrednosti` | Tested for 3 different initial temperatures: 100, 500, 1500. When T₀ is too low, the algorithm becomes more greedy and converges quickly to a nearby local minimum without exploring enough of the search space. When T₀ is too high, it initially accepts worse solutions with higher probability, allowing better exploration and slower but more thorough convergence. |
| `a` | Rate of temperature decrease | 0.995 (tested with various cooling rates, but it must align with other parameters such as initial temperature and iteration count to yield the best results). |
| `br_iter` | Number of iterations per temperature step | 10 (tested with 100k and 500k iterations). |

---

## Summary of Results

| Parameter | Result |
|------------|---------|
| Best temperature (T₀) | 1500 (for the largest number of iterations, 500k) |
| Best path length | ~1685.33 |
| Reference benchmark | 1540 |

---

## Technologies Used

- **Language:** Python 3.12.6  
- **Libraries:** NumPy, Matplotlib (for visualization)  
- **Concepts:** Heuristics, metaheuristic optimization, probabilistic search, path minimization

---

## Future Work

- Compare Simulated Annealing with **Genetic Algorithms** to analyze solution quality and convergence speed  
- Try other initialization strategies (e.g., **Nearest Neighbor heuristic**)  
- Experiment with higher initial temperatures (>1500) to explore deeper global search  
- Implement a GUI visualization for path evolution  

---

## Author
https://www.linkedin.com/in/sladjana-borcic/ | https://github.com/sladjana-b

---

## References Used

- Course material from *Optimization Algorithms in Engineering*, ETF Belgrade  
- Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). *Optimization by Simulated Annealing.* Science, 220(4598), 671–680
