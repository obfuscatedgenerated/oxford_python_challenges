import wikipedia as wiki # import dependencies
from bs4 import BeautifulSoup
import time
import random

ARTICLE = "Python_(programming_language)" # article to start at

page = wiki.page(ARTICLE, auto_suggest=False) # fetch page and store content

print("Starting at: "+page.title)

start_time = time.time() # get the start timestamp

for _ in range(20): # loop 20 times
    link = random.sample(page.links, 1) # get a random link from the page
    page = wiki.page(link[0], auto_suggest=False) # overwrite the page variable with the new page
    print("Currently at: "+page.title)

finish_time = time.time() # get the finish timestamp

print("Finished in: "+str(finish_time-start_time)+" seconds")

size_page = wiki.page("Wikipedia:Size_of_Wikipedia", auto_suggest=False) # fetch the info page holding the size of the Wikipedia
soup = BeautifulSoup(size_page.html(), "html.parser") # parse the HTML with bs4 (this takes a sec)
article_count = int(soup.select(".infobox-data")[0].text.replace(",", "")) # select the first element in the infobox-data class, and get the text, then remove commas and parse as int (this method assumes the structure of the page is the same)

print("There are "+str(article_count)+" articles in Wikipedia.")

calculated_time = (article_count / 20) * (finish_time-start_time)

print("It would take "+str(calculated_time)+" seconds ("+str(calculated_time/360)+" hours or "+str(calculated_time/8640)+" days) to crawl through all of Wikipedia with this method.")