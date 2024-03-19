## DB migrate
`docker exec {コンテナid} python -m app.migrate_db`

## db操作
`docker exec -it {コンテナid} bash`  
`mysql -u tester -p`  (パスワード入力)  
`use test;`  
`show tables;`  
`select * from {テーブル名}`
