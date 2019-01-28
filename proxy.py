#coding:utf-8
import re # 內建庫
import time # 內建庫
import requests # 第三方庫

'''
作者:lucas(網路暱稱:pratnket)

requests 模擬合法請求
re 正則表達式 取出結果 存入 tuple(元祖)

備註:代碼簡單易懂，適合新手練習。

'''

#https://www.my-proxy.com/free-proxy-list-1.html
def get_request_ip_my_proxy(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
    html = requests.get(url,headers=headers)
    datas = re.findall( r'(\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})[:](\d{1,5})[#]', html.text)
    return datas

#https://free-proxy-list.net/
def get_request_ip_free_proxy_list(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
    html = requests.get(url,headers=headers,timeout=30)
    datas = re.findall( r'<td>(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})</td><td>(\d{1,5})</td>', html.text)
    return datas

if __name__ == '__main__':

    ips = []
    for page in range(1,10):
        #0
        if page == 1:
            url = "https://free-proxy-list.net/"
            ips.extend(get_request_ip_free_proxy_list(url))
        #10
        if page <= 10:
            url = "https://www.my-proxy.com/free-proxy-list-" + str(page) + ".html"
            ips.extend(get_request_ip_my_proxy(url))

    filename = str(time.strftime("%H-%M-%S", time.localtime()) ) # 時間轉換成檔案名稱
    Deputy_file_name = ".txt" # 附檔名

    star = [":","\n"] # 換行符號
    for ip in ips:
        string = ip[0] + star[0] + ip[1] + star[1] # ip陣列轉換成字串
        
        # 檔案寫入
        with open (filename + Deputy_file_name,"a") as f:
            f.write(string)

    # 檢視數量結果
    print("IP池數量總計:" + str(len(ips)))
