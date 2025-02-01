arquivo=open("números.txt","w") 
for linha in range(1,5+1): 
 arquivo.write("%d\n" % linha) 
arquivo.close()