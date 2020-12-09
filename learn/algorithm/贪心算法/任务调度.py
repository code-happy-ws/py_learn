"""假设有一个中央调度机，有n个相同的任务需要调度到m台服务器上去执行，由于
每台服务器的配置不一样，因此，服务器执行一个任务所花费的时间也不同。
现在假设第i个服务器执行一个任务所花费的时间也不同。
现在假设第i个服务器执行一个任务需要的时间为t[i]。
例如: 有2个执行机a与b。执行一个任务分别需要7min, 10min，
有6个任务待调度。如果平分这6个任务，即a与b各3个任务，
则最短需要30min执行完所有。
如果a分4个任务，b分2个任务，则最短28min执行完。
请设计调度算法，使得所有任务完成所需要的时间最短，
输入m台服务器，每台机器处理一个任务的时间为t[i]，
完成n个任务，输出n个任务在m台服务器分布:
estimate_process_time(t, m, n)


分析：贪心算法
所求问题的全局最优解可以通过一系列局部最优解的选择来达到
(当前状态选取哪个可以达到局部最优解)
执行第n个任务时，分配给哪个服务器，取当前状态下取各服务器执行一个任务后总耗时最短的作为第n个任务的服务器"""


def minValue(cost, times: list):
    if not cost:
        return
    minNum = float('inf')
    minIndex = 0
    # 服务器个数
    server_num = len(times) if times else 0
    for i, time in enumerate(cost):
        if not times:
            if time < minNum:
                minNum = time
                minIndex = i
        else:
            # 计算已经耗时的任务和当前该任务执行需要花费的时间中的最小值
            if i < server_num and time + times[i] < minNum:
                minNum = time + times[i]
                minIndex = i
    return minNum, minIndex


def estimate_process_time(times, server_num, task_num):
    if not times:
        return
    if server_num <= 0 or task_num <= 0:
        return
    # 记录m台机器每台机器已经执行的任务时间
    cost = [0 for _ in range(server_num)]
    i = 0
    while i < task_num:
        print(cost,times)
        minNum, minIndex = minValue(cost, times)
        print(minNum, minIndex)
        # 选取已经花费时间+当前任务所需要时间的和中耗时最短的
        cost[minIndex] += times[minIndex]
        i += 1
        print(cost)
        print('------------')
    # 计算总的耗时时间，即计算cost数组中的最大值即为所求
    totalTime = float('-inf')
    # 计算每个服务器分配的任务序列
    taskArr = [0 for i in range(server_num)]
    for i, value in enumerate(cost):
        if value > totalTime:
            totalTime = value
        if value > 0:
            taskArr[i] = value / times[i] if times[i] != 0 else 0
    return totalTime, taskArr


def process():
    t = [7, 10]
    n = 6
    m = len(t)
    totalTime, taskArr = estimate_process_time(t, m, n)
    print("耗时最少为:", totalTime, "任务分配序列为:", taskArr)


if __name__ == "__main__":
    process()
