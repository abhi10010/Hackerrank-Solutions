import calendar

m, d, y = list(map(int, input().split()))
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(weekdays[calendar.weekday(y,m,d)])
