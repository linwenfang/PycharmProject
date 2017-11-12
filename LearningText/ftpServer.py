import socket
from pyftpdlib.handlers import ThrottledDTPHandler
# from pyftpdlib.servers import MultiprocessFTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.servers import ThreadedFTPServer
def hanshu(user,password,ftppath):
    authorizer=DummyAuthorizer()
    authorizer.add_user(user,password,ftppath,perm='elr')
    #下面这一句是任何人都可以访问的
    # authorizer.add_anonymous(ftppath)
    #头部
    handler=FTPHandler
    handler.authorizer=authorizer
    handler.banner="pyftpdlib based ftpd ready"
#ssl认证
    handler.tls_control_required=True
    handler.tls_data_required=True
#开启服务器
    #获取本机ip地址
    ip=socket.gethostbyname(socket.gethostname())

    #多线程
    server=ThreadedFTPServer((ip,21),handler)
    server.max_cons=48#ip总连接数
    server.max_cons_per_ip=3#每个ip连接总数
    server.serve_forever()#一直打开
if __name__ == '__main__':
    user='liuruiqing'
    password='123456'
    #ftp路径
    ftppath='E:\PycharmProjects\First\start'
    hanshu(user,password,ftppath)