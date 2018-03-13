## What is "Genius Lyrics Scraper"?
This program is a compliment to "Billboard Hot 100 Scraper.py".  "Billboard Hot 100 Scraper.py" scrapes song and artist names from the Billboard Hot 100 website, and organizes them into spreadsheets.  "Genius Lyrics Scraper.py" reingests those spreadsheets, and attempts to find the lyrics for each song, as they appear on Genius.com.

The code was custom engineered for a reseach project that required finding the lyrics of past Billboard Hot 100 pop singles about specific, named individuals (fictious or real).

- Note: "Billboard Hot 100 Scraper.py" scrapes the Billboard Hot 100 website, and attempts to identify which of the scraped songs contain specific, named individuals in their titles.  "Billboard Hot 100 Scraper.py" output is the input for "Genius Lyrics Scraper".  However, there is an intermediate step.  Before reingesting the Billboard Hot 100 Scraper's output, the spreadsheet must be hand coded.  Users must verify whether or not a name is actually contained in the song title, and code that record with a 1 at the end of the row (signifying the title contains a person's name), or a 0 (signifying the title does not contain a person's name).


## How to run "Genius Lyrics Scraper"
There are certain "run parameters" (variables that must be hard coded) users must set before running Billboard Hot 100 Scraper. These variables are defined in lines 8-10, the block of code labeled "##SET RUN PARAMETERS".

***directory*** - (str) Path to the folder where the coded spreadsheet (the file to be ingested/lyrics scraped).  

***file*** - (str) File name of the specific spreadsheet you want to run the Genius Lyrics Scraper on.

- Note: Included in this repository is "shs mnt checked - VERIFIED - Billboard Hot 100 (2010-01-02 -- 2016-12-31, t=100).xlsx", a sample input file.  Any Excel file ingested in "Genius Lyrics Scraper" must match the formatting of the "RawData" tab of the sample input file.


## How "Genius Lyrics Scraper" works
1. "Genius Lyrics Scraper" reads in the specified Excel sheet.
2. Using only data with a "1" in the "NAME_VERIFIED" column, "Genius Lyrics Scraper" generates an URL taking the form "Genius.com"+"ARTIST NAME"+"SONG NAME". This URL represents the suspected URL at Genius.com where the lyrics for that particular song would be found.
3. The "Genius Lyrics Scraper" tries all the links it generated.  If the URL does actually exist ("Response 200"), it records whatever lyrics are found at that URL.  If the URL does not exist ("Response 404"), the scraper records an error message.
4. The Scraper then outputs a txt file showing all lyrics it found using the above method. 
