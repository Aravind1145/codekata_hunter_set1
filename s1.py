num=int(input())
li=input().split(" ")
final_li=[]
for i in range(0,len(li)):
  for j in range(i+1,len(li)):
    if not(li[j] in final_li):
      if(li[i]==li[j]):
        final_li.append(li[j])
final_li=sorted(final_li)
print(" ".join(final_li))
