n = open("mapper_output.txt","r")  # open file, read-only
s = open("sorted_mapper_output.txt","w") # open file, write
lines = n.readlines()
lines.sort()
for line in lines:
	s.write(line)
n.close()
s.close()