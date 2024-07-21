# my_list=[1,-2,-13,41,28]
# my_list.append(9999)
# # my_list.insert(8000,999)
# # my_list.pop(2)
# new_list_2=[5,6,7,8]
# new_list=my_list+my_list_2
# print(len(my_list))
# cnt=my_list.count(2)
# print(cnt)
# agg func
# my_list.sort()
# print(*my_list)
 my_list=list(map(int,input().split(" ")))
# print(*my_list)
#  my_list=list(map(int,input().split(",")))
# cnt=(my_list.count(2))
# print(cnt)

# choice=int(input())

if(choice==1):
 my_list.append(999)
 print(*my_list)
elif(choice==2):
 my_list.pop(2)
 print(*my_list)
elif(choice==3):
 my_list.sort()
 print(*my_list)
else:
 print(f"good morning {len(my_list)}")








