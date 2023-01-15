import json
import requests
import uuid


def read_file():
    with open("./movie/top250.txt", encoding="utf8") as f:
        for item in f:
            yield item


def save_picture(src):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    rsp = requests.get(src, headers=headers)

    with open(f"./movie/picture/{uuid.uuid4()}.jpg", 'wb') as f:
        f.write(rsp.content)


def get_piture():
    item_iter = read_file()
    for item in item_iter:
        item_obj = json.loads(item)
        img = item_obj.get("img")
        save_picture(img)


def main():
    get_piture()


if __name__ == '__main__':
    main()
