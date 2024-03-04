from bs4 import BeautifulSoup
from datetime import datetime
from menu_parser import MenuParser

class DelikantiParser(MenuParser):
    def __init__(self, soup: BeautifulSoup, canteen_id: int):
        super().__init__(soup, canteen_id)
        self.price = "4.00"

    def parse_daily_offer(self) -> list:
        offer = self.soup.find("table", class_="prif-denne-table")
        days = offer.find_all("th", rowspan="6", limit=5)
        days_offer = []
        for day in days:
            days_offer += self.parse_day_offer(day)
        return days_offer


    def parse_day_offer(self, day: BeautifulSoup) -> list[dict]:
        date_title = day.text.split()[1]
        date = datetime.strptime(date_title, "%d.%m.%Y")
        date = date.strftime("%Y-%m-%d")
        soup_name = day.find_next_sibling().find_next_sibling().text.strip()
        element = day.find_parent("tr")
        meals = [{"name": soup_name, "price": self.price, "day": date, "canteen_id": self.canteen_id}]
        for i in range(4):
            element = element.find_next_sibling()
            meals.append(self.parse_meal(element, date))
        return meals

    def parse_meal(self, meal: BeautifulSoup, date: str) -> dict:
        name = meal.find_all("td")[1].text.strip()
        return {"name": name, "price": self.price, "day": date, "canteen_id": self.canteen_id}