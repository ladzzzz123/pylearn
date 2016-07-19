# open function is built into python
# for more information on built in functions go to http://docs.python.org/lib/built-in-functions.html

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
qty = 0
val = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    val = val + float(line[line.find(':')+2:len(line)])
    qty = qty + 1

avg = str(val/qty)

print 'Average spam confidence: '+avg