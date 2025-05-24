import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
color = [ 'blue', 'green', 'red', 'purple','gray','Navy','violet','Gold','Black']
data=[]
with open('step3/DOS_SUM.txt','r') as file:

    for line in file:
        data.append(line.strip().split())
    for i in range(9):
        x=[float(d[0]) for d in data]
        y=[float(d[i+1]) for d in data]
        plt.plot(x,y,color=color[i])

plt.axvline(0,color='red',linestyle='--',linewidth=1)
plt.xlabel("E-Ev(eV)")
plt.ylabel("DOS")
plt.title("BaTiO3 分态密度曲线图")
plt.savefig("output/stu.png")
plt.show()
