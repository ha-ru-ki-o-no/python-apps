import random
import time

while True:
    n = random.randint(5,15)
    print("合図が出たらエンターを押してください！")
    print("反応速度が0、01秒未満で押されていた場合は不正とします")
    time.sleep(n)
    start_time = time.time()
    input("!!!!!")
    end_time = time.time()
    a = end_time - start_time
    if a < 0.01 :
        print("不正です😡")
    else:
        print(f"{a:.4f}","秒です！")
    print("もう一度しますか？:")
    b = input()
    if b == "no":
        break
