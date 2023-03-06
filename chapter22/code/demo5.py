import jieba
import wordcloud

def cut_words(text):

    word_count = {} # {"北京"：5,...}

    words = jieba.lcut(text)

    for word in words:
        if len(word) == 1:
            continue
        else:
            word_count[word] = word_count.get(word, 0) + 1

    with open('word_path.txt', 'w', encoding='utf8') as f:
        for k ,v in word_count.items():
            f.write(f'{k}\t{v}\n')
    """
    北京 5
    南京 2
    ...
    """

def get_word_cloud():
    with open('word_path.txt', 'r', encoding='utf8') as f:
        text = f.read()

    wc = wordcloud.WordCloud(width=500, height=400, background_color='white',font_path='C:\Windows\Fonts\STSONG.TTF')
    wc.generate(text)
    wc.to_file('demo5.png')

if __name__ == '__main__':
    text = "中华人民共和国第十四届全国人民代表大会任期五年，自2023年3月开始。2023年2月24日，第十三届全国人民代表大会常务委员会第三十九次会议根据代表资格审查委员会提出的审查报告，确认2977名第十四届全国人民代表大会代表的代表资格有效"
    # cut_words(text)
    get_word_cloud()