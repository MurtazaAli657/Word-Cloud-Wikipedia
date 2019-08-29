import sys
from os import path
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

# get path to script's directory where it is.
currdir = os.path.dirname('__file__')

def get_wiki(query):
	# get best matching title for given query
	title = wikipedia.search(query)[0]

	# get wikipedia page for selected title
	page = wikipedia.page(title)
	return page.content


def create_wordcloud(text):
    # create numpy araay for wordcloud mask image getting from same working directory
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))

    # create set of stopwords. it is used for don't use "is, are, was, were etc" this type of words
    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white",
                    max_words=2000, 
                    mask=mask,
                    stopwords=stopwords)
    
    # generate wordcloud
    wc.generate(text)

    # save wordcloud image in same working directory
    wc.to_file(path.join(currdir, "wc.png"))

    #run the program
create_wordcloud(get_wiki("Pakistan"))
