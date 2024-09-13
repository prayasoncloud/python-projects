import requests
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK = "" #please have a look here 
API_KEY_NEWS = "" #please have a look here 



# stock= "https://www.alphavantage.co/"

# parameters_stock = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": "TSLA",
#     "apikey": API_KEY_STOCK
# }

# response = requests.get(url="https://www.alphavantage.co/query?", params=parameters_stock)
# response.raise_for_status()
# tsla_data_raw = response.json()
# tsla_data = tsla_data_raw["Time Series (Daily)"]

# def percentage_finder():
#     tsla_data = tsla_data_raw["Time Series (Daily)"]

#     tsla_data_iter = iter(tsla_data)
#     day1 = next(tsla_data_iter)
#     day2 = next(tsla_data_iter)
#     day1 = tsla_data[day1]["4. close"]
#     day2 = tsla_data[day2]["4. close"]

#     diff = float(day1) - float(day2)
#     percentage = (diff * 100) / float(day2) 
#     return percentage






# News= "https://newsapi.org/"





parameters_news = {
    "apikey": API_KEY_NEWS,
    "category": "business"
}
response = requests.get(url="https://newsapi.org/v2/top-headlines?", params=parameters_news)
response.raise_for_status()
news_data = response.json()

print(f"news data is a {type(news_data)}")


headline = news_data["articles"][0]["title"]


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