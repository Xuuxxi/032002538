from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from app import app

http_server=HTTPServer(WSGIContainer(app))
http_server.bind(5000,"0.0.0.0")            # 端口必须与flask端口相同
http_server.start(1)                        # num_processes默认值为1，即默认仅开启一个进程；如果<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程；如果>0，则创建num_processes个子进程。
IOLoop.instance().start()