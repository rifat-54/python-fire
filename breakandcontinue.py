# n=0
# while(n<6):
#     n+=1
#     if n==4:
#         # break
#         continue
#     print(n)

n=1
while(n<4):
    a=1
    while a<3:
        print(n,a)
        a+=1
    print("inner loop terminate")
    n+=1
    print("OUter loop exclude")

print("Outer loop terminate")