from graph import Graph

filename = "words.txt"
with open(filename) as f:
    word_list = f.read().splitlines() 

start_word = 'sail'

end_word = 'boat'

alphabet = list('abcdefghijklmnopqrstuvwxyz')

g = Graph()

g.add_vertex(start_word)

for i, letter in enumerate(start_word):
	for j, alpha in enumerate(alphabet):
		new_word = start_word[:i+1] + alpha[j] + start_word[i+1:]
		print(new_word)
