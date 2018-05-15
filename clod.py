# -*- coding:utf-8 -*-
#  -$ i'm TeslaT $-
from wordcloud import  WordCloud
import  matplotlib.pyplot as plt

def create_word_cloud(filename):
    text=open("{}.txt".format(filename),encoding='utf-8').read()
    wc=WordCloud(
        background_color="white",
        max_words=2000,
        font_path="C:\Windows\Fonts\SIMLI.TTF",
        height=1200,
        width=2000,
        max_font_size=150,
        random_state=50,

    )
    myword=wc.generate(text)
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file(qq_word.png)

create_word_cloud('b')