import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time
import os


def image_get(bf,ch):


    # ch ページ取得、解析
    #ch = 0
    # https://scraping-for-beginner.herokuapp.com/ <=スクレイピング練習サイトから
    
    #bf   格納先
    if ch == 0:
        load_url = 'https://scraping-for-beginner.herokuapp.com/image'
    else:
        pass
    
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    # 保存先
    out_folder = bf
    print(bf)

    #out_folder.mkdir(exist_ok=True)

    # imgタグのリンク取得
    for element in soup.find_all('img'):
        src = element.get('src')

        # 絶対パスで取得
        image_url = urllib.parse.urljoin(load_url, src)
        imgdata = requests.get(image_url)

        # URLからファイル名取得、保存フォルダと連結
        filename = image_url.split('/')[-1]
        out_path = os.path.join(out_folder,filename)
        print(out_path)
        # 画像データをファイル書き出し
        with open(out_path, mode='wb') as f:
            f.write(imgdata.content)

            time.sleep(1)


if __name__=='__main__':
    pass
    # # bf=r'C:\Users\kawa\pyworks\image\before'
    # ch=0

    # image_get(bf,ch)