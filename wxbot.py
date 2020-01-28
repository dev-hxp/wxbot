from wxpy import *
import datetime
import time
import threading

bot = Bot(console_qr=True)

group_name = '高乐仕'
message = '早上好，各位同志，现在是早上9点30分！ by hxp-bot'

# @bot.register(group)
# def repeat_message(msg):
#     if not msg.member == bot.self :
#         msg.forward(group)

# 获取现在时间
now_time = datetime.datetime.now()
# 获取明天时间
next_time = now_time + datetime.timedelta(days=+1)
next_year = next_time.date().year
next_month = next_time.date().month
next_day = next_time.date().day
# 获取明天9点时间
next_time = datetime.datetime.strptime(str(next_year)+"-"+str(next_month)+"-"+str(next_day)+" 09:30:00", "%Y-%m-%d %H:%M:%S")
# # 获取昨天时间
# last_time = now_time + datetime.timedelta(days=-1)

# 获取距离明天3点时间，单位为秒
timer_start_time = (next_time - now_time).total_seconds()

def send_msg():
    target = bot.groups().search(group_name)[0]
    target.send(message)
    timer = threading.Timer(86400, send_msg)

#定时器,参数为(多少时间后执行，单位为秒，执行的方法)
timer = threading.Timer(timer_start_time, send_msg)
timer.start()
    
embed()

