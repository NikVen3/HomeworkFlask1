import requests

import os

import time

import argparse

import concurrent.futures

import asyncio


def download_images(url):
    try:
        response = request.get(url)
        if response.status_code == 200:
            image_name = url.split('/')[-1]
            with open(image_name, 'w') as file:
                file.write(response.content)
            return image_name
    except Exception as e:
        return None


def process_url(url):
    start_time = time.time()
    image_name = download_images(url)
    end_time = time.time()
    if image_name:
        print(F"Downloaded {image_name} in {end_time - start_time:.2f} seconds")
    else:
        print(f"Failed to download image from {url}")


def multi_thereaded_download(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_url, urls)

async def async_download(urls):
    loop = asyncio.set_event_loop()
    sart_time = time.time()
    task = [loop.run_in_executor(None, process_url,urls) for url in urls]
    await asyncio.gather(*task)
    end_time = time.time()
    print(f"Total time taken: {end_time - sart_time:.2f} seconds")



def main():
    parser = argparse.ArgumentParser(description='Image Downloader')
    parser.add_argument('urls', nargs='+', help='List of image URLs')
    args = parser.parse_args()

    urls = args.uris


    print("Starting multi-thereaded download:")
    multi_thereaded_download(urls)

    print("Starting multi-process download:")
    multi_process_download(urls)

    print("Starting asynchronous download:")
    asyncio.run(async_download(urls))


if __name__ == "__main__":
    main()