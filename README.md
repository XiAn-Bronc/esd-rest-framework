# 创建新项目


* 创建项目
	```python
  django-admin startproject tutorial
  ```

* 创建虚拟环境
  ```python
  python -m venv env
  .\env\Scripts\activate
  
  pip install django
  pip install djangorestframework
  pip install pygments  # We'll be using this for the code highlighting
  ```


* 创建应用程序

  ```python
  python manage.py startapp snippets
  ```

* 更改项目名称（可选）

* 创建要使用的模型

  ```python
  # model.py
  from django.db import models
  from pygments.lexers import get_all_lexers
  from pygments.styles import get_all_styles
  
  LEXERS = [item for item in get_all_lexers() if item[1]]
  LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
  STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
  
  
  class Snippet(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      title = models.CharField(max_length=100, blank=True, default='')
      code = models.TextField()
      linenos = models.BooleanField(default=False)
      language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
      style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
  
      class Meta:
          ordering = ['created']
  ```

* 为代码段模型创建初始迁移，并首次同步数据库
  ```python
  python manage.py makemigrations snippets
  python manage.py migrate
  ```

* 启动开发服务器

  ```python
  python manage.py runserver
  ```

