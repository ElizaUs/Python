import re

class MyParser:
    def __init__(self, date, currency):
        self.date1 = date
        self.currency1 = currency

    def parse(self):
        f_str = self.read()
        # find date
        current_date = re.search("\d\d\W\d\d\W\d\d\d\d\s", f_str)
        print("\nCurrent date: " + current_date.group())

        # get available codes
        raw_codes = re.findall(">""[A-Z]{3}", f_str)

        # create new list with correct currency
        currency_list = []
        for x in raw_codes:
            y = x.replace('>', '')
            currency_list.append(y)

        # get available rates
        currency_values = re.findall("[0-9]{2}[,][0-9]{4}", f_str)
        currency_values.remove("50,2224")
        #create dictionary for currency-currency value
        #global dictionary
        dictionary = dict(zip(currency_list,currency_values))
        print(dictionary)
        return dictionary

'''
# f_str2 = f_str.lstrip("Центральный банк Российской Федерации установил с")

'''