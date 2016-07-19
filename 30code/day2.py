# Enter your code here. Read input from STDIN. Print output to STDOUT

meal = float(raw_input('meal cost: '))
tip = float(raw_input('tip % :'))/100
tax = float(raw_input('tax % :'))/100

total = round(meal + meal*tip + meal*tax)

print 'The total meal cost is '+ str(int(total))+' dollars.'