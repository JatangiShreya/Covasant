# DAY-5
# Question-8:
# Given a URL, download that and parse 
# and download all links inside that page 
    # in thread -Today
    # BeautifulSoup for parsing html, requests for downloading
import requests
from bs4 import BeautifulSoup
import threading
import os
from urllib.parse import urljoin

# Function to download a page and parse all links
def download_and_parse(url: str):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        urls = set()
        for link in links:
            href = link['href']
            absolute_url = urljoin(url, href)
            urls.add(absolute_url)
        print(f"Found {len(urls)} links on {url}")
        download_links_concurrently(urls)
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_links_concurrently(urls: set):
    threads = []
    for link in urls:
        thread = threading.Thread(target=download_link, args=(link,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
def download_link(link: str):
    try:
        response = requests.get(link)
        file_name = link.split('/')[-1] or 'index.html'
        if not file_name.endswith('.html'):
            file_name += '.html'
        with open(file_name, 'w') as file:
            file.write(response.text)
        print(f"Downloaded {link} to {file_name}")
    except requests.RequestException as e:
        print(f"Error downloading {link}: {e}")
if __name__ == '__main__':
    start_url = "https://example.com"
    download_and_parse(start_url)
