class Splitter:
    def __init__(self):
        self.input = open('./input.txt')
    
    def iterate(self):
        threes = 0
        twos = 0
        for line in self.input:
            # build dict of letter counts
            letter_counts = self.split(str.strip(line))
            # convert to list of counts
            vals = list(letter_counts.values())
            if vals.count(2) > 0:
                twos += 1
            if vals.count(3) > 0:
                threes += 1
        
        print(twos, threes)
        print(f"Result is {twos} * {threes} = {twos * threes}")

    
    def split(self, word):
        letters = list(word)
        counts = {}
        for letter in letters:
            if counts.get(letter) == None:
                counts.update({letter: 1})
            elif counts.get(letter):
                counts[letter] += 1
        return counts






s = Splitter()
s.iterate()