lista = [1, 12, 11, 5, 7, 24, 8]
listy = lista.copy() 
print(listy)
x = 0
result = []
j = 0
while(j < 7):
    
    for i in listy:
        
        if (x<=i):
            
            x = i
            print(x)
            
    result.insert(0, x)
            
    j = j+1
    listy.remove(x)
    x = 0
    
print(result)
