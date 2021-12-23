class State:
    def __init__(self, array,depth = 0) -> None:
        self.array = array
        self.taille = len(array)
        self.depth = depth

    def generate_actions(self):
        from Action import Action
        #result = []
        checked = {}
        for i in range(self.taille):
            if (self.array[i]>2):
                remainder = 1
                partition = self.array[i] - remainder
                while(remainder < partition):
                    if(not f"{self.array[i]}=>({partition},{remainder})" in checked):
                        #result.append(Action(self,index=i, partition=partition, remainder=remainder))
                        yield Action(self,index=i, partition=partition, remainder=remainder)
                        checked[f"{self.array[i]}=>({partition},{remainder})"] = True
                    remainder += 1
                    partition = self.array[i] - remainder
    


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