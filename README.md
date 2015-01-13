README
======

簡易 RSS Reader です。

OPML のインポートのみ (というか、livedoor Reader) 対応させてます。
なので、1 つのサイトを現状登録する事は出来ません。

CSS, JS については、省略しています。

## 依存関係

Python のバージョンは 2.7.9 で確認しています。
また、依存しているライブラリについては、``requirements.txt`` に書いています。

## セットアップ

一応 migrate をかけた ``rss_reader.db`` を置いていますが、
そちらの動作も確認する場合は下記手順で migrate できます。

```bash
$ pip install -r requirements.txt
$ python migrate/manage.py version_control
$ python migrate/manage.py upgrade
```

ダウングレードさせる場合は下記の通りに実行して下さい。

``$ python migrate/manage.py downgrade 0``

## 実行方法

``reader.py`` が実行ファイルになっています。下記の通りに実行して下さい。

``$ python reader.py``
