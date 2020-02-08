# playagricola-cards-scraper

playagricola.comのカードリストをCSV形式で取得するスクリプトです。

## init

```sh
$ cd playagricola-cards-scraper/
$ pip install -r requirements.txt
```

## exec

`scraper.py` 17行目の `CARD_ID` を、目的のデッキに対応する値に設定してください。(デフォルトはJ4デッキ)

```sh
$ python scraper.py
```

正常に終了すると、result.csvが出力されます。
