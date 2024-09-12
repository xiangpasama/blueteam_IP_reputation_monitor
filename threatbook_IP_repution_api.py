import requests
import time

# 定义 API 的 URL
url = "https://api.threatbook.cn/v3/ip/query"

# 定义 API 密钥
apikey = "******"

# 定义需要监控的 IP 地址列表
ip_list = [
    "45.79.181.251",
    "92.255.85.253"  
]

# 遍历 IP 地址列表
for ip in ip_list:
    query = {
        "apikey": apikey,
        "resource": ip
    }

    # 发送 GET 请求
    response = requests.get(url, params=query)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析 JSON 数据
        data = response.json()

        # 获取 IP 地址的基本信息
        basic_info = data.get("data", {}).get(ip, {}).get("basic", {})

        # 获取地理位置信息
        carrier = basic_info.get("carrier", "N/A")
        location = basic_info.get("location", {})
        country = location.get("country", "N/A")
        province = location.get("province", "N/A")
        city = location.get("city", "N/A")

        # 打印 IP 地址的地理位置信息
        print(f"IP: {ip}, Carrier: {carrier}, Country: {country}, Province: {province}, City: {city}")

        # 初始化一个集合来存储结果，使用集合自动去重
        results = set()

        # 遍历 JSON 数据，提取所需的信息
        if 'intelligences' in data.get("data", {}).get(ip, {}):
            for intel_key, intel_value in data["data"][ip]['intelligences'].items():
                if isinstance(intel_value, list):
                    for item in intel_value:
                        if 'source' in item and 'intel_types' in item and 'update_time' in item:
                            # 将 intel_types 列表转换为元组
                            intel_types_tuple = tuple(item['intel_types'])
                            # 将每个 "source", "intel_types", "update_time" 作为一个元组添加到结果集合中
                            results.add((item['update_time'],item['source'], intel_types_tuple ))

        # 打印其他获取的信息
        for result in sorted(results):
            print(','.join(map(str, result)))
        print("\n")  # 在每个 IP 地址的结果之间添加空行
    else:
        print(f"Failed to fetch data for IP {ip}: {response.status_code}")
    
    # 暂停 10 秒
    time.sleep(10)