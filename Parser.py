import re

class MyParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        f_str = self.read()
        # find date
        current_date = re.search("\d\d\W\d\d\W\d\d\d\d\s", f_str)
        print("\nCurrent date: " + current_date.group())

       # get available codes
        currency_list = re.findall("(?<=td>)[A-Z]{3}", f_str)

        # get available rates
        currency_values = re.findall("(?<=td>)[0-9]{2}[,][0-9]{4}", f_str)
        #create dictionary for currency-currency value
        dictionary = dict(zip(currency_list,currency_values))
        print(dictionary)
        return dictionary

'''
# f_str2 = f_str.lstrip("Центральный банк Российской Федерации установил с")

'''
