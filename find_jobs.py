# 1 - step install and import modules

# --> (pip, pip3) install requests
# --> (pip, pip3) install lxml
# --> (pip, pip3) install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


links = []
salarys = []
job_titles = []
jop_skills = []
requirements = []
company_names = []
location_names = []


# 2 - step use requests to fetch the page url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=navbg")

# 3 - step save page content in a variable
src = result.content
# print(src)

# 4 - step use beautifulsoup to parse the page content

# lxml is a parser that is used to parse the page content
soup = BeautifulSoup(src, "lxml")
# print(soup)

# 5 - step find the element that contains the job cards
# find job_title, jop_skill, company_name, location

job_title = soup.find_all("a", {"class": "css-17s97q8"})
# print(job_title)
company_name = soup.find_all("a", {"class": "css-17s97q8"})
# print(company_name)
location_name = soup.find_all("span", {"class": "css-5wys0k"})
# print(location_name)
jop_skill = soup.find_all("div", {"class": "css-y4udm8"})
# print(jop_skill)


# 6 - step extract the text from the job card element
for i in range(len(job_title)):
    job_titles.append(job_title[i].text)
    links.append(job_title[i].get("href"))
    company_names.append(company_name[i].text)
    location_names.append(location_name[i].text)
    jop_skills.append(jop_skill[i].text)


# 7 - step save the data in csv file and fill the values
with open("/home/gerges/Web Scraping/jops.test.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(["Job Title", "Company Name", "Location", "Jop Skills", "Link", "Salary", "Requirements"])
    wr.writerows(zip_longest(job_titles, company_names, location_names, jop_skills, links, salarys, requirements))

