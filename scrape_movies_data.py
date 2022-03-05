import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


# 2000 all movies

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



# Scrape Def


def scrape(strg, num, nam, yrs, rnt, rat, vot, gne, pro, plo, img, star, inf, mor):
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


            s = link.find("p", {"class":  ""} )
            names = s.find("a", {"class": ""} )


            for i in range(0,1):
                val = s.text.replace('  ', '').replace('\n' , '').replace('|', '').replace('Director:', '').replace('Stars:', ', ').replace(' ,', ',')
                star.append(val)

  
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



# Calling scrape on 2001 datasets

scrape('https://www.imdb.com/search/title/?title_type=feature&year=2001-01-01,2001-12-31&start=%s&ref_=adv_nxt',
       4266, name_2001, year_2001, Runtime_2001, rating_2001, vote_2001, genre_2001, profit_2001, plot_2001, img_2001, star_2001, more_info_2001, more_info_href_2001)



# Printing
count = 0
for i in range(0, len(name_2001)):
    count += 1
    print("Name: ", name_2001[i], '\n' , "Year: ", year_2001[i], "\n","Runtime: ",  Runtime_2001[i], "\n", "Rating: ", rating_2001[i], "\n", 
         "Votes: ", vote_2001[i], "\n", "Profits: ",  profit_2001[i], "\n", "Genre: ", genre_2001[i], "\n", "Plot: ", plot_2001[i], "\n",
         "Image: ", img_2001[i], "\n", "Crew: ", star_2001[i], "\n", "More Info: ",  more_info_2001[i], "\n", "Href: ", more_info_href_2001[i], "\n\n" )
    
    
print("")
print(count)


    



