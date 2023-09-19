graph = {
    '1': set(['2', '3']),
    '2': set(['1', '4', '5']),
    '3': set(['1', '6']),
    '4': set(['2']),
    '5': set(['2', '6']),
    '6': set(['3', '5'])
}


def bfs(graph, start, visited = [],queue = []):

    visited.append(start)
    queue.append(start)

    for v in queue:
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(f"Поиск в ширину: {bfs(graph, '1')}")
