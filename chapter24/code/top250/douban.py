import requests
import re
import json
import time

def save_file(result):
    with open("./movie/top250.txt", 'a', encoding='utf8') as f:
        f.write(json.dumps(result, ensure_ascii=False) + '\n')


def parse_text(page_text):
    """
    {"rank":1, "img":"src", "title":"天堂电影院", "guide":"朱塞佩·托纳多雷"}
    :param text:
    :return:
    """
    for item in page_text:
        yield {
            "rank": item[0],
            "img": item[1],
            "title": (item[2] + item[3]).replace("&nbsp;", '').replace(" ", ''),
            "guide": re.sub('\s|\n', '', item[4]).split(";")[0].strip("&nbsp")
        }


def main(offset):
    url = "https://movie.douban.com/top250?start=%s" % offset
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    pattern = re.compile('<em class="">(\d+)</em>.*?'
                         + '<a.*?src="(.*?)".*?'
                         + '<span class="title">(.*?)</span>.*?'
                         + '<span class="other">(.*?)</span>.*?'
                         + '<p class="">(.*?) </p>.*?',
                         re.S
                         )

    page_text = re.findall(pattern, response.text)
    result_iter = parse_text(page_text)

    for result in result_iter:
        save_file(result)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(1, 11):
        main((i - 1) * 25)
    end_time = time.time()
    print(end_time-start_time) # 4.754207134246826