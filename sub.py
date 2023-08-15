import ctypes, sys, subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def init():
    if is_admin():
        # 代码运行在管理员模式下
        # 执行您需要的操作cmd+R 调出，输入 regedit
        # 搜索 计算机\HKEY_CLASSES_ROOT\WeChatRobot.CWeChatRobot 看是否注入 
        subprocess.run(["CWeChatRobot.exe", "/regserver"])
    else:
        # 请求管理员权限
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == '__main__':
    init()
