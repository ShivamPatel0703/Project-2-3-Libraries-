import pyplot
import matplotlib
# Median Developer Salaries by Age
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']

birthdays = [325955, 298058	, 328923, 320832, 327917,
         330541, 353415	, 351791, 347516, 339007, 318820,
             335722]

plot.xlabel('Birthday Months')
plot.ylabel('Birthday per month ')
plot.title('Birthday Chart ')
plot.plot(months, birthdays)

plot.show()
