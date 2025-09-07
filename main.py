#   _____            _____            _     _                                _    _                       _                  _   
#  / ____|          |  __ \          | |   | |                              | |  | |                     | |                | |  
# | |       ______  | |__) |  _   _  | |_  | |__     ___    _ __    ______  | |  | |  ___    ___   _ __  | |_    ___   ___  | |_ 
# | |      |______| |  ___/  | | | | | __| | '_ \   / _ \  | '_ \  |______| | |  | | / __|  / _ \ | '__| | __|  / _ \ / __| | __|
# | |____           | |      | |_| | | |_  | | | | | (_) | | | | |          | |__| | \__ \ |  __/ | |    | |_  |  __/ \__ \ | |_ 
#  \_____|          |_|       \__, |  \__| |_| |_|  \___/  |_| |_|           \____/  |___/  \___| |_|     \__|  \___| |___/  \__|
#                             __/ |                                                                                             
#                            |___/                                                                                              

# auther:KIH0530
# github:https://github.com/KIH0530
# version:1.0




import time
import random

st = time.time()
et = None 
ts = None
sum = 0
times = 50

print("start calculate pi")

def calc_pi_car(n):
    num_points_circle = 0
    num_points_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            num_points_circle += 1
        num_points_total += 1
    return 4 * num_points_circle / num_points_total

def calc_pi_f(n):
    PI = 0
    for n in range(int(n)):
        PI += 1 / pow(16, n) * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
    return PI


for i in range(0,times):
    print(calc_pi_car(1000000 + (10000*i)))
    print(calc_pi_f(1000*i))
    print(pow(i*i,3))

et = time.time()
t = round(et-st,2)
print("finish! use time:",t,"second")
