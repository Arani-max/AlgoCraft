from collections import deque

def generate_bfs_steps(graph, start_node):
    """
    Генерирует последовательность шагов для визуализации обхода графа в ширину (BFS)
    Каждый шаг описывает состояние графа в определенный момент времени
    """
    visited = set()
    queue = deque([start_node])
    steps = []
    
    # Отмечаем стартовую вершину как посещенную
    visited.add(start_node)
    
    steps.append({
        "description": f"Инициализация: начинаем с вершины {start_node}",
        "queue": list(queue),
        "visited": list(visited),
        "current": start_node
    })
    
    while queue:
        current_node = queue.popleft()
        
        steps.append({
            "description": f"Извлекаем вершину {current_node} из очереди",
            "queue": list(queue),
            "visited": list(visited),
            "current": current_node
        })
        
        # Перебираем соседей текущей вершины
        # Сортируем для детерминированного порядка отображения
        for neighbor in sorted(graph.get(current_node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                steps.append({
                    "description": f"Посещаем соседа {neighbor} вершины {current_node} и добавляем в очередь",
                    "queue": list(queue),
                    "visited": list(visited),
                    "current": current_node
                })
                
    steps.append({
        "description": "Обход завершен!",
        "queue": [],
        "visited": list(visited),
        "current": None
    })
    
    return steps

if __name__ == "__main__":
    # Пример структуры графа (список смежности)
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Получаем шаги для визуализации
    animation_steps = generate_bfs_steps(sample_graph, 'A')
    
    # Выводим симуляцию шагов тренажёра в консоль
    for i, step in enumerate(animation_steps, 1):
        print(f"Шаг {i}: {step['description']}")
        print(f"  Текущая вершина: {step['current']}")
        print(f"  Очередь: {step['queue']}")
        print(f"  Посещенные: {step['visited']}")
        print("-" * 40)