import json
import time
from scrape_irs import scrape_irs
from download_irs import download_irs


def main():
    result = []
    year1 = 0
    year2 = 0
    with open("input.txt") as inputFile:
        for line in inputFile:
            searchValues = line.strip('\n').split(",")
            if len(searchValues) > 1:                           # if the input we read is an arr larger than size 1,
                for x in range(1, len(searchValues)):           # then we have to deal with downloads, calc the diff
                    searchValues[x] = searchValues[x].strip()   # in the dates to get the range
                    if x == 1:
                        year1 = int(searchValues[x])
                    elif x == 2:
                        year2 = int(searchValues[x])
            print(searchValues)
            if year1 > 0 and year2 > 0:
                yearMin = min(year1, year2)
                yearDiff = max(year2, year1) - yearMin
                download_irs(searchValues, yearMin, yearDiff)
                year1 = 0
                year2 = 0
            else:
                scrape_irs(searchValues, result)

    if len(result) > 0:
        print(result)
        filename = 'json/output' + time.strftime("%Y%m%d-%H%M%S") + ".json"
        with open(filename, "w") as outputFile:
            json.dump(result, outputFile, indent=4)
            outputFile.close()


if __name__ == "__main__":
    main()
