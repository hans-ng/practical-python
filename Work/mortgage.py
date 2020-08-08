# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000.0

while principal > 0:
    months = months + 1

    if extra_payment_start_month <= months < extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    if current_payment > principal * (1+rate/12):
        total_paid = total_paid + principal * (1+rate/12)
        principal = 0
    else:
        total_paid = total_paid + current_payment
        principal = principal * (1+rate/12) - current_payment
        
    # print(months, round(total_paid, 2), round(principal, 2))
    print(f'{months:4d} {total_paid:10.2f} {principal:10.2f}')

print('Total paid', round(total_paid, 2))
print('Total months', months)