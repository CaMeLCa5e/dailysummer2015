daily_hours = 0
numbers = []

while daily_hours < 6:
    print "At the top i is %d" % daily_hours
    numbers.append(daily_hours)

    daily_hours = daily_hours + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % daily_hours


print "The numbers: "

for num in numbers:
    print num