


class FancyDict:
    def __init__(self):
        self.grid_dict = {}
    
    def modify_dict(self, grid_dict):
        for key, value in self.grid_dict.items():
        # print(key)
        # print(value)
            for key_inner, value_inner in value.items():
            # print(key_inner)
            # print(value_inner)
                self.grid_dict[key][key_inner] = int(input("Enter a Number at " +key + " " + key_inner + ": " ))

    
    def sum_region_dict(grid, row):
        global total
        print(grid)
        for key, value in grid.items():
            print(key)
            print(value)
            for key_inner, value_inner in value.items():
                print(key_inner)
                print(value_inner)
                total += value_inner

        print(total)
    

fancyDict = FancyDict()
fancyDict.modify_dict(0)
fancyDict.sum_region_dict(0)


