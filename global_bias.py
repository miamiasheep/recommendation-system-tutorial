import sys
import math

if len(sys.argv)!= (1+1):
	print('1: output file')
	exit(-1)
input = 'MovieLens.train'
test_file = 'MovieLens.test'
output = sys.argv[1]

### calculate global bias
### first element for total score, second element for the amount of ratings
bias = [0,0]   
with open(input,'r') as f:
	for line in f:
		words = line.split()
		rating = int(words[2])
		bias[0] += rating
		bias[1] += 1

### predicting
rmse = 0
g = open(output,'w')
with open(test_file,'r') as f:
	for line in f:
		words = line.split()
		pred = float(bias[0])/bias[1]
		g.write('%f\n' % pred)
g.close()	

### calculate training RMSE
ans = float(bias[0])/bias[1]
rmse = 0 
count = 0 
with open(input,'r') as f:
	for line in f:
		words = line.split()
		rating = int(words[2])
		rmse += pow(ans-rating,2)
		count += 1
### need to be modified in python3
print ('rmse: %f\n' % math.sqrt(rmse/count))
	

		
