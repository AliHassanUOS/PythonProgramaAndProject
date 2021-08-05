from bs4 import BeautifulSoup as soup
import requests
import lxml
from urllib.request import urlopen as uReq
import string
import re
import json

meurl = 'https://www.geekyshows.com'

uclien = uReq(meurl)

page = uclien.read()

uclien.close()

psoup = soup(page, "html.parser")

filename = "abstracts.csv"
f = open(filename, "w")
header = "Titles , Abstracts \n"

f.write(header)

coniner = psoup.findAll("a", {"class": "title"})
acc = psoup.findAll("p", {"class": "snippet"})

for con in coniner:
    ref = con.get('href')

    murl = 'https://link.springer.com' + ref + ''

    uclen = uReq(murl)

    pag = uclen.read()

    uclen.close()

    psou = soup(pag, "html.parser")

    nme = psou.find("h1", {"class": "ArticleTitle"})
    coer = psou.find("p", {"class": "Para"})

    # coer = coer.getText()
    # coer = coer.replace(",", " ")
    #
    # nme = nme.getText()
    # nme = nme.replace(",", " ")
    # print(coer)
    # print(nme)
    #   print(ime)

    # print("success")
    # f.write(nme.encode('ascii', 'ignore') + "," + coer.encode('ascii', 'ignore') + "\n")

print("123")
n = 20
while n <= 13000:
    print(n)
    m = str(n)
    ul = 'https://link.springer.com/search/page/3?date-facet-mode=between&dc.title=nano&showAll=true&query=nanotechnology&facet-content-type=%22Article%22' + m + ''
    uclien = uReq(ul)

    page = uclien.read()

    uclien.close()

    psoup = soup(page, "html.parser")

    coniner = psoup.findAll("a", {"class": "title"})

    for con in coniner:
        ref = con.get('href')

        murl = 'https://link.springer.com' + ref + ''

        uclen = uReq(murl)

        pag = uclen.read()

        uclen.close()

        psou = soup(pag, "html.parser")

        nme = psou.find("h1", {"class": "ArticleTitle"})
        coer = psou.find("p", {"class": "Para"})
        #
        # coer = coer.getText()
        #
        # coer = coer.replace(",", " ")
        #
        # nme = nme.getText()
        # nme = nme.replace(",", " ")
        # print(coer)
        # print(nme)

        # f.write(nme.encode('ascii', 'ignore') + "," + coer.encode('ascii', 'ignore') + "\n")
        # print(n)
    n = n + 20

