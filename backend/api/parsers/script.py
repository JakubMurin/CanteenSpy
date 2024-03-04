from bs4 import BeautifulSoup
import requests
from freefood import FreeFoodParser
from delikanti import DelikantiParser
from eat_and_meat import EatMeatParser

free_food = {"free-food": 2,
            "fayn-food": 4,
            "fiit-food": 5}

free_food_url = "http://www.freefood.sk/menu"
eat_and_meat_url = "http://eatandmeet.sk/tyzdenne-menu"
delikanti_url = "https://www.delikanti.sk/prevadzky/3-jedalen-prif-uk/"


# FREEFOOD #
# for canteen, canteen_id in free_food.items():
#     response = requests.get(free_food_url)

#     # Check if the request was successful (status code 200)
#     if response.status_code != 200:
#         print('Failed to fetch the HTML content. Status code:', response.status_code)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     free_parser = FreeFoodParser(soup, canteen_id, canteen)
#     with open(f"{canteen}.json", "w", encoding="utf-8") as file:
#         print(free_parser.parse_daily_offer(), file=file)


# DELIKANTI #
# response = requests.get(delikanti_url)

# Check if the request was successful (status code 200)
# if response.status_code != 200:
#     print('Failed to fetch the HTML content. Status code:', response.status_code)
# soup = BeautifulSoup(response.text, 'html.parser')

# DELIKANTI DEMO
with open("api/parsers/delikanti.html", "r", encoding="utf-8") as file:
    response = file.read()
soup = BeautifulSoup(response, 'html.parser')

delikanti_parser = DelikantiParser(soup, 3)
with open("delikanti.json", "w", encoding="utf-8") as file:
    print(delikanti_parser.parse_daily_offer(), file=file)

# EAT & MEAT #
response = requests.get(eat_and_meat_url)

if response.status_code != 200:
    print('Failed to fetch the HTML content. Status code:', response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
eat_meat_parser = EatMeatParser(soup, 1)
with open("eat_meat.json", "w", encoding="utf-8") as file:
    print(eat_meat_parser.parse_daily_offer(), file=file)




