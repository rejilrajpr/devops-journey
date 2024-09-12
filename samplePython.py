import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='server_health.log', level=logging.INFO)

def check_server_health(url):
    try:
        # Send HTTP GET request to the server
        response = requests.get(url)

        # Log the status of the server
        if response.status_code == 200:
            logging.info(f"{datetime.now()}: Server {url} is up. Status code: {response.status_code}")
            print(f"Server {url} is up.")
        else:
            logging.warning(f"{datetime.now()}: Server {url} is down. Status code: {response.status_code}")
            print(f"Server {url} is down. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(f"{datetime.now()}: Failed to reach {url}. Error: {e}")
        print(f"Failed to reach {url}. Error: {e}")

if __name__ == "__main__":
    url_to_check = 'https://jsonplaceholder.typicode.com/posts'   # Replace with the actual URL you want to check
    check_server_health(url_to_check)
