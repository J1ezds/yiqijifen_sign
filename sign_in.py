import requests
import json

url = "https://api.m.points.yiqijifen.com/mall/miniapp/points_mission/signin"

headers = {
    "Host": "api.m.points.yiqijifen.com",
    "Connection": "keep-alive",
    "Content-Length": "2",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "X-PointsShop-Token": "请把抓到的Token填入这里",
    "content-type": "application/json",
    "Referer": "https://servicewechat.com/wxffbeadbd7aa1464d/61/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}

data = "{}"

requests.packages.urllib3.disable_warnings()

req = requests.post(url, json.dumps(data), headers = headers, verify = False)

print(req.text)