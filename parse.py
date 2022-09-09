import httpx
import asyncio
import datetime

from dataclasses import dataclass
from bs4 import BeautifulSoup
from tqdm import tqdm


from db_manager import add_data_to_db

HOME_PAGE = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/"


@dataclass
class Advertisement:
    image: str
    title: str
    data: str
    city: str
    beds: str
    descriptions: str
    price: str
    currency: str


def parse_single_advertisement(advertisement_soup: BeautifulSoup):
    title = advertisement_soup.select_one(".title").text.strip()
    unformatted_date = (
        advertisement_soup.select_one(".date-posted").text.strip().replace("/", "-")
    )
    data_is_today = unformatted_date[0] == "<"
    data = (
        unformatted_date
        if data_is_today is False
        else datetime.date.today().strftime("%d-%m-%Y")
    )

    city = advertisement_soup.select_one(".location > span").text.strip()
    beds = (
        advertisement_soup.select_one(".bedrooms")
        .text.strip()
        .replace("\n", " ")
        .replace("  ", "")
    )
    descriptions = (
        advertisement_soup.select_one(".description")
        .text.strip()
        .replace("\n", " ")
        .replace("  ", "")
    )

    unformatted_price = advertisement_soup.select_one(".price").text.strip()
    price_is_indicated = unformatted_price[0] != "P"

    price = unformatted_price[1:] if price_is_indicated is True else unformatted_price
    currency = unformatted_price[0] if price_is_indicated is True else "-"

    images = advertisement_soup.select(".image")
    images = images[0].find_all("img")[0]
    image = images["data-src"] if images.has_attr("data-src") else images["src"]

    add_data_to_db(
        image=image,
        title=title,
        data=data,
        city=city,
        beds=beds,
        descriptions=descriptions,
        price=price,
        currency=currency,
    )


def get_single_page_advertisement(page_soup: BeautifulSoup):
    quotes = page_soup.select(".search-item")
    return [parse_single_advertisement(quote) for quote in quotes]


def get_all_advertisement():
    response = httpx.get(f"{HOME_PAGE}c37l1700273/")
    first_page_soup = BeautifulSoup(response.content, "html.parser")
    all_quote = get_single_page_advertisement(first_page_soup)

    for page_index in tqdm(range(2, 94)):
        response = httpx.get(f"{HOME_PAGE}/page-{page_index}/c37l1700273")
        page_soup = BeautifulSoup(response.content, "html.parser")
        all_quote.extend(get_single_page_advertisement(page_soup))

    return all_quote


if __name__ == "__main__":
    get_all_advertisement()
