package main


import "fmt"

/*
#接口=》父类实现=》多种子类实现=》多态
 .定义接口IPerson，定义吃喝睡三个抽象方法：
 .定义一个IPerson的实现类Worker劳动者，拥有劳动方法Work（）（output string）其中output是工作产出，休息方法Rest（）
 .继承Woker实现三个不同职业的子类：程序员Coder，老师Teacher，农民Farmer，并创建一个Woker集合；
 .从命令行循环寄售【今天星期几】的输入，如果是周一到周五全体工作，如果是周六周日程序员工作其他人休息；
*/
//.定义接口IPerson，定义吃喝睡三个抽象方法：
type IPerson interface{
	Eat()
	Drink()
	Sleep()
}

//继承Woker实现三个不同职业的子类：程序员Coder，老师Teacher，农民Farmer，并创建一个Woker集合；
type Person struct{
	name string
	sex int
}
//人的吃喝睡都是共性
func (p *Person) Eat(){
	fmt.Println("吃东西啦！！")
}
func (p *Person) Drink(){
	fmt.Println("喝水啦！！")
}
func (p *Person) Sleep(){
	fmt.Println("睡觉啦！！")
}

//定义一个IPerson的实现类Worker劳动者，拥有劳动方法Work（）（output string）其中output是工作产出，休息方法Rest
type IWorker interface{
	Work()(output string)
	Rest()

}
type Coder struct{
	Person
}
type Teacher struct{
	Person
}
type Famer struct{
	Person
}

//功能实例化
func (c *Coder)Work()(output string){
	fmt.Printf("%s正在辛勤的工作\n",c.name)
	return "今日码农的任务完成啦~"
}
func (t *Teacher)Work()(output string){
	fmt.Printf("%s正在辛勤的工作\n",t.name)
	return "今日的任务完成啦~"
}
func (f *Famer)Work()(output string){
	fmt.Printf("%s正在辛勤的工作\n",f.name)
	return "今日的任务完成啦~"
}


func (t *Teacher)Rest(){
	fmt.Println("今天周末好好睡一觉！")
}
func (f *Famer)Rest(){
	fmt.Println("今天周末好好睡一觉！")
}
func (c *Coder)Rest(){
	fmt.Println("今天周末好好加班！！")
}

func main(){

	Works :=make([]IWorker,0)
	coder :=Coder{Person{"张三",1}}
	teacher :=Teacher{Person{"李四",0}}
	famer := Famer{Person{"王五",1}}
	Works = append(Works,&coder)
	Works = append(Works,&teacher)
	Works = append(Works,&famer)

	fmt.Println("今天是工作日！")
	for _,w :=range Works{

			fmt.Println(w.Work())
	}
	fmt.Println("今天是休息日！")
	for _,r :=range Works{
//断言方法1
//		if c,ok :=r.(*Coder);ok{
//			c.Rest()
//		}else{
//			r.Rest()
//		}
		//断言方法2
		switch r.(type){
		case *Coder:
			r.Work()
		default:
			r.Rest()
		}

	}

}