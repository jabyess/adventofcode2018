class Traverse:
    def __init__(self):
        self.sum = 0
        self.final = 0
        self.collection = {}
        self.file = open('./input.txt')
        self.iterations = 0


    def update(self):
        # if it doesnt exist, add to dict
        if self.collection.get(self.sum) == None:
            self.collection.update({self.sum: 1})
        elif self.collection.get(self.sum) == 1:
            print('----done----', self.sum, self.iterations)
            self.final = self.sum
            return self.final

    def loop_input(self):
        # make sum
        line = str.strip(self.file.readline())

        if line:
            self.sum += int(line)
            self.update()
        else:
            self.iterations += 1
            self.file.seek(0)


    def do_loop(self):
        while self.final == 0:
            self.loop_input()
    
t = Traverse()
t.do_loop()