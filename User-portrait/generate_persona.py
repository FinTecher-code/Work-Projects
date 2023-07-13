# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

text = "客户类型, 性别, 是否农户, 工作,职务, 有无子女,是否有通讯地址, 是否有家庭电话, 是否有手机号码,是否有配偶手机号\
     是否有公司电话,住房情况, 计息周期, 还款方式, 担保方式, 贷款形式,产品名称"


# 加载背景图
color_mask = np.array(Image.open("./person.png"))
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
plt.savefig("./result.jpg")

