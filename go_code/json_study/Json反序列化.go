package main

import (
	"encoding/json"
	"fmt"
)

type Human struct{
	Name string
	Age int
	Sex bool
	Hobbies []string
}

var jsonStr string
var zq Human
var mmap map[string]interface{}
var

func init(){

		//jsonStr :="[{\"age\":22,\"hobbies\":[\"学习\",\"RNG牛逼\",\"男\"],\"name\":\"张三\",\"sex\":true},{\"age\":25,\"hobbies\":[\"eat\",\"喝\",\"嫖赌\"],\"name\":\"李四\",\"sex\":false}]"
	jsonStr ="{\"age\":22,\"hobbies\":[\"学习\",\"RNG牛逼\",\"男\"],\"name\":\"张三\",\"sex\":true}"
}

//结构体反序列化
func main21(){
	erro := json.Unmarshal([]byte(jsonStr), &zq)
	if erro !=nil{
		fmt.Println("反序列化失败,erro=",erro)

	}else{
		fmt.Printf("反序列化成功:%#v\n",zq)
	}
}

//切片反序列化
func main22(){
	erro := json.Unmarshal([]byte(jsonStr), &mmap)
	if erro !=nil{
		fmt.Println("反序列化失败,erro=",erro)

	}else{
		fmt.Printf("反序列化成功:%#v\n",mmap)
	}
}

func main(){
	main22()
}