# item=[]
# op_list=[]
# limit=int(input())
# for i in range(limit):
#     name,*line=input().split()
#     print(name)
#     print(line)
#     nos=list(map(int,line))
#     print(nos)
#     l1=[name,nos]
#     item.append(l1)
#     print("item-", item)
#     print("item-0-",item[0][0])
#     if item[0][0]=="insert":
#         print("yes")
#         print(item[0][i])
#         op_list.insert(item[0][1][0],item[0][1][1])
#         print("oplist",op_list)

l1=[]
for i in range(int(input())):
    op=list(input().split())
    if op[0]=="insert":
        l1.insert(int(op[1]),int(op[2]))
    elif op[0]=="print":
        print(l1)
    elif op[0]=="remove":
        l1.remove(int(op[1]))
    elif op[0]=="append":
        l1.append(int(op[1]))
    elif op[0]=="sort":
        l1.sort()
    elif op[0]=="pop":
        l1.pop()
    elif op[0]=="reverse":
        l1.reverse()
    # print(l1)