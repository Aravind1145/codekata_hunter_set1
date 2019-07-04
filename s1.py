num=int(input())
li=input().split(" ")
final_li=[]
for i in range(0,len(li)):
  for j in range(i+1,len(li)):
    if not(li[j] in final_li):
      if(li[i]==li[j]):
        final_li.append(li[j])
final_li=sorted(final_li)
if(len(final_li)==0):
  print("unique")
else:
  print(" ".join(final_li))
