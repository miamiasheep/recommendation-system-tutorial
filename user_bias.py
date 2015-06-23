import sys
import math

if len(sys.argv)!= (1+1):
	print('1: output file')
	exit(-1)
input = 'MovieLens.train'
test_file = 'MovieLens.test'
output = sys.argv[1]

### calculate user bias
bias = {}
with open(input,'r') as f:
	for line in f:
		words = line.split()
		user = int(words[0])
		rating = int(words[2])
		'''
		calculate the bias while reading the file one by one!
		You should let the bias be the dictionary mapping user into 
		a list structure that the first element is the total rating
		and the second element is the number of ratings of the user
		
		Guide:
		If the user is not in the key of the bias
		(can be determined by [if user not in bias.keys()] clause)
		You should initialize a list corresponding the user.
		ex: bias[user] = [rating,1]
		If the user is already in the key
		You can just add the value of the total ratings and total number of ratings
		'''
### predicting
count = 0
rmse = 0
g = open(output,'w')
with open(test_file,'r') as f:
	for line in f:
		words = line.split()
		user = int(words[0])
		pred = float(bias[user][0])/bias[user][1]
		g.write('%f\n' % pred)
g.close()		

### calculate training RMSE
rmse = 0
count = 0
with open(input,'r') as f:
	for line in f:
		words = line.split()
		user = int(words[0])
		rating = int(words[2])
		pred = float(bias[user][0])/bias[user][1]
		rmse += pow(rating-pred,2)
		count += 1
print ('rmse: %f\n' % math.sqrt(rmse/count))

