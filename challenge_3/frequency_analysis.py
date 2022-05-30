import matplotlib.pyplot as plt # import dependencies
import wikipedia as wiki
from collections import Counter

ARTICLE = "Oxford" # article to be analysed

page = wiki.page(ARTICLE, auto_suggest=False) # fetch page and store content

content = page.content

content_stripped = "".join(filter(str.isalpha, content)).upper() # strip non-alphanumeric characters and convert to uppercase

content_length = len(content_stripped) # get length of content and count of each letter using Counter from collections
letter_count = Counter(content_stripped)

letter_percentage = {} # create empty dictionary to store letter percentages

for letter in letter_count: # iterate through the letter count dict, and calculate the percentage of each letter
    letter_percentage[letter] = (letter_count[letter] / content_length) * 100

letter_percentage = {k: v for k, v in sorted(list(letter_percentage.items()))} # one-liner to sort dict by key

x = letter_percentage.keys() # set x values to be the keys of the letter_percentage dict
y = letter_percentage.values() # set y values to be the values of the letter_percentage dict

fig, ax = plt.subplots() # create a figure and an axis

ax.bar(x, y, color=[(0.09, 0.33, 0.56), (0.02, 0.51, 0.82), (0.38, 0.69, 0.72), (0.72, 0.89, 1.00)]) # plot the x and y values, using a nice blue colour palette

ax.set(title="Frequency Analysis - "+ARTICLE+" on Wikipedia", xlabel="", ylabel="Frequency (%)") # set the title, axis labels and window title
fig.canvas.manager.set_window_title("Challenge 3.2: Frequency Analysis")

plt.show() # show the plot