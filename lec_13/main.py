import time
import threading
import multiprocessing
from collections import Counter
from tqdm import tqdm


def count_words_sequential(filename):
    word_freq = Counter()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in tqdm(file, desc="Sequential Processing", unit=" lines"):
            words = line.split()
            word_freq.update(words)
    return word_freq


def process_chunk(chunk, result_queue):
    word_freq = Counter()
    for line in chunk:
        words = line.split()
        word_freq.update(words)
    result_queue.put(word_freq)


def count_words_multithread(filename, num_threads=4):
    word_freq = Counter()
    result_queue = queue.Queue()

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        chunk = lines[start:end]
        thread = threading.Thread(target=process_chunk, args=(chunk, result_queue))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    while not result_queue.empty():
        word_freq.update(result_queue.get())

    return word_freq


def count_words_multiprocess(filename, num_processes=4):
    word_freq = Counter()
    result_queue = multiprocessing.Queue()

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_processes
    processes = []

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_processes - 1 else len(lines)
        chunk = lines[start:end]
        process = multiprocessing.Process(target=process_chunk, args=(chunk, result_queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    while not result_queue.empty():
        word_freq.update(result_queue.get())

    return word_freq


if __name__ == "__main__":
    import queue

    # Generate a large text file
    with open("large_text_file.txt", "w", encoding="utf-8") as file:
        for _ in range(100000):
            file.write("This is a sample sentence with random words. " * 10 + "\n")

    # Measure execution time for sequential processing
    start_time = time.time()
    word_freq_seq = count_words_sequential("large_text_file.txt")
    seq_time = time.time() - start_time

    # Measure execution time for multithreading
    start_time = time.time()
    word_freq_thread = count_words_multithread("large_text_file.txt")
    thread_time = time.time() - start_time

    # Measure execution time for multiprocessing
    start_time = time.time()
    word_freq_process = count_words_multiprocess("large_text_file.txt")
    process_time = time.time() - start_time

    # Display results
    print(f"Sequential Execution Time: {seq_time:.2f} seconds")
    print(f"Multithreading Execution Time: {thread_time:.2f} seconds")
    print(f"Multiprocessing Execution Time: {process_time:.2f} seconds")

    # Compare results
    assert word_freq_seq == word_freq_thread == word_freq_process, "Results do not match!"

    # Calculate speedup
    speedup_thread = seq_time / thread_time
    speedup_process = seq_time / process_time

    print(f"Speedup (Multithreading): {speedup_thread:.2f}x")
    print(f"Speedup (Multiprocessing): {speedup_process:.2f}x")
