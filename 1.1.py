import heapq
from typing import Dict, List, Tuple, Optional

def kth_shortest_path_with_names(
        graph: Dict[str, List[Tuple[str, int]]],
        start: str,
        target: str,
        K: int
) -> Optional[Tuple[int, List[str]]]:


    # 优先队列存储(总时间, 当前站点, 路径)
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    # 记录每个站点被访问的次数
    count = {}

    # 存储找到的到达目标站点的路径
    results = []

    while pq and len(results) < K:
        total_time, current_station, path = heapq.heappop(pq)

        # 初始化或增加当前站点的访问次数
        count[current_station] = count.get(current_station, 0) + 1

        # 如果到达目标站点，记录结果
        if current_station == target:
            results.append((total_time, path))
            if len(results) == K:
                break

        # 剪枝：如果当前站点已被访问K次，不再扩展
        if count[current_station] > K:
            continue

        # 如果当前站点在图中没有邻居，跳过
        if current_station not in graph:
            continue

        # 扩展相邻站点
        for next_station, travel_time in graph[current_station]:
            # 避免简单循环 （默认不会两次经过同一站点）
            if next_station in path:
                continue

            new_total_time = total_time + travel_time
            new_path = path + [next_station]
            heapq.heappush(pq, (new_total_time, next_station, new_path))

    if len(results) >= K:
        return results[K - 1]  # 返回第K短路径的(时间, 路径)
    else:
        return None

# 1. 直接使用中文站名构建图
subway_graph = {
    "北京": [("天津", 30), ("上海", 120)],
    "天津": [("北京", 30), ("南京", 60), ("济南", 45)],
    "上海": [("北京", 120), ("南京", 90), ("杭州", 30)],
    "南京": [("天津", 60), ("上海", 90), ("合肥", 40)],
    "济南": [("天津", 45), ("青岛", 50)],
    "青岛": [("济南", 50)],
    "杭州": [("上海", 30)],
    "合肥": [("南京", 40)]
}

# 找从北京到南京的第2短路径
K=int(input("请问你想要第几短路径？"))
result = kth_shortest_path_with_names(subway_graph, "北京", "杭州", K)

if result:
    time, path = result
    print(f"第{K}短路径: {' → '.join(path)}")
    print(f"总时间: {time}分钟")
else:
    print(f"未找到第{K}短路径")




