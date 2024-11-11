import bs4
import requests
url="https://www.premierleague.com/fixtures"


r=requests.get(url)


soup=bs4.BeautifulSoup(r.content,"html.parser")

print(soup.prettify())