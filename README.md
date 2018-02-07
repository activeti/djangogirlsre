#作業メモ

## 仮想環境の作成
python3 -m venv myvenv
## 仮想環境有効化
source ./myenv/bin/activate
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
 以下参照
 [GitHub登録からプッシュまでの流れ](https://qiita.com/KosukeQiita/items/cf39d2922b77ac93f51d)