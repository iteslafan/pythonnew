# -*- coding:utf-8 -*-
#  -$ i'm TeslaT $-
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image


# d = os.path.dirname(__file__)
# print(d)

def create_word_cloud(filename):
    path_f = input('输入文件名称')
    path_s = input('输入保存名称')
    text = open("{}.txt".format(filename), encoding='utf-8').read()
    # alice_mask=np.array(Image.open('alice_mask.png'))
    wc = WordCloud(
        background_color="white",
        max_words=3500,
        font_path='C:\Windows\Fonts\SIMLI.TTF',
        height=1700,
        width=3000,
        max_font_size=150,
        random_state=50,
        margin=2,
        prefer_horizontal=0.8,
        min_font_size=13

        # mask=alice_mask
    )
    # 分词
    # myword=\
    wc.generate(text)
    # image_colors = ImageColorGenerator(alice_mask)
    # plt.imshow(wc,interpolation='bilinear')
    plt.imshow(wc)

    plt.axis("off")
    # plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    # 保存
    wc.to_file(path_s + '.png')
    plt.show()


if __name__ == '__main__':
    create_word_cloud(path_f)
