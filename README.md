HerokuLoggingServer
===

受け付けたリクエスト内容をログ出力する Heroku アプリです。

### heroku 環境作成

```
$ heroku login
$ git clone https://github.com/n4cl/HerokuLoggingServer.git
$ cd HerokuLoggingServer
$ heroku create
$ git push heroku main
```

### ログの監視

```
$ heroku logs --tail
```
