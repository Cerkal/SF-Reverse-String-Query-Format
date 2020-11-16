import sys
import os

def main():

    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Expects one argument of file path!")
        sys.exit()

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    query_words = ["SELECT", "FROM", "WHERE", "LIMIT", "ORDER BY", "AND", "OR"]

    with open(filepath) as fp:
        for line in fp:
            
            line = line.strip()
            
            start = line.find("\'")+1
            end = line.rfind("\'")

            outputLine = line[start : end].strip()
            
            if outputLine:
                outputLine = bytes(outputLine, "utf-8").decode("unicode_escape")
            
                first_word = outputLine.split()[0]

                if first_word not in query_words:
                    output = "\t{}".format(outputLine)
                else:
                    output = "{}".format(outputLine)

                print(output)

if __name__ == '__main__':
    main()
