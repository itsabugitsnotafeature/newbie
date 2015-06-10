__author__ = 'ununoctium'

import requests
import re
import WhemAmIDueProperties

targetMonthChar = ''

def main():
    global targetMonthChar
    ermaVisits = getErmaVisits()

    if ( getExpectedMonthChar() == targetMonthChar ):
        print ermaVisits

    else :
        print "Num to target month mismatch. Lucky that I'm smart enough to compensate."



def getErmaVisits():
    global targetMonthChar

    #
    # ToDo : Only good for monolithicly increasing months in a Single Year :: Needs more logic
    #
    totalDelta = WhemAmIDueProperties.eachDelta * \
                 ( WhemAmIDueProperties.targetMonthNum -
                   WhemAmIDueProperties.startMonth
                   )

    getUrl = constructGetUrl(WhemAmIDueProperties.startMonth,
                             WhemAmIDueProperties.startDate,
                             WhemAmIDueProperties.startYear,
                             totalDelta)

    getNextUrl = constructGetUrl(WhemAmIDueProperties.startMonth,
                                 WhemAmIDueProperties.startDate,
                                 WhemAmIDueProperties.startYear,
                                 totalDelta + WhemAmIDueProperties.eachDelta)

    getCallContent = makeGetCall(getUrl)
    targetDate = re.search(WhemAmIDueProperties.resultRegExpString, getCallContent).group(0)
    targetDate = re.search(WhemAmIDueProperties.resultDateRegExpString, targetDate).group(0)
    targetMonthChar = re.search(WhemAmIDueProperties.monthReExpString, targetDate).group(0)

    getCallContent = makeGetCall(getNextUrl)
    nextTargetDate = re.search(WhemAmIDueProperties.resultRegExpString, getCallContent).group(0)
    nextTargetDate = re.search(WhemAmIDueProperties.resultDateRegExpString, nextTargetDate).group(0)
    nextTargetMonth = re.search(WhemAmIDueProperties.monthReExpString, nextTargetDate).group(0)

    if (targetMonthChar == nextTargetMonth):
        resultString = "\n** Wow ! Its your lucky month. Aunt Erma is visiting you twice this month. *"

        resultString += "\nFirst visit is day AFTER : " + str(targetDate)
        resultString += "\nSecond visit is day AFTER : " + str(nextTargetDate)

    else:
        resultString = "Aunt Erma visiting day AFTER : " + str(targetDate)

    return resultString




def constructGetUrl(theMonth, theDate, theYear, theDelta):
    return 'http://www.timeanddate.com/date/dateadded.html?m1=' + \
           str(theMonth) + \
           '&d1=' + \
           str(theDate) + \
           '&y1=' + \
           str(theYear) + \
           '&type=add&ay=&am=&aw=&ad=' + \
           str(theDelta)


def makeGetCall(getUrl):
    r = requests.get(getUrl)
    return r.content


def getExpectedMonthChar():
    options = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return options[WhemAmIDueProperties.targetMonthNum]


def getMonthNum(thisMonth):
    options = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return options[thisMonth]


if __name__ == '__main__':
    main()



