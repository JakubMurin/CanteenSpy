from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from menu_parser import MenuParser


class EatMeatParser(MenuParser):

    def parse_daily_offer(self) -> list:
        days_offer = []
        for i in range(1, 8):
            day = self.soup.find("div", id=f"day-{i}")
            days_offer += self.parse_day_offer(day)
        return days_offer
    
    def parse_day_offer(self, day: BeautifulSoup) -> list[dict]:
        if day.text.strip() == "ZATVORENÉ":
            return []
        date = self.date_in_current_week(int(day.get("id")[-1]))
        meals = day.find_all("div", class_="menu-details")
        meals = map(lambda m: self.parse_meal(m, date), meals)
        return list(meals)
    
    def parse_meal(self, meal: BeautifulSoup, date: str) -> dict:
        name = meal.find("p", class_="desc").text
        price = meal.find("span", class_="price").text
        price = price.split()[0].replace(",", ".")
        return {"name": name, "price": price, "day": date, "canteen_id": self.canteen_id}
    
    def date_in_current_week(self, day_no: int) -> str:
        date = datetime.now()
        today_no = date.weekday()
        delta_days = day_no - today_no - 1
        date += timedelta(days=delta_days)
        return date.strftime("%Y-%m-%d")