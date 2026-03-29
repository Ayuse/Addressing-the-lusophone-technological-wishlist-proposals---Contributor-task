import csv
import concurrent.futures
import requests

CSV_FILE = "Task 2 - Intern.csv"


def get_status_code(url):
    """
    Makes a request to a URL and prints the status code and URL.

    Args:
        url (str): URL to which a request is to be made

    Returns:
        Prints: (STATUS CODE) URL on success
                (None) URL on connection failure
    """
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        status_code = response.status_code
        print(f"({status_code}) {url}")
    except requests.exceptions.RequestException as e:
        status_code = e.response.status_code if e.response else None
        print(f"({status_code}) {url}")


def process_csv(csv_file):
    """
    Reads URLs from a CSV file and prints their status codes concurrently.

    Args:
        csv_file (str): Path to the CSV file containing URLs
    """
    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        urls = [row["urls"].strip() for row in csv_reader]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(get_status_code, urls)


if __name__ == "__main__":
    process_csv(CSV_FILE)
