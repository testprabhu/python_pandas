import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Target page
base_url = "urlhere"
output_folder = "url_images"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

def is_valid_image_url(url):
    # Skip thumbnails or tiny preview images
    return any(url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png"]) and "thumb" not in url.lower()

def download_image(img_url):
    try:
        filename = os.path.join(output_folder, os.path.basename(urlparse(img_url).path))
        if not os.path.exists(filename):
            print(f"Downloading {img_url}")
            img_data = requests.get(img_url).content
            with open(filename, 'wb') as f:
                f.write(img_data)
        else:
            print(f"Already downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {img_url} -> {e}")

def get_full_resolution_urls(soup):
    fullres_urls = []
    # Image links are often in anchor tags pointing to a larger version
    for a in soup.find_all("a", href=True):
        href = a['href']
        if is_valid_image_url(href):
            fullres_urls.append(urljoin(base_url, href))
    return fullres_urls

def scrape_images_from_gallery(url):
    print(f"Scraping {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to load page: {url}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    return get_full_resolution_urls(soup)

if __name__ == "__main__":
    image_urls = scrape_images_from_gallery(base_url)
    print(f"Found {len(image_urls)} full-res image(s)")

    for img_url in image_urls:
        download_image(img_url)
