with open('file1.txt') as f1, open('file2.txt') as f2:
    for i in f1:
        f2.write(i)