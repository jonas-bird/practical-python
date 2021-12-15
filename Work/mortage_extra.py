# mortgage.py
#
# Exercise 1.9

months = 0
principle = 500000
rate = .05
base_payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108

while principle > 0:
    months += 1
    if months <= extra_payment_end_month and months >= extra_payment_start_month:
        principle = principle * (1+rate/12) - (base_payment + extra_payment)
        total_paid = total_paid + (base_payment + extra_payment)
    else:
        principle = principle * (1+rate/12) - base_payment
        total_paid = total_paid + base_payment
total_paid = round(total_paid, 2)
print('Total paid', total_paid, 'Over', months, 'months')
