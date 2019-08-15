
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
                "x" : int(coords[0]),
                "y" : int(coords[1][:-1]),
                "w" : int(size[0]),
                "h" : int(size[1].strip())
            }
            obj.append(temp)
            print(line)
        
        print(obj[1])
        self.info = obj

    def find_max(self): 
        longest_width = 0
        longest_height = 0
        for i in self.info:
          curr_width = i["x"] + i["w"]
          curr_height = i["y"] + i["h"]

          if curr_height > longest_height:
              longest_height = curr_height
          if curr_width > longest_width:
              longest_width = curr_width
        self.fabric_width = longest_width
        self.fabric_height = longest_height
        print(self.fabric_width, self.fabric_height)

        
            
    def build_grid(self):
        self.grid = [["." for n in range(1000)] for k in range(1000)]
        


p = Parser()
p.find_max()
p.build_grid()
