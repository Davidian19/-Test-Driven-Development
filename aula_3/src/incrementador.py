class Change:
    def troca(self, a):
        # verifica se é uma lista
        if type(a) is list:
                if len(a) != 0:
                    # verifica se é uma lista de números
                    for item in a:
                        if type(item) is int:
                            number = True
                        elif type(item) is float:
                            number = True
                        else:
                            number = False
                    if number == True:

                        # verifica se a lista tem mais de um número
                        if len(a) > 1:

                            tempMax = max(a)
                            tempMin = min(a)
                            a.remove(tempMax)
                            a.remove(tempMin)
                            return a

                        else:
                            a.pop()
                            return a
                    else:
                        return a
                else:
                    return a
        else:
            return a
