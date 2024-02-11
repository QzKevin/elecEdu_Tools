# 国家中小学智慧教育平台下载器

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![version](https://img.shields.io/badge/Version-2.0-purple.svg)

本工具用于快速解析下载**国家中小学智慧教育平台**中电子课本PDF文件

> 本工具使用python3.x开发，项目开源页面release处有已导出的exe可执行文件，可直接下载使用，非windows用户请下载源代码到本地，安装python运行环境并配置运行所需要的库即可使用

## 安装程序

### 本地Python安装依赖库
```
pip install -r requirements.txt
```

### 下载可执行程序包
- 方法一：进入本项目的[Releases](https://github.com/QzKevin/elecEdu_Tools/releases)页面下载对应平台的可执行文件（更新可能不及时）
- 方法二：进入本项目的[Actions](https://github.com/QzKevin/elecEdu_Tools/actions)页面选择对应平台的构建在Artifacts栏目下找到以elecEdu命名的文件下载即可

> Windows平台为单文件可执行程序，下载即可使用，Mac和Linux平台为zip压缩包,通过各自平台安装第三方软件的方法安装即可使用

## 使用方法

1. 将电子课本的页面网址粘贴到程序窗口的输入框中
2. 点击“**解析**”按钮，工具会解析有效的电子课本PDF网址输出到输出框，可自行复制浏览器访问
3. 点击“**下载**”按钮，选择好下载目录和文件名，本工具会将电子课本PDF文件下载到您指定的位置
4. 本工具有两个解析源（解析源一般比较稳定，如有问题可提交issue，会在下个版本进行优化），请视情况选择使用
5. 可选择浏览器打开文件选项，这样以后无论**解析**还是**下载**都会自动跳转到浏览器页面
6. v2.0新增右键菜单和快捷键适配优化，随时随地便捷下载电子课本
