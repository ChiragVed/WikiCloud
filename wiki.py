# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:59:14 2017

@author: chirag
"""
#from wordcloud import WordCloud
from os import path
import os
from PIL import Image
import datetime
import numpy as np
import wikipedia
from wordcloud import WordCloud, STOPWORDS

current_dir = os.path.abspath(os.curdir)
cloud_mask=np.array(Image.open(path.join(current_dir,'cloud1.JPG')))
readable = datetime.datetime.fromtimestamp(1510241584).isoformat()

def get_wikicontent(query):
#get the complete article from WIKI
   title= wikipedia.search(query)[0]
   page = wikipedia.page(title)
   return page.content

def create_wc(txt):
#This method get the popular 100 words from the article and generates a wordcloud and saves it locally
 stpwords= set(STOPWORDS)
 wc=WordCloud(background_color='black',mask=cloud_mask,stopwords=stpwords,max_words=100)
 wc.generate(txt)
 os.chdir("genwc")
 filename = var1+'wordcloud.png'

 wc.to_file(path.join(os.path.abspath(os.curdir),filename)) 

 
#WIKI Article to be searched
var1 = "Github"
create_wc(get_wikicontent(var1))


 