# 鬼ライティングアプリ





https://github.com/user-attachments/assets/d1329be6-f237-4fff-83e2-c43e2a04f62e
# 概要
Udemyの動画講座「100 Days of Code: The Complete Python Pro Bootcamp」のポートフォリオ課題(ヒント・模範解答無し)のお題に従い、厳しいデスクトップライティングアプリを作成いたしました。<br>
なぜ厳しいかというと、10秒間文字を打たないとそれまで書いてきた文章が消えてしまうからです。<br>
文章が消されないように、強制的にライティングさせるという意図のGUIライティングアプリです。<br>
Pythonに標準で組み込まれているGUIライブラリである、tkinterを使用しました。
# 使用技術
- tkinter
- threading(スレッドを使った並行処理をサポートするためのPythonの標準モジュール)
# 開発環境
- Python 3.12
# 開発期間
約5日
# 機能一覧
- 10秒のカウントダウン機能
- 10秒間文字入力が無ければ打ってきた文章を削除する機能
- 「終わり」ボタンをクリックすると入力文字数を表示し、入力内容をPCに保存する機能
# 実行方法
- まず、こちらのURLよりPython 3.12系をダウンロードします。https://www.python.org/downloads/<br>
  ※「Add Python to PATH」にチェックを入れることで環境変数を自動設定します。
- 次に、こちらのコマンドで任意のフォルダにリポジトリをクローンします。`git clone https://github.com/Erika0701momo/Disappearing-Text-Writing-App.git`
- 次に、こちらのコマンドでプロジェクトフォルダに移動します。`cd Disappearing-Text-Writing-App`
- 最後に、`python main.py`(もしくは`python3 main.py`)を実行するとアプリが立ち上がります。
# 苦労したところ
- カウントダウンタイマーの動作です。スレッドを使いタイマーを動作させましたが、スレッドを量産してしまいタイマーの動きがおかしくなったり、それを解決したら今度は文字入力が遅くなりました。<br>
スレッドを強制終了させることで解決に至りました。スレッドを理解することは困難でした。
- UIにも苦戦しました。カウントダウンの数字の表示で、なかなか思うようなレイアウトにならず、試行錯誤しました。
# 支援とリソース
詰まってしまった時は、就労移行支援事業所のプログラミング講師の方と適宜コミュニケーションを取りながら進めました。また、ChatGPTも活用しました。
