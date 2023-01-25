# countdown project 
import time

timer = input("Enter which time (hour minute seccond): ")
hour = int(timer.split(" ")[0])
minute = int(timer.split(" ")[1])
seccond = int(timer.split(" ")[2])
# print(time_total)
# print(f"{hour:02d}:{minute:02d}:{seccond:02d}")
if hour < 24 and minute < 60 and seccond < 60:
    time_total = (hour * 3600) + (minute * 60) + seccond
    while time_total != 0:
        H = time_total // 3600
        M = (time_total % 3600 ) //60
        S = time_total - ((H * 3600) + (M *60))
        print(f"{H:02d}:{M:02d}:{S:02d}" , end="\r")
        time.sleep(1)
        time_total = time_total -1

    print("time is end".title())

else:
    print("!!ERROR INPUT!!\nhour is limt 24\nminute is limt 60\nseccond is limt 60")
