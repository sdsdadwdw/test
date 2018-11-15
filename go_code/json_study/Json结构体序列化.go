package main

import (
	"encoding/json"
	"fmt"
)

type Person struct{
	Name string
	Age int
	Sex bool
	Hobbies []string
}

var (
	ym,chh Person
	ps []Person
	mMap,yMap map[string]interface{}
	mSlice []map[string]interface{}
)

//初始化
func init(){
	//初始化结构体数据
	ym=Person{"杨茂",20,true,[]string{"学习","IG牛逼","女"}}
	chh=Person{"chh",18,false,[]string{"学习","RNG牛逼","男"}}
	ps = make([]Person,0)
	ps = append(ps,ym,chh)

	//初始化map数据
	mMap = make(map[string]interface{})
	mMap["name"] ="张三"
	mMap["sex"]=true
	mMap["age"]=22
	mMap["hobbies"]=[]string{"学习","RNG牛逼","男"}
	yMap = make(map[string]interface{})
	yMap["name"] ="李四"
	yMap["sex"]=false
	yMap["age"]=25
	yMap["hobbies"]=[]string{"eat","喝","嫖赌"}

	//初始化切片
	mSlice = make([]map[string]interface{},0)
	mSlice = append(mSlice,mMap,yMap)

}

//序列化切片
func main13(){
	bytes, erro := json.Marshal(mSlice)
	if erro !=nil{
		fmt.Println("序列化失败，erro=",erro)
	}else{
		mSliceStr := string(bytes)
		fmt.Println("序列化成功结果是：",mSliceStr)
	}

}

//序列化map
func main12(){
	bytes, erro := json.Marshal(mMap)
	if erro !=nil{
		fmt.Println("序列化失败，erro=",erro)
	}else{
		mapStr := string(bytes)
		fmt.Println("序列化成功结果是：",mapStr)
	}
}

//Json结构体 序列化
func main11(){
	bytes, erro := json.Marshal(ps)
	if erro !=nil{
		fmt.Println("序列化失败，erro=",erro)
	}else{
		jsonStr := string(bytes)
		fmt.Println("序列化成功，结果为:",jsonStr)
	}
}

func main(){
	main13()
}