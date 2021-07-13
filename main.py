import typing as ty
import aiohttp
import asyncio
import re

phone_regex_str = (
    r"[^a-zA-Z0-9]{1}\+?([7,8]{1})[ -]?\(?([0-9]{3})\)?[ -]?"
    r"([0-9]{3})[ -]?([0-9]{2})[ -]?([0-9]{2})[^a-zA-Z0-9]{1}"
)
phone_regex = re.compile(phone_regex_str)


async def get_page_content(session: aiohttp.ClientSession, url: str):
    """load web-page by url"""
    async with session.get(url) as resp:
        return await resp.text()


def find_phones_in_html(text: str) -> ty.List[ty.Iterable[str]]:
    """find phones in text/html"""
    return phone_regex.findall(text)


def make_phone_format(phones: ty.List[ty.Iterable[str]]) -> ty.List[str]:
    """return phone in right format"""
    return ["".join(phone) for phone in phones]


async def scrape_pages_phones(urls: ty.List[str]):
    """scrape web-pages asynchronously, find phones and return dict with phones in right format"""
    res = {}

    async with aiohttp.ClientSession() as session:
        for url in urls:
            text = await get_page_content(session, url)
            text = find_phones_in_html(text)
            res[url] = make_phone_format(text)
        return res


def get_phones_in_web_pages(urls: ty.List[str]) -> ty.Dict[str, ty.List[str]]:
    """scrape web-pages for phones (start async loop)"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(scrape_pages_phones(urls))
    return result
