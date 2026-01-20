# 2026-01-20  02:21:55
import re
def simple():
    result=re.match(".","m")
    print(result.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())

def more_alp():
    ret=re.match(r'[1,9]?\d',"09")
    print(ret.group())
    ret=re.match(r'[a-zA-Z_]{3,8}',"abcdefghijklm")
    print(ret.group())
def start_end():
    email_li=["1415058131@qq.com","xiaowang@163.com",".comxiaowang@11.com"]
    for email in email_li:
        ret=re.match(r'\w{4,20}@163.com$',email)
        if ret:
            print("{}的地址是正确的".format(ret.group()))
        else:
            print(f"{email}邮箱地址不正确")
    print("-"*50)
    ret=re.match(r'[1-9]?\d$',"40")
    if ret:
        print(ret.group())
    else:
        print("fail match")
def split_group():
    '''
    match group
    :return:
    '''
    ret = re.match(r'[1-9]?\d$|100', "100")
    if ret:
        print(ret.group())
    else:
        print("fail match")
    ret = re.match(r'[1-9][0-9]|[1-9]', "11")
    if ret:
        print(ret.group())
    else:
        print("fail match")
    print('-'*50)
    email_li = ["1415058131@qq.com", "xiaowang@163.com", ".comxiaowang@11.com"]
    for email in email_li:
        ret = re.match(r'\w{4,20}@(163|qq).com$', email)
        if ret:
            print(ret.group())
        else:
            print(f"{email}邮箱地址不正确")
def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches) # 跳过第一个匹配项
        second_match = next(matches) # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None

text = "abc123def456ghi789"
pattern = r"\d+"
second_match = find_second_match(pattern, text)
print(second_match)