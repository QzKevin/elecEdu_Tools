import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import requests
import webbrowser
import io
import json
import os

# 功能函数
# 请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

# 获取contentID
def getContentID(url):   
    for non_empty in url[url.find('?') + 1:].split('&'):
        if non_empty.split('=')[0] == 'contentId':
            contentId = non_empty.split('=')[1]
            break
    return contentId

# 解析链接
def origin01(contentID):
    url = f'https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/{contentID}.pkg/pdf.pdf'
    return url

def origin02(contentID):
    url = f'https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/{contentID}.pkg/pdf.pdf'
    return url

# 文件夹选择函数
def select_file():
    selected_file_path = filedialog.askdirectory()
    select_path.set(selected_file_path)

# 获取文件名
def getFilename(contentId):
    response = requests.get(f"https://s-file-1.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{contentId}.json")
    try:
        data = json.loads(response.text)
        return data["title"] # 返回教材标题
    except:
        return None

# 文件下载函数
def download_pdf(pdf_name,pdf_url):
    save_path = os.path.join(path_select.get(), f"{pdf_name}.pdf")
    response = requests.get(pdf_url, headers=headers)
    bytes_io = io.BytesIO(response.content)
    with open(save_path, mode='wb') as f:
        f.write(bytes_io.getvalue())
        text.insert("insert",f'{pdf_name}.pdf,下载成功！')

# 下拉菜单控件状态检测函数
def ensure(event):
    return(cbo.get())

# 解析函数
def analyze():
    url = url_get.get()
    contentID = getContentID(url)
    tab = origin01(contentID)
    cbo.bind("<<ComboboxSelected>>", ensure)
    if cbo.get() == "解析源1":
        tab = origin01(contentID)
    elif cbo.get() == "解析源2":
        tab =origin02(contentID)
    if chkValue.get() == True:
        webbrowser.open_new_tab(tab)
    return tab

def analyze_button():
    tab = analyze()
    text.insert("insert",tab + "\n")

# 下载函数
def main():
    url = url_get.get()
    contentID = getContentID(url)
    tab = analyze()
    download_pdf(getFilename(contentID), tab)

# GUI
#实例化创建应用程序窗口,大部分命令与tkinter相似
root = ttk.Window(
        title="国家中小学智慧教育平台下载器",        #设置窗口的标题
        themename="litera",                       #设置主题
        size=(540,320),                           #窗口的大小
        position=(100,100),                       #窗口所在的位置
        minsize=(0,0),                            #窗口的最小宽高
        maxsize=(1920,1080),                      #窗口的最大宽高
        resizable=None,                           #设置窗口是否可以更改大小
        alpha=1.0,                                #设置窗口的透明度(0.0完全透明）
        )
# 禁止调节窗口大小
root.resizable(False,False)
root.iconbitmap('logo.ico')

lb = ttk.Label(text="教材链接：",font=("宋体",15),bootstyle="primary")
lb.place(x=20,y=15)
lb2 = ttk.Label(text="解析源：",font=("宋体",15),bootstyle="primary")
lb2.place(x=20,y=205)
lb3 = ttk.Label(text="是否在浏览器打开文件",font=("宋体",15),bootstyle="primary")
lb3.place(x=270,y=205)

# 输入框
url_get = ttk.Entry(root,show=None,bootstyle ="primary",width= 55)
url_get.place(x=120,y=15)

# 输出用文本框
text = ttk.Text(root,width=69,height=5)
text.place(x=20,y=50)

# 文件夹路径选择控件
select_path = ttk.StringVar()
path_select = ttk.Entry(root, width=50,textvariable = select_path)
path_select.place(x=20,y=160)
b3 = ttk.Button(root,width=13, text="选择文件路径", command=select_file).place(x=400,y=160)

# 解析源选择
cbo = ttk.Combobox(
            master=root,
            bootstyle = PRIMARY,
            width= 12,
            height= 10,
            font = ("宋体",12),
            values=['解析源1', '解析源2'],
        )
cbo.place(x= 100,y=202)

# 按钮
b1 = ttk.Button(root, text="解析", width = 30,bootstyle=(PRIMARY, "outline-toolbutton"),command=analyze_button)
b1.place(x=20,y = 250)
b2 = ttk.Button(root, text="下载", width = 30,bootstyle=(PRIMARY, "outline-toolbutton"),command=main)
b2.place(x=280,y = 250)
chkValue = ttk.BooleanVar()
ck = ttk.Checkbutton(bootstyle="primary-round-toggle",variable = chkValue)
ck.place(x=490,y=210)

# 开始主循环
root.mainloop()