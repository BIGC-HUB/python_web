from flask import Flask

# 先要初始化一个 Flask 实例
app = Flask(__name__, static_url_path='')
# 定义路由和路由处理函数的方式如下
# ==========================
# 用 app.route 函数定义路由，参数是一个 path 路径
# 下一行紧跟着的函数是处理这个请求的函数
# @ 是一个叫装饰器的东西, 现在无必要知道具体的原理, 只要用它就好了
# 注意 methods 参数是一个 list，它规定了这个函数能接受的 HTTP 方法
@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')

# 运行服务器
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
    # app.run() 开始运行服务器
    # 所以你访问下面的网址就可以打开网站了
    # http://127.0.0.1:2000/
