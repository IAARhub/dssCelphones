from __future__ import division
import random
import math
import time as tm
import numpy as np
#Prescriptive Analytics

# We define our limiting factor ...
print('Welcome! Im here to help you buying your phone')
tm.sleep(1.5)
print('Please tell me how much money you have available to invest (in USD):')
money = input()

# We implement AHP algorithm to compute subjective judgment on criteria preferences.
print('Do you prefer a celphone that is cheap or one with a good camera?')
tm.sleep(.300)
print('Type 1 for it is the same for me')
print('Type 2 for the cheap one')
print('Type 3 for the one with good camera')
q1 = input()

if q1 > 3:
	print('ERROR: Please enter a valid number within the range...')
	tm.sleep(.500)
	print('Do you prefer a celphone that is cheap or one with a good camera?')
	tm.sleep(.300)
	print('Type 1 for it is the same for me')
	print('Type 2 for the cheap one')
	print('Type 3 for the one with good camera')
	q1 = input()
elif q1 != 1:	
	print('In which degree?')
	tm.sleep(.300)
	print('Type 3 for a bit more/less important ')
	print('Type 5 for more/less important')
	print('Type 7 for much more/less important ')
	print('Type 9 for absolutely more/less important ')
	q1b = input()
	if q1 == 3:
		q1b = 1 / q1b
else:
	q1b == 1

print('Do you prefer a celphone that is cheap or one that last more time?')
tm.sleep(.300)
print('Type 1 for it is the same for me')
print('Type 2 for the cheap one')
print('Type 3 for the one that last more')
q2 = input()

if q2 > 3:
	print('ERROR: Please enter a valid number within the range...')
	tm.sleep(.500)
	print('Do you prefer a celphone that is cheap or one that last more time?')
	tm.sleep(.300)
	print('Type 1 for it is the same for me')
	print('Type 2 for the cheap one')
	print('Type 3 for the one that last more')
	q2 = input()
elif q2 != 1:	
	print('In which degree?')
	tm.sleep(.300)
	print('Type 3 for a bit more/less important ')
	print('Type 5 for more/less important')
	print('Type 7 for much more/less important ')
	print('Type 9 for absolutely more/less important ')
	q2b = input()
	if q2 == 3:
		q2b = 1 / q1b
else:
	q2b == 1

print('Do you prefer a celphone that has a good camera or one that last more time?')
tm.sleep(.300)
print('Type 1 for it is the same for me')
print('Type 2 for the one with good camera')
print('Type 3 for the one that last more time')
q3 = input()

if q3 > 3:
	print('ERROR: Please enter a valid number within the range...')
	tm.sleep(.500)
	print('Do you prefer a celphone that has a good camera or one that last more time?')
	print('Type 1 for it is the same for me')
	print('Type 2 for the one with good camera')
	print('Type 3 for the one that last more time')
	q3 = input()
elif q3 != 1:	
	print('In which degree?')
	tm.sleep(.300)
	print('Type 3 for a bit more/less important ')
	print('Type 5 for more/less important')
	print('Type 7 for much more/less important ')
	print('Type 9 for absolutely more/less important ')
	q3b = input()
	if q3 == 3:
		q3b = 1 / q3b
else:
	q3b == 1
	

# Criteria Matrix
criteria_matrix = np.array([
[1, q1b, q2b], 
[1/q1b, 1, q3b], 
[1/q2b,1/q3b,1]])

# Column Sum
col_sum = criteria_matrix.sum(axis=0)

# Normalised Criteria Matrix
normalised_criteria_matrix = criteria_matrix / col_sum

# We calculate the eighen vector
eighen_vector = normalised_criteria_matrix.mean(1)

eighen_vector =  np.reshape(eighen_vector, (1, 3))

# So now we know the weights of the criteria... 

# TOPSIS ALGORITHM IMPLEMENTATION



# This is the number of alternatives
nalt = 10000

# Decision Matrix
decision_matrix = np.array([[random.randint(50,3000), random.randint(5,20), random.randint(6,72)]])

for x in range (1, nalt):
	decision_matrix = np.vstack([decision_matrix, np.array([random.randint(50,3000), random.randint(5,20), random.randint(6,72)])])

c1 = decision_matrix[:,0]
c2 = decision_matrix[:,1]
c3 = decision_matrix[:,2]

colsum1 = 0
colsum2 = 0
colsum3 = 0

# We calculate the norm of each column in our decision matrix

for x in c1:
	x = x ** 2
	colsum1 = colsum1 + x
	#tm.sleep(.010)


for x in c2:
	x = x ** 2
	colsum2 = colsum2 + x
	#tm.sleep(.010)


for x in c3:
	x = x ** 2
	colsum3 = colsum3 + x
	#tm.sleep(.010)


colsum1 = math.sqrt(colsum1)
colsum2 = math.sqrt(colsum2)
colsum3 = math.sqrt(colsum3)

norm = np.array([[colsum1, colsum2, colsum3]])

	
# Normalised Decision Matrix
n_decision_matrix = np.true_divide(decision_matrix, norm)

# Weighted Normalised Decision Matrix
wn_decision_matrix =  np.multiply(n_decision_matrix, eighen_vector)


# We define the ideal solution and anti ideal solution
ideal = np.vstack([np.amin(n_decision_matrix[:,0], axis=0), np.amax(n_decision_matrix[:,1], axis=0), np.amax(n_decision_matrix[:,2], axis=0)])
anti_ideal = np.vstack([np.amax(n_decision_matrix[:,0], axis=0), np.amin(n_decision_matrix[:,1], axis=0), np.amin(n_decision_matrix[:,2], axis=0)])

scored_alternatives = []
indexes = []

n = 0

# We calculate distances to ideal and anti ideal solution, alongside with the performance score
for x in wn_decision_matrix:
	distTo_ideal = np.linalg.norm(x-ideal)
	distTo_anti_ideal = np.linalg.norm(x-anti_ideal)
	performance_score = distTo_anti_ideal / (distTo_ideal + distTo_anti_ideal)
	n = n + 1
	append_value = (performance_score, n)
	indexes.append(append_value)
	scored_alternatives.append(performance_score)


# We ranked our altternatives
ranked_alternatives = sorted(indexes, key=lambda alternative: alternative[0], reverse=True)


scored_alternatives = np.reshape(np.array([scored_alternatives]), (nalt, 1))
	

# We define the best alternative
ii = 0
i = ranked_alternatives[ii][1]-1
best_alternative = decision_matrix[[i], :] 

tm.sleep(1)

# Agent sends message to the human partner
print('According to your budget, the best alternative is: ')
tm.sleep(1.5)
print('[[Price, CameraMP, UseLife]]')

# If solution is not within budget then iterate until find an affordable alternative
while best_alternative[0][0] > money:
	ii = ii + 1
	i = ranked_alternatives[ii][1]-1
	best_alternative = decision_matrix[[i], :] 	
print(best_alternative) 








