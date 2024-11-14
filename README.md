 Heuristic Algorithm Path Planning Verification
1. Selected Algorithms for Path Planning Verification:
a. Traditional Algorithms
• b. Heuristic Algorithms (Genetic Algorithm, Simulated Annealing)
The traditional algorithms, such as Greedy and Dijkstra, choose the nearest distance at each step, which often leads to getting stuck in a local optimum, failing to obtain the global optimum. Thus, they cannot always find the best route in practical scenarios. Another disadvantage is that the time complexity can be very high, resulting in longer computation times for more complex calculations.
Heuristic algorithms (HA) can accurately find the optimal solution, and their time complexity becomes increasingly advantageous with higher complexity cases. However, the disadvantage is that the "optimal solution" might not always be the "best solution." Based on the complexity of our data's path planning, we can obtain a satisfactory solution within a relatively short period. The data used consists of the latitude and longitude of actual orders from Kaggle, as shown below:
•
 
 2. Comparison of Results from Implemented Heuristic Algorithms and Traditional Algorithms
(Output: Optimal path as per data index order, minimum distance)
a. Greedy
◦ ◦
b. Dijkstra
• Optimal Path: [0, 8, 3, 4, 7, 1, 2, 5, 6]
Minimum Distance: 183.79714557074675
• Path visualization for the Dijkstra algorithm is shown below:
 Optimal Path: [0, 8, 4, 3, 7, 1, 2, 5, 6]
Minimum Distance: 188.11217727991738
◦ Path visualization for the Greedy algorithm is shown below:
  •

   c. Genetic Algorithm
Optimal Path: [0, 3, 7, 1, 2, 6, 5, 4, 8]
• Minimum Distance: 0.17250545785920712
•
  d. Simulated Annealing
• Optimal Path: [0, 3, 7, 1, 2, 6, 5, 4, 8]
• Minimum Distance: 0.17250545785920712

  From the comparison above, it can be concluded that the Heuristic Algorithm can achieve a globally optimal result. Therefore, for route planning, it is recommended to select from the Heuristic Algorithm methods.





	d、Simulated Annealing
		最佳路线： [0, 3, 7, 1, 2, 6, 5, 4, 8]
		最佳距离： 0.17250545785920712
如上对比数据，可得出结论，Heuristic Algorithm可以得到全局最优结果，故路径规划选择算法可以从Heuristic Algorithm算法中获得。
