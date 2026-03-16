B = int(input())
total_tickets = int(input())
other = int(input())
if B + other > total_tickets:
    print('N')
else:
    print(f'Y {total_tickets-B-other}')