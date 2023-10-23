import requests
from bs4 import BeautifulSoup

# Indicar url de la pagina
url = ""

if __name__ == "__main__":
     page = requests.get(url)
     soup = BeautifulSoup(page.content, 'html.parser')

     def has_data_search(tag):
          return tag.has_attr("data-search-sol-meta")
     
     results = soup.find_all(has_data_search)

     for job in results:
        try:
            title = job.find("a", attrs={"data-automation": "jobTitle"}).get_text()
            company = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
            joblink = "" + job.find("a", attrs={"data-automation": "jobTitle"})["href"]
            salary = job.find("span", attrs={"data-automation": "jobSalary"})

        except Exception as e:
            print("Exception: {}".format(e))
            pass