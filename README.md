# heuristic-algorithm

旅行商问题（TSP）

模拟退火解决方案

遗传算法解决方案

Greedy and Dijkstra 算法无法找到最佳解



Heuristic Algorithm路径规划算法验证报告


1、路径规划验证选择的算法：
	a、传统算法（Greedy, Dijkstra）
	b、Heuristic Algorithm（Genetic Algorithm，Simulated Annealing）

	传统算法的路径规划每一步都选取最近距离，很大程度都会陷入到局部最优解无法获取全局最优解，故无法在实际的路线规划中获得最佳路线，而且另外一个缺点是时间复杂度过高，越复杂的计算时间消耗越久。
	HA算法能准确找到最优解，并且对于越复杂的情况时间复杂度越有优势，缺点是最优解并非最佳解，根据我们数据的路径规划的复杂程度，都可以较短时间内得到最佳解。
	
	数据选取为foodhwy实际订单的经纬度数据如下：







2、现在已实现的Heuristic Algorithm有2种算法和传统的2种算法结果对比(输出结果：最优路径为数据的index顺序，最佳距离最短路径)：
	a、Greedy
		最优路径 [0, 8, 4, 3, 7, 1, 2, 5, 6]
		最佳距离 188.11217727991738
		如下图所示为：greedy算法路径




	b、Dijkstra
		最佳路线：  [0, 8, 3, 4, 7, 1, 2, 5, 6]
		最佳距离：  183.79714557074675
		如下图所示为：Dijkstra算法路径	




	c、Genetic Algorithm
		最佳路径：  [0, 3, 7, 1, 2, 6, 5, 4, 8]
		最佳距离：  0.17250545785920712




	d、Simulated Annealing
		最佳路线： [0, 3, 7, 1, 2, 6, 5, 4, 8]
		最佳距离： 0.17250545785920712
如上对比数据，可得出结论，Heuristic Algorithm可以得到全局最优结果，故路径规划选择算法可以从Heuristic Algorithm算法中获得。
