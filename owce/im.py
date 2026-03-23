with open("names.txt", mode="r", encoding="UTF-8") as fileIn, open("names.py", mode="w", encoding="UTF-8") as fileOut:
      fileOut.write("names = [")
      for line in fileIn:
            name = line.split("\n")[0]
            fileOut.write("\"" + name + "\",")
      fileOut.write("]")