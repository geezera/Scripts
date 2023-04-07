import sys
import json

def write_result(result_list, output_filename):
    with open(output_filename, 'w') as f:
        json.dump({'ips': result_list}, f, indent=4)
        #for item in result_set:
        #    f.write(item+'\n')

output_filename = 'result.json'
output_filename_misses = 'result_missed.json'
a = set()
b = set()

input_filename = sys.argv[1]
print(f'processing {input_filename}')

with open(input_filename) as f:
    for line in f:
        split_line = line.split(',')
        if '.' in split_line[0]:
            if len(split_line) > 1:
                ip1, ip2, *_ = split_line
            else:
                ip1, ip2 = split_line[0], None
        else:
            n, ip1, ip2, *_ = split_line
        
        if ip1:
            # clean ip1
            digit_index = [x.isdigit() for x in ip1].index(True)
            cleaned_ip1 = ip1[digit_index:].strip()
            
            a.add(cleaned_ip1)
        
        if ip2:
            b.add(ip2.strip())
  
print('done')
print('--------------------')  
print(f'length a: {len(a)}')
print(f'length b: {len(b)}')
print(f'length intersection: {len(a&b)}')
   
diff = a-b 
print(f'length a-b: {len(diff)}')

negative_diff = b-a
print(f'length b-a: {len(negative_diff)}')

print('--------------------')

write_result(list(diff), output_filename)
print(f'Result written to {output_filename}')
    
if negative_diff:
    write_result(list(negative_diff), output_filename_misses)
    print(f'Missed match result written to {output_filename_misses}')
