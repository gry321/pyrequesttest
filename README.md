### 作者：郭若垚，班级：二（2），住：南京市
进行爬虫
Requests_ddos 用进程生成小进程爬虫（比较消耗CPU）
Requests 用进程爬虫，还用了锁
dns_attack 查询DNS，危害力不大
Big_message 使用socket通信，用”.内容:*次数“可以重复字符串（比如fromfromfrom就是 .from:*3 ），用“*文件名:?路径”可以读取文件（比如本目录下的test.txt文件就是 *test.txt:?.）