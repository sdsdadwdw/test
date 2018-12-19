package main

import (
	"./objects"
	"log"
	"net/http"
	"os"
)

func main(){
	//注册HTTP处理函数Objects.Handler，如果有客户端访问本机HTTP且URL以/objects/开头则交给objects.Handler处理
	http.HandleFunc("/objects/",objects.Handler)
	//调用http.ListenAndServe函数监听端口，该端口由系统变量LISTEN_ADDRESS定义，非正常情况log.Fatal将返回错误并退出程序
	log.Fatal(http.ListenAndServe(os.Getenv("LISTEN_ADDRESS"),nil))
}