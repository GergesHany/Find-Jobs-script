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
jop_posted = []
job_titles = []
jop_skills = []
requirements = []
company_names = []
location_names = []

number_of_page = 0

while True:

    try:
        # 2 - step use requests to fetch the page url
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbg&q=python&start={number_of_page}")

        # 3 - step save page content in a variable
        src = result.content
        # print(src)


        # 4 - step use beautifulsoup to parse the page content
        # lxml is a parser that is used to parse the page content
        soup = BeautifulSoup(src, "lxml")
        # print(soup)
        

        page_limit = soup.find("strong").text
        page_limit = int(page_limit)

        if number_of_page >= page_limit // 15:
            print("Done all pages")
            break

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
        posted_new = soup.find_all("div", {"class": "css-4c4ojb"})
        # print(posted_new)
        posted_old = soup.find_all("div", {"class": "css-do6t5g"})
        # print(posted_old)

        posted = [*posted_new, *posted_old]

        # 6 - step extract the text from the job card element
        for i in range(len(job_title)):
            jop_ti = job_title[i].text
            jop_ti = jop_ti.replace("-", "")
            job_titles.append(jop_ti)
            links.append(job_title[i].get("href"))
            comp = company_name[i].text
            comp = comp.replace("-", "")
            company_names.append(comp)
            location_names.append(location_name[i].text)
            jop_skills.append(jop_skill[i].text)
            jop_posted.append(posted[i].text.strip())

        print(f"Page {number_of_page} Done")
        number_of_page += 1

    except:
        print("Error")
        break

# for lin in links:
#    result1 = requests.get(lin)
#    src1 = result1.content
#    soup1 = BeautifulSoup(src1, "lxml")
#    salary = soup1.find("span", {"class": "css-47jx3m"}).text
#    salarys.append(salary)
#    req = soup1.find("section", {"class": "css-ghicub"}).text
#    requirements.append(req)

# 7 - step save the data in csv file and fill the values
with open("/home/gerges/Web Scraping/jops.test.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(["Job Title", "Company Name", "Location", "Jop Skills", "Link", "Salary", "Requirements", "Jop Posted"])
    wr.writerows(zip_longest(job_titles, company_names, location_names, jop_skills, links, salarys, requirements, jop_posted))
