# TSP-Simulated-Annealing
Solving the Traveling Salesman Problem using Simulated Annealing and the 2-opt heuristic in Python

# TSP Solver using Simulated Annealing

This project implements the **Travelling Salesman Problem (TSP)** optimization using the **Simulated Annealing** metaheuristic.  
It was developed as part of my academic work in *Microwave & RF Electronics (ETF Belgrade)* to explore algorithmic optimization techniques and numerical methods in Python. The task was to find the shortest path between 263 cities, whose coordinates are provided in the file _in263 (4).txt, without returning to the original city, and display the resulting shortest path. The search space consisted of 263! possible permutations, representing all possible city visit orders, making brute-force search computationally infeasible.

---

##  Overview

The **Travelling Salesman Problem (TSP)** is a classic optimization problem aiming to find the shortest possible route that visits each city exactly once and returns to the starting point.  
The **Simulated Annealing (SA)** algorithm mimics the physical process of annealing — gradually cooling a material to reach a state of minimal energy.

---

##  Algorithm Summary

- **Initial Solution**: A random path through all cities.  
- **Neighbor Function**: 2-opt swap to slightly modify the route.  
- **Acceptance Criterion**: A probabilistic function allowing worse solutions early on to escape local minima.  
- **Cooling Schedule**: The temperature decreases according to an exponential cooling scheme, following T = T₀ × αⁿ, where T₀ is the initial temperature, α ∈ (0,1) is the cooling rate, and n is the iteration number.

The process continues until the system “cools” below a threshold temperature.

---

## Key Parameters

| Parameter | Description | Example |
|------------|--------------|----------|
| `temperaturne_vrednosti` | Tried for 3 different temperatures: 100, 500, 1500
| `a` | Rate of temperature decrease | 0.995 (tested with various cooling rates, but it needs to align with other parameters as well (like starting temperature, number of iterations...)) in order to get the best results.
| br_iter | Number of iterations per temperature step | 10 (tested with 100k and 500k iterations) |
---

**Summary of results:**
| Parameter | Result |
|------------|---------|
| Best temperature (T₀) | 1500 | (for the largest number of iterations, 500k!)
| Best path length | ~1685.33 |
| Reference benchmark | 1540 |


## Technologies Used

- **Language:** Python 3.12.6 
- **Libraries:** NumPy, Matplotlib (for visualization)  
- **Concepts:** Heuristics, metaheuristic optimization, probabilistic search, path minimization.

---

##  Future Work

- Compare Simulated Annealing with **Genetic Algorithms**
- Try other ways of generating the starting path instead of random initialization  (for example, Nearest Neighbor heuristic, popular for solving TSP problems)
- Implement GUI visualization for path evolution.  
---

##  Author
[LinkedIn](https://www.linkedin.com/in/sladjana-borcic/) | [GitHub](https://github.com/sladjanab-art)

