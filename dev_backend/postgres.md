# PostgreSQL

## 数据类型

```txt
----------------- 数值类型
smallint -> 2 Byte
integer/int -> 4 Byte
bigint -> 8 Byte
real -> 4 Byte (单精度浮点)
double precision -> 8 Byte (双精度浮点)
numeric(p, s) / decimal(p, s) -> 精确数值
serial -> 自增整数 (4 Byte)
bigserial -> 自增大整数 (8 Byte)
----------------- 字符串类型
char(n)      -- 定长，不足补空格
varchar(n)   -- 变长，有长度限制
text         -- 变长，无长度限制（推荐使用）
bytea        -- 二进制数据
----------------- 日期时间类型
date         -- 日期 (YYYY-MM-DD)
time         -- 时间 (HH:MI:SS)
timestamp    -- 日期+时间
timestamptz  -- 带时区的时间戳（推荐使用）
interval     -- 时间间隔
----------------- 其他常用类型
boolean      -- true/false/null
uuid         -- UUID 类型
json         -- JSON 数据（文本存储）
jsonb        -- JSON 数据（二进制存储，支持索引，推荐）
array        -- 数组类型，如 integer[]
inet/cidr    -- IP 地址/网段
```

## 数据库操作

```sql
-- 创建数据库
CREATE DATABASE mydb;
-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS mydb;
-- 创建数据库时指定编码
CREATE DATABASE mydb WITH ENCODING 'UTF8';
-- 删除数据库
DROP DATABASE mydb;
-- 删除可能不存在的数据库
DROP DATABASE IF EXISTS mydb;
-- 显示当前数据库
SELECT current_database();
-- 列出所有数据库
\l              -- psql 命令
SELECT datname FROM pg_database;
-- 切换数据库（psql）
\c mydb
```

## 表操作

```sql
-- 建表示例
CREATE TABLE users (
    id SERIAL PRIMARY KEY,              -- 自增主键
    username VARCHAR(50) NOT NULL UNIQUE,
    email TEXT NOT NULL,
    age INTEGER CHECK (age > 0 AND age < 150),
    status CHAR(1) DEFAULT 'A',
    created_at TIMESTAMPTZ DEFAULT NOW()
);
-- 使用 IDENTITY（SQL 标准，推荐）
CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
-- 添加表注释
COMMENT ON TABLE users IS '用户表';
-- 添加列注释
COMMENT ON COLUMN users.username IS '用户名';
-- 修改表名
ALTER TABLE users RENAME TO members;
-- 列出当前 schema 的所有表
\dt             -- psql 命令
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public';
-- 查看表结构
\d users        -- psql 命令
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'users';
-- 清空表（重置序列）
TRUNCATE TABLE users RESTART IDENTITY;
-- 删除表
DROP TABLE users;
DROP TABLE IF EXISTS users CASCADE;  -- 级联删除依赖对象
```

## 字段操作

```sql
-- 添加字段
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
-- 删除字段
ALTER TABLE users DROP COLUMN phone;
-- 修改字段类型
ALTER TABLE users ALTER COLUMN phone TYPE TEXT;
-- 重命名字段
ALTER TABLE users RENAME COLUMN phone TO mobile;
-- 设置/删除默认值
ALTER TABLE users ALTER COLUMN status SET DEFAULT 'A';
ALTER TABLE users ALTER COLUMN status DROP DEFAULT;
-- 设置/删除 NOT NULL
ALTER TABLE users ALTER COLUMN email SET NOT NULL;
ALTER TABLE users ALTER COLUMN email DROP NOT NULL;
```

## 数据操作 (DML)

```sql
-- 插入数据
INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com');
-- 批量插入
INSERT INTO users (username, email) VALUES
    ('bob', 'bob@example.com'),
    ('charlie', 'charlie@example.com');
-- 插入并返回生成的 ID（PostgreSQL 特有）
INSERT INTO users (username, email)
VALUES ('dave', 'dave@example.com')
RETURNING id;
-- 插入子查询结果
INSERT INTO users_backup SELECT * FROM users WHERE status = 'A';
-- 更新数据
UPDATE users SET status = 'I' WHERE id = 1;
-- 更新并返回结果
UPDATE users SET email = 'new@example.com'
WHERE id = 1
RETURNING *;
-- 删除数据
DELETE FROM users WHERE id = 1;
-- 删除并返回
DELETE FROM users WHERE status = 'I' RETURNING id;
-- UPSERT（插入或更新）
INSERT INTO users (id, username, email)
VALUES (1, 'alice', 'alice@new.com')
ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;
-- UPSERT（插入或忽略）
INSERT INTO users (username, email)
VALUES ('alice', 'alice@example.com')
ON CONFLICT DO NOTHING;
```

## 查询操作

```sql
-- 基本查询
SELECT * FROM users;
SELECT id, username FROM users WHERE status = 'A';
-- 去重
SELECT DISTINCT status FROM users;
-- 排序
SELECT * FROM users ORDER BY created_at DESC;
-- 分页（LIMIT + OFFSET）
SELECT * FROM users LIMIT 10 OFFSET 20;  -- 第 3 页，每页 10 条
-- 模式匹配
SELECT * FROM users WHERE username LIKE 'a%';      -- 以 a 开头
SELECT * FROM users WHERE username LIKE '__';      -- 恰好两个字符
SELECT * FROM users WHERE email ~ '^[a-z]+@';      -- 正则匹配
SELECT * FROM users WHERE email ~* '^[A-Z]+@';     -- 正则匹配（不区分大小写）
-- IN 操作
SELECT * FROM users WHERE status IN ('A', 'B', 'C');
-- BETWEEN
SELECT * FROM users WHERE age BETWEEN 18 AND 30;
-- CASE WHEN
SELECT username,
    CASE status
        WHEN 'A' THEN '活跃'
        WHEN 'I' THEN '禁用'
        ELSE '未知'
    END AS status_text
FROM users;
```

## 索引

```sql
-- 创建普通索引
CREATE INDEX idx_users_email ON users(email);
-- 创建唯一索引
CREATE UNIQUE INDEX idx_users_username ON users(username);
-- 创建复合索引
CREATE INDEX idx_users_status_created ON users(status, created_at DESC);
-- 创建部分索引（只索引满足条件的行）
CREATE INDEX idx_active_users ON users(username) WHERE status = 'A';
-- 创建表达式索引
CREATE INDEX idx_users_lower_email ON users(LOWER(email));
-- 创建 GIN 索引（用于 JSONB、全文搜索、数组）
CREATE INDEX idx_users_data ON users USING GIN(data);
-- 删除索引
DROP INDEX idx_users_email;
-- 查看表的索引
\di users*      -- psql 命令
```

## 聚合函数与常用函数

```sql
----------------- 聚合函数
COUNT(*)         -- 统计行数
COUNT(DISTINCT col)  -- 去重计数
SUM(col)         -- 求和
AVG(col)         -- 平均值
MAX(col) / MIN(col)  -- 最大/最小值
STRING_AGG(col, ',') -- 字符串聚合
ARRAY_AGG(col)   -- 数组聚合
----------------- 字符串函数
CONCAT('a', 'b', 'c')       -- 字符串拼接 -> 'abc'
'Hello' || ' ' || 'World'   -- 拼接操作符 -> 'Hello World'
LOWER('ABC')                -- 转小写 -> 'abc'
UPPER('abc')                -- 转大写 -> 'ABC'
LENGTH('hello')             -- 长度 -> 5
LPAD('42', 5, '0')          -- 左填充 -> '00042'
RPAD('42', 5, '0')          -- 右填充 -> '42000'
TRIM('  hello  ')           -- 去除两端空格 -> 'hello'
SUBSTRING('hello' FROM 2 FOR 3)  -- 子串 -> 'ell'
REPLACE('hello', 'l', 'L')  -- 替换 -> 'heLLo'
SPLIT_PART('a,b,c', ',', 2) -- 分割取值 -> 'b'
----------------- 数值函数
CEIL(3.2)        -- 向上取整 -> 4
FLOOR(3.8)       -- 向下取整 -> 3
ROUND(3.14159, 2)-- 四舍五入 -> 3.14
TRUNC(3.14159, 2)-- 截断 -> 3.14
MOD(10, 3)       -- 取模 -> 1
ABS(-5)          -- 绝对值 -> 5
RANDOM()         -- 随机数 [0, 1)
----------------- 日期时间函数
CURRENT_DATE     -- 当前日期
CURRENT_TIME     -- 当前时间
CURRENT_TIMESTAMP / NOW()  -- 当前时间戳
EXTRACT(YEAR FROM NOW())   -- 提取年份
DATE_TRUNC('month', NOW()) -- 截断到月初
AGE(timestamp1, timestamp2)-- 计算时间差
NOW() + INTERVAL '1 day'   -- 日期加减
NOW() - INTERVAL '2 hours'
date1 - date2              -- 两个日期相差天数
----------------- NULL 处理
COALESCE(col1, col2, 'default')  -- 返回第一个非 NULL 值
NULLIF(a, b)     -- 如果 a = b 返回 NULL，否则返回 a
```

## 视图

```sql
-- 创建视图
CREATE VIEW active_users AS
SELECT id, username, email
FROM users
WHERE status = 'A';
-- 创建或替换视图
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email, created_at
FROM users
WHERE status = 'A';
-- 创建带 CHECK OPTION 的视图
CREATE VIEW young_users AS
SELECT * FROM users WHERE age < 30
WITH CHECK OPTION;  -- 通过视图插入/更新时强制检查条件
-- 删除视图
DROP VIEW active_users;
DROP VIEW IF EXISTS active_users CASCADE;
-- 物化视图（缓存查询结果）
CREATE MATERIALIZED VIEW user_stats AS
SELECT status, COUNT(*) as cnt FROM users GROUP BY status;
-- 刷新物化视图
REFRESH MATERIALIZED VIEW user_stats;
REFRESH MATERIALIZED VIEW CONCURRENTLY user_stats;  -- 并发刷新，不阻塞读
```

## 集合操作

```sql
-- 并集（去重）
SELECT username FROM users_a
UNION
SELECT username FROM users_b;
-- 并集（保留重复）
SELECT username FROM users_a
UNION ALL
SELECT username FROM users_b;
-- 交集
SELECT username FROM users_a
INTERSECT
SELECT username FROM users_b;
-- 差集
SELECT username FROM users_a
EXCEPT
SELECT username FROM users_b;
```

## 连接查询

```sql
-- 内连接
SELECT u.username, o.order_id
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
-- 左外连接
SELECT u.username, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
-- 右外连接
SELECT u.username, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
-- 全外连接
SELECT u.username, o.order_id
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;
-- 交叉连接（笛卡尔积）
SELECT * FROM users CROSS JOIN products;
```

## 子查询

```sql
-- 标量子查询
SELECT username,
    (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;
-- IN 子查询
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders WHERE amount > 100);
-- EXISTS 子查询
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = u.id);
-- 派生表
SELECT * FROM (
    SELECT username, COUNT(*) as cnt
    FROM users GROUP BY username
) AS t
WHERE cnt > 1;
```

## CTE（公用表表达式）

```sql
-- 基本 CTE
WITH active_users AS (
    SELECT * FROM users WHERE status = 'A'
)
SELECT * FROM active_users WHERE age > 18;
-- 多个 CTE
WITH
    active AS (SELECT * FROM users WHERE status = 'A'),
    young AS (SELECT * FROM active WHERE age < 30)
SELECT * FROM young;
-- 递归 CTE（如查询组织树）
WITH RECURSIVE org_tree AS (
    -- 基础查询（根节点）
    SELECT id, name, parent_id, 1 AS level
    FROM departments
    WHERE parent_id IS NULL
    UNION ALL
    -- 递归查询
    SELECT d.id, d.name, d.parent_id, t.level + 1
    FROM departments d
    INNER JOIN org_tree t ON d.parent_id = t.id
)
SELECT * FROM org_tree ORDER BY level;
```

## 窗口函数

```sql
-- ROW_NUMBER：行号
SELECT username, created_at,
    ROW_NUMBER() OVER (ORDER BY created_at) AS row_num
FROM users;
-- RANK：排名（有并列会跳过）
SELECT username, score,
    RANK() OVER (ORDER BY score DESC) AS rank
FROM users;
-- DENSE_RANK：密集排名（有并列不跳过）
SELECT username, score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM users;
-- 分区窗口
SELECT dept, username, salary,
    ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank
FROM employees;
-- 窗口聚合
SELECT username, salary,
    AVG(salary) OVER () AS company_avg,
    AVG(salary) OVER (PARTITION BY dept) AS dept_avg
FROM employees;
-- LAG / LEAD：前后行值
SELECT username, salary,
    LAG(salary) OVER (ORDER BY id) AS prev_salary,
    LEAD(salary) OVER (ORDER BY id) AS next_salary
FROM employees;
```

## 约束

```sql
CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(50) NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    status CHAR(1) DEFAULT 'A',
    dept_id INTEGER,
    -- 主键约束
    PRIMARY KEY (id),
    -- 唯一约束
    UNIQUE (username),
    UNIQUE (email),
    -- 检查约束
    CHECK (age > 0 AND age < 150),
    CHECK (status IN ('A', 'I', 'D')),
    CHECK (email LIKE '%@%'),
    -- 外键约束
    FOREIGN KEY (dept_id) REFERENCES departments(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
-- 外键的删除策略
-- ON DELETE CASCADE     -- 级联删除
-- ON DELETE SET NULL    -- 设为 NULL
-- ON DELETE SET DEFAULT -- 设为默认值
-- ON DELETE RESTRICT    -- 禁止删除（默认）
-- ON DELETE NO ACTION   -- 延迟检查，效果类似 RESTRICT
-- 添加约束
ALTER TABLE users ADD CONSTRAINT chk_age CHECK (age > 0);
-- 删除约束
ALTER TABLE users DROP CONSTRAINT chk_age;
```

## 序列 (SEQUENCE)

```sql
-- 创建序列
CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
-- 获取下一个值
SELECT nextval('user_id_seq');
-- 获取当前值
SELECT currval('user_id_seq');  -- 需要先调用 nextval
-- 设置序列值
SELECT setval('user_id_seq', 100);
SELECT setval('user_id_seq', 100, false);  -- 下次 nextval 返回 100
-- 删除序列
DROP SEQUENCE user_id_seq;
-- 查看所有序列
\ds     -- psql 命令
```

## 用户与权限

```sql
-- 创建用户
CREATE USER myuser WITH PASSWORD 'mypassword';
-- 创建角色（可以用于权限分组）
CREATE ROLE readonly;
-- 授予数据库权限
GRANT CONNECT ON DATABASE mydb TO myuser;
-- 授予 schema 权限
GRANT USAGE ON SCHEMA public TO myuser;
-- 授予表权限
GRANT SELECT, INSERT, UPDATE ON users TO myuser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO myuser;
-- 授予序列权限（用于 SERIAL 字段）
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO myuser;
-- 撤销权限
REVOKE INSERT ON users FROM myuser;
-- 设置默认权限（新建对象自动授权）
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO readonly;
-- 修改密码
ALTER USER myuser WITH PASSWORD 'newpassword';
-- 删除用户
DROP USER myuser;
-- 查看当前用户
SELECT current_user, session_user;
-- 查看所有用户
\du     -- psql 命令
SELECT * FROM pg_user;
-- 查看表权限
\dp users   -- psql 命令
```

## 事务

```sql
-- PostgreSQL 默认自动提交，使用 BEGIN 开启显式事务
BEGIN;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
-- 回滚
BEGIN;
    DELETE FROM users;
ROLLBACK;
-- 保存点
BEGIN;
    INSERT INTO users (username) VALUES ('alice');
    SAVEPOINT sp1;
    INSERT INTO users (username) VALUES ('bob');
    ROLLBACK TO sp1;  -- 只回滚到保存点，alice 仍存在
COMMIT;
-- 事务隔离级别
BEGIN ISOLATION LEVEL READ COMMITTED;      -- 默认
BEGIN ISOLATION LEVEL REPEATABLE READ;
BEGIN ISOLATION LEVEL SERIALIZABLE;
-- 查看当前隔离级别
SHOW transaction_isolation;
```

## Schema（模式）

```sql
-- Schema 是数据库内的命名空间，用于组织表等对象
-- 创建 schema
CREATE SCHEMA myschema;
-- 在指定 schema 中创建表
CREATE TABLE myschema.users (id SERIAL PRIMARY KEY);
-- 查看当前 search_path
SHOW search_path;
-- 设置 search_path
SET search_path TO myschema, public;
-- 删除 schema
DROP SCHEMA myschema CASCADE;
```

## JSONB 操作

```sql
-- 创建带 JSONB 列的表
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL
);
-- 插入 JSON 数据
INSERT INTO events (data) VALUES ('{"type": "click", "page": "/home"}');
-- 查询 JSON 字段
SELECT data->>'type' AS event_type FROM events;  -- 返回文本
SELECT data->'page' FROM events;                  -- 返回 JSON
-- 嵌套访问
SELECT data->'user'->>'name' FROM events;
-- 包含查询
SELECT * FROM events WHERE data @> '{"type": "click"}';
-- 存在查询
SELECT * FROM events WHERE data ? 'type';      -- 键存在
SELECT * FROM events WHERE data ?| array['type', 'page'];  -- 任一键存在
SELECT * FROM events WHERE data ?& array['type', 'page'];  -- 所有键存在
-- GIN 索引优化 JSONB 查询
CREATE INDEX idx_events_data ON events USING GIN(data);
```

## 扩展 (Extensions)

```sql
-- 查看已安装扩展
\dx     -- psql 命令
SELECT * FROM pg_extension;
-- 查看可用扩展
SELECT * FROM pg_available_extensions;
-- 安装扩展
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";      -- UUID 生成
CREATE EXTENSION IF NOT EXISTS "pg_trgm";        -- 模糊搜索
CREATE EXTENSION IF NOT EXISTS "hstore";         -- 键值对类型
CREATE EXTENSION IF NOT EXISTS "postgis";        -- 地理信息
-- 使用 UUID
SELECT uuid_generate_v4();
-- 使用 pg_trgm 进行模糊搜索
SELECT * FROM users
WHERE username % 'alice'  -- 相似度匹配
ORDER BY similarity(username, 'alice') DESC;
```

## 维护命令

```sql
-- VACUUM：回收死元组空间
VACUUM users;             -- 普通清理
VACUUM FULL users;        -- 完全清理（会锁表）
VACUUM ANALYZE users;     -- 清理并更新统计信息
-- ANALYZE：更新统计信息（用于查询优化器）
ANALYZE users;
-- REINDEX：重建索引
REINDEX INDEX idx_users_email;
REINDEX TABLE users;
-- 查看表大小
SELECT pg_size_pretty(pg_total_relation_size('users'));
-- 查看数据库大小
SELECT pg_size_pretty(pg_database_size(current_database()));
-- 查看活动连接
SELECT * FROM pg_stat_activity;
-- 终止连接
SELECT pg_terminate_backend(pid) FROM pg_stat_activity
WHERE datname = 'mydb' AND pid <> pg_backend_pid();
```

## pg_hba.conf 访问控制

PostgreSQL 使用 `pg_hba.conf` 文件控制客户端访问（而非 MySQL 的 `user@host` 格式）：

```conf
# TYPE  DATABASE  USER  ADDRESS       METHOD
local   all       all                 peer        # Unix socket 本地连接
host    all       all   127.0.0.1/32  scram-sha-256  # 本地 IPv4
host    all       all   ::1/128       scram-sha-256  # 本地 IPv6
host    mydb      myuser 192.168.1.0/24 scram-sha-256  # 局域网访问
host    all       all   0.0.0.0/0     scram-sha-256  # 所有 IP（生产慎用）
```

修改后需重新加载配置：
```sql
SELECT pg_reload_conf();
```

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
