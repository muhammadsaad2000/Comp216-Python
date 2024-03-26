import requests
import time
import threading

# Part A
def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        content = response.content

        # Generate a file name based on the URL
        file_name = url.split('/')[-1] + '.jpg'

        # Write the contents to the file
        with open(file_name, 'wb') as file:
            file.write(content)

        print(f"Downloaded {url} as {file_name}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Part B
def download_sequentially(urls):
    start_time = time.perf_counter()

    for url in urls:
        download_file(url)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Sequential download time: {elapsed_time} seconds")

# Part C
def download_with_threads(urls):
    start_time = time.perf_counter()
    threads = []

    # Creating threads for each URL
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    # Waiting for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Threaded download time: {elapsed_time} seconds")

if __name__ == "__main__":
    # Image URLs
    img_urls = [
        'https://images.unsplash.com/photo-1504208434309-cb69f4fe52b0',
        'https://images.unsplash.com/photo-1485833077593-4278bba3f11f',
        'https://images.unsplash.com/photo-1593179357196-ea11a2e7c119',
        'https://images.unsplash.com/photo-1526515579900-98518e7862cc',
        'https://images.unsplash.com/photo-1582376432754-b63cc6a9b8c3',
        'https://images.unsplash.com/photo-1567608198472-6796ad9466a2',
        'https://images.unsplash.com/photo-1487213802982-74d73802997c',
        'https://images.unsplash.com/photo-1552762578-220c07490ea1',
        'https://images.unsplash.com/photo-1569691105751-88df003de7a4',
        'https://images.unsplash.com/photo-1590691566903-692bf5ca7493',
        'https://images.unsplash.com/photo-1497206365907-f5e630693df0',
        'https://images.unsplash.com/photo-1469765904976-5f3afbf59dfb'
    ]

    # Part B
    print("Part B:")
    download_sequentially(img_urls)

    # Part C
    print("\nPart C:")
    download_with_threads(img_urls)
