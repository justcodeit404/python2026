# 2026-01-18  12:32:39
import random
import time
import sys
# sys.getrecursionlimit(2000)
class Sort():
    def __init__(self,n):
        self.arr=[0]*n
        self.len=n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i]=random.randint(1,1000000)
    def partition(self,left,right):

        arr=self.arr
        k=i=left
        for i in range(left,right):
            if arr[i]<arr[right]:
                arr[i],arr[k]=arr[k],arr[i]
                k+=1
        arr[k],arr[right]=arr[right],arr[k]
        return k
    def quick_sort(self,left,right):
        if left<right:
            pivot=self.partition(left,right)
            self.quick_sort(left,pivot-1)
            self.quick_sort(pivot+1,right)
    def adjust_maxheap(self,pos,li_len):
        arr=self.arr
        dad=pos
        son=dad*2+1
        while son<li_len:
            if son+1<li_len and arr[son]<arr[son+1]:
                son=son+1
            if arr[son]>arr[dad]:
                arr[dad],arr[son]=arr[son],arr[dad]
                dad=son
                son=dad*2+1
            else:
                break


    def heap_sort(self,left,right):
        arr=self.arr
        for i in range(self.len//2-1,-1,-1):
            self.adjust_maxheap(i,self.len)
        arr[0],arr[-1]=arr[-1],arr[0]
        for arr_len in range(self.len-1,1,-1):
            self.adjust_maxheap(0,arr_len)
            arr[0],arr[arr_len-1]=arr[arr_len-1],arr[0]
    def test_time(self,sort_func,*args,**kwargs):
        start_time=time.time()
        sort_func(*args,**kwargs)
        end_time=time.time()
        print(f'用时{end_time-start_time}s')
if __name__ == '__main__':
    my_sort=Sort(10000)
    print(my_sort.arr)
    my_sort.test_time(my_sort.quick_sort,0,9999)
    print(my_sort.arr)
