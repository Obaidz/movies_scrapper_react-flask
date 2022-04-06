import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import pymongo
import certifi
import datetime




# Database connection

URI = "mongodb+srv://obaidu467:obaidcool@cluster0.kurvu.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())
db = client["fin_project"]
mo_data = db["movie_data"]

# ==========================



# 2000 all movies
list_2000 = []

#Dataset 2001
list_2001 = []

#Dataset 2002
list_2002 = []

#Dataset 2003
list_2003 = []

#Dataset 2004
list_2004 = []

#Dataset 2005
list_2005 = []

#Dataset 2006
list_2006 = []

#Dataset 2007
list_2007 = []

#Dataset 2008
list_2008 = []

#Dataset 2009
list_2009 = []

#Dataset 2010
list_2010 = []

#Dataset 2011
list_2011 = []

#Dataset 2012
list_2012 = []

#Dataset 2013
list_2013 = []

#Dataset 2014
list_2014 = []

#Dataset 2015
list_2015 = []

#Dataset 2016
list_2016 = []

#Dataset 2017
list_2017 = []

#Dataset 2018
list_2018 = []

#Dataset 2019
list_2019 = []

#Dataset 2020
list_2020 = []

#Dataset 2021
list_2021 = []

#Dataset 2022
list_2022 = []

# Scrape Def
def scrape(strg, num, lis):
    contr = 1
    while contr < num:
        url2 = strg % contr
        res = requests.get(url2)

        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.findAll('div', attrs= {'class' : 'lister-item mode-advanced'})


        for link in data:


            #Getting data
            name = link.h3.a.text
            year = link.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(', '').replace(')', '') 
            time = link.p.find('span', class_ = 'runtime').text.replace(' min', '') if link.p.find('span', class_ = 'runtime') else 'none'
            gen = link.p.find('span', class_ = 'genre').text.replace(' ', '').replace('\n' , '') if link.p.find('span', class_ = 'genre') else 'none'
            rating = link.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n', '') if link.find('div', class_ = 'inline-block ratings-imdb-rating') else 'none'
            total_v = link.find_all('span', attrs = {'name' : 'nv'}) if link.find_all('span', attrs = {'name' : 'nv'}) else 'none'
            try:
                votes = total_v[0].text.replace(" ", '') if len(total_v) > 0 else 'Not Found'

            except AttributeError as err:
                votes = 'None'

            try:
                gross_p = total_v[1].text.replace(" ", '') if len(total_v) > 1 else 'Not Found'

            except AttributeError as err:
                gross_p = 'None'


            plt = link.find_all("p", {"class":  "text-muted"})
            my_plt = plt[1].text.replace('\n', '') if len(plt) > 1 else 'Not Found'
            imageDiv =  link.find("div", {"class": "lister-item-image float-left"})
            image = imageDiv.find("img", "loadlate")['loadlate']


            


            for i in range(0,1):
                val = link.find("p", {"class":  ""} ).text.replace('  ', '').replace('\n' , '').replace('|', '').replace('Director:', '').replace('Stars:', ', ').replace(' ,', ',') if link.find("p", {"class":  ""} ) else "Not Found" 
                #star.append(val)


            data = {"movie_title": name,
            "year": year,
            "runtime": time,
            "genre": gen,
            "rating": rating,
            "votes": votes,
            "gross_profit": gross_p,
            "crew": val,
            "plot": my_plt,
            "image": image,
            "href": link.h3.a['href'],
            "created_daytime": str(datetime.datetime.now())}
            
            lis.append(data)
            #Append





        contr += 50



# Method for cheching if field exists in data base
def add_db(lst):
    my_ctr = 0
    add_ctr = 0
    for i in lst:
        dub = mo_data.find({"movie_title" : i["movie_title"]})
        cnt = 0

        for j in dub:
            cnt += 1

        if cnt < 1:
            mo_data.insert_one(i)
            add_ctr += 1
        else:
            pass
        my_ctr += 1

    print("Total scraped: ", my_ctr)
    print("Inserted", add_ctr)

# Calling scrape on 2000 datasets
'''
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2000-01-01,2000-12-31&start=%s&ref_=adv_prv',
       6000, list_2000)

add_db(list_2000)


# Calling scrape on 2001 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2001-01-01,2001-12-31&start=%s&ref_=adv_nxt',
       6000, list_2001)

add_db(list_2001)


# Calling scrape on 2002 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2002-01-01,2002-12-31&start=%s&ref_=adv_nxt',
       6000, list_2002)
add_db(list_2002)

# Calling scrape on 2003 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2003-01-01,2003-12-31&start=%s&ref_=adv_nxt',
       6000, list_2003)

add_db(list_2003)



# Calling scrape on 2004 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2004-01-01,2004-12-31&start=%s&ref_=adv_nxt',
       6000, list_2004)

add_db(list_2004)



# Calling scrape on 2005 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2005-01-01,2005-12-31&start=%s&ref_=adv_nxt',
       6000, list_2005)

add_db(list_2005)


# Calling scrape on 2006 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2006-01-01,2006-12-31&start=%s&ref_=adv_nxt',
       6000, list_2006)

add_db(list_2006)



# Calling scrape on 2007 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2007-01-01,2007-12-31&start=%s&ref_=adv_nxt',
       6500, list_2007)
add_db(list_2007)



# Calling scrape on 2008 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2008-01-01,2008-12-31&start=%s&ref_=adv_nxt',
       7000, list_2008)
add_db(list_2008)
print("data 2008 has been moved to DB")



# Calling scrape on 2009 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2009-01-01,2009-12-31&start=%s&ref_=adv_nxt',
       8000, list_2009)
add_db(list_2009)
print("data 2009 has been moved to DB")



# Calling scrape on 2010 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2010-12-31&start=%s&ref_=adv_nxt',
       8000, list_2010)
add_db(list_2010)
print("data 2010 has been moved to DB")



# Calling scrape on 2011 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2011-01-01,2011-12-31&start=%s&ref_=adv_nxt',
       9000, list_2011)
add_db(list_2011)
print("data 2011 has been moved to DB")



# Calling scrape on 2012 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2012-01-01,2012-12-31&start=%s&ref_=adv_nxt',
       9500, list_2012)
add_db(list_2012)
print("data 2012 has been moved to DB")


# Calling scrape on 2013 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2013-01-01,2013-12-31&start=%s&ref_=adv_nxt',
       10000, list_2013)
add_db(list_2013)
print("data 2013 has been moved to DB")


# Calling scrape on 2014 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2014-01-01,2014-12-31&start=%s&ref_=adv_nxt',
       10000, list_2014)
add_db(list_2014)
print("data 2014 has been moved to DB")


# Calling scrape on 2015 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2015-01-01,2015-12-31&start=%s&ref_=adv_nxt',
       10000, list_2015)
print("Scrapping Done")
add_db(list_2015)
print("data 2015 has been moved to DB")


# Calling scrape on 2016 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2016-01-01,2016-12-31&start=%s&ref_=adv_nxt',
       10000, list_2016)
print("Scrapping Done")
add_db(list_2016)
print("data 2016 has been moved to DB")

'''




'''
# Calling scrape on 2017 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2017-01-01,2017-12-31&start=%s&ref_=adv_nxt',
       10000, list_2017)

print("Scrapping Done")
add_db(list_2017)
print("data 2017 has been moved to DB")


# Calling scrape on 2018 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2018-01-01,2018-12-31&start=%s&ref_=adv_nxt',
       10000, list_2018)

print("Scrapping Done")
add_db(list_2018)
print("data 2018 has been moved to DB")


# Calling scrape on 2019 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2019-01-01,2019-12-31&start=%s&ref_=adv_nxt',
       10000, list_2019)
print("Scrapping Done")
add_db(list_2019)
print("data 2019 has been moved to DB")



# Calling scrape on 2020 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&start=%s&ref_=adv_nxt',
       10000, list_2020)
print("Scrapping Done")
add_db(list_2020)
print("data 2020 has been moved to DB")


# Calling scrape on 2021 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2021-01-01,2021-12-31&start=%s&ref_=adv_nxt',
       10000, list_2021)
print("Scrapping Done")
add_db(list_2021)
print("data 2021 has been moved to DB")


# Calling scrape on 2022 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&start=%s&ref_=adv_nxt',
       10000, list_2022)
print("Scrapping Done")
add_db(list_2022)
print("data 2022 has been moved to DB")

'''

# Calling scrape on 2017 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2017-01-01,2017-12-31&start=%s&ref_=adv_nxt',
       10000, list_2017)

print("Scrapping Done")
add_db(list_2017)
print("data 2017 has been moved to DB")

'''
# Calling scrape on 2018 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2018-01-01,2018-12-31&start=%s&ref_=adv_nxt',
       10000, list_2018)

print("Scrapping Done")
add_db(list_2018)
print("data 2018 has been moved to DB")


# Calling scrape on 2019 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2019-01-01,2019-12-31&start=%s&ref_=adv_nxt',
       10000, list_2019)
print("Scrapping Done")
add_db(list_2019)
print("data 2019 has been moved to DB")


# Calling scrape on 2020 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&start=%s&ref_=adv_nxt',
       10000, list_2020)
print("Scrapping Done")
add_db(list_2020)
print("data 2020 has been moved to DB")


# Calling scrape on 2021 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2021-01-01,2021-12-31&start=%s&ref_=adv_nxt',
       10000, list_2021)
print("Scrapping Done")
add_db(list_2021)
print("data 2021 has been moved to DB")


# Calling scrape on 2022 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&start=%s&ref_=adv_nxt',
       10000, list_2022)
print("Scrapping Done")
add_db(list_2022)
print("data 2022 has been moved to DB")

'''

'''
# Calling scrape on 2001 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2001-01-01,2001-12-31&start=%s&ref_=adv_nxt',
       6000, list_2001)

count1 = 0
for i in list_2001:
    count1 += 1
    print("")
    print(i)
print(count1)




# Calling scrape on 2002 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2002-01-01,2002-12-31&start=%s&ref_=adv_nxt',
       6000, list_2002)

count2 = 0
for i in list_2002:
    count2 += 1
    print("")
    print(i)
print(count2)



# Calling scrape on 2003 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2003-01-01,2003-12-31&start=%s&ref_=adv_nxt',
       6000, list_2003)

count3 = 0
for i in list_2003:
    count3 += 1
    print("")
    print(i)
print(count3)


# Calling scrape on 2004 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2004-01-01,2004-12-31&start=%s&ref_=adv_nxt',
       6000, list_2004)

count4 = 0
for i in list_2004:
    count4 += 1
    print("")
    print(i)
print(count4)


# Calling scrape on 2005 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2005-01-01,2005-12-31&start=%s&ref_=adv_nxt',
       6000, list_2005)

count5 = 0
for i in list_2005:
    count5 += 1
    print("")
    print(i)
print(count5)


# Calling scrape on 2006 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2006-01-01,2006-12-31&start=%s&ref_=adv_nxt',
       6000, list_2006)

count6 = 0
for i in list_2006:
    count6 += 1
    print("")
    print(i)
print(count6)


# Calling scrape on 2007 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2007-01-01,2007-12-31&start=%s&ref_=adv_nxt',
       6500, list_2007)

count7 = 0
for i in list_2007:
    count7 += 1
    print("")
    print(i)
print(count7)



# Calling scrape on 2008 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2008-01-01,2008-12-31&start=%s&ref_=adv_nxt',
       7000, list_2008)

count8 = 0
for i in list_2008:
    count8 += 1
    print("")
    print(i)
print(count8)


# Calling scrape on 2009 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2009-01-01,2009-12-31&start=%s&ref_=adv_nxt',
       8000, list_2009)

count9 = 0
for i in list_2009:
    count9 += 1
    print("")
    print(i)
print(count9)


# Calling scrape on 2010 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2010-12-31&start=%s&ref_=adv_nxt',
       8000, list_2010)

count10 = 0
for i in list_2010:
    count10 += 1
    print("")
    print(i)
print(count10)


# Calling scrape on 2011 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2011-01-01,2011-12-31&start=%s&ref_=adv_nxt',
       9000, list_2011)

count11 = 0
for i in list_2011:
    count11 += 1
    print("")
    print(i)
print(count11)


# Calling scrape on 2012 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2012-01-01,2012-12-31&start=%s&ref_=adv_nxt',
       9500, list_2012)

count12 = 0
for i in list_2012:
    count12 += 1
    print("")
    print(i)
print(count12)


# Calling scrape on 2013 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2013-01-01,2013-12-31&start=%s&ref_=adv_nxt',
       10000, list_2013)

count13 = 0
for i in list_2013:
    count13 += 1
    print("")
    print(i)
print(count13)



# Calling scrape on 2014 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2014-01-01,2014-12-31&start=%s&ref_=adv_nxt',
       10000, list_2014)

count14 = 0
for i in list_2014:
    count14 += 1
    print("")
    print(i)
print(count14)


# Calling scrape on 2015 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2015-01-01,2015-12-31&start=%s&ref_=adv_nxt',
       10000, list_2015)

count15 = 0
for i in list_2015:
    count15 += 1
    print("")
    print(i)
print(count15)


# Calling scrape on 2016 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2016-01-01,2016-12-31&start=%s&ref_=adv_nxt',
       10000, list_2016)

count16 = 0
for i in list_2016:
    count16 += 1
    print("")
    print(i)
print(count16)

# Calling scrape on 2017 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2017-01-01,2017-12-31&start=%s&ref_=adv_nxt',
       10000, list_2017)


# Calling scrape on 2018 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2018-01-01,2018-12-31&start=%s&ref_=adv_nxt',
       10000, list_2018)


# Calling scrape on 2019 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2019-01-01,2019-12-31&start=%s&ref_=adv_nxt',
       10000, list_2019)


# Calling scrape on 2020 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&start=%s&ref_=adv_nxt',
       10000, list_2020)

count20 = 0
for i in list_2020:
    count20 += 1
    print("")
    print(i)
print(count20)

# Calling scrape on 2021 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2021-01-01,2021-12-31&start=%s&ref_=adv_nxt',
       10000, list_2021)


# Calling scrape on 2022 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&start=%s&ref_=adv_nxt',
       10000, list_2022)


count22 = 0
for i in list_2022:
    count22 += 1
    print("")
    print(i)
print(count22)

'''
