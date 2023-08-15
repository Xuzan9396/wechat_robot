from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Signal,QObject
from ui.Ui_console_ui import Ui_MainWindow
import sys
import datetime
import thread_wechat
import sub
# pip install PySide6==6.5.2


class PrintLogger(QObject):  # 继承 QObject，这样我们就可以使用信号了
    update_signal = Signal(str)

    def __init__(self, stdout):
        super().__init__()  # 调用 QObject 的初始化方法
        self.stdout = stdout

    def write(self, text):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_text = f"{current_time} {text}"
        self.update_signal.emit(formatted_text)  # 发射信号
        # self.stdout.write(formatted_text)


    def flush(self):
        pass


class MyWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.bind()
    def bind(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.startFunc)
        

        self.print_logger = PrintLogger(sys.stdout)
        # Redirect sys.stdout
        sys.stdout = self.print_logger
        # Connect signal and slot
        self.print_logger.update_signal.connect(self.append_text_to_plainTextEdit) # Connect to the appendPlainText method of your QPlainTextEdit

        self.ui.msg_button.clicked.connect(self.send_msg)

        print("Hello, world!")
    def startFunc(self):
        '''
            开启服务，启动服务
        '''
        port_text = self.ui.ws_port.text()
        if not self.is_valid_port(port_text):
            self.show_warning("端口错误", "请输入 1 到 65535之间的端口号")
            return 
        ws_path = self.ui.ws_path.text()
        if not ws_path  or not ws_path.startswith("/") :
            self.show_warning("路径错误", "请输入路径,格式 /xxxx")
            return
        ws_token = self.ui.ws_token.text()
        if ws_token:
            print(f"客户端连接ws的验证格式为: Authorization:Bearer {ws_token}", ws_token)

        print("启动端口:", port_text)
        if not hasattr(self, 'thread1'):
            self.thread1 = thread_wechat.myWechatThread(1, "wechat_hook_thread", int(port_text),ws_token,ws_path)
        self.thread1.start()


    def is_valid_port(self, port_text):
        try:
            port = int(port_text)
            return 1 <= port <= 65535
        except ValueError:
            return False

    def show_warning(self, title, message):
        QMessageBox.warning(self, title, message)
    def append_text_to_plainTextEdit(self, text):
        '''
            将text追加到QPlainTextEdit中
        '''
        self.ui.console_text.appendPlainText(text)  # 假设你的QPlainTextEdit的对象名是output_plainTextEdit
    def send_msg(self):
        '''
            发送消息
        '''
        wxid = self.ui.send_wxid.text().strip()
        if wxid == "":
            self.show_warning("错误", "请输入微信ID")
            return
        content = self.ui.send_msg_text.toPlainText().strip()
        if content == "":
            self.show_warning("错误", "请输入消息内容")
            return
        print(f"发送消息给{wxid}，内容：{content}")
        # 当需要传递数据并调用线程中的方法时
        thread_wechat.myWechatThread.send_test_msg(wxid,content)
if __name__ == "__main__":
    try:
        sub.init()
        app = QApplication([])
        app.lastWindowClosed.connect(lambda: print("Window closed!"))
        window = MyWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error: {e}")
