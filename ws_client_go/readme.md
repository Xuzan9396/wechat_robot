案例
go run ws_client.go  -addr="xxx.xxx.xxx.xxx:port" -wxid="wxid_xxxxxxxx" -ws_auth="auth123" -ws_path="/"


GOOS=windows GOARCH=amd64 go build -x -v -ldflags "-s -w" -o ws_client.exe ws_client.go && upx ws_client.exe


GOOS=darwin GOARCH=amd64 go build -x -v -ldflags "-s -w" -o ws_client_darwin_amd64 ws_client.go && ws_client_darwin_amd64


GOOS=darwin GOARCH=arm64 go build -x -v -ldflags "-s -w" -o ws_client_darwin_arm64 ws_client.go && upx ws_client_darwin_arm64
