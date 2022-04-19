import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Sterilizer/dp/B083KM6BZS/ref=sr_1_2_sspa?crid=3VGJCVAAVO16D&keywords=Instant%2BPot%2BDuo%2BEvo%2BPlus%2B10-in-1%2BPressure%2BCooker&qid=1650373231&sprefix=instant%2Bpot%2Bduo%2Bevo%2Bplus%2B10-in-1%2Bpressure%2Bcooker%2Caps%2C165&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSTFSUTExMlRISFJYJmVuY3J5cHRlZElkPUEwNDk4MjUxMkdONjEwQ0REUjhDSyZlbmNyeXB0ZWRBZElkPUEwMzU3ODI1M0FWMDg4N1lYWjNYQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
header = {
    "Accept-Language": "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.82 Safari/537.36"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 90
my_email = "erkan09@hotmail.co.uk"
password = "geliveringari9"

if price_as_float < BUY_PRICE:
    message=f"{title} is now{price}"

    with smtplib.SMTP("smtp-mail.outlook.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="erkan0901@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}")

