from tabulate import tabulate
import json, time



def create_table(path):

    with open(path, 'r') as infile:
        score = json.load(infile)

    keys = []
    values = []
    for key in score:
        keys.append(key)
        values.append(score[key])

    table = tabulate([keys, values], headers="firstrow")

    return table


def main():

    print("jsontotable.py is running...")

    while True:
        time.sleep(0.25)

        with open("request.txt", 'r') as infile:
            text = infile.read()
            open("request.txt", 'w').close()

        if text == 'send table':
            print("request recieved")
            with open("path.txt", "r") as infile:
                path = infile.read()

            table = create_table(path)

            with open("table.txt", 'w') as outfile:
                outfile.write(table)
            print("request fulfilled")



if __name__ == "__main__":
    main()
