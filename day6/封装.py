# 2026-01-11  18:16:41
class House:
    def __init__(self,house_type,area):
        '''
        房子初始化
        :param house_type:
        :param area:
        '''
        self.house_type = house_type
        self.area = area
        self.free_area=area
        self.items_list=[]


