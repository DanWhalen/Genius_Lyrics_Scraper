##genius.com
import pandas as pd
import re, requests, os, sys, datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


##SET RUN PARAMETERS
directory = "C:/Python 3.6/Python/Git Personas/DanWhalen/Genius_Lyrics_Scraper/Files to reingest/"
file = "shs mnt checked - VERIFIED - Billboard Hot 100 (2010-01-02 -- 2016-12-31, t=100).xlsx"


##EXTRACT DATA FROM SPECIFIED EXCEL FILE
xl = pd.ExcelFile(os.path.join(directory, file))
df = xl.parse("RawData")
df = df.loc[df['NAME_VERIFIED'] == 1]

artist = df["ARTIST"].tolist()
song = df["SONG"].tolist()
date = df["DATE"].tolist()

ztuples = list(zip(artist,song))
zlist = []
for z in ztuples:
        zlist.append(list(z))


##GENERATE SUSPECTED URLs BASED ON EXCEL INPUT DATA
links = []

for z in zlist:
        a = z[0]
        a = a.replace("-"," ")
        a = a.lower().replace(" ","-")
        featuring = a.find("-featuring-")
        feat = a.find("-feat-")
        and_his_orchestra = a.find("-and-his-orchestra")
        and_his_orch = a.find("-and-his-orch")
        if featuring > 0:
                a = a[:featuring]
        elif and_his_orchestra > 0:
                a = a[:and_his_orchestra]
        elif and_his_orch > 0:
                a = a[:and_his_orch]
        elif feat > 0:
                a = a[:feat]
        s = z[1]
        s = s.lower().replace(" ","-")
        stem = (a+'-'+s+'-lyrics')
        clean_stem = re.sub(r"\'|\:|\!|\+|\(|\)|\,|\"|\?|\.|\$|\"|", r"", stem)
        clean_stem = clean_stem.replace("&","and")
        links.append('https://genius.com/'+clean_stem)


##TRY ALL URLs GENERATED ABOVE, AND RECORD WHETHER OR NOT URL ACTUALLY EXISTS
check = []
for l in links:
    req = requests.get(l)
    check.append(req)

cstr = []
for c in check:
    cstr.append(str(c))


##DEFINE CUSTOM FUNCTION
def get_lyrics(link):
        global lyrics_list
        lyrics_list = []
        try:
                text = []
                req = Request(str(link), headers={'User-Agent': 'Explorer'})
                webpage = urlopen(req).read()
                bs_html = BeautifulSoup(webpage, 'lxml')
                lyrics = bs_html.findAll("div", {"class": "lyrics"})
                for l in lyrics:
                        text.append(str(l))
                html_as_txt = str(text[0])
                soup = BeautifulSoup(html_as_txt, 'lxml')
                result = soup.text
                lyrics_list.append(result)
        except:
                lyrics_list.append("LINK DOES NOT WORK (404): "+str(link))
        return(lyrics_list)


##NAVIGATE TO ALL URLs, AND RECORD LYRICS FOUND THERE (IF URL ACTUALLY EXISTS)
lyrics_text = []
for l in links:
        lyrics_text.append(get_lyrics(l))


##WRITE OUT RESULTS TO TXT FILE
verification_counter = 0
sys.stdout = open("OUTPUT.txt",'w', encoding='utf-8')

print("FROM FILE: "+str(file))
print("RUN DATE: "+str(datetime.datetime.now()))
print("Response 200: "+str(cstr.count("<Response [200]>")))
print("Response 404: "+str(cstr.count("<Response [404]>")))
print("Total: "+str(len(cstr)))
print("--------------------------------------------------")
print("--------------------------------------------------")
print("")

for i in range(0,len(zlist)):
	print(str(zlist[i]))
	print("First appearance on Billboard Hot 100: "+str(date[i])[:10])
	print("Link attempted: "+str(links[i]))
	print("Link response: "+str(cstr[i]))
	print("")
	print(lyrics_text[i][0])
	print("--------------------------------------------------")
	print("")
	verification_counter = verification_counter + 1
	
print("RECORDS WRITTEN: "+str(verification_counter))

sys.stdout.close()

