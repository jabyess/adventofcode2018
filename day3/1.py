
class Parser:
    def __init__(self):
        self.input = open('./input.txt')

        self.parse_input(self.input)


    def parse_input(self, input):
        obj = []
        # temp = input.split('\n')
        for line in input:
            l = line.split(" ")
            coords = l[2].split(",")
            size = l[3].split("x")

            temp = {
                "id" : l[0],
                "x" : coords[0],
                "y" : coords[1][:-1],
                "w" : size[0],
                "h" : size[1].strip()
            }
            obj.append(temp)
            print(line)
        
        print(obj[1])
            
            



p = Parser()
# p.parse_input()


