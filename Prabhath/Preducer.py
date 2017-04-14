sorted_input = open("sorted_mapper_output.txt","r")   
reducer_output = open("reducer_results.txt", "w")   

age_medication ={}


for line in sorted_input:  
#Total medication for each age:
 data = line.strip().split("\t") 
 if data[0] in age_medication:
  age_medication[data[0]] = age_medication[data[0]]+int(data[1])
 else:
  age_medication[data[0]] = int(data[1])
  
print '\n-------------------------\n'
print 'Total number for each medication type for each age:'
reducer_output.write("Total medication for each age:\n")
for k,v in age_medication.items():
	print '{0}\t{1}'.format(k,v)
	reducer_output.write("{0}\t\t{1}\n".format(k, v))
 

  
  
sorted_input.close()
reducer_output.close()

n = open("reducer_results.txt","r")  # open file, read-only
s = open("reducer_main_output.txt","w") # open file, write
lines = n.readlines()
lines.sort()
for line in lines:
	s.write(line)
n.close()
s.close()