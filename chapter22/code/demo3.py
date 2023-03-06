import wordcloud

# 创建词云对象
w = wordcloud.WordCloud(width=1000, height=700, background_color='white', font_path='C:\Windows\Fonts\STSONG.TTF')
text = "深度学习 人工智能 神经网络物联网"
# 传入文本对象
w.generate(text)
w.to_file('3.png')