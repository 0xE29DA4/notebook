# Django
## 项目结构

- project_name/settings.py
	- 项目配置项
- project_name/urls.py
	- 项目路由配置
- project_name/wsgi.py
	- 项目与 WSGI 协议兼容的 web 服务器入口
- app_name/admin.py
	- 提供了 admin 后台管理
- app_name/apps.py
	- 应用配置项
- app_name/models.py
	- 用于操作应用的数据库模型
- app_name/tests.py
	- 用于单元测试
- app_name/views.py
	- 用于编写视图
- templates
	- 模板存放路径
- db.sqlite3
	- 数据库文件
- manage.py
	一般无需编辑此文件，通常在终端输入 `python manage.py <命令>` 来和项目交互，可以输入 `python manage.py help` 查看帮助

## project 与 app

一个 django project 由若干 app 组成，一个 app 也可被用到不同项目，通过 `python manage.py startapp <app>` 创建一个 app

## manage.py 指令


|        命令        | 备注       |
| :--------------: | -------- |
| startapp \<name> | 创建一个 App |
|                  |          |

