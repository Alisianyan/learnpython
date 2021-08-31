# importing csv module
import csv
  
# csv file name
filename = "mtesrl_20150626_MD0000600002_stats.txt"
  
# initializing the titles and rows list
percentile_values=[50, 90, 99, 99.9]
fields = []
rows = []
result = {}
to_print = {}
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    next(csvfile)
    next(csvfile)
    csvreader = csv.DictReader(csvfile, delimiter='\t')
      
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
  
#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows:
    if row['EVENT'] is None:
        continue   
    if row['EVENT'] in result:
        result[row['EVENT']].append(int(row['AVGTSMR']))
    else:
        result[row['EVENT']] = [int(row['AVGTSMR'])]
#print(result)
for key, value in result.items():
    value.sort()

for k in result:
    to_print[k]=[]
    
def count_percentile(event, percent):
    temp_l = result[event]
    return temp_l[int(len(temp_l)*percent/100)]
    
def values_per_eventname(event, percent):
    to_print[event].append(count_percentile(event, percent))

for event, value in result.items():
    to_print[event].append(min(result[event]))
    for percent in percentile_values:
        values_per_eventname(event, percent);
        
for x in to_print:
    val = to_print[x]
    print ('{EVENTNAME} min={0} 50%={1} 90%={2}, 99%={3} 99.9%={4}'.format(*val, EVENTNAME=x))
    
#for event, value in result.items():    
#    print ('{} min={} 50%={} 90%={}, 99%={} 99.9%={}'.format(event, min(value), count_percentile(event, 50), count_percentile(event, 90), count_percentile(event, 99), #count_percentile(event, 99.9)))