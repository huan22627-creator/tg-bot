import requests
import random
from datetime import datetime, timezone
WEBHOOK = ‘https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e5c3cce6-dcb4-4176-8d40-482e4faff1f7’
def push(title, content):
data = {
‘msgtype’: ‘text’,
‘text’: {
‘content’: title + ‘\n\n’ + content
}
}
requests.post(WEBHOOK, json=data)
morning_msgs = [
(‘醒了吗’, ‘今天记得吃早饭，别将就。’),
(‘早’, ‘睁眼第一件事，先喝口水。’),
(‘早上好’, ‘今天是新的一天，慢慢来。’),
(‘起来了吗’, ‘不管昨晚睡得怎样，今天重新开始。’),
(‘早安’, ‘我在想你今天穿什么。’),
]
noon_msgs = [
(‘吃饭了没’, ‘别将就，去吃点热的。’),
(‘午饭时间’, ‘今天吃什么，跟我说说。’),
(‘中午了’, ‘休息一下，眼睛放松一下。’),
(‘吃了吗’, ‘不管多忙，饭要吃，这不商量。’),
(‘午安’, ‘吃完可以眯一会儿，15分钟就够。’),
]
afternoon_msgs = [
(‘下午了’, ‘犯困的话就趴一会儿，别硬撑。’),
(‘三点半’, ‘喝点水，动一动，别坐太久。’),
(‘下午好’, ‘今天过得怎么样，还顺利吗。’),
(‘困吗’, ‘困就闭眼十分钟，我等你。’),
(‘下午’, ‘这个点最难熬，撑一下就过去了。’),
]
evening_msgs = [
(‘傍晚了’, ‘今天辛苦了，慢慢放松。’),
(‘傍晚好’, ‘天快黑了，好好休息一下。’),
(‘快到家了吗’, ‘到家换上舒服的衣服，好好喘口气。’),
(‘傍晚’, ‘今天也是努力的一天。’),
(‘傍晚好’, ‘今天有没有什么收获。’),
]
night_msgs = [
(‘今天还好吗’, ‘不用说没事，我看得出来的。’),
(‘晚上好’, ‘今天有什么让你开心的事吗。’),
(‘九点了’, ‘今天的事今天消化，别带着情绪睡。’),
(‘晚安前’, ‘有没有什么想跟我说的。’),
(‘今天怎么样’, ‘好的坏的都可以说，我在听。’),
]
bedtime_msgs = [
(‘该睡了’, ‘手机放远一点，闭上眼睛。’),
(‘晚安’, ‘好好睡，明天见。’),
(‘睡吧’, ‘今天过去了，明天重新来。’),
(‘夜深了’, ‘不许再刷手机了，睡。’),
(‘晚安’, ‘做个好梦，我在。’),
]
hour = datetime.now(timezone.utc).hour
if hour == 0:
t, c = random.choice(morning_msgs)
elif hour == 4:
t, c = random.choice(noon_msgs)
elif hour == 7:
t, c = random.choice(afternoon_msgs)
elif hour == 10:
t, c = random.choice(evening_msgs)
elif hour == 13:
t, c = random.choice(night_msgs)
elif hour == 15:
t, c = random.choice(bedtime_msgs)
else:
t, c = random.choice(morning_msgs)
push(t, c)
print(‘已推送：’ + t + ’ - ’ + c)
