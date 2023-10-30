# l=list(map(int,input().split()))
# l.sort()
# r=""
# for i in range(len(l)):
#     r+=str(l[i])
# l.sort(reverse=True)
# k=""
# for i in range(len(l)):
#     k+=str(l[i])
# if(int(r)>int(k)):
#     print(int(r))
# else:
#     print(int(k))

nums=[7,10,9,8,100]
nums=sorted(map(str,nums))
num=sorted(map(str,nums),key=lambda x:x *10)
n=sorted(map(str,nums),key=lambda x:x *10,reverse=True)
print(nums)
print(num)
print(n)
print(str(int(''.join(n)))) 

