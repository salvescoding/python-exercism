class Allergies():

    ELEMENT = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }
    ELEMENT_NUM = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats"
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
          return True if self.ELEMENT[item] <= self.score else False


    @property
    def lst(self):
        new_list = []
        score = self.score
        if score == 257:
            return ['eggs']
        while score > 0:
            element = self.ELEMENT_NUM.get(score, self.ELEMENT_NUM[min(
                self.ELEMENT_NUM.keys(), key=lambda k: abs(k-score))])
            print(element)
            if score in self.ELEMENT_NUM.keys():
                new_list.append(self.ELEMENT_NUM[score])
            if element not in new_list:
                new_list.append(element)
                self.ELEMENT_NUM = {key: val for key, val in self.ELEMENT_NUM.items() if val !=
                 element}
            score -= self.ELEMENT[element]
        print(score)
        print(new_list)
        return new_list




        # check the largest int smaller than the self.score
        # add the key to the list and decrease the score


