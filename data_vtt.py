import csv

english = 4
korean = 5
language = english
titles = ["INTERESTING FACTS ABOUT", "story about", "Brief Overview", "Story Behind"]
subscribeTxt = "subscribe to our YouTube channel"
projectDir = "/Users/choir/Eash Classic/Nocturne/"
downloadDir = "/Users/choir/Downloads/"

# open the CSV file for reading
with open(downloadDir + 'data.csv', 'r') as csvfile:
    # create a CSV reader object
    reader = csv.reader(csvfile)

    # open the text file for writing
    with open(projectDir + 'data.vtt', 'w') as textfile:
        textfile.write('WEBVTT')
        textfile.write('\n\n')
        # write each row from the CSV to the text file
        rowNo = 0
        sectionRowNo = 0
        for row in reader:
            rowNo = rowNo + 1
            sectionRowNo = sectionRowNo + 1
            columnNo = 0;
            timePeriod = ""
            for column in row:
                sentence = ""
                columnNo = columnNo + 1
                if (columnNo == 1):
                    print(column)
                    textfile.write(column)
                    textfile.write('\n')
                elif (columnNo == 2):
                    timePeriod = column + ".000";
                elif (columnNo == 3):
                    timePeriod = timePeriod + " --> " + column + ".000"
                    print(timePeriod)
                    textfile.write(timePeriod)
                    textfile.write('\n')
                elif (columnNo == language):
                    if any(title in column for title in titles):
                        sentence = sentence + column.upper()
                        sectionRowNo = 0
                    elif subscribeTxt in column:
                        sentence = sentence + column
                    else:
                        # sentence = str(sectionRowNo) + ". " + column
                        sentence = column

                    print(sentence)
                    textfile.write(sentence)
                    textfile.write('\n\n')
                else:
                    textfile.write('\n')
