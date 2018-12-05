class Splitter:
    def __init__(self):
        self.input = open('./input.txt')
        self.words = []

        for word in self.input:
            self.words.append(str.strip(word))

    
    def iterate(self):
        diff_word = []
        diff_letter = ''

        for i in range(len(self.words)):
            
            for j in range(i + 1, len(self.words) -1):
                letters = []
                for letter in range(len(self.words[i])):
                    if self.words[i][letter] != self.words[j][letter]:
                        letters.append(self.words[i][letter])
            
                if len(letters) == 1:
                    diff_letter = letters[0]
                    diff_word.append(self.words[i])
                    final_word = list(diff_word[0])
                    print(final_word)
                    print(final_word.remove(diff_letter))
                    print("".join(final_word))



s = Splitter()
s.iterate()