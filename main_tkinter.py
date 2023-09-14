import tkinter as tk
from tkinter import filedialog
from functools import partial
import os
from sub.img_resize import resize_tra
from sub.img_getter import image_get


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("500x400")
        # top_frame
        frame_top = tk.Frame(self.master, borderwidth=2, relief='solid')
        # left_frame
        frame_left = tk.Frame(self.master)
        # right_frame
        frame_right = tk.Frame(self.master)
        # bottom_frame
        frame_bottom_left = tk.Frame(
            self.master, borderwidth=2, relief='solid')
        frame_bottom_right = tk.Frame(
            self.master, borderwidth=2, relief='solid')

        # button,label作成
        Label = tk.Label(frame_top, text="webサイトを指定して画像取得",
                         fg='#f00', bg='#000', height=2, width=60)
        button1 = tk.Button(text="参照", height=2, width=8,
                            command=partial(self.btn_click, "bf"))
        button2 = tk.Button(text="参照", height=2, width=8,
                            command=partial(self.btn_click, "af"))
        self.Label1 = tk.Label(
            frame_left, text="前：取得するサイトの画像格納先を選択", fg='#f00', bg='#000', height=2, width=60)
        self.Label2 = tk.Label(
            frame_left, text="後：取得した画像のリサイズ保存先を選択", fg='#f00', bg='#000', height=2, width=60)
        button3 = tk.Button(text="実行", height=2, width=8, command=self.submit)

        Label.pack(padx=5, pady=10)

        item = ['Webスクレイピング入門', 'Aサイト(未実装)', 'Bサイト(未実装)']
        global val
        val = tk.IntVar()
        val.set(0)

        for i in range(len(item)):
            tk.Radiobutton(frame_top, value=i, variable=val,
                           text=item[i]).pack(anchor=tk.W)

        self.Label1.pack(pady=10)
        self.Label2.pack(pady=10)
        button1.pack(in_=frame_right, pady=10)
        button2.pack(in_=frame_right, pady=10)

        item2 = ['png  ->  jpg(未実装）', 'jpg  ->  png',]
        global val1
        val1 = tk.IntVar()
        val1.set(10)
        for i in range(len(item2)):
            tk.Radiobutton(frame_bottom_left, value=i+10,
                           variable=val1, text=item2[i]).pack(anchor=tk.W)

        button3.pack(in_=frame_bottom_right)

        # フレームの配置
        # frame_top.pack(side = tk.TOP, expand = True)
        frame_top.place(x=30)
        frame_left.pack(side=tk.LEFT, expand=True)
        frame_right.pack(side=tk.LEFT, expand=True)
        frame_bottom_left.place(x=30, y=300)
        frame_bottom_right.place(x=400, y=310)

    def btn_click(self, afbf):

        # 実行中のフォルダパスを取得
        dirname = os.path.dirname(__file__)
        # 実行中のフォルダパスを絶対パスで取得
        iDir = os.path.abspath(dirname)
        # ダイアログを開き、選択したフォルダの絶対パスを取得
        folder_name = filedialog.askdirectory(initialdir=iDir)
        if afbf == 'bf':
            global bf
            self.Label1['text'] = folder_name
            bf = self.Label1['text']
        elif afbf == 'af':
            global af
            self.Label2['text'] = folder_name
            af = self.Label2['text']

    def submit(self):
        ch = val.get()
        ch2 = val1.get()
        print(bf, af, ch, ch2, sep='\n')
        if 'bf' in globals() and 'af' in globals():
            if ch == 0 and ch2 == 11:

                # スクレイピング呼び出し
                image_get(bf, ch)

                # リサイズ関数呼び出し
                resize_tra(bf, af)

            elif ch > 0 or ch2 == 10:
                print('未実装が含まれています。')
        elif ch > 0 or ch2 == 10:
            print('未実装が含まれます')

        else:
            print('フォルダ未指定')


if __name__ == "__main__":

    root = tk.Tk()
    root.title("scraping & resize_PG")
    app = Application(master=root)
    app.mainloop()
