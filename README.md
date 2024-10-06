# FastAPI + SQLModel + Alembic

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