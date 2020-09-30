from bs4 import BeautifulSoup
import requests
from typing import Optional


def get_article_for_packers(url: str) -> Optional[str]:
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        return soup.select('.nfl-c-article__container')[0].text
    except Exception:
        return ''
