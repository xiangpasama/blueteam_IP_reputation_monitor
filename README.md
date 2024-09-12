# blueteam_IP_reputation_monitor
用于监控企业互联网出口IP/映射IP/云服务器IP，是否已经被威胁情报平台标记为恶意或者可疑，由此判断内网或云资源是否失陷，目前包含微步在线威胁情报和华为云威胁情报的IP信誉检查。

纯python 3.11下编写

## 微步在线的情报API

可以用企业邮箱注册账号，找微步在线销售开通总量1000个的IP分析API，控制台绑定公司出口IP【绑定IP才能使用key】，每月监测一次，一次50个IP，可以用20个月，发现被标记之后自行排查是否有服务器中毒，并向微步在线申请IP加白。

python threatbook_IP_repution_api.py

apikey和ip_list都需要自行填写，apikey = ""，ip_list = [ ]

每请求一个IP，一定要暂停10秒，不然输出的结果会存在一些混乱或者错误的信息。

输出的结果包含ip，ip地理位置，ip威胁情报最后一次更新的时间【按时间排序】，威胁情报来源，威胁情报标签，总体比较直观
```
IP: 45.79.181.251, Carrier: Akamai Technologies, Inc., Country: United States, Province: New Jersey, City: Cedar Knolls
2018-08-02 21:00:33,ThreatBook Labs,('IDC',)
2022-05-11 20:10:23,ThreatBook Labs,('IDC',)
2022-11-09 15:13:00,ThreatBook Labs,('Scanner',)
2022-11-24 09:11:05,ThreatBook Labs,('Scanner',)
2023-01-21 11:58:47,Open Source ,('Suspicious',)
2023-01-21 12:15:18,Open Source ,('Suspicious',)
2023-06-21 03:23:13,ThreatBook Labs,('Scanner',)
2023-07-05 12:58:04,ThreatBook Labs,('Zombie',)
2023-08-25 05:16:55,Open Source ,('Malware',)
2023-08-29 09:55:17,Open Source ,('Suspicious',)
2024-06-06 10:30:03,Open Source ,('Malware',)
2024-06-29 02:13:53,Open Source ,('Spam',)
2024-07-01 06:26:35,Open Source ,('Scanner',)
2024-08-27 12:09:18,ThreatBook Labs,('Brute Force',)
2024-08-31 18:11:05,ThreatBook Labs,('Spam', 'Zombie')
2024-09-10 04:06:07,Open Source ,('Suspicious',)
2024-09-11 01:53:22,Open Source ,('Suspicious',)
2024-09-11 02:01:54,Open Source ,('Suspicious',)
2024-09-11 15:04:03,Open Source ,('Malware',)
2024-09-12 01:10:48,binarydefense.com,('Malware',)
2024-09-12 01:10:59,Open Source ,('Scanner',)
2024-09-12 01:11:57,blocklist.de,('Scanner',)
2024-09-12 01:47:29,Open Source ,('Suspicious',)
2024-09-12 01:51:33,Open Source ,('Suspicious',)
2024-09-12 09:00:13,ThreatBook Labs,('Spam',)

IP: 92.255.85.253, Carrier: Chang Way Technologies Co. Limited, Country: Russia, Province: Moscow, City: Moscow
2023-02-27 12:14:00,ThreatBook Labs,('Dynamic IP',)
2024-01-18 06:38:56,ThreatBook Labs,('Spam',)
2024-09-10 03:25:00,Open Source ,('Scanner',)
2024-09-10 04:11:22,Open Source ,('Suspicious',)
2024-09-11 01:53:25,Open Source ,('Suspicious',)
2024-09-11 02:04:37,Open Source ,('Suspicious',)
2024-09-11 02:04:41,Open Source ,('Suspicious',)
2024-09-11 15:04:18,Open Source ,('Malware',)
2024-09-12 01:08:57,Open Source ,('Scanner', 'Zombie')
2024-09-12 01:10:49,binarydefense.com,('Malware',)
2024-09-12 01:11:48,blocklist.de,('Scanner',)
2024-09-12 01:47:17,Open Source ,('Suspicious',)
2024-09-12 01:50:47,Open Source ,('Suspicious',)
```
## 华为云的情报API



