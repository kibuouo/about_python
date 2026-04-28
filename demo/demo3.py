import random
def guess_number():
    while True:
        print("猜猜数字是多少？")
        print("提示：数字在1到100之间")
        number=random.randint(1,100)
        i=5
        while i:
            try:
                guess=int(input("请输入你的猜测："))
                if guess<1 or guess>100:
                    print("请输入1到100之间的数字")
                    continue
                if guess<number:
                    i-=1
                    print("太小了！还有",i,"次机会")
                elif guess>number:
                    i-=1
                    print("太大了！还有",i,"次机会")
                else:
                    print("恭喜你，猜对了！")
                    break
            except ValueError:
                print("请输入一个有效的数字！")
        else:
            print("很遗憾，你没有猜对。正确答案是：", number)
        play_again=input("你想再玩一次吗？(y/n): ")
        if play_again.lower()=='n':
            print("谢谢游戏！")
            break
if __name__=="__main__":
    guess_number()
    