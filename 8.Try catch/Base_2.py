#Base2
try:
    raise Exception (GG!!)
except ZeroDivisionError:
    print("除以零错误发生")
except ValueError:
    print("值错误发生")
except Exception as e:
    print(f"发生了异常：{e}")