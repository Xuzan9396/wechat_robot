# wechat_robot
WeChat 机器人，python + websocket + go 实现
项目地址 : [https://github.com/Xuzan9396/wechat_robot](https://github.com/Xuzan9396/wechat_robot)
## 步骤

1. **系统准备**: 准备 Windows 系统，可以选择腾讯云服务器,或者win10。

2. **微信版本要求**:
    - 使用微信版本 3.7.0.30。
    - 设置微信不要自动更新。
    - 打开微信，登录到你自己的账号。

   ![image](https://github.com/Xuzan9396/wechat_robot/assets/24741439/2f88944a-9f8e-4178-a299-83aa716aa592)
   
   3.7.0.30 版本下载地址: [下载地址](https://pan.baidu.com/s/1Fln_5ZlotxtI4a5EyhWEdQ?pwd=7gbe)

3. **启动机器人**: 可以使用 Python 启动或直接运行 GUI 程序。
    - Python 启动:
      ```bash
      pip install -r requirements.txt 
      python main.py
      ```
   - 也可以自己打包gui
   - 打包命令
     ```bash
     pyinstaller -F -w --icon=ui/img/wechat.ico main.py
     ```
     
   
    - 或者使用我打包好的，在项目wechat_gui目录可以测试,GUI 程序启动:
      ```bash
      wechat_gui.exe
      ```
   

4. **WebSocket 通信配置**: GUI页面是通过 WebSocket 协议传输。
    - WebSocket 端口
    - WebSocket 认证: 默认认证规则，会在你的头部添加 `Authorization: Bearer <your_token>`
    - WebSocket Path 认证: 默认路径为 `/`

5. **WebSocket 客户端测试**: 可以打开 WebSocket 客户端进行测试，例如发送一条消息，WebSocket 协议如下：
   ```json
   { 
     "action": "SendText",
     "params": {
       "receiver": "filehelper",
       "msg": "消息发送到文件夹了，请查收"
     }
   }

6. **简单的 WebSocket 客户端测试**: 使用 Go 编写的简单 WebSocket 客户端进行测试,在ws_client_go 目录下,或者运行打包的程序
```
有golang环境的可以直接运行
go run ws_client.go  -addr="你的服务器地址" -wxid="没有就不需要填写" -ws_auth="你的ws服务器认证信息" -ws_path="你的ws服务器路径，默认 /"
例如：
go run ws_client.go  -addr="xxx.xxx.xxx.xxx:port" -wxid="wxid_xxxxxxxx" -ws_auth="auth123" -ws_path="/"

windows 系统 cmd 运行
.\ws_client.exe -addr="你的服务器地址" -wxid="没有就不需要填写" -ws_auth="你的ws服务器认证信息" -ws_path="你的ws服务器路径，默认 /"

mac 系统 arm 架构的
.\ws_client_darwin_arm64  -addr="你的服务器地址" -wxid="没有就不需要填写" -ws_auth="你的ws服务器认证信息" -ws_path="你的ws服务器路径，默认 /"

mac 系统 amd64 架构的
.\ws_client_darwin_amd64 -addr="你的服务器地址" -wxid="没有就不需要填写" -ws_auth="你的ws服务器认证信息" -ws_path="你的ws服务器路径，默认 /"
```  
- -addr : 你的服务器ip地址，如果是本地就输入 127.0.0.1:xxxx
- path: /
- -ws_auth： 你的token,gui界面的token
- wxid: 没有就为空


## 演示
![wechat](https://github.com/Xuzan9396/wechat_robot/assets/24741439/f57b43ad-c116-44b5-9658-e34898152cdd)


## 其他
 `除了发消息，还有其他功能，有需求的去看源码吧`

[依赖库 https://github.com/ljc545w/ComWeChatRobot](https://github.com/ljc545w/ComWeChatRobot)
