import requests
import schedule
import logging
import datetime
import time

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def create_appointment():
    # 获取 enterDate 为明天日期
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y%m%d')

    # 请求 URL
    url = 'https://webapi.mybti.cn/Appointment/CreateAppointment'

    # 请求头
    headers = {
        'Host': 'webapi.mybti.cn',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': your_token_here,  # 替换为实际的 token
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://webui.mybti.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 19_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YiTongXing/6.2.4',
        'Referer': 'https://webui.mybti.cn/',
    }

    # 请求体
    data = {
        "lineName": "昌平线",
        "snapshotWeekOffset": 0,
        "stationName": "沙河站",
        "enterDate": tomorrow,
        "snapshotTimeSlot": "0630-0930",
        "timeSlot": "0830-0840"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"[{datetime.datetime.now()}] 状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] 请求失败: {e}")


# 每天中午 12:01 执行任务
schedule.every().day.at("12:01").do(create_appointment)

if __name__ == "__main__":
   logging.info("预约脚本已启动，等待定时执行...")
   while True:
        schedule.run_pending()
        time.sleep(1)
