import wordcloud
import matplotlib.pyplot as plt

w = wordcloud.WordCloud()

text = "AI 5G IOT"

w.generate(text)

w.to_file('outdemo01.png')
# plt.figure()
# plt.imshow(word, interpolation="bilinear")
#
# plt.axis('off')
# plt.show()

