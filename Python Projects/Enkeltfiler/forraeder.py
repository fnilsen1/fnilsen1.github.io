#Gjør om til en ascii string + fjern mellomrom
s=[12, 8, 10, 5, 15, 3, 2, 1, 9, 11, 13, 7, 10, 4, 15, 9, 13, 1, 14, 11, 10, 2, 5, 6, 7, 4, 15, 9, 1, 6, 1, 14, 5, 3, 4, 2, 9, 7, 8, 11, 13, 6, 1, 14, 6, 11, 9, 15, 9, 14, 1, 9, 9, 
   4, 6, 11, 2, 13, 7, 15, 8, 3, 1, 12, 9, 
   4, 6, 11, 2, 13, 7, 15, 8, 3, 1, 12, 9, 
   8, 6, 10, 13, 10, 5, 15, 3, 2, 1, 9, 11, 13]   

#1-15:
#1 2 3 4 5 6 7 8 9  :  ;  <  =  >  ?
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#må ta -48

#<8:5?3219;=7:4?9=1>;:25674?9161>5342978;=61>6;9?9>19946;2=7?831<946;2=7?831<986:=:5?3219;=



#'46;2=7?831<9'
#4, 6, 11, 2, 13, 7, 15, 8, 3, 1, 12, 9

#:5?3219;=
#10, 5, 15, 3, 2, 1, 9, 11, 13,

#Ikke verdt det
#4, 15, 9
#6, 1, 14

#[12, 8,      7, 10,      13, 1, 14, 11, 10, 2, 5, 6, 7,        1,        5, 3, 4, 2, 9, 7, 8, 11, 13,      6, 11, 9, 15, 9, 14, 1, 9, 9,            8, 6, 10, 13,       ]


#Variabler på en linje
#Kanskje z=ord()
#13

a,b=[],[]
s='<8:5?3219;=7:4?9=1>;:25674?961>5342978;=61>6;9?9>199'+'46;2=7?831<9'*2+'8'
for k in s:
	y=ord(k)-48
	if y in a:
		if len(a)>10:b+=[a]
		a=a[a.index(y)+1:]
	a+=[y]
for e in sorted(b):print(e)

