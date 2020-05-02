#import true or false txt
trueOrFalseIndexList = [] #save the index of right results
trueOrFalseDirtyIndexList = []
trueOrFalseContext = open("bridgeOut.txt","r")
lines = list(trueOrFalseContext)
#print(lines)
count = 0
for tfResponse in lines:
    count += 1
    if(tfResponse == "Okay\n"):
       trueOrFalseIndexList.append(count)
    else:
        trueOrFalseDirtyIndexList.append(count)

#print(trueOrFalseIndexList)
#print(len(trueOrFalseIndexList))
trueOrFalseContext.close()


#import txt file
f = open("bridgein.txt","r")
lines = list(f)
unfilterContext = []
filterContext = []
txtCount = 0
#filter out through true or false table
for txtReponse in lines:
    txtCount += 1
    if(txtCount in trueOrFalseDirtyIndexList):
        unfilterContext.append(txtReponse)
    else:
        filterContext.append(txtReponse)

#print("Total has "+str(txtCount)+" lines")
#print("Only "+str(len(filterContext))+" lines are useful")
print(str(len(unfilterContext))+" lines are filter out through bridgeIn.txt")

f.close()

#filter
river = ["A", "M","O"]

location = []
for index1 in range(1,53):
    location.append(index1)

erected = ["CRAFTS","EMERGING","MATURE","MODERN"]

purpose = ["WALK", "AQUEDUCT", "RR", "HIGHWAY"]

length = ["SHORT","MEDIUM","LONG"]

lanes = ["1","2","4","6"]

clear_g = ["N","G"]

T_or_D = ["THROUGH","DECK"]

material = ["WOOD","IRON","STEEL"]

span = ["SHORT","MEDIUM","LONG"]

rel_l = ["S","S-F","F"]

type = ["WOOD\n","SUSPEN\n","SIMPLE-T\n","ARCH\n","CANTILEV\n","CONT-T\n"]

cleanText = [[]]

for line in filterContext:
    eachLine = line.split(",")
    if(eachLine[1] in river and eachLine[2] and eachLine[3] in erected and eachLine[4] in purpose
      and eachLine[5] in length and eachLine[6] in lanes and eachLine[7] in clear_g and eachLine[8] in T_or_D
      and eachLine[9] in material and eachLine[10] in span and eachLine[11] in rel_l and repr(eachLine[12] in type)):
        cleanText.append(eachLine)

cleanText.remove(cleanText[0])
#print(cleanText)

cleanString = []

for line in cleanText:
    string =",".join(line)
    cleanString.append(string)

print(str(len(cleanString))+" sets of data are useful")

with open("program1.txt","w") as f:
    for item in cleanString:
        f.write(item)

f.close()


