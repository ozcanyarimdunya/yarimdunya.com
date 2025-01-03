# Combining Multiprocessing and Threading in Python: A Practical Example

In this post, we'll explore how to use Python's `multiprocessing` and `concurrent.futures` modules together. The
provided example demonstrates how to process tasks using multiple processes, with each process managing multiple
threads. This hybrid approach is especially useful for handling workloads that involve both CPU-intensive and I/O-bound
operations.

---

## Understanding the Code Structure

The script is organized into a class `Program`, which encapsulates the logic for managing processes and threads. Here's
a breakdown of its components:

### 1. **Initialization**

The `Program` class is initialized with:

- **Processes**: Number of processes to spawn.
- **Threads**: Number of threads each process manages.
- **Items**: A list of items to process.

```python
class Program:
    def __init__(self, processes: int = 4, threads: int = 10):
        self.processes = processes
        self.threads = threads
        self.items = [1, 2, 3, 4, 5]
```

### 2. **Main Entry Point**

The `run` method kicks off the process-thread combination by calling `start_workers`.

```python
def run(self):
    print(f"Running program with {self.processes} processes and {self.threads} threads")
    self.start_workers()
```

### 3. **Managing Processes**

The `start_workers` method:

- Creates a **queue** to distribute tasks.
- Spawns processes and assigns the `worker` method to each.
- Adds items to the queue.
- Signals the processes to stop once all tasks are completed.

```python
def start_workers(self):
    queue = JoinableQueue()
    workers = [Process(target=self.worker, args=(queue,)) for _ in range(self.processes)]
    for worker in workers:
        worker.start()
    for item in self.items:
        queue.put(item)
    queue.join()
    for _ in workers:
        queue.put(None)
    for worker in workers:
        worker.join()
```

### 4. **Worker Logic**

Each worker process retrieves tasks from the queue, processes them, and marks them as done.

```python
def worker(self, queue: JoinableQueue):
    while True:
        item = queue.get()
        if item is None:
            break
        self.process_item(item)
        queue.task_done()
```

### 5. **Processing Items**

The `process_item` method demonstrates multiprocessing and multithreading integration. For each item, it creates a
thread pool to perform smaller subtasks concurrently.

```python
def process_item(self, item):
    print(f"Processing item: {item} in process {current_process().name}/{self.__class__.__name__}")
    time.sleep(1)
    with ThreadPoolExecutor(max_workers=self.threads) as executor:
       executor.map(self.thread_item, range(item))
```

### 6. **Thread Tasks**

Each thread performs a simulated task, such as I/O, represented by a `time.sleep`.

```python
def thread_item(self, i):
    print(f"Threading i: {i} in thread {current_thread().name}/{self.__class__.__name__}")
    time.sleep(0.5)
```

---

## Key Features of the Code

1. **Hybrid Concurrency**:
    - Multiprocessing is used for parallel execution across CPU cores.
    - Threading handles concurrent subtasks within each process.

2. **Task Distribution with Queues**:
    - `JoinableQueue` ensures task synchronization between producers (main process) and consumers (worker processes).

3. **Scalability**:
    - The number of processes and threads can be adjusted to optimize performance for different workloads.

---

## Running the Program

The `main` function initializes the `Program` and starts execution.

```python
def main():
    program = Program()
    program.run()


if __name__ == "__main__":
    main()
```

When you run the script, it will:

1. Start processes and distribute tasks via the queue.
2. Each process will execute its tasks using threads.
3. Results will be displayed in the console with details of the process and thread handling each task.

---

## Sample Output

```plaintext
Running program with 4 processes and 10 threads
Starting 4 processes with 10 threads each
Processing item: 1 in process Process-1/Program
Threading i: 0 in thread ThreadPoolExecutor-0_0/Program
Processing item: 2 in process Process-2/Program
Threading i: 0 in thread ThreadPoolExecutor-1_0/Program
Threading i: 1 in thread ThreadPoolExecutor-1_0/Program
...
```

---

## Advantages of This Approach

1. **Efficient Resource Utilization**: Combines the strengths of multiprocessing and threading.
2. **Concurrency for Mixed Workloads**: Handles both CPU and I/O-bound tasks effectively.
3. **Modular Design**: Easily customizable for different tasks and configurations.

---

## Conclusion

This example demonstrates a powerful concurrency model in Python by combining multiprocessing and threading. Use this
approach for workloads where tasks can be split into parallelizable chunks requiring varying levels of computation and
I/O operations.

Experiment with the `processes` and `threads` parameters to find the optimal balance for your application!

Happy Coding! 🚀
