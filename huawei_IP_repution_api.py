import requests
import json
from datetime import datetime
import time

# 请求的URL
base_url = "https://isecurity.huawei.com/public/ui/scp/v1/intelligence/ip-addresses"

# 请求的headers
headers = {
    "Host": "isecurity.huawei.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Accept": "application/json",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://isecurity.huawei.com/security/service/intelligence/search",
    "Content-Type": "application/json",
    "Csrf-Token": "c-gajxpi7uqp45ap49k908nvuncbenhh0404g9en1gjz457upg",
    "Redirect_code": "401",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=4",
    "Te": "trailers",
    "Connection": "keep-alive"
}

# 请求的cookies
cookies = {
    "HWWAFSESTIME": "17248317",
    "HWWAFSESID": "a28717320ca8",
    "ztsg_ruuid": "5a89e30d7cd7a351-a955-4fb4",
    "lang": "zh_CN",
    "idss_cid": "5945a3ee-61c0-4885-a6c2",
    "uid": "B6-DC-A5-C3-22-48-9F-4A-5C-1A",
    "hwssotinter3": "31062777257171",
    "authmethod": "77-22-F7",
    "hwssotinter": "4F-6D-57-E3-71",
    "hwsso_uniportal": "V003GAXbw4kPgq3atfo7ztDeSVoZ7W2pFBn1WGC_aQanfjislcw7mKZ0_aEkrZCyoXERrBRFnAdosdA_c_c",
    "suid": "B6-DC-A5-C3-22-48-9F-4A",
    "scpsession": "x-qrk5he89mrnybzvzpgjxburta"
}

ip_list = [
    "45.79.181.251",
    "92.255.85.253"  
]

# 遍历IP列表并发送请求
for ip in ip_list:
    full_url = f"{base_url}?ip={ip}"
  # 发送请求
    response = requests.get(full_url, headers=headers, cookies=cookies,timeout=10)

    # 打印响应内容
    if response.status_code == 200:
        # 解析JSON数据
        data = response.json()
        # 提取"result"参数
        result = data.get('result')
        # 如果"result"参数存在
        if result is not None:   
            print(f'IP: {ip}, Result: {result}')  
        else:
            print(f'IP: {ip}, Result: limited')
        
        # 检查'context'是否存在
        context = data.get('context')
        if context is not None:
            # 初始化变量来存储最新的lastSeen时间
            latest_last_seen = None
            
            # 遍历histThreats列表，提取最新的lastSeen时间
            for threat in data.get('context', {}).get('histThreats', []):
                last_seen_date = datetime.strptime(threat.get('lastSeen', ''), '%Y-%m-%d %H:%M:%S')
                if latest_last_seen is None or last_seen_date > latest_last_seen:
                    latest_last_seen = last_seen_date
            
            # 如果找到了最新的lastSeen时间，打印它
            print(f'Latest Last Seen: {latest_last_seen.strftime("%Y-%m-%d %H:%M:%S")}')

        else:
            print('No last seen dates found.')
    print(f"等待3小时后再次请求...")
    time.sleep(10800) 
