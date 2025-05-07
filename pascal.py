def  pascal(numrows):
    triangle=[]
    for i  in range(numrows):
        row=[1]*(i+1)
        for j in  range(1,i):
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return  triangle

print(pascal(5))