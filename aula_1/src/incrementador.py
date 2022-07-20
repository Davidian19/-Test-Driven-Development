class IncError(Exception):
    pass

class Incrementador:
    def inc(self, List):
        if type(List) is list:
            listTemp = []
            for c in List:
                if type(c) is int and c > 0:
                        c += 1
                        listTemp.append(c)
                else:
                    raise IncError(f"{c} não é natural")
            return listTemp
        else:
            if type(List) is int and List > 0:
                res = List + 1
            else:
                raise IncError(f"{List} não é natural")
            return res
