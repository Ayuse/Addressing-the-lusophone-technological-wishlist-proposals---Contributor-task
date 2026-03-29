## Addressing the Lusophone technological wishlist proposals - Task 2

### Objective of the task:
  Create a Python script to get and print the status code of the response of a list of URLs from a .csv file.

### My approach:
  - read the CSV file using `csv.DictReader` to access the `urls` column by name, stripping any extra whitespace
  - define a `get_status_code()` function that makes an HTTP GET request to each URL with a `timeout=10` to prevent hanging and `allow_redirects=True` to follow redirects
  - handle request failures gracefully using `requests.exceptions.RequestException`, printing `(None)` when no status code is available
  - use `concurrent.futures.ThreadPoolExecutor` with 4 workers to check multiple URLs in parallel, speeding up execution on large lists
  - print each result in the required format: `(STATUS CODE) URL`
