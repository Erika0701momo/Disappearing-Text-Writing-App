import tkinter as tk
import threading
import time
from tkinter import messagebox

class WritingApp(tk.Frame):
    # text Widgetに関する情報を格納する変数
    text = None

    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("590x510")
        self.frame = tk.Frame(self.master)
        # timer_labelでウィンドウが広がらないようにする
        self.frame.grid(padx=20)

        self.timer_label = tk.Label(self.frame, text="", font=("Meiryo", 20), anchor="w")
        self.timer_label.grid(column=2, row=3)

        self.text = tk.Text(self.frame, bg="#202020", fg="white", font=("Meiryo",12), width=50, height=15, relief=tk.GROOVE, bd=20)
        self.text.grid(column=1, row=0)
        self.text.bind_all("<KeyPress>", self.reset_timer)

        self.start_button = tk.Button(self.frame, text="スタート！", bg="#c0c0c0", fg="black", width=10, command=self.start_timer)
        self.start_button.grid(column=1, row=2, pady=2)

        self.end_button = tk.Button(self.frame, text="終わり！", bg="#c0c0c0", fg="black", width=10, command=self.finish_timer)
        self.end_button.grid(column=1, row=3, pady=5)

        self.save_button = tk.Button(self.frame, text="保存する", bg="#c0c0c0", fg="black", width=10)
        self.save_button.grid(column=1, row=4)

        # タイマー用変数
        self.second = 10
        self.flag = True
        self.t = None

    def start_timer(self):
        # 既存のスレッドがあれば停止する
        if self.t and self.t.is_alive():
            self.flag = False
            self.t.join() # スレッドの終了を待つ

        # スレッド処理
        self.t = threading.Thread(target=self.timer)
        self.flag = True
        self.second = 10
        self.timer_label.configure(text="")
        self.t.start()

    def timer(self):
        while self.flag:
            self.second -= 1
            if 6 > self.second > -1:
                self.timer_label.configure(text=self.second)
            if self.second == 0:
                self.text.delete("1.0", tk.END)
                self.finish_timer()
            time.sleep(1)

    def reset_timer(self, event):
        self.second = 10
        self.start_timer()


    def finish_timer(self):
        self.flag = False
        self.timer_label.configure(text="")

if __name__ == "__main__":
    root = tk.Tk()
    # デフォルトの背景色を変更
    root.tk_setPalette(background="#252525")
    app = WritingApp(master=root)
    app.mainloop()
