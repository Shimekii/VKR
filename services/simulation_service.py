# генератор событий
from multiprocessing import Process, Queue
from core.map.MAP import MAP

# генератор событий
def generate_worker(q, l, d, size, total_events, stop_event, queue):
    threat = MAP(q, l, d, size)
    count_events = 0
    batch_size = total_events / 10
    buffer = []
    while count_events < total_events:
        if stop_event.is_set():
            return
        
        events = threat.step()
        if events[0] == "event":
            count_events += 1
            buffer.append(events[1])
        elif events[0] == "transition" and events[4]:
            count_events += 1
            buffer.append(events[3])

        if len(buffer) >= batch_size:
            queue.put(("batch", buffer.copy(), count_events))
            buffer.clear()

    if buffer:
        queue.put(("batch", buffer, count_events))

# создает процесс для генерации событий
def start_generation_service(q_matrix, l_matrix, d_matrix, size, total_events, stop_event):
    queue = Queue()
    process = Process(
        target=generate_worker,
        args=(q_matrix, l_matrix, d_matrix, size, total_events, stop_event, queue)
    )
    process.start()
    return process, queue