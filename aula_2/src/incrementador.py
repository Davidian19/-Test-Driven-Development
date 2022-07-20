class Change:
    def troca(self, a):
        if type(a) is list:
            tam = len(a)
            if tam > 0:
                newList = a[1:]
                temp = a[0]
                newList.append(temp)
                return newList
            else:
                return a
        else:
            print(f"{a} não é uma lista")
            pass
