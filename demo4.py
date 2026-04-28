import random
def game():
    while True:
        r=random.randint(0,100)
        #print(r)
        print("猜一个数字,0-100")
        i=10
        while i:
            try:
                s=int(input("输入一个数字: "))
                if s<0 or s>100:
                    print("重新输入")
                    continue
                if r>s:
                    i-=1
                    print(f"小了,还有{i}次机会")
                elif r<s:
                    i-=1
                    print(f"大了,还有{i}次机会")
                else:
                    print("答对了")
                    break
            except ValueError:
                print("非法输入")
        else:
            print(f"答题失败,正确答案是{r}")
        play=input("是否重新开始,请输入Y/N: ")
        if play.lower()=='n':
            print("游戏结束")
            break
if __name__=='__main__':
    game()
#随机数字游戏