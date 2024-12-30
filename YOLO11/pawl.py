import requests
import os
import json
def main(page):
    url = "https://image.baidu.com/search/acjson"
    params = {
        "tn": "resultjson_com",
        "logid": "8216501909612899911",
        "ipn": "rj",
        "ct": "201326592",
        "fp": "result",
        "word": word,
        "queryWord": word,
        "cl": "2",
        "lm": "-1",
        "ie": "utf-8",
        "oe": "utf-8",
        "st": "-1",
        "z": "0",
        "ic": "0",
        "hd": "0",
        "latest": "0",
        "copyright": "0",
        "face": "0",
        "istype": "2",
        "nc": "1",
        "pn": 30*page,
        "rn": "30",
        "gsm": "1e",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    # 拿响应对象
    data = requests.get(url,headers = headers, params = params).json()['data']
    # r = requests.get(url, headers=headers, params=params).text
    # r = r.replace("'",'')
    # print(r)
    # r = json.loads(r)
    # data = r['data']
    n=1
    for i in data[:-1]:
        img_url = i['hoverURL']
        if not img_url:  # 如果 hoverURL 为空
            img_url = i['middleURL']  # 使用 middleURL
        type = i['type']
        type = type if type else '.jpg'
        img_code = requests.get(img_url, headers=headers).content
        # 保存图片
        with open(f'{word}/{page+1}-{n}.{type}','wb') as f: 
            f.write(img_code)
        n+=1
if __name__ == '__main__':
    word = '交通道路行人'
    if not os.path.exists(word):
        os.mkdir(word)
    for page in range(10,20):
        main(page)