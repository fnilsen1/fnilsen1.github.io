a,b="mantysonstorfrelorson","janfebmaraprmaijunjulaugsepoktnovdes"
c,d=[32,30,32,31,32,31,32,32,31,32,31,32],0
for k in range(12):
 e=b[3*k%36:3*k%36+3]
 for i in range(1,c[k]):
  print(a[3*(d)%21:3*(d)%21+3],i,e)
  d+=1



