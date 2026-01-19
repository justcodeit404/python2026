# 2026-01-18  14:08:01
my_list="this is a test string from xxx"
print(my_list)
def change_low(str_name:str):
    return str_name.lower()
my_list.sort(key=change_low)
print(my_list)