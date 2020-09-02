import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.amazon.ca/s?k=monitor&rh=p_72%3A11192170011&dc&qid=1599078110&rnid=11192166011&ref=sr_nr_p_72_1"

#Create connection to website 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"a-section a-spacing-medium"})

containers2 = page_soup.findAll("div", {"class": "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"})
container2 = containers2[0]
link = container2.finalAll("a", {"class": "a-link-normal"})
print(link)


container = containers[0]

# href = container.findAll("a", {"class": "a-link-normal s-no-outline"})
# print(href)


# rating_container = container.findAll("span", {"class": "a-size-base"})
# number_ratings = rating_container[0].text

