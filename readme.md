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
# ⌨️ (1:04:34) Automate The News - Exporting Data to a CSV File
# ⌨️ (1:12:34) Automate The News - Headless mode
# ⌨️ (1:18:18) Automate The News - Preparing Script to Be Run Everyday
# ⌨️ (1:30:17) Automate The News - Convert py to exe
# ⌨️ (1:37:18) Automate The News - Schedule Python Script with crontab (macOS)
# ⌨️ (1:42:16) Project #3 - Automate Excel Report - Create a Pivot Table with Python
# ⌨️ (1:49:42) Automate Excel Report - Add a Bar Chart
# ⌨️ (2:05:02) Automate Excel Report - Write Excel Formulas with Python
# ⌨️ (2:19:18) Automate Excel Report - Format Cells
# ⌨️ (2:23:04) Automate Excel Report - Convert Pivot Table to Excel Report
# ⌨️ (2:25:32) Automate Excel Report - Generate Excel Reports with One Click (py to exe)
# ⌨️ (2:33:22) Project #4 - Automate WhatsApp