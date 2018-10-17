# sqlmap 笔记
---------------

### sqlmap常用命令

-u "url" 被注入的网址？id=11

--dbms=mysql 使用哪种数据库

--level(2-5) 注入等级越高越全

--cookie="cookie" 抓包的cookie值 要用 --level=2 以上


--dbs 爆数据库名称ta
--tables -D "db_name" 爆出数据库的列名表名

--columns -T "table_name" -D "db_name" 爆出数据库表的字段名

--dump -C "column_name" -T ""

--sql-shell 进入sql语句界面

--os-shell 进入系统dos 或 shell 命令界面
