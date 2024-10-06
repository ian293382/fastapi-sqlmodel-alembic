# FastAPI + SQLModel + Alembic 
## 使用 Alembic 來進行資料庫版本管理

```sql
mysql> DESCRIBE song;
+----+--------------+------+-----+---------+----------------+
| id | int          | NO   | PRI | NULL    | auto_increment |
| name | varchar(255) | NO   |     | NULL    |                |
| artist | varchar(255) | NO   |     | NULL    |                |
+----+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> DESCRIBE song;
+----+--------------+------+-----+---------+----------------+
| id | int          | NO   | PRI | NULL    | auto_increment |
| name | varchar(255) | NO   |     | NULL    |                |
| artist | varchar(255) | NO   |     | NULL    |                |
| description | varchar(255) | NO |         | NULL           |
| count | varchar(64) | NO   |     | 0      |                |
+----+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

示範 Alembic 實作過程
：由於他是專注在sql 表格欄位生成 所以要將其他東西創建出來要再補 他不會自動擴增api 內部需求需要自行修改model

安裝
`$pip install alembic`


初始化：將會自動生成出 遷移軟體相關設定去牽動資料庫
`alembic init migrations`

創建遷移表格文件 
`alembic revision --autogenerate -m "create songs table"`

升級表格
`alembic upgrade head`

相對升級
`alembic upgrade +1`

相對降低等級
`alembic downgrade -1`

目前版本
`alembic current`

## docker-compose

`docker-compose run --rm web alembic init -t async migrations`

`docker-compose run --rm web alembic revision --autogenerate -m "Add description and count to Song"`
