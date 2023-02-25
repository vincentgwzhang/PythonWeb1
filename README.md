建立虚拟环境
python3 -m venv django_venv #建立虚拟环境
cd django_venv/bin
source activate # 进入虚拟环境

pip list # 看当前虚拟环境下有什么包
pip install django


# 创建 django 工程
django-admin startproject <project_name>

# 在网站的基础上创建应用
cd <project_name>
python3 manage.py startapp app