# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

text = "男性, 居住上海, 开户年限3年,建筑行业, 持有活期存款,持有定期存款, 持有结构性存款, 大量购买表外理财,少量购买保险\
     当年开通手机银行,手机银行活跃用户, 无贷款, 代发薪存款留存率高,复购概率高"


# 加载背景图
color_mask = np.array(Image.open("./personPay.png"))
wc = WordCloud(
    mask=color_mask,
    background_color='white',
    contour_width=10,  # 词云形状边宽宽度
    contour_color='gray',  # 词云形状边宽颜色
    font_path="/Library/Fonts/Arial Unicode.ttf"
)
wc.generate(text)
image_colors = ImageColorGenerator(color_mask)
# 在只设置mask的情况下 会得到一个拥有图片形状的词云 axis默认为on 会开启边框
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("./resultPay.jpg")

