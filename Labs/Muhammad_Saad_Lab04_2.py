import time
import threading

# Function 1
def function_with_loop(name):
    for _ in range(100_000):
        time.sleep(0.0001)
    print(f"{name}: Loop completed")

# Function 2
def execute_function_sequentially(times):
    start_time = time.time()
    for _ in range(times):
        function_with_loop(f"Sequential_{_ + 1}")
    elapsed_time = time.time() - start_time
    print(f"Sequential execution completed in {elapsed_time:.4f} seconds")

# Function 3
def execute_function_with_threads(times):
    start_time = time.time()
    threads = []
    for _ in range(times):
        thread = threading.Thread(target=function_with_loop, args=(f"Thread_{_ + 1}",))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time
    print(f"Threaded execution completed in {elapsed_time:.4f} seconds")

# Statements to call the functions
# a. To call the function in step 2 ten times
execute_function_sequentially(10)

# b. To call the function in step 3 ten times
execute_function_with_threads(10)
