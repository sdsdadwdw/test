package objects
import (
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

func put(w http.ResponseWriter, r *http.Request){
	//put函数首先获取URL中<object_name>的部分，r.URL成员变量记录了HTTP请求的URL,用EscapedPath(),方法转义以后的部分路径
	//URL将以/区分 分为三部分
	f,e  :=os.Create(os.Getenv("STORAGE_ROOT") + "/objects/" + strings.Split(r.URL.EscapedPath(),"/")[2])
	if e !=nil{
		log.Println(e)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	defer f.Close()
	//将内容写如本地此盘文件f中
	io.Copy(f,r.Body)
}
