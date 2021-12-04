# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code
day = 1

if day == 1:
    print("#####################")
    print("####### DAY 1 #######")
    print("#####################")
    print()
    import DayCode.day1 as day1
    day1.runCode()