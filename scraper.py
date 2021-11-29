import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

# url = 'https://reviews.birdeye.com/reside-707-156792934137505'
# url = 'https://reviews.birdeye.com/the-drake-hotel-144625764558018'
url = 'https://reviews.birdeye.com/the-guesthouse-hotel-149199612803232'
response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

# m = soup.find_all('div', "Review__mainReviewWrapper__31Kf0")
m = soup.find_all("span", "Review__reviewPara__2qFYA")
# print(len(m))

# rating = soup.find_all("span", "RatingStar__bew-avgstars__2enAh")
rating = soup.find_all("div", "Review__starWrapper__2nXNj")
count = 0
# print(len(rating))

# for i in range(len(m)):
#     print("new " + str(i))
#     list1 = list(rating[i])
#     # print(list1)
#     count = 0
#     for elem in list1:
#         on = elem.find("span", "RatingStar__be-star-on__28Wmg")
#         if on is not None:
#             count += 1
#         # print(count)
#         # print(elem.find("span", "RatingStar__be-star-on__28Wmg"))
#         print()
#     print(count)
    # if ("RatingStar__be-star-on__28Wmg" in list1):
    #         print("h")
    # for l in list1:
    #     e = list(l)
    #     # print(len(e))
    #     # matching = [d for d in e if "RatingStar__be-star-on__28Wmg" in d]
    #     # print(matching)
    #     # print()
    #     for tag in e:
    #         print(tag.find("span")['class'])
    #         # j = "RatingStar__be-star-on__28Wmg"
    #         # print(e.contains(j))
    #         print(tag)
    #         print()
        # if ("RatingStar__be-star-on__28Wmg" in l):
        #     print("h")
        # print(l.contains("RatingStar__be-star-on__28Wmg"))
    # print(l.count("RatingStar__be-star-on__28Wmg"))
    # link = rating[i]['span']
    # print()
    # print(link)
    # print()
# for r in rating:
#     e = soup.find_all("span", "RatingStar__be-star-on__28Wmg")
#     print("hello: " + str(e))
#     print()
# print(rating)

# time.sleep(1)

# open the file in the write mode

# import pandas as pd
# df = pd.read_csv('test.csv', header=None)
# df.rename(columns={0: 'name', 1: 'id'}, inplace=True)
# df.to_csv('test_with_col.csv', index=False) # save to new csv file

f = open('/Users/melissacho/Documents/cs410/defgh.csv', "w")

# # create the csv writer
writer = csv.writer(f)
# r = csv.reader(f)
# row0 = next(r)
# row0.append(["Summary", "Text", "Score"])

# # write a row to the csv file

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
            # print(count)
            # print(elem.find("span", "RatingStar__be-star-on__28Wmg"))
            # print()
    # print(count)
    if count == 0:
        row.append(0)
    else:
        row.append(count)

    writer.writerow(row)
    # print(row)

    i+= 1

    # print(summary)
    # print(text)
    # print(element))
    # writer.writerow(element)
    time.sleep(1)



# # close the file
# f.close()
