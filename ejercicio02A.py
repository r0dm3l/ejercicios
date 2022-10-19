
A=int(input("ingrese la cantidad de numeros que deseé"))
list1=[]
list2=[]

for i in range(1,A+1):
    num=int(input(f"ingrese el numero {i} ="))
    
    list1.append(num)
    
print(list1)
#quitando repetidos de la lista1
d= set(list1)

#tranformando a lista y ordenado de menor a mayor
e=list(d)
e.sort()

#creando la lista 2
for i in e:
    
    n=list1.count(i)
    list2.append(n)

d= set(list1)
print(e)
print(list2)