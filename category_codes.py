import requests
from bs4 import BeautifulSoup

#print(page.text)

#recipe_elements = results.find_all("div", class_="")

def get_codes():
  URL = ""
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  job_elements = soup.find_all("div", class_="code_list__code-list-table")
  for job_element in job_elements:
    codes = job_element.find_all("td", class_="code")
    for code in codes:
      code = code.string.strip()
      print(code)

get_codes()
