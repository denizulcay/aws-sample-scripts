"""
This class crawls TCB Scan for a new chapter of One Piece and creates a notification
"""
import time
from pathlib import Path
from re import sub

import requests
from bs4 import BeautifulSoup


# https://tcbscans.me/chapters/7803/one-piece-chapter-{chapter}

class OnePieceCrawler:
    _url = "https://tcbscans.me/mangas/5/one-piece"

    @staticmethod
    def get_current_chapter():
        with open(Path(__file__).parent / 'count.txt', 'r') as file:
            chapter = int(file.read())

        return chapter

    @staticmethod
    def record_current_chapter(chapter):
        with open(Path(__file__).parent / 'count.txt', 'w') as file:
            file.write(str(chapter))

    def crawl(self):
        # A GET request to the API
        response = requests.get(self._url)

        soup = BeautifulSoup(response.content, "html.parser")
        # Get latest chapter
        latest_chapter = soup.find_all("div", {"class": "text-lg font-bold"})[0].text
        latest = int(latest_chapter.split(" ")[-1])
        # Get latest title
        title = soup.find_all("div", {"class": "text-gray-500"})[0].text
