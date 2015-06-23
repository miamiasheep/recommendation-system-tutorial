import sys
import math

if len(sys.argv)!= (1+1):
	print('1: output')
	exit(-1)
input = 'MovieLens.train'
test_file = 'MovieLens.test'
output = sys.argv[1]

### calculate user bias
bias = {}
with open(input,'r') as f:
	for line in f:
		words = line.split()
		item = int(words[1])
		rating = int(words[2])
		if item not in bias.keys():
			bias[item] = [rating,1]
		else:
			bias[item][0] += rating
			bias[item][1] += 1

### just for testing

g = open(output,'w')
with open(test_file,'r') as f:
	for line in f:
		words = line.split()
		item = int(words[1])
		if item in bias.keys():
			pred = float(bias[item][0])/bias[item][1]
		else: ### for cold start items
			pred = 2.5
		g.write('%f\n' % pred)
g.close()

### calculate training RMSE
rmse = 0
count = 0
with open(input,'r') as f:
	for line in f:
		words = line.split()
		item = int(words[1])
		rating = int(words[2])
		pred = float(bias[item][0])/bias[item][1]
		rmse += pow(rating-pred,2)
		count += 1
print ('rmse: %f\n' % math.sqrt(rmse/count))
		


		

		
