# MySQL 常用语句

查看表结构注释

查看数据表和最后修改时间

```sql
SELECT
    TABLE_NAME,
    UPDATE_TIME
FROM
    INFORMATION_SCHEMA. TABLES
WHERE
    TABLE_SCHEMA = '数据库名';
```
