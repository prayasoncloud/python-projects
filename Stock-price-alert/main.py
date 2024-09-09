import requests
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK = "QA13QMWBH2DKHI7G"

API_KEY_NEWS = "da07f2541c744da9bfdaf1a028761cb2"

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": "TSLA",
#     "apikey": API_KEY_STOCK
# }

# response = requests.get(url="https://www.alphavantage.co/query?", params=parameters)
# response.raise_for_status()
# tsla_data = response.json()

# def percentage_finder():
#     tsla_data = tsla_data["Time Series (Daily)"]

#     tsla_data = iter(tsla_data)
#     day1 = next(tsla_data)
#     day2 = next(tsla_data)

#     diff = day1 - day2
#     percentage = (diff * 100) / day2 
#     return percentage

# stock= "https://www.alphavantage.co/"

# News= "https://newsapi.org/"

param = {
    "apikey": API_KEY_NEWS,
    "category": "business"
}
response = requests.get(url="https://newsapi.org/v2/top-headlines?", params=param)
response.raise_for_status()
news_data = response.json()
print(f"news data is a {type(news_data)}")

headline = news_data["articles"][0]["title"]

print(f"Headline is a {type(headline)}")

print(headline)


# SMS= "https://www.twilio.com/en-us"

"""

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""