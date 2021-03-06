import sys

__author__ = 'ununoctium'

import requests
import re
import WhemAmIDueProperties

targetMonthChar = ''

def main():
    global targetMonthChar
    ermaVisits = getErmaVisits( WhemAmIDueProperties.targetMonthNum )

    if ( getExpectedMonthChar(WhemAmIDueProperties.targetMonthNum) == targetMonthChar ):
        print ermaVisits

    else :
        # print "Num to target month mismatch. Lucky that I'm smart enough to compensate."
        newTargetMonthNum = WhemAmIDueProperties.targetMonthNum + 1
        while ( getExpectedMonthChar(WhemAmIDueProperties.targetMonthNum) != targetMonthChar ):
            ermaVisits = getErmaVisits(newTargetMonthNum)
            newTargetMonthNum +=1
        print ermaVisits


def getErmaVisits(thisTargetMonthNum):
    global targetMonthChar

    if ( thisTargetMonthNum <= WhemAmIDueProperties.startMonth
         and WhemAmIDueProperties.targetYearNum == 2015
         ):
        print "Can't go before the month of " + \
              getExpectedMonthChar(thisTargetMonthNum) + ". \nBreaks " \
              "my <3logic<3 to say this Princess. \nSorry ! "
        sys.exit()

    #
    # ToDo : Only good for monolithicly increasing months in a Single Year :: Needs more logic
    #
    if ( WhemAmIDueProperties.targetYearNum == 2015 ):
        totalDelta = WhemAmIDueProperties.eachDelta * \
                 ( thisTargetMonthNum -
                   WhemAmIDueProperties.startMonth
                   )
    else:
        multiplier = WhemAmIDueProperties.targetYearNum - WhemAmIDueProperties.startMonth
        totalDelta = WhemAmIDueProperties.eachDelta * \
                 ( ( 12 * multiplier ) +
                   thisTargetMonthNum - WhemAmIDueProperties.startMonth
                 ) + 2

    # totalDelta = WhemAmIDueProperties.eachDelta * \
    #              ( thisTargetMonthNum -
    #                WhemAmIDueProperties.startMonth
    #                )

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
        # resultString = "\n** Wow ! Its your lucky month. Aunt Erma is visiting you twice this month. *"

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


def getExpectedMonthChar(thisMonthNum):
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
    return options[thisMonthNum]


def getMonthNum(thisMonthChar):
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
    return options[thisMonthChar]


if __name__ == '__main__':
    main()



