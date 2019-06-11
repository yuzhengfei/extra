# extra-income
毕业设计 --外包项目网站 -- vue+python+flask+uwsgi+nginx+mysql




## 启动步骤：
### 启动后台：
1. cd back 
2. virtualenv --no-site-packages extra_env
3. pip install -r requirements.txt 
4. python run.py
> 以上开启后台dev环境
5. uwsgi extra_uwsgi.ini
6. sudo ln -s /home/genhongchan/code/python_web/extra-income/back/extra_nginx.conf  /etc/nginx/conf.d/
7. sudo /etc/init.d/nginx start

> 以上开启pro环境，开启uwsgi+nginx **5-7为本人Ubuntu启动方式,pro环境下忽略3**


### 启动前端：
1. cd front
2. npm install
3. npm run dev
> 以上开启前端dev环境
4. npm run build

> 以上开启前端pro环境，**pro环境下忽略3**


### V0.0.1 腾讯云发布
#### 项目第一个版本已经在腾讯云上线，地址为：[http://193.112.9.242:3390/static/index.html](http://193.112.9.242:3390/static/index.html)，由于是第一版，可能会有一些意想不到的bug，欢迎把我服务器搞蹦。
> （ps.云服务器为学生版入门服务器，带宽和速度方面受限，可能会出现下载过慢的问题,另外请在IE9以上访问）
