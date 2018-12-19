package objects

import "net/http"

func Handler(w http.ResponseWriter, r *http.Request){
	//出现请求先判断客户端的方法是put or get在进行相应的处理并返回
	m :=r.Method
	if m ==http.MethodPut{
		put(w,r)
		return
	}
	if m == http.MethodGet{
		get(w,r)
		return
	}
	//当不是上诉两种方式将返回405MethodNotAllowed错误
	w.WriteHeader(http.StatusMethodNotAllowed)
}