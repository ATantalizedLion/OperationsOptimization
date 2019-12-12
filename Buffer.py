

#test 1 
obj1List1 =  [1489100.0, 1489100.0, 1638660.0, 1690960.0] 
obj2List1 =  [-4.0, -4.0, -4.0, -4.0] 
obj3List1 =  [1377700.0, 1377700.0, 1370300.0, 1578700.0] 
obj4List1 =  [4244500.0, 4244500.0, 4379260.0, 4848360.0]
#test 2
obj1List2 =  [1833820.0, 1738480.0, 1964820.0] 
obj2List2 =  [-9.0, -8.0, -8.0] 
obj3List2 =  [1839000.0, 1888000.0, 1839000.0] 
obj4List2 =  [5511820.0, 5514480.0, 5642820.0]
#test 3
obj1List3 =  [1018460.0, 1097980.0, 1124500.0] 
obj2List3 =  [-1.0, -1.0, -1.0] 
obj3List3 =  [1538400.0, 1538400.0, 1538400.0] 
obj4List3 =  [4095260.0, 4174780.0, 4201300.0]
#test 4
obj1List4 =  [1354840.0, 1398940.0, 1488120.0, 1478720.0] 
obj2List4 =  [-7.0, -6.0, -6.0, -6.0] 
obj3List4 =  [1553500.0, 1548000.0, 1709000.0, 1987000.0] 
obj4List4 =  [4461840.0, 4494940.0, 4906120.0, 5452720.0]
#test 5
obj1List5 =  [1834580.0, 1736500.0, 1973680.0, 2015680.0, 2365800.0] 
obj2List5 =  [-6.0, -5.0, -5.0, -5.0, -5.0] 
obj3List5 =  [1979100.0, 1979100.0, 1968200.0, 1968200.0, 1968200.0] 
obj4List5 =  [5792780.0, 5694700.0, 5910080.0, 5952080.0, 6302200.0]

#Data is old and bad (extra weight mult), fix:
for i in range(len(obj3List1)):
    obj3List1[i] = obj3List1[i]/2
    obj4List1[i] = 2*obj3List1[i]+obj1List1[i]

for i in range(len(obj3List2)):
    obj3List2[i] = obj3List2[i]/2
    obj4List2[i] = 2*obj3List2[i]+obj1List2[i]

for i in range(len(obj3List3)):
    obj3List3[i] = obj3List3[i]/2
    obj4List3[i] = 2*obj3List3[i]+obj1List3[i]

for i in range(len(obj3List4)):
    obj3List4[i] = obj3List4[i]/2
    obj4List4[i] = 2*obj3List4[i]+obj1List4[i]

for i in range(len(obj3List5)):
    obj3List5[i] = obj3List5[i]/2
    obj4List5[i] = 2*obj3List5[i]+obj1List5[i]
    

