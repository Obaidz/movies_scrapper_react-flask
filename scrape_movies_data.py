import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


# 2000 all movies
name_2000 = []
year_2000 = []
Runtime_2000 = []
rating_2000 = []
vote_2000 = []
genre_2000 = []
profit_2000 = []
plot_2000 = []
img_2000 = []
star_2000 = []
more_info_2000 =[]
more_info_href_2000 = []

#Dataset 2001
name_2001 = []
year_2001 = []
Runtime_2001 = []
rating_2001 = []
vote_2001 = []
genre_2001 = []
profit_2001 = []
plot_2001 = []
img_2001 = []
star_2001 = []
more_info_2001 =[]
more_info_href_2001 = []


#Dataset 2002
name_2002 = []
year_2002 = []
Runtime_2002 = []
rating_2002 = []
vote_2002 = []
genre_2002 = []
profit_2002 = []
plot_2002 = []
img_2002 = []
star_2002 = []
more_info_2002 =[]
more_info_href_2002 = []


#Dataset 2003
name_2003 = []
year_2003 = []
Runtime_2003 = []
rating_2003 = []
vote_2003 = []
genre_2003 = []
profit_2003 = []
plot_2003 = []
img_2003 = []
star_2003 = []
more_info_2003 =[]
more_info_href_2003 = []


#Dataset 2004
name_2004 = []
year_2004 = []
Runtime_2004 = []
rating_2004 = []
vote_2004 = []
genre_2004 = []
profit_2004 = []
plot_2004 = []
img_2004 = []
star_2004 = []
more_info_2004 =[]
more_info_href_2004 = []

#Dataset 2005
name_2005 = []
year_2005 = []
Runtime_2005 = []
rating_2005 = []
vote_2005 = []
genre_2005 = []
profit_2005 = []
plot_2005 = []
img_2005 = []
star_2005 = []
more_info_2005 =[]
more_info_href_2005 = []

#Dataset 2006
name_2006 = []
year_2006 = []
Runtime_2006 = []
rating_2006 = []
vote_2006 = []
genre_2006 = []
profit_2006 = []
plot_2006 = []
img_2006 = []
star_2006 = []
more_info_2006 =[]
more_info_href_2006 = []

#Dataset 2007
name_2007 = []
year_2007 = []
Runtime_2007 = []
rating_2007 = []
vote_2007 = []
genre_2007 = []
profit_2007 = []
plot_2007 = []
img_2007 = []
star_2007 = []
more_info_2007 =[]
more_info_href_2007 = []

#Dataset 2008
name_2008 = []
year_2008 = []
Runtime_2008 = []
rating_2008 = []
vote_2008 = []
genre_2008 = []
profit_2008 = []
plot_2008 = []
img_2008 = []
star_2008 = []
more_info_2008 =[]
more_info_href_2008 = []

#Dataset 2009
name_2009 = []
year_2009 = []
Runtime_2009 = []
rating_2009 = []
vote_2009 = []
genre_2009 = []
profit_2009 = []
plot_2009 = []
img_2009 = []
star_2009 = []
more_info_2009 =[]
more_info_href_2009 = []

#Dataset 2010
name_2010 = []
year_2010 = []
Runtime_2010 = []
rating_2010 = []
vote_2010 = []
genre_2010 = []
profit_2010 = []
plot_2010 = []
img_2010 = []
star_2010 = []
more_info_2010 =[]
more_info_href_2010 = []

#Dataset 2011
name_2011 = []
year_2011 = []
Runtime_2011 = []
rating_2011 = []
vote_2011 = []
genre_2011 = []
profit_2011 = []
plot_2011 = []
img_2011 = []
star_2011 = []
more_info_2011 =[]
more_info_href_2011 = []

#Dataset 2012
name_2012 = []
year_2012 = []
Runtime_2012 = []
rating_2012 = []
vote_2012 = []
genre_2012 = []
profit_2012 = []
plot_2012 = []
img_2012 = []
star_2012 = []
more_info_2012 =[]
more_info_href_2012 = []

#Dataset 2013
name_2013 = []
year_2013 = []
Runtime_2013 = []
rating_2013 = []
vote_2013 = []
genre_2013 = []
profit_2013 = []
plot_2013 = []
img_2013 = []
star_2013 = []
more_info_2013 =[]
more_info_href_2013 = []


#Dataset 2014
name_2014 = []
year_2014 = []
Runtime_2014 = []
rating_2014 = []
vote_2014 = []
genre_2014 = []
profit_2014 = []
plot_2014 = []
img_2014 = []
star_2014 = []
more_info_2014 =[]
more_info_href_2014 = []

#Dataset 2015
name_2015 = []
year_2015 = []
Runtime_2015 = []
rating_2015 = []
vote_2015 = []
genre_2015 = []
profit_2015 = []
plot_2015 = []
img_2015 = []
star_2015 = []
more_info_2015 =[]
more_info_href_2015 = []

#Dataset 2016
name_2016 = []
year_2016 = []
Runtime_2016 = []
rating_2016 = []
vote_2016 = []
genre_2016 = []
profit_2016 = []
plot_2016 = []
img_2016 = []
star_2016 = []
more_info_2016 =[]
more_info_href_2016 = []

#Dataset 2017
name_2017 = []
year_2017 = []
Runtime_2017 = []
rating_2017 = []
vote_2017 = []
genre_2017 = []
profit_2017 = []
plot_2017 = []
img_2017 = []
star_2017 = []
more_info_2017 =[]
more_info_href_2017 = []

#Dataset 2018
name_2018 = []
year_2018 = []
Runtime_2018 = []
rating_2018 = []
vote_2018 = []
genre_2018 = []
profit_2018 = []
plot_2018 = []
img_2018 = []
star_2018 = []
more_info_2018 =[]
more_info_href_2018 = []

#Dataset 2019
name_2019 = []
year_2019 = []
Runtime_2019 = []
rating_2019 = []
vote_2019 = []
genre_2019 = []
profit_2019 = []
plot_2019 = []
img_2019 = []
star_2019 = []
more_info_2019 =[]
more_info_href_2019 = []


#Dataset 2020
name_2020 = []
year_2020 = []
Runtime_2020 = []
rating_2020 = []
vote_2020 = []
genre_2020 = []
profit_2020 = []
plot_2020 = []
img_2020 = []
star_2020 = []
more_info_2020 =[]
more_info_href_2020 = []


#Dataset 2021
name_2021 = []
year_2021 = []
Runtime_2021 = []
rating_2021 = []
vote_2021 = []
genre_2021 = []
profit_2021 = []
plot_2021 = []
img_2021 = []
star_2021 = []
more_info_2021 =[]
more_info_href_2021 = []
list_2021 = []

#Dataset 2022
name_2022 = []
year_2022 = []
Runtime_2022 = []
rating_2022 = []
vote_2022 = []
genre_2022 = []
profit_2022 = []
plot_2022 = []
img_2022 = []
star_2022 = []
more_info_2022 =[]
more_info_href_2022 = []
list_2022 = []

# Scrape Def
# Scrape Def
def scrape(strg, num, nam, yrs, rnt, rat, vot, gne, pro, plo, img, star, inf, mor, lis):
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


            data = {"Movie_title": name,
            "Year": year,
            "Runtime": time,
            "Genre": gen,
            "Rating": rating,
            "Votes": votes,
            "Gross profit": gross_p,
            "Crew": val,
            "Plot": my_plt,
            "Image": image,
            "link": link.h3.a,
            "href": link.h3.a['href']}
            
            lis.append(data)
            #Append
            nam.append(name)
            yrs.append(year)
            rnt.append(time)
            rat.append(rating)
            vot.append(votes)
            pro.append(gross_p)
            gne.append(gen)
            plo.append(my_plt)
            img.append(image)
            inf.append(link.h3.a)
            mor.append(link.h3.a['href'])




        contr += 50

'''
# Calling scrape on 2000 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2000-01-01,2000-12-31&start=%s&ref_=adv_prv',
       6000, name_2000, year_2000, Runtime_2000, rating_2000, vote_2000, genre_2000, profit_2000, plot_2000, img_2000, star_2000, more_info_2000, more_info_href_2000)

# Calling scrape on 2001 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2001-01-01,2001-12-31&start=%s&ref_=adv_nxt',
       6000, name_2001, year_2001, Runtime_2001, rating_2001, vote_2001, genre_2001, profit_2001, plot_2001, img_2001, star_2001, more_info_2001, more_info_href_2001)


# Calling scrape on 2002 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2002-01-01,2002-12-31&start=%s&ref_=adv_nxt',
       6000, name_2002, year_2002, Runtime_2002, rating_2002, vote_2002, genre_2002, profit_2002, plot_2002, img_2002, star_2002, more_info_2002, more_info_href_2002)

# Calling scrape on 2003 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2003-01-01,2003-12-31&start=%s&ref_=adv_nxt',
       6000, name_2003, year_2003, Runtime_2003, rating_2003, vote_2003, genre_2003, profit_2003, plot_2003, img_2003, star_2003, more_info_2003, more_info_href_2003)

# Calling scrape on 2004 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2004-01-01,2004-12-31&start=%s&ref_=adv_nxt',
       6000, name_2004, year_2004, Runtime_2004, rating_2004, vote_2004, genre_2004, profit_2004, plot_2004, img_2004, star_2004, more_info_2004, more_info_href_2004)


# Calling scrape on 2005 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2005-01-01,2005-12-31&start=%s&ref_=adv_nxt',
       6000, name_2005, year_2005, Runtime_2005, rating_2005, vote_2005, genre_2005, profit_2005, plot_2005, img_2005, star_2005, more_info_2005, more_info_href_2005)


# Calling scrape on 2006 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2006-01-01,2006-12-31&start=%s&ref_=adv_nxt',
       6000, name_2006, year_2006, Runtime_2006, rating_2006, vote_2006, genre_2006, profit_2006, plot_2006, img_2006, star_2006, more_info_2006, more_info_href_2006)


# Calling scrape on 2007 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2007-01-01,2007-12-31&start=%s&ref_=adv_nxt',
       6500, name_2007, year_2007, Runtime_2007, rating_2007, vote_2007, genre_2007, profit_2007, plot_2007, img_2007, star_2007, more_info_2007, more_info_href_2007)


# Calling scrape on 2008 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2008-01-01,2008-12-31&start=%s&ref_=adv_nxt',
       7000, name_2008, year_2008, Runtime_2008, rating_2008, vote_2008, genre_2008, profit_2008, plot_2008, img_2008, star_2008, more_info_2008, more_info_href_2008)



# Calling scrape on 2009 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2009-01-01,2009-12-31&start=%s&ref_=adv_nxt',
       8000, name_2009, year_2009, Runtime_2009, rating_2009, vote_2009, genre_2009, profit_2009, plot_2009, img_2009, star_2009, more_info_2009, more_info_href_2009)

# Calling scrape on 2010 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2010-01-01,2010-12-31&start=%s&ref_=adv_nxt',
       8000, name_2010, year_2010, Runtime_2010, rating_2010, vote_2010, genre_2010, profit_2010, plot_2010, img_2010, star_2010, more_info_2010, more_info_href_2010)


# Calling scrape on 2011 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2011-01-01,2011-12-31&start=%s&ref_=adv_nxt',
       9000, name_2011, year_2011, Runtime_2011, rating_2011, vote_2011, genre_2011, profit_2011, plot_2011, img_2011, star_2011, more_info_2011, more_info_href_2011)


# Calling scrape on 2012 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2012-01-01,2012-12-31&start=%s&ref_=adv_nxt',
       9500, name_2012, year_2012, Runtime_2012, rating_2012, vote_2012, genre_2012, profit_2012, plot_2012, img_2012, star_2012, more_info_2012, more_info_href_2012)

# Calling scrape on 2013 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2013-01-01,2013-12-31&start=%s&ref_=adv_nxt',
       10000, name_2013, year_2013, Runtime_2013, rating_2013, vote_2013, genre_2013, profit_2013, plot_2013, img_2013, star_2013, more_info_2013, more_info_href_2013)


# Calling scrape on 2014 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2014-01-01,2014-12-31&start=%s&ref_=adv_nxt',
       10000, name_2014, year_2014, Runtime_2014, rating_2014, vote_2014, genre_2014, profit_2014, plot_2014, img_2014, star_2014, more_info_2014, more_info_href_2014)

# Calling scrape on 2015 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2015-01-01,2015-12-31&start=%s&ref_=adv_nxt',
       10000, name_2015, year_2015, Runtime_2015, rating_2015, vote_2015, genre_2015, profit_2015, plot_2015, img_2015, star_2015, more_info_2015, more_info_href_2015)

# Calling scrape on 2016 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2016-01-01,2016-12-31&start=%s&ref_=adv_nxt',
       10000, name_2016, year_2016, Runtime_2016, rating_2016, vote_2016, genre_2016, profit_2016, plot_2016, img_2016, star_2016, more_info_2016, more_info_href_2016)


# Calling scrape on 2017 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2017-01-01,2017-12-31&start=%s&ref_=adv_nxt',
       10000, name_2017, year_2017, Runtime_2017, rating_2017, vote_2017, genre_2017, profit_2017, plot_2017, img_2017, star_2017, more_info_2017, more_info_href_2017)


# Calling scrape on 2018 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2018-01-01,2018-12-31&start=%s&ref_=adv_nxt',
       10000, name_2018, year_2018, Runtime_2018, rating_2018, vote_2018, genre_2018, profit_2018, plot_2018, img_2018, star_2018, more_info_2018, more_info_href_2018)


# Calling scrape on 2019 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2019-01-01,2019-12-31&start=%s&ref_=adv_nxt',
       10000, name_2019, year_2019, Runtime_2019, rating_2019, vote_2019, genre_2019, profit_2019, plot_2019, img_2019, star_2019, more_info_2019, more_info_href_2019)


# Calling scrape on 2020 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&start=%s&ref_=adv_nxt',
       10000, name_2020, year_2020, Runtime_2020, rating_2020, vote_2020, genre_2020, profit_2020, plot_2020, img_2020, star_2020, more_info_2020, more_info_href_2020)


'''
# Calling scrape on 2021 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2021-01-01,2021-12-31&start=%s&ref_=adv_nxt',
       10000, name_2021, year_2021, Runtime_2021, rating_2021, vote_2021, genre_2021, profit_2021, plot_2021, img_2021, star_2021, more_info_2021, more_info_href_2021, list_2021)


'''
# Calling scrape on 2022 datasets
scrape('https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&start=%s&ref_=adv_nxt',
       10000, name_2022, year_2022, Runtime_2022, rating_2022, vote_2022, genre_2022, profit_2022, plot_2022, img_2022, star_2022, more_info_2022, more_info_href_2022, list_2022)

'''

count21 = 0
for i in list_2021:
    count21 += 1
    print("")
    print(i)
print(count21)

'''
# Printing
count = 0
for i in range(0, len(name_2000)):
    count += 1
    print("Name: ", name_2000[i], '\n' , "Year: ", year_2000[i], "\n","Runtime: ",  Runtime_2000[i], "\n", "Rating: ", rating_2000[i], "\n", 
         "Votes: ", vote_2000[i], "\n", "Profits: ",  profit_2000[i], "\n", "Genre: ", genre_2000[i], "\n", "Plot: ", plot_2000[i], "\n",
         "Image: ", img_2000[i], "\n", "Crew: ", star_2000[i], "\n", "More Info: ",  more_info_2000[i], "\n", "Href: ", more_info_href_2000[i], "\n\n" )
    
    
print("")
print(count)


   '''


    



