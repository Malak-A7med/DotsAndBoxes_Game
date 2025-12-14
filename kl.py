  def available_action(self):
        actions=[]
        for rows in range(size):
            for colums in range(size-1):
                if self.horizontal [rows][colums]==0:
                    actions.append(("H",rows , colums))
        for rows in range (size-1):
            for colums in range (size):
                if self.vertical[rows][colums]==0:
                    actions.append(("V",rows , colums))
        return actions