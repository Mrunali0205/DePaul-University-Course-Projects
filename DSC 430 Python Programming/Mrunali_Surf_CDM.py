# Name:- Mrunali Vikas Patil
# Date:- 02-22-24
# Video Link:- https://www.youtube.com/watch?v=NuM0LIJKNR4
# “I have not given or received any unauthorized assistance on this assignment.”  


import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urljoin, urlparse
import re

def is_cdm_url(url):
    """
    Check if the URL belongs to the 'cdm.depaul.edu' domain.

    Args:
        url (str): The URL to be checked.

    Returns:
        bool: True if the URL is part of 'cdm.depaul.edu', False otherwise.
    """
    parsed_url = urlparse(url)
    return "cdm.depaul.edu" in parsed_url.netloc

def clean_text(text):
    """
    Clean the text by removing non-alphabetic words and words in the ignored list.

    Args:
        text (str): The text to be cleaned.

    Returns:
        list: A list of cleaned, lower-cased words.
    """
    ignored_words = set(['var', 'function', 'if', 'true', 'return', 'null', 'false', 'let', 'const'])
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())
    return [word for word in words if word not in ignored_words]

def find_most_common_words(start_url, max_links):
    """
    Crawl the web starting from a given URL and find the most common words.

    Args:
        start_url (str): The starting URL for the web crawling.
        max_links (int): The maximum number of links to visit.

    Returns:
        list of tuples: A list of the 25 most common words and their counts.
    """
    visited_links = set()
    word_counter = Counter()
    links_to_visit = [start_url]

    while links_to_visit and len(visited_links) < max_links:
        current_url = links_to_visit.pop(0)
        if current_url in visited_links or not is_cdm_url(current_url):
            continue

        try:
            response = requests.get(current_url, timeout=5)
            if response.status_code == 200:
                visited_links.add(current_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                content_text = ' '.join(t.get_text() for t in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'article']))
                words = clean_text(content_text)
                word_counter.update(words)

                for link in soup.find_all('a', href=True):
                    href = urljoin(current_url, link['href'])
                    if href not in visited_links and is_cdm_url(href):
                        links_to_visit.append(href)
        except Exception:
            pass  # Ignoring exceptions for simplicity

    return word_counter.most_common(25)

if __name__ == "__main__":
    """
    Main function to execute the web crawling and word counting process.
    It starts from the given URL and processes up to a maximum number of links.
    Finally, it prints the 25 most common words found.
    """
    start_url = "http://cdm.depaul.edu"
    max_links_to_visit = 100  # You can adjust this number as needed

    most_common_words = find_most_common_words(start_url, max_links_to_visit)

    print("The 25 most common words on the CDM website are:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
