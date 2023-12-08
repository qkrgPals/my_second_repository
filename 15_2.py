import pandas as pd
import matplotlib.pyplot as plt

#막대그래프 그리기
""" x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
#clr = ["r", "g", "b"]
clr = ["C2", "lime", "#57ADCC"] """

##수평 그래프 그리기
""" #plt.barh(x_years, y_data)

#{x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")

plt.show() """

##산점도 그래프 그리기

""" plt.scatter(1, 1)

plt.scatter(x+1.5, y+1.5, 100, 2, alpah=0.5)

plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
plt.colorbar() """

##히스토그램 그리기
""" #plt.hist({data}, bins={구간수})
plt.hist(rn, bins=10)
plt.legend()
plt.show()

#plt.hist(rn,  bins=10, label="def") 

#plt.hist(rn,  bins=10, label="def", alpha=0.5)

plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step") """
#========================================================
##파이챠트 그리기
""" rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

#plt.pie(rate)

#plt.pie(rate, labels=labels)

#plt.pie(rate, labels=labels, autopct='%d%%')
#plt.pie(rate, labels=labels, autopct='%.1d%%')
#plt.pie(rate, labels=labels, autopct='%.1f%%')

#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)
#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270)

#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)

#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
#lt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.2, 0.5, 1])
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0.1, 0.1])
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0.1])
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.5, 0, 0])

plt.show() """

#------------------------------------------------------------

#패널 스타일 설정
""" print(plt.style.available)

#plt.style.use("bmh")
#plt.style.use("ggplot")
#plt.style.use("classic")
#plt.style.use("Solarize_Light2")
#plt.style.use("dark_background")
plt.style.use("fast")

plt.plot([2,3,6,7,10], [1,4,5,8,9])

plt.show() """

#------------------------------------------------------------

#포맷 설정
""" #plt.rcParams['figure.figsize'] = (6, 3)
#plt.rcParams['figure.figsize'] = (4, 3)

#plt.rcParams['font.size'] = 15
#plt.rcParams['font.size'] = 5
#plt.rcParams['font.size'] = 20

#plt.rcParams['lines.linewidth'] = 5

#plt.rcParams['lines.linestyle'] = '--'

#plt.rcParams['xtick.top'] = True

#plt.rcParams['ytick.right'] = True

#plt.rcParams['xtick.direction'] = 'in'
#plt.rcParams['ytick.direction'] = 'in'

#plt.rcParams['ytick.major.size'] = 12

#plt.rcParams['xtick.minor.visible'] = True

plt.plot([2,3,6,7,10], [1,4,5,8,9])

plt.show() """

#------------------------------------------------------------

#객체 활용
""" #fig, ax = plt.subplots()

#왼, 밑, 두께, 높이
#ax = fig.add_axes([0, 0, 0, 0])
#ax = fig.add_axes([1, 1, 0, 0])
#ax = fig.add_axes([1, 1, 1, 1])

#fig, ax = plt.subplots(1, 1)
#fig, ax = plt.subplots(1, 2)
#fig, ax = plt.subplots(2, 2)
#fig, ax = plt.subplots(3, 3)


x = [1,4,5,8,9]
y1 = [2,3,6,7,10]

fig, ax = plt.subplots(2, 2)

#fig, ax = plt.subplots(2, 2, sharex=True)
#fig, ax = plt.subplots(2, 2, sharey=True)

ax[0][0].plot(x, y1)
ax[0][1].plot(x, y1)
ax[1][0].plot(x, y1)
ax[1][1].plot(x, y1)

plt.show() """

#------------------------------------------------------------

#Y축 동시 출력
# 사용 데이터
""" x = [1,4,5,8,9]

y1 = [2,3,6,7,10]
y2 = [10,8,6,4,2]

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Data")
ax1.set_ylabel("Y1")
ax1.plot(x, y1)

ax2 = ax1.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x, y2)

ax1.plot(x, y1, color="C1")
ax2.plot(x, y2, color="C2")

ax1.plot(x, y1, color="C1", label="y1 Data")
ax1.legend(loc="upper right")

ax2.plot(x, y2, color="C2", label="y2 Data")
ax2.legend(loc="lower right")

plt.show() """

#------------------------------------------------------------

#이종 그래프 출력
""" x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2")
ax2.set_ylabel("Y2data")

ax1.plot(x, y1, "-o", color="C1", label="XData")
ax2.bar(x, y2, color="C2", label="YData")

ax1.legend()
ax2.legend()

plt.show() """

#------------------------------------------------------------

#다중 그래프 출력
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

plt.subplot(2, 1, 1)    # 1set
plt.plot(x1, y1, "o-")

plt.subplot(2, 1, 2)
plt.plot(x2, y2, ".-")

plt.subplot(2, 1, 1)

plt.show()