import tkinter as tk
import tkinter.filedialog
import threading
import time
from tkinter import messagebox

class WritingApp(tk.Frame):
    # text Widgetに関する情報を格納する変数
    text = None

    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("590x500")
        self.frame = tk.Frame(self.master)
        # timer_labelでウィンドウが広がらないようにする
        self.frame.grid(padx=20)

        self.timer_label = tk.Label(self.frame, text="", font=("Meiryo", 20), anchor="w")
        self.timer_label.grid(column=2, row=3)

        self.text = tk.Text(self.frame, bg="#202020", fg="white", font=("Meiryo",12), width=50, height=15, relief=tk.GROOVE, bd=20)
        self.text.grid(column=1, row=0)
        self.text.bind_all("<KeyPress>", self.start_and_reset_timer)

        self.end_button = tk.Button(self.frame, text="終わり！", bg="#c0c0c0", fg="black", width=10, command=self.finish_timer)
        self.end_button.grid(column=1, row=2, pady=5)

        self.save_button = tk.Button(self.frame, text="保存する", bg="#c0c0c0", fg="black", width=10, command=self.save_text)
        self.save_button.grid(column=1, row=3)

        # タイマー用変数
        self.second = 10
        self.flag = False  # フラグを初期化
        self.t = None # スレッドの初期化

        # 入力されたキーを格納するリスト
        self.key = []

    def start_and_reset_timer(self, event):
        # 入力されたキーを取得
        key = event.keysym
        self.key.append(key)

        # 最初のキーが入力されたらタイマー開始
        if len(self.key) == 1:
            # スレッド処理
            self.flag = True
            self.t = threading.Thread(target=self.timer)
            self.second = 10
            self.timer_label.configure(text="")
            self.t.start()
        else:
            # タイマーをリセット
            self.second = 10

    def timer(self):
        while self.flag:
            time.sleep(1)  # 1秒待機
            self.second -= 1
            # タイマー残りが5秒以下になったら表示
            if 6 > self.second >= 0 and self.flag:
                self.timer_label.configure(text=self.second)
            elif self.second < 0:
                # 0秒以下になると入力テキストを全部消す
                self.text.delete("1.0", tk.END)
                self.timer_label.configure(text="")

    def finish_timer(self):
        self.flag = False
        self.timer_label.configure(text="")
        text_cont = len(self.text.get(0., tk.END)) - 1
        messagebox.showinfo("終了です", f"お疲れ様でした！\n打った文字数は{str(text_cont)}文字でした。")

    def save_text(self, event=None):
        """テキストに名前を付けて保存する"""
        f_type = [("Text", ".txt")]

        file_path = tkinter.filedialog.asksaveasfilename(filetypes=f_type, defaultextension=".txt")

        if file_path != "":
            with open(file_path, "w") as f:
                f.write(self.text.get("1.0", "end-1c"))

        return

if __name__ == "__main__":
    root = tk.Tk()
    # デフォルトの背景色を変更
    root.tk_setPalette(background="#252525")
    root.title("鬼ライティングアプリ")
    app = WritingApp(master=root)
    app.mainloop()
