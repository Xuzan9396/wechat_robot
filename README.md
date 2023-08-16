# wechat_robot
wechat机器人

## 步骤
 1. 需要准备windows系统，可以选择腾讯云服务器
 2. 需要依赖微信版本 3.7.0.30，设置不要自动更新，打开微信登录你自己的微信
 <img width="393" alt="image" src="https://github.com/Xuzan9396/wechat_robot/assets/24741439/2f88944a-9f8e-4178-a299-83aa716aa592">
 3. 可以python 启动
   pip install -r requirements.txt 
   python main.py
  或者直接打开gui程序
  wechat_gui.exe
 4. gui页面是通过ws协议传输
  ws 端口
  ws 认证，默认认证规则，会在你的头部添加 Authorization: Bearer 你的token
  ws path认证，默认:/
 5. 可以打开ws client 测试，例如我发送一条消息，ws协议如下
```json
{ "action": "SendText", "params": {"receiver": "filehelper", "msg": "消息发送到文件夹了，请查收"}}
```
6. 写的简单的ws客户端可以测试
   
使用go run ws_client.go 
然后输入你的服务器连接地址 



## 演示
![wechat](https://github.com/Xuzan9396/wechat_robot/assets/24741439/f57b43ad-c116-44b5-9658-e34898152cdd)
