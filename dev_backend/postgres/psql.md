# PSQL

## PSQL Client Command

| Command  | Comment        | Equivalent SQL                                                           |
| :------: | -------------- | ------------------------------------------------------------------------ |
|    \d    | list databases | `SELECT * FROM pg_database;`                                             |
|   \dt    | list tables    | `SELECT * FROM information_schema.tables WHERE table_type='BASE TABLE';` |
|   \dn    | list schemas   | `SELECT * FROM information_schema.schemata;`                             |
| \d TABLE |                | information_schema.columns                                               |

## psql 常用命令

```sql
\l              -- 列出所有数据库
\c dbname       -- 切换数据库
\dt             -- 列出当前 schema 的表
\dt *.*         -- 列出所有 schema 的表
\d tablename    -- 查看表结构
\di             -- 列出索引
\ds             -- 列出序列
\dv             -- 列出视图
\df             -- 列出函数
\du             -- 列出用户/角色
\dp             -- 列出权限
\dx             -- 列出扩展
\x              -- 切换扩展显示模式
\timing         -- 显示查询耗时
\i file.sql     -- 执行 SQL 文件
\o output.txt   -- 输出到文件
\q              -- 退出 psql
```
