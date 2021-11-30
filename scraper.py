import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd


def parse(url, flag):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    m = soup.find_all("span", "Review__reviewPara__2qFYA")

    rating = soup.find_all("div", "Review__starWrapper__2nXNj")
    count = 0

    f = open('/Users/melissacho/Documents/cs410/scraper4.csv', "a")

    # # create the csv writer
    writer = csv.writer(f)

    if flag == 1:
        writer.writerow(["Summary", "Text", "Score"])
    i = 0
    for element in m:
        row = []
        split_list = element.get_text(strip=True, separator='\n').splitlines()

        if (0 < len(split_list)):
            summary = split_list[0]
        else:
            summary = ''

        if (1 < len(split_list)):
            text = split_list[1]
        else:
            text = ''

        row.append(str(summary))
        row.append(str(text))

        # print("i" + str(i))
        if i > 8:
            break;
        list1 = list(rating[i])
        # print(list1)
        count = 0
        for elem1 in list1:
            list2 = elem1.find("span", "RatingStar__bew-avgstars__2enAh")
            for elem in list2:
                # print("elem: " + str(elem))
                on = elem.find("span", "RatingStar__be-star-on__28Wmg")
                if on is not None:
                    count += 1
 
        if count == 0:
            #neutral
            row.append(3)
        else:
            row.append(count)

        writer.writerow(row)
        # print(row)

        i+= 1

        time.sleep(1)


# url = 'https://reviews.birdeye.com/reside-707-156792934137505'
# url = 'https://reviews.birdeye.com/the-drake-hotel-144625764558018'
url = 'https://reviews.birdeye.com/the-guesthouse-hotel-149199612803232'

parse(url, 1)

for i in range(2, 55):
    url1 = 'https://reviews.birdeye.com/the-guesthouse-hotel-149199612803232' + '?page=' + str(i)
    print(url1)
    parse(url1, 0)
