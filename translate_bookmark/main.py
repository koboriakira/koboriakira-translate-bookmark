from translate_bookmark.config import get_argument
from translate_bookmark.writer import write_csv
from translate_bookmark.analyse import analyse
from translate_bookmark.url import Url


def cli() -> None:
    url: Url = get_url()
    article = url.get_article()
    if article is None:
        print('can\'t scrape.')
        return
    result = analyse(text=article)
    if result is None:
        print('can\'t analyse.')
        return
    use_translate = get_argument('translate')
    write_csv(result=result, url=url, use_translate=use_translate)


def get_url():
    url: str = get_argument(key='url')
    return Url(url=url)
