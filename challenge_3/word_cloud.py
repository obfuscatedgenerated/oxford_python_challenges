from wordcloud import WordCloud # import dependencies
import matplotlib.pyplot as plt
import wikipedia as wiki
from collections import Counter
from string import ascii_uppercase

ARTICLE = "Python_(programming_language)" # article to be analysed

page = wiki.page(ARTICLE, auto_suggest=False) # fetch page and store content

content = page.content

wc = WordCloud().generate(content) # generate wordcloud from content

plt.imshow(wc, interpolation="bilinear") # create image in matplotlib
plt.axis("off")

plt.show() # show the plot