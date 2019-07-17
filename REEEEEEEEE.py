import time
def con_to_ascii():
    line=[""]
    fileob=open("logorle.txt","r")
    File_RLE=fileob.readlines()
    fileob.close()
    for i in File_RLE:
        
        substang=([i[y:y+3] for y in range(0, len(i), 3)])
        k=len(substang)
        k1=0
        while k-1 != k1:
            a=substang[k1]
            multi=((int(a[0])*10)+(int(a[1])))
            b=0
            while multi != b:
                line.append(a[2])
                b=b+1
            k1=k1+1
    print("".join(line))
          
        
            
con_to_ascii()
time.sleep(100)
