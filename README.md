# 国家中小学智慧教育平台下载器

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![version](https://img.shields.io/badge/Version-2.0-purple.svg)

本工具用于快速解析下载**国家中小学智慧教育平台**中电子课本PDF文件

> 本工具使用python3.x开发，项目开源页面release处有已导出的exe可执行文件，可直接下载使用，非windows用户请下载源代码到本地，安装python运行环境并配置运行所需要的库即可使用

## 项目需要的运行库
windows用户安装python环境后终端执行：
```
pip install ttkbootstrap
pip install requests
pip install webbrowser
pip install json
pip install io
pip install os
```
> macOS用户请百度运行库安装方法，上面的是windows用户安装方法


## 使用方法

1. 将电子课本的页面网址粘贴到程序窗口的输入框中
2. 点击“**解析**”按钮，工具会解析有效的电子课本 DF网址输出到输出框，可自行复制浏览器访问
3. 点击“**下载**”按钮，选择好下载目录和文件名，本工具会将电子课本PDF文件下载到您指定的位置
4. 本工具有两个解析源（解析源一般比较稳定，有问题可提交issue，会在下个版本进行优化），请视情况选择使用
5. 可选择浏览器打开文件选项，这样以后无论**解析**还是**下载**都会自动跳转到浏览器页面
6. v2.0新增右键菜单和快捷键适配优化，随时随地便捷下载电子课本
