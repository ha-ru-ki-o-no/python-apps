import random


while True:
    n = random.randint(1,100)
    a = input("1~100までの数字を当ててください。")
    print(a)
    print("入力された文字：",a)
    m = "正解は"+ str(n) + "です"
    for i in range(4):
        if n == int(a) :
            print("正解です！")
            m = ""
            break
        else:
            print("不正解です。")
            if n-5 < int(a) < n+5:
                print("惜しい")
            elif n-5 > int(a):
                print(a,"より大きい")
            elif n+5 < int(a):
                print(a,"より小さい")
            a = input("もう一度挑戦しましょう！数字を入力してください")
            print("入力された文字：",a)
    print(m)
    print("もう一度しますか？:")
    b = input()
    if b == "no":
        break

    


