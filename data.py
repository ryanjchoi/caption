import csv

english = 4
korean = 5
language = english
titleNos = [1]
projectDir = "/Users/choir/Eash Classic/Moonnight Sonata/"

# open the CSV file for reading
with open(projectDir + 'data.csv', 'r') as csvfile:
    # create a CSV reader object
    reader = csv.reader(csvfile)

    # open the text file for writing
    with open(projectDir + 'data.srt', 'w') as textfile:
        # write each row from the CSV to the text file
        rowNo = 0
        sectionRowNo = 0
        for row in reader:
            rowNo = rowNo + 1
            sectionRowNo = sectionRowNo + 1
            columnNo = 0;
            timePeriod = ""
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
                        sectionRowNo = 0
                    else:
                        column = str(sectionRowNo) + ". " + column

                    print(column)
                    textfile.write(column)
                    textfile.write('\n')
                    textfile.write('\n')
                else:
                    textfile.write('\n')
