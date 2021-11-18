# Regular sync webscrapper that gets target url addresses
# from text file

import datetime

import bs4
import requests


url_addreses = []

try:
    with open("news_sites.txt", "r", encoding="utf-8") as file:
        for line in file:
            stripped_line = line.strip()
            url_addreses.append(stripped_line)
        # print(url_addreses[:15])
except FileNotFoundError:
    print("Can't find the file")


def get_url(address: str) -> tuple:
    """
    Build url address and gets html text of
    """
    url = f"https://{address}"

    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text, address
    except (requests.exceptions.InvalidHeader, requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError):
        return None, address


def get_title(html_text: str) -> str:
    if html_text:
        soup = bs4.BeautifulSoup(html_text, 'html.parser')
        header = soup.select_one('title')
        # print(header.text)
        if not header:
            return "Missing title"
        return header.text.strip()
    return "No html data"


def get_all_titles():
    for url in url_addreses:
        html, address = get_url(url)
        title = get_title(html)
        print(f"{address} - {title}.")


def main():
    t_start = datetime.datetime.now()
    get_all_titles()
    t_total = datetime.datetime.now() - t_start
    print(f"Done in {t_total.total_seconds():.2f} sec.")



if __name__ == '__main__':
    main()
