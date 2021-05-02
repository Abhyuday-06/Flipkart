from bs4 import BeautifulSoup
from urllib.request import urlopen as uopen

user_input = input("Enter the name of the thing that you want to search on Flipkart:")
n = user_input.replace(' ', '+')
flipkart_url = 'https://www.flipkart.com/search?q=' + str(n) 


def download_data(url):
    response = uopen(url)
    page_html = response.read()
    response.close()
    soup = BeautifulSoup(page_html,'html.parser')
    containers = soup.findAll("div", {'class': "_13oc-S"})
    cnt = len(containers)
    for i in range(0, cnt):
        print(i + 1, '--------')
        try:
            print("Name:", containers[i].find("a", {'class': 's1Q9rs'}).text)
        except AttributeError:
            print("", end='')
        try:
            print("Name:", containers[i].find("div", {'class': '_4rR01T'}).text)
        except AttributeError:
            print("", end='')
        try:
            print("It's price is ", containers[i].find("div", {'class': '_30jeq3'}).text)
        except AttributeError:
             print("", end='')
        try:
            print("It's price is ", containers[i].find("div", {'class': '_30jeq3 _1_WHN1'}).text)
        except AttributeError:
             print("", end='')
        try:
            print("Some description:", containers[i].find("li", {'class': 'rgWa7D'}).text)
        except AttributeError:
            print("", end='')
        try:
            print("Some description:", containers[i].find("div", {'class': '_3Djpdu'}).text)
        except AttributeError:
            print("")


download_data(flipkart_url)
