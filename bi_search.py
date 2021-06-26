def insertion_sort(list1):
   for index in range(1,len(list1)):

     curr_value = list1[index]
     position = index

     while position>0 and list1[position-1]>curr_value:
         list1[position]=list1[position-1]
         position = position-1

     list1[position]=curr_value

nlist = list(map(int,input().split()))
insertion_sort(nlist)
print(nlist)