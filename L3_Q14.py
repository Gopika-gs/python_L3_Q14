f1 = open('D:/DORA/mashup/python/file1.txt','r')
f2 = open('D:/DORA/mashup/python/file2.txt','r')
c1 = f1.readlines()
c2 = f2.readlines()
for i,j in zip(c1,c2):
    print(i + j)
    
