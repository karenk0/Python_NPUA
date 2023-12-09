import os
import time
import threading
import multiprocessing

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper

def generate_text_file(filename):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    f = open(filename, 'w')
    for _ in range(10**6):
        sentence = "".join([planets[i] + " " for i in range(7)])
        f.write(sentence + "\n")
    f.close()

@timing_decorator
def word_counter(filename):
    word_frequencies = {}
    f = open(filename, 'r')
    for line in f:
        words = line.split()
        for word in words:
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1
    f.close()
    return word_frequencies

@timing_decorator
def word_counter_multithread(filename, num_threads):
    word_frequencies = {}

    def process_chunk(chunk):
        local_word_frequencies = {}
        for line in chunk:
            words = line.split()
            for word in words:
                if word in local_word_frequencies:
                    local_word_frequencies[word] += 1
                else:
                    local_word_frequencies[word] = 1
        return local_word_frequencies

    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    chunk_size = len(lines) // num_threads
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=lambda: word_frequencies.update(process_chunk(chunk)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_frequencies

def process_chunk(chunk, frequency_dict):
    local_word_frequencies = {}
    for line in chunk:
        words = line.split()
        for word in words:
            if word in local_word_frequencies:
                local_word_frequencies[word] += 1
            else:
                local_word_frequencies[word] = 1
    for key, value in local_word_frequencies.items():
        if key in frequency_dict:
            frequency_dict[key] += value
        else:
            frequency_dict[key] = value

@timing_decorator
def word_counter_multiprocess(filename, num_processes):
    word_frequencies = multiprocessing.Manager().dict()

    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    chunk_minimal_size = len(lines) // num_processes
    chunks = [lines[i:i + chunk_minimal_size] for i in range(0, len(lines), chunk_minimal_size)]

    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=process_chunk, args=(chunk, word_frequencies))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return dict(word_frequencies)


if __name__ == "__main__":
    num_threads = 8
    num_processes = 8

    generate_text_file("lec13file.txt")
   
    _, seq_counting_time = word_counter("lec13file.txt")

    _, multithread_counting_time = word_counter_multithread("lec13file.txt", num_threads)

    _, multiprocess_counting_time = word_counter_multiprocess("lec13file.txt", num_processes)

    print(f"Sequential exe Time: {seq_counting_time:.10f} sec")
    print(f"Multithreading exe Time: {multithread_counting_time:.10f} sec")
    print(f"Multiprocessing exe Time: {multiprocess_counting_time:.10f} sec")

    multithread_speedup = seq_counting_time / multithread_counting_time
    print(f"Multithreading Speedup: {multithread_speedup:.5f}x")
    
    multiprocess_speedup = seq_counting_time / multiprocess_counting_time
    print(f"Multiprocessing Speedup: {multiprocess_speedup:.5f}x")