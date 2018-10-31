import pandas;
import random;
import numpy;
import sys;

number_of_nodes=int(sys.argv[1]);
target_file_name=sys.argv[2];


output = numpy.zeros((number_of_nodes,number_of_nodes),dtype=numpy.int); 


for i in range(number_of_nodes):
	for j in range(number_of_nodes):
		if(random.randint(0,10)>5):
			output[i][j]=1;
			output[j][i]=1;

# print output;

numpy.savetxt(target_file_name,output,delimiter=",",fmt=('%2u'))	


