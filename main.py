# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code
day = 3

if day == 1:
    print()
    print("#####################")
    print("####### DAY 1 #######")
    print("#####################")
    print()
    import DayCode.day1 as day1
    day1.runCode()
if day == 2:
    print()
    print("#####################")
    print("####### DAY 2 #######")
    print("#####################")
    print()
    import DayCode.day2 as day2
    day2.runCode()
if day == 3:
    print()
    print("#####################")
    print("####### DAY 3 #######")
    print("#####################")
    print()
    import DayCode.day3 as day3
    day3.runCode()