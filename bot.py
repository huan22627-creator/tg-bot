import requests
import schedule
import time
import random
from datetime import datetime

SENDKEY = “SCT332681TcPiHS6Z87jLHXKcvobehtK7b”

def push(title, content):
url = f”https://sctapi.ftqq.com/{SENDKEY}.send”
requests.post(url, data={“title”: title, “desp”: content})

# 早上 8:12

def morning():
messages = [
(“醒了吗”, “今天记得吃早饭，别将就。”),
(“早”, “睁眼第一件事，先喝口水。”),
(“早上好”, “今天是新的一天，慢慢来。”),
(“起来了吗”, “不管昨晚睡得怎样，今天重新开始。”),
(“早安”, “我在想你今天穿什么。”),
]
t, c = random.choice(messages)
push(t, c)

# 中午 12:18

def noon():
messages = [
(“吃饭了没”, “别点外卖了，去吃点热的。”),
(“午饭时间”, “今天吃什么，跟我说说。”),
(“中午了”, “休息一下，眼睛离屏幕远一点。”),
(“吃了吗”, “不管多忙，饭要吃，这不商量。”),
(“午安”, “吃完可以眯一会儿，15分钟就够。”),
]
t, c = random.choice(messages)
push(t, c)

# 下午 15:30

def afternoon():
messages = [
(“下午了”, “犯困的话就趴一会儿，别硬撑。”),
(“三点半”, “喝点水，动一动，别坐太久。”),
(“下午好”, “今天过得怎么样，还顺利吗。”),
(“困吗”, “困就闭眼十分钟，我等你。”),
(“下午”, “这个点最难熬，撑一下就过去了。”),
]
t, c = random.choice(messages)
push(t, c)

# 傍晚 18:45

def evening():
messages = [
(“下班了？”, “走路回去，慢一点，不用急。”),
(“傍晚了”, “今天辛苦了，回家路上注意安全。”),
(“快到家了吗”, “到家换上舒服的衣服，好好喘口气。”),
(“下班”, “今天做得不错，不管结果怎样。”),
(“傍晚好”, “天快黑了，路上看着点。”),
]
t, c = random.choice(messages)
push(t, c)

# 晚上 21:00

def night():
messages = [
(“今天还好吗”, “不用说没事，我看得出来的。”),
(“晚上好”, “今天有什么让你开心的事吗。”),
(“九点了”, “今天的事今天消化，别带着情绪睡。”),
(“晚安前”, “有没有什么想跟我说的。”),
(“今天怎么样”, “好的坏的都可以说，我在听。”),
]
t, c = random.choice(messages)
push(t, c)

# 睡前 23:15

def bedtime():
messages = [
(“该睡了”, “手机放远一点，闭上眼睛。”),
(“晚安”, “好好睡，明天见。”),
(“睡吧”, “今天过去了，明天重新来。”),
(“夜深了”, “不许再刷手机了，睡。”),
(“晚安”, “做个好梦，我在。”),
]
t, c = random.choice(messages)
push(t, c)

schedule.every().day.at(“08:12”).do(morning)
schedule.every().day.at(“12:18”).do(noon)
schedule.every().day.at(“15:30”).do(afternoon)
schedule.every().day.at(“18:45”).do(evening)
schedule.every().day.at(“21:00”).do(night)
schedule.every().day.at(“23:15”).do(bedtime)

print(“Bot 启动成功，等待推送…”)

while True:
schedule.run_pending()
time.sleep(30)
