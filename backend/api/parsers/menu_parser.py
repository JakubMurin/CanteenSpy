from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class MenuParser(ABC):
    def __init__(self, soup: BeautifulSoup, canteen_id: int):
        self.soup = soup
        self.canteen_id = canteen_id

    @abstractmethod
    def parse_daily_offer(self) -> list:
        pass

    @abstractmethod
    def parse_day_offer(self, day: BeautifulSoup) -> list[dict]:
        pass

    @abstractmethod
    def parse_meal(self, meal: BeautifulSoup, date: str) -> dict:
        pass