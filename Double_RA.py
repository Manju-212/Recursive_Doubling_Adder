import math
from tabnanny import check
N = int(input("Enter the Number :"))
vfile = open("DRA_"+str(N)+".v", "w")
code = "module Recursive_Doubling_Adder(A,B,Cin,Sum,Cout);\n\n"
code = code + "input ["+str(N - 1)+":0] A,B;\noutput [" + \
    str(N)+":0] Sum;input [1:0] Cin;\noutput Cout;\n"
declaration = "\n"
kgp = []
for i in range(0, int(math.sqrt(N))*2 + 1):
    declaration = declaration + "wire [1:0] kgp_"+str(i)+" ["+str(N-1)+":0];\n"
    # kgp.append("kgp_"+str(i)+"")
declaration += "wire ["+str(N - 1)+":0] x_sum;\n\n\n"
declaration += "wire ["+str(N)+":0] carry;\n\n\nassign carry[0] = Cin[0];\n\n"
for j in range(0, N):
    declaration = declaration + \
        "assign kgp_0["+str(j)+"]={A["+str(j)+"],B["+str(j)+"]};\n"
declaration += "\n\n\n"
for j in range(0, N):
    declaration = declaration + \
        "assign x_sum["+str(j)+"]=A["+str(j)+"]^B["+str(j)+"];\n"
call = "\n"
f = 0
z = 0
value = int(math.log(N, 2))
print(value)
# call = call + "KGP k_" + \
#     str(f)+"(kgp_"+str(z)+"["+str()+"],kgp_" + \
#     str(z)+"["+str()+"],kgp_"+str(z + 1)+");\n"
for k in range(0, value + 1):
    inc = int(math.pow(2, k))
    print("increment = ", inc)
    print("stage k = ", k)
    for p in range(0, N + 1):
        if((p + inc) <= N):
            if(p == 0):
                call = call + "KGP k" + \
                    str(f)+"(kgp_"+str(k) + \
                    "["+str(inc - 1)+"],Cin,kgp_"+str(k + 1)+"["+str(inc - 1)+"]);\n"
            else:
                call = call + "KGP k"+str(f)+"(kgp_"+str(k)+"["+str(p + inc - 1)+"],kgp_"+str(
                    k)+"["+str(p - 1)+"],kgp_"+str(k + 1)+"["+str(p + inc - 1)+"]);\n"
    #         print(p," -> ",p + inc)
    #         if((p - 1)<=inc):
    #             call = call + "KGP k_"+str(f)+"(kgp_"+str(z)+"["+str()+"],2'b00,kgp_"+str(z + 1)+");\n"
    #         else:
            f = f + 1
        else:
            break
    call = call + "\n\n\n"
    # print("\n")
carry = "\n"
l = 1
check = 1
c = 0
for k in range(0,value):
    inc = int(math.pow(2, k))
    print("increment = ", inc)
    print("stage k = ", k)
    if(check != value):
        for h in range(c,int(math.pow(2,check)) - 1):   
            carry = carry + "assign carry["+str(l)+"] = kgp_"+str(check)+"["+str(l-1)+"][0];\n"
            l = l + 1
            print(l ," up")
    else:
        for e in range(check - 1,N):
            if(l<=N):
              carry = carry + "assign carry["+str(l)+"] = kgp_"+str(check)+"["+str(l-1)+"][0];\n"
              l = l + 1
              print(l ,"down")
            
    check = check + 1
sum = "\n"
carry += "assign Cout = carry["+str(N)+"];\n"
for d in range(0,N):
   sum += "assign Sum["+str(d)+"]= x_sum["+str(d)+"] ^carry"+"["+str(d)+"]"";\n"
sum += "assign Sum["+str(N)+"]= carry"+"["+str(N)+"]"";\n"
kgp ="\n\n"
kgp += "module KGP(A,B,kgp);\ninput [1:0]A,B;\ninout [1:0] kgp;\nassign kgp[1] = A[1]&A[0] | B[1]&A[0] | A[1]&B[1];\nassign kgp[0] = A[1]&A[0] | B[0]&A[0] | A[1]&B[0];\nendmodule"
vfile.write(code + declaration + call + carry + sum +  "\n\nendmodule" + kgp)
vfile.close()
