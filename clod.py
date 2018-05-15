# -*- coding:utf-8 -*-
#  -$ i'm TeslaT $-
from wordcloud import  WordCloud , ImageColorGenerator
import  matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
# d = os.path.dirname(__file__)
# print(d)
def create_word_cloud(filename):
    text=open("{}.txt".format(filename),encoding='utf-8').read()
    alice_mask=np.array(Image.open('alice_mask.png'))
    wc = WordCloud(
        background_color="white",
        max_words=2000,
        font_path='C:\Windows\Fonts\SIMLI.TTF',
        height=1200,
        width=2000,
        max_font_size=150,
        random_state=50,
        mask=alice_mask
    )
    # 分词
    # myword=\
    wc.generate(text)
    # image_colors = ImageColorGenerator(alice_mask)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")


    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    # 保存
    wc.to_file('alice_word.png')
    plt.show()


create_word_cloud('b')