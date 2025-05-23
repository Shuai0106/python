import statistics
import csv
data=[]
with open('step9/admit2.csv','r') as file:
    reader = csv.reader(file)
    header =next(reader)
    for row in reader:
        data.append(row)

n = input()
if n=='1':
    ls1=[ch[1] for ch in data if float(ch[8])>=0.8]
    ls2=[ch for ch in ls1 if int(ch)>=4]
    print(f'Top University in >=80%:{len(ls2)/len(ls1)*100:.2f}%')
elif n=='Research':
    ls3=[ch[5] for ch in data if float(ch[8])>=0.9]
    ls4=[ch[5] for ch in data if float(ch[8])<=0.7]
    ls5=[ch for ch in ls3 if ch!='0']
    ls6=[ch for ch in ls4 if ch!='0']
    print(f'Research in >=90%:{len(ls5)/len(ls3)*100:.2f}%')
    print(f'Research in <=70%:{len(ls6)/len(ls4)*100:.2f}%')
elif n=='2':
    ls7=[int(ch[3]) for ch in data if float(ch[8])>=0.8]
    print(f'TOEFL Average Score:{statistics.mean(ls7):.2f}')
    print(f'TOEFL Max Score:{max(ls7):.2f}')
    print(f'TOEFL Min Score:{min(ls7):.2f}')
elif n=='3':
    ls8 =[float(ch[4]) for ch in data if float(ch[8])>=0.8]
    print(f'CGPA Average Score:{statistics.mean(ls8):.3f}')
    print(f'CGPA Max Score:{max(ls8):.3f}')
    print(f'CGPA Min Score:{min(ls8):.3f}')
else:
    print('ERROR')