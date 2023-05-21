# ⌨️ (0:00:00) Intro
- youtube
  - https://youtu.be/PXMJ6FS7llk
- source code
  - https://github.com/ifrankandrade/automation
# ⌨️ (0:00:31) Project #1 Table Extraction - Extract Tables from Websites
- ウェブサイトからのテーブル抽出
  - pandasライブラリが使用可能
- `pip install pandas`
- `pip install lxml`
- `pip install jupyter`
- 参照データ
  - https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)
# ⌨️ (0:09:38) Table Extraction - Extract Tables from PDFs
- `pip install tk`
- `pip install ghostscript`
- goastscript本体のインストール
  - https://ghostscript.com/releases/gsdnld.html
- `pip install opencv-python-headless`
- `pip install camelot-py`
# ⌨️ (0:13:06) Project #2 - Web Automation & Web Scraping - HTML Basics - Tags and Elements
- articleタグ
  - html5で新しく追加された
  - ウェブページのアクセシビリティを向上させることができ、検索エンジンにとっても有益
    - 検索エンジンは、articleタグを使用して、ページ内の主要なコンテンツを特定し、より正確な検索結果を提供することができます。
    - スクリーンリーダーやその他の支援技術も、articleタグを使用してコンテンツを適切にナビゲートできる
- navタグ
  - ページ内のナビゲーション領域
    - ペジネーションの部分など
- table
  - tr
    - table row
  - td
    - table data

```html
<table>
    <tr>
        <td>a</td>
        <td>b</td>
    </tr>
    <tr>
        <td>c</td>
        <td>d</td>
    </tr>
</table>
```
- iframe
  - 他のページの埋め込みを行える
# ⌨️ (0:24:22) Web Automation & Web Scraping - XPath - Syntax, Functions and Operators
- xpath
  - xml path language
  - XMLドキュメントからノードを取得するためのクエリ言語
    - HTMLページの要素の取得にも利用できる
  - CSSと似てる
- syntax
  - `//tagName`
    - 要素の選択
  - `//tagName[1]`
    - 一致する要素の内，最初に一致した要素を選択
  - `//tagName[@AttributeName="Value"]`
    - 属性名を指定して，要素を選択
  - `//tagName[contains(@AttributeName, "Value")]`
    - 属性名の部分一致検索で，要素を選択
  - `//tagName[srarts-with(@AttributeName, "Value")]`
    - 属性名の前方一致検索で，要素を選択
  - `//tagName[(expression 1) and (expression 2)]`
    - 条件１と２の両方に当てはまる要素を選択
  - `//tagName/tagName`
    - 子要素の選択
  - `//tagName/text()`
    - 要素内のテキストの選択
# ⌨️ (0:28:06) Web Automation & Web Scraping - XPath - Test Your XPath
- xpath playground
  - https://scrapinghub.github.io/xpath-playground/
- chromeのinspectモードでxpathを用い多検索を行う方法
  - inspectモードを開く
  - 「要素」タブ内で`ctrl + f`を押す
  - 検索モードが開く
# ⌨️ (0:33:38) Web Automation & Web Scraping - XPath - Special Characters and Syntax
- `/`
  - 子ノードを検索する
- `//`
  - 全てのノードを検索する

ex.)
```html
<article>
    <h1>Titanic(1997)</h1>
    <p>84 years later...</p>
</article>
```
```xpath
//article/text()
-> None
```
```xpath
//article//text()
-> Titanic(1997)
-> 84 years later...
```
- `/.`
  - 現在のノードを検索する
- `/..`
  - 親ノードを検索する

ex.)
```html
<article>
    <h1>Titanic(1997)</h1>
    <p>84 years later...</p>
</article>
```
```xpath
//h1/.
-> <h1>Titanic(1997)</h1>
```
```xpath
//h1/..
-> <article> <h1>Titanic(1997)</h1> <p>84 years later...</p> </article>
```
- `*`
  - ワイルドカード検索
  - ex.) `./*`
    - すべての子ノードの取得
    - `/..`の逆の意味

ex.)
```html
<article>
    <h1>Titanic(1997)</h1>
    <p>84 years later...</p>
</article>
```
```xpath
//article/*
-> <h1>Titanic(1997)</h1>
-> <p>84 years later...</p>
```
```xpath
//article/*/text()
-> Titanic(1997)
-> 84 years later...
```
# ⌨️ (0:38:17) Automate The News - Installing Selenium and ChromeDriver
- chrome driverのインストール
  - https://chromedriver.chromium.org/downloads
  - zipを展開した際の展開先のパスを後で使用する
- `pip install selenium`
# ⌨️ (0:44:46) Automate The News - Finding Elements
- chromeのinspectモードで所望のxpathがどのようになるかをチェックしたうえでスクリプトを書いていく
# ⌨️ (1:12:34) Automate The News - Headless mode
- これまではseleniumがブラウザを自動で開いていたが，ブラウザを開くことなくスクリプトを実行する方法もある
  - ヘッドレスモード
- Options()
  - seleniumの設定を変更できる
  - デフォルトでfalseになってるheadlessモードをtrueにする
- pythonスクリプトの実行
  - pythonファイルを開いた状態で右上の実行ボタンを押す
# ⌨️ (1:18:18) Automate The News - Preparing Script to Be Run Everyday
- スクリプトを定期的に自動で実行させる
- import os
  - osとのインタラクションを可能にする
    - フォルダの作成など
- ファイルパスに`/`を直接指定しない方がいい
  - 理由
    - OSによってディレクトリ間の区切り文字が異なるから
      - MacOSは`/`だが，WindowsOSは`\`
  - 対処法
    - `os.path.join()`を使用する
      - OSと対話的にパスを作成してくれる
- 出力ファイルを常にスクリプトが存在するパスと同じ場所に配置されるようにするための処置
  - `os.path.dirname(sys.executable)`
    - スクリプト自体が存在するディレクトリのパスを取得する
      - これを出力ファイルのパスに含めることで，スクリプトがどこから実行されても，出力ファイルが同じ場所に保存されるようになる
# ⌨️ (1:30:17) Automate The News - Convert py to exe
- `pip install pyinstaller`
  - pyファイルを自動で実行可能な状態にするため
- `pyinstaller --onefile <file name>`
  - 実際に．pyファイルを実行可能なファイルに変換する
    - buildディレクトリとdistディレクトリが作成される
    - distディレクトリの中に`<file name>.exe`が作成されている
- 実行可能になったら，ファイルをクリックするだけでスクリプトが実行されるようになる
  - Pythonがインストールされていないマシンでも実行できる
- 自動作成されるファイルたちについて
  - buildディレクトリ
    - 必要なPythonモジュールとリソースの置き場
    - スクリプトの依存関係の解析
      - node_modulesディレクトリ的なやつ
  - distディレクトリ
    - ビルドプロセスの採取的な出力が保存される
      - 実行可能なバイナリ（.exe），スクリプト（.app）
  - `<python script file name>.spec`
    - ビルドプロセスの詳細を定義
    - 初回のPyInstaller実行時に自動的に生成され、その後の実行時には既存の.specファイルが使用される
    - ビルド設定を再現するために使用される
      - package.json的なやつ
      - Gitで追跡すべき
# ⌨️ (1:37:18) Automate The News - Schedule Python Script with crontab (macOS)
- `crontab -e`
  - スケジュール実行を定義するファイルを開くためのコマンド
  - 実行間隔，実行ファイルへのパスを設定する
- `crontab -l`
  - 設定されたコマンドの一覧を表示
    - 正しく設定できているか確認できる
- WindowsOSでの設定
  - タスクスケジューラを起動
  - タスクの作成
  - タスクの名前，トリガの設定
  - アクションの作成
    - 実行ファイルのパスを指定
  - 条件を修正
    - すべてのチェックを外す
      - 条件なしで実行されるようにする
  - 設定
    - 失敗した場合もすぐに再実行する設定
  - OK
# ⌨️ (1:42:16) Project #3 - Automate Excel Report - Create a Pivot Table with Python
- 従業員が各生産ラインで費やしている時間をピポットテーブルにまとめるスクリプト
  - ![](https://storage.googleapis.com/zenn-user-upload/5c230e5ebde3-20230521.png)
# ⌨️ (1:49:42) Automate Excel Report - Add a Bar Chart
- `pip install openpyxl`
  - スクリプトでエクセルの操作を実行するためのライブラリ
# ⌨️ (2:05:02) Automate Excel Report - Write Excel Formulas with Python
- エクセル関数をスクリプトで作成する
- `get_column_letter()`
  - 数字で取得アクセスする列データを英語に変換する
    - ex.)
      - 1 -> A
      - 2 -> B
- エクセルを開いて編集しているとき，一時保存用のファイルが作成されている
  - `$~ <file name>.xlsx`
# ⌨️ (2:19:18) Automate Excel Report - Format Cells
# ⌨️ (2:23:04) Automate Excel Report - Convert Pivot Table to Excel Report
# ⌨️ (2:25:32) Automate Excel Report - Generate Excel Reports with One Click (py to exe)
# ⌨️ (2:33:22) Project #4 - Automate WhatsApp