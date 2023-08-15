package main

import (
	"flag"
	"fmt"
	"github.com/gorilla/websocket"
	"log"
	"net/http"
	"net/url"
	"os"
	"os/signal"
	"time"
)

var addrs = flag.String("addr", "服务器地址:12725", "ws 服务器地址")
var wxid = flag.String("wxid", "需要发送的wxid", "测试发送给这个微信号ID")
var ws_auth = flag.String("ws_auth", "Bearer gui里面的token", "ws 服务器认证信息")
var ws_path = flag.String("ws_path", "/", "ws 服务器路径")

func main() {

	flag.Parse()
	log.SetFlags(0)

	interrupt := make(chan os.Signal, 1)
	signal.Notify(interrupt, os.Interrupt)

	u := url.URL{Scheme: "ws", Host: *addrs, Path: *ws_path}
	log.Printf("connecting to %s", u.String())
	c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{
		"Authorization": []string{fmt.Sprintf("Bearer %s", ws_auth)},
	})
	if err != nil {
		log.Fatal("dial:", err)
	}
	defer c.Close()

	log.Println("ws 连接成功")
	ticker := time.NewTicker(3 * time.Second)
	defer ticker.Stop()

	byPing := []byte(fmt.Sprintf(`{ "action": "SendText", "params": {"receiver": "%s", "msg": "66666666666"}}`, *wxid))

	timer := time.NewTimer(5 * time.Second)
	go readWeChat(c)
	for {
		select {
		case <-timer.C:
			// 认证登录
			err := c.WriteMessage(websocket.BinaryMessage, byPing)
			if err != nil {
				log.Println("write:", err)
				timer.Stop()
				return
			}
			log.Println("消息发送成功:", string(byPing))
			timer.Stop()

		case <-interrupt:
			log.Println("interrupt")
			err := c.WriteMessage(websocket.CloseMessage, websocket.FormatCloseMessage(websocket.CloseNormalClosure, ""))
			if err != nil {
				log.Println("write close:", err)
				return
			}
		}
	}

}

func readWeChat(c *websocket.Conn) {
	for {
		_, message, err := c.ReadMessage()
		if err != nil {
			log.Println("read:", err)
			return
		}
		log.Println("recv: ", string(message))

	}
}
