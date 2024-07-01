import os

def write_in_new_file(f1, f2):
    f = open(f1, "r")
    lines = f.readlines()
    f.close()

    with open(f2, "w") as nf:
        count = 0
        for line in lines:
            """write lines except for line n.5"""
            if count != 4:
                nf.write(line)
            count += 1            
    print(nf.closed)

def is_f_empty(file):
    if os.stat(file).st_size == 0:
        return True
    return False

def write_specific_lines(f1, f2, lines_num):
    lines_num.sort()
    with open(f1,'r') as f:
        lines = []
        for i, line in enumerate(f):
            if i in lines_num:
                lines.append(line.strip())
            elif i > lines_num[-1]:
                break
    with open(f2,'w') as nf:
        for line in lines:
            nf.write(line + '\n')

    

# write_in_new_file("test.txt","new_file.txt")
# print(is_f_empty("test.txt"))
# write_specific_lines('test.txt', 'new_file.txt', [2,3])
