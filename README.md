# FastAPI + SQLModel + Alembic

mysql> DESCRIBE song;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| name   | varchar(255) | NO   |     | NULL    |                |
| artist | varchar(255) | NO   |     | NULL    |                |
| id     | int          | NO   | PRI | NULL    | auto_increment |
+--------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> DESCRIBE song;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| name        | varchar(255) | NO   |     | NULL    |                |
| artist      | varchar(255) | NO   |     | NULL    |                |
| id          | int          | NO   | PRI | NULL    | auto_increment |
| description | varchar(255) | NO   |     |         |                |
| count       | varchar(64)  | NO   |     | 0       |                |
+-------------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)