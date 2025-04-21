# Question-9:
# Given a URL, download that and parse 
# and download all links inside that page 
    # in asyncio 
    # BeautifulSoup for parsing html, requests for downloading

import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def get_links_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()

    for tag in soup.find_all('a', href=True):
        href = tag['href']
        full_url = urljoin(url, href)
        if urlparse(full_url).scheme in ('http', 'https'):
            links.add(full_url)

    return list(links)


async def download_link(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            print(f"Downloaded: {url} (Status: {response.status})")
            return url, text
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return url, None

async def download_all_links(links):
    async with aiohttp.ClientSession() as session:
        tasks = [download_link(session, url) for url in links]
        return await asyncio.gather(*tasks)


def main(url):
    print(f"Fetching main page: {url}")
    links = get_links_from_url(url)
    print(f"Found {len(links)} links. Starting async downloads...\n")

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(download_all_links(links))


    for url, content in results:
        if content:
            print(f"Downloaded content from: {url[:50]}...\n")

if __name__ == "__main__":
    main("https://example.com")
    
