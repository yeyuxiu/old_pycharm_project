# % [-] [0] [m] [.n] 格式化字符 % 参数
print("格式化内容是 %s" % "ssss")

# 占位宽度
tempate = "格式化内容是 |%20s|"
print(tempate % 'hello') # 格式化内容是 |               hello|
tempate = "格式化内容是 |%-20s|"
print(tempate % 'hello') # 格式化内容是 |hello               |
