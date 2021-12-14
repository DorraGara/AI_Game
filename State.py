class State:
    def __init__(self, array,depth = 0) -> None:
        self.array = array
        self.taille = len(array)
        self.depth = depth

    def generate_actions(self):
        from Action import Action
        result = []
        for i in range(self.taille):
            if (self.array[i]>2):
                x=1
                while(x<self.array[i]-x):
                    result.append(Action(self,i,self.array[i]-x,x))
                    x=x+1
        return result

    def to_string(self):
        return self.array

    def is_final(self):
        for i in range(self.taille):
            if(self.array[i]> 2):
                return False
        return True
    def is_player1(self):
        return self.depth % 2 == 0

    def is_player2(self):
        return self.depth % 2 != 0