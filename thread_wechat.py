import sys
from threading import Thread
import wechat.ws_server as ws_servers
from wechat.wxRobot import WeChatRobot, get_wechat_pid_list,_WeChatRobotClient
import comtypes
from PySide6.QtCore import QThread


class myWechatThread (QThread):
    def __init__(self, threadID, name,wsPort: int,wsToken: str,wsPath: str):
        super(myWechatThread, self).__init__()
        self.threadID = threadID
        self.name = name
  
        ws_servers.SERVER_PORT = wsPort
        ws_servers.SEC_TOKEN = wsToken
        ws_servers.WS_PATH = wsPath
        
    def run(self):
        comtypes.CoInitialize()
        try:
            print ("开启线程： " + self.name)
            self.sartWechat()
        except Exception as e:
            print("Exception in thread:", e)
        finally:
            comtypes.CoUninitialize()
     

    def sartWechat(self):
        pid_list = get_wechat_pid_list()
        if not pid_list:
            print('没有发现微信进程！')
            sys.exit(-1)
    
        print(f'微信进程：{pid_list}')
        _WeChatRobotClient._instance = None
        wx_bot = WeChatRobot(pid_list[0])
        wx_bot.StartService()
        print('StartReceiveMessage')
        wx_bot.StartReceiveMessage(port=ws_servers.TCP_HOOK_PORT)  # 微信的消息都会推送到TCP 

        self.my_server = ws_servers.WebsocketServer(wx_bot)  # 具体配置请在文件头自己配置
        self.my_server.run()

        # 正常情况，以下代码不会执行
        print('StopService')
        self.wx_bot.StopService()
    @staticmethod
    def send_test_msg( wxid: str,content: str):
        # 使用传入的数据做某事
        print(f"从主线程收到的数据: {wxid},{content}")
        pid_list = get_wechat_pid_list()
        if not pid_list:
            print('没有发现微信进程！')
            sys.exit(-1)
    
        print(f'微信进程：{pid_list}')
        wx_bot = WeChatRobot(pid_list[0])
        wx_bot.StartService()
        print('StartReceiveMessage')
        wx_bot.StartReceiveMessage(port=ws_servers.TCP_HOOK_PORT)  # 微信的消息都会推送到TCP 
        # result = wx_bot.SendText("filehelper", "hello world")
        result = wx_bot.SendText(wxid, content)
        print(f"发送消息结果: {result}")
                # 正常情况，以下代码不会执行
        print('StopService')
        wx_bot.StopService()
        
        


