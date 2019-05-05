GetSliceKey = "FortniteKey.text"

FortniteKey = open(GetSliceKey, "w")

inputString = raw_input("Enter your list of numbers. ")

sliceSize = int(raw_input("Enter your window. "))

slice = inputString

print(slice)

for i in range(len(inputString)-(sliceSize-1)):
	print(inputString[i:sliceSize+i])
	

