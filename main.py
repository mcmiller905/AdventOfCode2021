# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code
day = 2

if day == 1:
    print("#####################")
    print("####### DAY 1 #######")
    print("#####################")
    print()
    import DayCode.day1 as day1
    day1.runCode()
if day == 2:
    print("#####################")
    print("####### DAY 2 #######")
    print("#####################")
    print()
    import DayCode.day2 as day2
    day2.runCode()