#作業メモ

## 仮想環境の作成
python3 -m venv myvenv
## 仮想環境有効化
source ./myvenv/bin/activate
(無効化) deactivate
## (vscode使用のみ)vscodeのワークスペース設定
settings.jsonに以下を記載
>{
>    "python.pythonPath": "${workspaceFolder}/myvenv/bin/python",
>    "python.linting.pylintEnabled": false,
>    "python.linting.flake8Enabled": true
>}
## Djangoインストール
> pip install django==1.11
## プロジェクト作成
> django-admin startproject mysite .

## git設定
git init
git add -A .
git commit -m "Inisial commit"
git config --global user.name [ユーザ名]
git config --global user.email [emailアドレス]
git remote add origin https://github.com/activeti/djangogirlsre.git
git push origin master
.gitignoreあとで作成してしまった場合は「git rm -r --cached .」実行

以下参照
[GitHub登録からプッシュまでの流れ](https://qiita.com/KosukeQiita/items/cf39d2922b77ac93f51d)

## mysite/settings修正
言語、タイムゾーン設定

## アプリケーション作成
python management startapp blog

## model作成
/blog/models.py参照
マイグレーションファイル生成
python manage.py makemigration
マイグレーションSQL確認
python manage.py sqlmaigrate blog 0001
ちなみに中身こんなん

>> BEGIN;
>> --
>> -- Create model Post
>> --
>> CREATE
>> TABLE "blog_post"
>>  ("id" integer NOT NULL PRIMARY KEY >>AUTOINCREMENT,
>>   "title" text NOT NULL,
>>    "text" > text NOT NULL, "created_date" date >>NOT NULL,
>>     "published_date" date NULL,
>>      "auther_id" integer NOT NULL > REFERENCES >>"auth_user" ("id"));
>> CREATE INDEX "blog_post_auther_id_275a1b8c" ON >>"blog_post" ("auther_id");
>> COMMIT;


適応
python migrate blog

## 管理画面確認
Postモデルをadmin画面に登録するため、blog/admin.pyに追記が必要
開発サーバ起動
python manage.py runserver
http://localhost:8000/admin
にアクセスしてもアカウントがないのでまだログインできない
管理アカウント作成
python manage.py createsuperuser
いろいろ入力

## デプロイ!!
Herokuにアップロードするための手順はスキップ
環境書き出しだけ行う
pip freeze > requirements.txt

※ デプロイ環境とローカルの設定をファイルで指定する方法は必要だと思うので、
 あとで調べよう。


 ## クエリセット
 python manage.py shell とすると対話モードになる
 ORMのコマンドがいろいろ打てる

## テンプレート&静的ファイル

静的ファイル置き場
>blog/
>    static/
>        blog/
>            css/
>                blog.css

load もstaticと記述するのみ チュートリアルみたいな設定は無し
静的ファイルの置き方はこちら参照
[Python Django入門 (4)](https://qiita.com/kaki_k/items/6e17597804437ef170ae)
