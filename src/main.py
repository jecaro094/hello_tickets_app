
# from pathlib import Path
from src.utils import get_logger, get_data_from_hello_tickets
# from src.requests import HelloTicketsAPIClient
# import src.constants as const
# import pandas as pd

logger = get_logger(__name__)


# file_name = 'experiences.csv'
# future_date = "2026-07-24"
# file_path = Path().cwd() / file_name

# df = pd.read_csv(file_path)
        
# for idx, row in df.iterrows():
#     product_id = int(row['product_id'])
#     test_url = row['link']


# api_client = HelloTicketsAPIClient(
#     base_url=const.BASE_URL_HELLO_TICKETS, 
# )

# product_endpoint = f"products/{product_id}"
# dates_endpoint = f"products/{product_id}/dates"
# options_endpoint = f"products/{product_id}/tour-grades"

# # product_data = get_data_from_hello_tickets(api_client, product_endpoint, logger)
# dates_data = get_data_from_hello_tickets(api_client, dates_endpoint, logger)

# # TODO Improve
# date = next(iter(dates_data.get('dates', [])), {})
# date_value = date.get('date', None)
# date_payload = {'date': date_value} if date_value else {'date': future_date}

# options_data = get_data_from_hello_tickets(
#     api_client,
#     options_endpoint, 
#     logger,
#     params=date_payload
# )


## NOTE The commented (above) stands for hellotickets info retrieval
## NOTE The below, stands for amigos provider info retrieval.

import re
import json
import requests
from bs4 import BeautifulSoup

url = "https://amigotours.com/tours/united-states/new-york/niagara-falls-washington-philly-tour-from-new-york"

# Step 1: Fetch HTML
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# Step 2: Extract the JSON blob containing ventrataId
json_blob = None
for script in soup.find_all("script"):
    if script.string and "ventrataId" in script.string:
        json_blob = script.string
        break

if not json_blob:
    raise ValueError("Could not find embedded JSON")

# Step 3: Extract JSON object
match = re.search(r'\{.*"ventrataId".*\}', json_blob, re.DOTALL)
data = json.loads(match.group(0))

product_id = data["props"]['pageProps']['tour']['ventrataId']
print("Product ID:", product_id)

# Step 4: Fetch Ventrata product info to get optionId
api_url = f"https://amigotours.com/api/ventrata/product?productId={product_id}"
product_data = requests.get(api_url).json()
# NOTE From product data, retrieve title and description.

option_id = product_data["options"][0]["id"]
print("Option ID:", option_id)


# NOTE From below, retrieve options.
# https://amigotours.com/api/ventrata/availability?productId=b78934e0-6cce-4d52-842b-bf62556a0800&optionId=8da8b39e-5875-43b3-9439-23673fe99d5d&localDateStart=2026-06-01&localDateEnd=2026-06-30