from bs4 import BeautifulSoup
from datetime import datetime
from menu_parser import MenuParser

class FreeFoodParser(MenuParser):
    def __init__(self, soup: BeautifulSoup, canteen_id: int, canteen: str):
        super().__init__(soup, canteen_id)
        self.canteen = canteen

    def parse_daily_offer(self) -> list:
        offer = self.soup.find(id=self.canteen)
        day_offers = offer.find("ul", class_="daily-offer").find_all("li", recursive=False)
        days = map(self.parse_day_offer, day_offers)
        menus = [menu for d in days for menu in d]
        return menus


    def parse_day_offer(self, day: BeautifulSoup) -> list[dict]:
        date_title = day.find("span", class_="day-title").text.split(", ")[1]
        date = datetime.strptime(date_title, "%d.%m.%Y")
        date = date.strftime("%Y-%m-%d")
        meals = day.find_all("li")
        meals = map(lambda m: self.parse_meal(m, date), meals)
        return list(meals)


    def parse_meal(self, meal: BeautifulSoup, date: str) -> dict:
        name, alergen = meal.find(text=True, recursive=False).split("A:")
        name = f"{name.strip()} ({alergen.strip()})"
        price = meal.find("span", class_="brand price").text.strip("€")
        return {"name": name, "price": price, "day": date, "canteen_id": self.canteen_id}
