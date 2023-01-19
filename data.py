import csv

english = 4
korean = 5
language = english
titleNos = [1,27]

# open the CSV file for reading
with open('data.csv', 'r') as csvfile:
    # create a CSV reader object
    reader = csv.reader(csvfile)

    # open the text file for writing
    with open('data.txt', 'w') as textfile:
        # write each row from the CSV to the text file
        rowNo = 0
        for row in reader:
            columnNo = 0;
            timePeriod = ""
            rowNo = rowNo + 1
            for column in row:
                columnNo = columnNo + 1
                if (columnNo == 1):
                    print(column)
                    textfile.write(column)
                    textfile.write('\n')
                elif (columnNo == 2):
                    timePeriod = column + ",000";
                elif (columnNo == 3):
                    timePeriod = timePeriod + " --> " + column + ",000"
                    print(timePeriod)
                    textfile.write(timePeriod)
                    textfile.write('\n')
                elif (columnNo == language):
                    if (rowNo in titleNos):
                        column = column.upper()
                    else:
                        column = str(rowNo-1) + ". " + column

                    print(column)
                    textfile.write(column)
                    textfile.write('\n')
                else:
                    skip = True
                    textfile.write('\n')
