""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target) """

#------------------------------------------------------------

#순위 매기기
""" from faker import Faker as fk
import os

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
            f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
            #temp.color_name()) """


""" df["aver"] = df.postcode.rank(method="average")
#print(df[["postcode", "aver"]])
print("\n------------------------------\n")

df["dense"] = df.postcode.rank(method="dense")
#print(df[["postcode", "dense"]])
print("\n------------------------------\n")

df["min"] = df.postcode.rank(method="min")
#print(df[["postcode", "min"]])
print("\n------------------------------\n")

df["first"] = df.postcode.rank(method="first")
#print(df[["postcode", "first"]])
print("\n------------------------------\n")

df["max"] = df.postcode.rank(method="max", ascending=False)
df["max"] = df.postcode.rank(method="max")
#print(df[["postcode", "max"]])
print("\n------------------------------\n")

print(df[["postcode", "max", "min", "first", "aver", "dense"]])
print("\n------------------------------\n") """

#------------------------------------------------------------

#컬럼-로우 변경
#print(df.transpose())

#------------------------------------------------------------

#누적계산
""" #print(df["postcode"].expanding().sum())
#print(df["postcode"].expanding())
print(df["postcode"].expanding().max()) """

#------------------------------------------------------------

#정렬 찾기
""" print(df.postcode.idxmax(axis=0)) # 가장 작은수
print("\n------------------------------\n")
print(df.postcode.idxmin(axis=0)) # 가장 큰수
 """
#------------------------------------------------------------

#빈 DataFrame  확인
""" print(df.empty)
print(df.company.empty)
print(df.postcode.empty) """

#------------------------------------------------------------

#인자 검색
#print(df.isin([85083]))
#print(df.isin(["민김송"]))
#print(df.isin(["이정숙"]))

#print(df.isin([95938, 33885]))

#print(df.isin([52585, 67051, "김영수"]))

#------------------------------------------------------------

#기간 계산
""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """

""" #i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)
print("\n------------------------------\n")

#print(df.at_time("09:00"))
#print(df.at_time("03:00"))

print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="03:00", end_time="09:00"))"""

#------------------------------------------------------------

#시간간격 데이터 생성
""" i = pd.date_range("2023-11-10", periods=10, freq="3D")
#i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)

print(df)

#print(df.first("3D"))
#print(df.first("5D"))
#print(df.first("7D"))

#print(df.last("3D"))
#print(df.last("5D"))
print(df.last("7D")) """

#------------------------------------------------------------

#코스피지수
#pip install Finance-DataReader
#pip install plotly
#pip install bs4

""" import FinanceDataReader as fdr
#(Kospi 지수 확인)
#ksp = fdr.DataReader("KS11", "2023")
ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n------------------------------\n") """

#(최고가 확인)
""" print(ksp["High"].max())
print(ksp["High"].idxmax())
print("\n------------------------------\n") """

#(최저가 확인)
""" print(ksp["Low"].min())
print(ksp["Low"].idxmin())
print("\n------------------------------\n") """

#(최고가 값 찾기)
""" print(ksp["Volume"].nlargest(n=5))
print(ksp["Volume"].nlargest(n=10))
print("\n------------------------------\n") """

#(최하위 값 찾기)
""" #print(ksp["Volume"].nsmallest(n=5))
#print(ksp["Close"].nsmallest(n=5))
print(ksp["Close"].nlargest(n=5))
print("\n------------------------------\n") """

#(kospi 3000 달성 최초일 찾기)
""" #cond = ksp["Close"] >= 3000
cond = ksp["Close"] >= 2000
print(ksp[cond].index[0])
print("\n------------------------------\n") """

#(위(shift) 값 참조, 처리)
""" #print(ksp["Volume"] > ksp["Volume"].shift())
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
#print(ksp)
# print(ksp["up"] != ksp["up"].shift().cumsum())
# print("\n------------------------------\n")
ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
#print("\n------------------------------\n")

#(연속 증가값 확인)
ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
#print(ksp)

#(연속 상승값 확인)
print(ksp["up_cnt"].max())
print("\n------------------------------\n") """
#------------------------------------------------------------

#부동산 정보 처리
import pandas as pd

#(변환)
#target = "./data/apt.csv"

#df = pd.read_csv(target, encoding="CP949")
#df.to_csv("./data/conv_apt.csv", encoding="utf8")
df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())
print("\n------------------------------\n")

#(컬럼명 바꾸기)
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)

#(컬럼 타입변경)
#print(df.dtypes)
df["분양가"] = df["분양가"].convert_dtypes()
#print(df.dtypes)

#(array로 변환하기)
#arr = df.to_numpy()
#print(arr)
#print(arr[2])
#print(len(arr))

#(요약정보)
#print(df.describe())

#(축변환하기)
print(df.transpose())
print("\n------------------------------\n")
print(df.T.head())

#(정렬)
#(컬럼이름 출력)
#(필터 출력)
#(인덱스 지정 선택)
#(인덱스 필터)
#(필터)
#(비트연산 필터)
#(컬럼 추가)
#(NaN 행 제거)
#(NaN 데이터 출력)
#(데이터 종류별 출력)
#(그룹핑)

#------------------------------------------------------------

#타이타닉 정보

#------------------------------------------------------------

#아이리스 정보 처리