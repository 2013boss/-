from easygui import *

from webbrowser import *

while tuple:

    webmode = ["搜索", "网页链接"]

    mode = choicebox("请选择一个模式：", title="the web网页游览器", choices=webmode)

    if mode == "搜索":
        searchtype = enterbox("请输入要搜索的内容：", title="the web网页游览器")

        open_new_tab("https://www.baidu.com/s?wd=" + searchtype)
    elif mode == "网页链接":
        searchtype = enterbox("请输入要打开的网页链接：", title="the web网页游览器")

        open_new_tab(searchtype)
    else:
        break
