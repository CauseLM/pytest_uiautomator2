# _*_ coding：utf-8 _*_

# 正常登录测试数据
succeed_data = [
    {"name": "登录功能-登录成功", "username": "xxx123@163.com", "password": "xxx123", "agree": True, "success": True,
     "except": "登录成功"},
]

# 异常登录 - username
error_username_data = [
    {"name": "登录功能-账号异常-账号为空", "username": "", "password": "xxx123", "agree": True, "success": False,
     "except": "无法登录"},
    {"name": "登录功能-账号异常-账号不存在", "username": "xxx", "password": "xxx123", "agree": True, "success": False,
     "except": "账号不存在"},
    {"name": "登录功能-账号异常-账号格式错误", "username": "xxx123@qq@163.com", "password": "xxx123", "agree": True,
     "success": False, "except": "账号不存在"}
]

# 异常登录 - password
error_password_data = [
    {"name": "登录功能-密码异常-密码为空", "username": "xxx123@163.com", "password": "", "agree": True, "success": False,
     "except": "无法登录"},
    {"name": "登录功能-密码异常-密码错误", "username": "xxx123@163.com", "password": "xxx", "agree": True, "success": False,
     "except": "邮箱密码不匹配"},
    {"name": "登录功能-密码异常-密码50位", "username": "xxx123@163.com",
     "password": "xxx123xxx123xxx123xxx123xxx123xxx123xxx123xxx123xxx123xxx123", "agree": True, "success": False,
     "except": "邮箱密码不匹配"}
]

# 异常登录 - 未agree协议
error_not_agree_data = [
    {"name": "登录功能-协议异常-未同意协议", "username": "xxx123@163.com", "password": "xxx123", "agree": False, "success": False,
     "except": "请先勾选同意"}
]
