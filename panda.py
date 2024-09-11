import pandas as pd
df=pd.read_csv("/content/airlines_reviews.csv.zip")
print(df)
fl=0
for i in range(0,8100):
  if df['Type of Traveller'][i]=="Family Leisure":
    fl+=1
print("People Travelling with Family:",fl)
sl=0
for i in range(0,8100):
  if df['Type of Traveller'][i]=="Solo Leisure":
    sl+=1
print("Solo Travellers:",sl)
sa=[]
for i in range(0,8100):
  if df['Airline'][i]=="Singapore Airlines":
    sa.append(df['Name'][i])
print("Names of people travelling in Singapore Airlines:",sa)
ts=[]
for i in range(0,8100):
  if 'to London Heathrow' in df['Route'][i]:
    ts.append(df['Airline'][i])
print("Airlines providing flights to London Heathrow:",set(ts))
print(len(set(ts)),'Airlines out of 10 Airlines provide flights to London Heathrow')
pf=0
for i in range(0,8100):
  if df['Month Flown'][i]=="February 2024":
    pf+=1
print("No. of People who travelled in the month February in 2024:",pf)
qa=0
qn=[]
for i in range(0,8100):
  if df['Airline'][i]=="Qatar Airways":
    if df['Food & Beverages'][i]==5 and df['Staff Service'][i]==5:
      qa+=1
      qn.append(df['Name'][i])
print("No. of Qatar travellers who loved food and staff service:",qa,"\n Their names:",qn)
ec=0
bc=0
for i in range(0,8100):
  if df['Class'][i]=="Economy Class":
    ec+=1
  if df['Class'][i]=="Business Class":
    bc+=1
print("People in Economy:",ec,"\nPeople in Business Class:",bc,"\nRatio of business class to economy:",bc/ec)
tencount=0
yescount=0
for i in range(0,8100):
  if df['Verified'][i]=="False":
    print("Overall Rating:",df['Overall Rating'][i],"Recommendation:",df['Recommended'][i])
    if(int(df['Overall Rating'][i])==10):
      tencount+=1
    if(df['Recommended'][i]=="yes"):
      yescount+=1
print("False Reviews who rated 10:",tencount,"False Reviews who recommended:",yescount)
er=0
et=0
for i in range(0,8100):
  if df['Airline'][i]=="Emirates":
    et+=1
    if df['Recommended'][i]=='yes':
      er+=1
print("Emirates travellers who recommend the airline:",er,"out of",et,"Emirate travellers")
