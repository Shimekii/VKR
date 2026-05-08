# генератор событий
from multiprocessing import Process, Queue
from core.map.MAP import MAP

# генератор событий
def generate_worker(q, l, d, total_events, stop_event, queue):
    mapProcess = MAP(q, l, d)
    count_events = 0
    batch_size = total_events / 10
    buffer = []
    while count_events < total_events:
        if stop_event.is_set():
            return
        
        events = mapProcess.step()
        if events[0] == "event":
            count_events += 1
            buffer.append(events[1])
        elif events[0] == "transition" and events[2]:
            count_events += 1
            buffer.append(events[1])

        if len(buffer) >= batch_size:
            queue.put(("batch", buffer.copy(), count_events))
            buffer.clear()

    if buffer:
        queue.put(("batch", buffer, count_events))

# создает процесс для генерации событий
def start_generation_service(q_matrix, l_matrix, d_matrix, total_events, stop_event):
    queue = Queue()
    process = Process(
        target=generate_worker,
        args=(q_matrix, l_matrix, d_matrix, total_events, stop_event, queue)
    )
    process.start()
    return process, queue