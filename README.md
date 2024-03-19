## DB migrate
`docker exec {コンテナid} python -m app.migrate_db`

## db操作
`docker exec -it {コンテナid} bash`  
`mysql -u tester -p`  (パスワード入力)  
`use test;`  
`show tables;`  
`select * from {テーブル名}`

## 流れ

issue確認，ブランチ切る  
`git checkout -b {ブランチ名}`  
↓  
コードの変更，動作確認  
変更を保存したら  
`docker compose build`  
`docker compose up`  
↓  
変更を加えたファイルをステージング  
`git add {addしたいファイル名}`  
addしたファイルを確認したいとき  
`git status`  
↓  
addしたファイルをcommit  
`git commit -m "コミットメッセージ"`  
commitの確認  
`git log`  
↓  
commitしたファイルをpush  
`git push origin {作業しているブランチ}`  


今いるブランチの確認  
`git branch`

issueの内容を実装できたらpull requestを作成→後藤がレビュー