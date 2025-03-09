'''Write a function words_with_char() that accepts a list of strings words and a character x. Return a list of indices 
representing the words that contain the character x. The returned list may be in any order.
'''




def words_with_char(words, x):
	soln = []
	for i,word in enumerate(words): 
		if x in word:
			soln.append(i)
	return soln
words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words,x))
'''
answer[i] == "HulkSmash" if i is divisible by 3 and 5.
answer[i] == "Hulk" if i is divisible by 3.
answer[i] == "Smash" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''
def hulk_smash(n):
	soln = []
	for i in range(1,n+1):
		if i %3 == 0 and i % 5 == 0:
			soln.append("HulkSmash")
		elif i % 3 == 0:
			soln.append("Hulk")
		elif i % 5 == 0:
			soln.append("Smash")
		else:
			soln.append(f'{i}')
	return soln
print(hulk_smash(15))

def shuffle(message, indices):
	soln = [""]*len(message)

	print(message.index("e"))

	for i,v in enumerate(indices):
		soln[v] = message[i]
		

	return soln
	
print(shuffle("findme",[0, 1, 2, 3, 4, 5]))

def minimum_boxes(meals, capacity):
	meals.sort(reverse=True)
	capacity.sort(reverse=True)
	
	
	

	