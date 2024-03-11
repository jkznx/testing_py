def funnyString(s):
    r = s[::-1]
    ar1=[]
    ar2=[]
    for i in range(1,len(r)):
        ar1.append(abs(ord(r[i])-ord(r[i-1])))
        ar2.append(abs(ord(s[i])-ord(s[i-1])))        
    if ar1==ar2:
        return "Funny"    
    return "Not Funny"
