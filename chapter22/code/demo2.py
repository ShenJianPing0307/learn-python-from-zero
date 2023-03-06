import wordcloud

# 创建词云对象
w = wordcloud.WordCloud(width=1000, height=700, background_color='white')
text = "AI 5G IOT"
# 传入文本对象
w.generate(text)
w.to_file('2.png')