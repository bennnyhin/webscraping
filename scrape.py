import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = "https://www.amazon.ca/s?k=monitor&rh=p_72%3A11192170011&dc&qid=1599078110&rnid=11192166011&ref=sr_nr_p_72_1"

#Create connection to website 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#create create list of containers which have information about product
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"a-section a-spacing-medium"})

container = containers[0]

rating_container = container.findAll("span", {"class": "a-size-base"})
number_ratings = rating_container[0].text
print(number_ratings)

# link = container.findAll("a", {"class": "a-link-normal a-text-normal"})
# print(link["href"]


#trying to get the link of each of the products to get more in-depth information

# link = container2.finalAll("a", {"class": "a-link-normal"})
# print(link)

# href = container.findAll("a", {"class": "a-link-normal s-no-outline"})
# print(href)