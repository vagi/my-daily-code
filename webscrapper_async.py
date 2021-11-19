# coding=utf-8

import bs4
import asyncio
import aiohttp

import datetime


url_addresses = []
# Gets data from text file, cleans it
# and builds urls addresses
try:
    with open("news_sites.txt", "r", encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split("|")[0]
            url_addresses.append(f"https://{stripped_line}")
except FileNotFoundError:
    print("Can't find the file")


async def get_html_content(url: str) -> str:
    """
    Gets html text from all urls addresses asynchronously
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                resp.raise_for_status()
                return await resp.text()
        except (aiohttp.ClientConnectionError, aiohttp.ClientResponseError):
            await session.close()


async def get_title(html_text: str) -> str:
    """
    Parses header of each html page using tag <title>
    """
    if html_text:
        soup = bs4.BeautifulSoup(html_text, 'html.parser')
        header = soup.select_one('title')
        if not header:
            return "Missing title"
        return header.text.strip()
    return "No html data"


async def get_all_titles() -> None:
    """
    Creates tasks as many as there are url addresses in the list
    and executes them in the loop
    """
    tasks = []
    for url in url_addresses:
        tasks.append((url, asyncio.get_event_loop().create_task(get_html_content(url))))    # get_event_loop.create_task

    for url, data in tasks:
        html = await data
        title = await get_title(html)
        address = url.split("//")[-1]
        print(f"{address} - {title}.")


def main() -> None:
    t_start = datetime.datetime.now()
    asyncio.run(get_all_titles())
    t_total = datetime.datetime.now() - t_start
    print(f"Done in {t_total.total_seconds():.2f} sec.")



if __name__ == '__main__':
    main()
