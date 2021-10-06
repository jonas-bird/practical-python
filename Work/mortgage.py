# mortgage.py
#
# Exercise 1.7

months = 0
principle = 500000
rate = .05
payment = 2684.11
total_paid = 0.0

while principle > 0:
    months += 1
    if months <= 12:
        principle = principle * (1+rate/12) - (payment + 1000)
        total_paid = total_paid + (payment + 1000)
    else:
        principle = principle * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid, 'Over', months, 'months')
