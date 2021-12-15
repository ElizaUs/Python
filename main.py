# This is a sample Python script.
import Parser

def main():
     with open("Currency.html", "r", encoding='utf-8') as data:
      result = Parser.MyParser.parse(data)

      check = input("\nChoose currency that you want to find: ")
      if check in result:
       print("Currency: " + check, "\nValue: " + str(result[check]))
      else:
          print ("No such currency")

if __name__ == "__main__":
  main()
