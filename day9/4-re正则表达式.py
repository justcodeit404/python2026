# 2026-01-20  02:21:55
import re
def simple():
    result=re.match(".","m")
    print(result.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())


simple()