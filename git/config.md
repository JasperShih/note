
* --system  
包含系统上每一个用户及他们仓库的通用配置

* --global  
只针对当前用户

* 当前使用仓库的 Git 目录中的 config 文件（no add argument）  
针对该仓库

> 每一个级别覆盖上一级别的配置

~~~bash
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
~~~