#Importing Modules
import pandas as pd
import numpy as np



# Linear Regression 30 pts

class Linear_regression:
    
    def __init__(self, x, y, m, c, epochs, L):
       self.x = x
       self.y = y
       self.m = m
       self.c = c
       self.epochs = epochs
       self.L = L
        
        
    def gradient_descent(self) :
        for a in range(self.epochs):
            Dm=[]
            Dc=[]
            for i in range(len(self.x)):
                for j in range(len(self.x[i])):
                    ypredi = (self.x[i][j] *self.m) + self.c
                    Dm.append(self.x[i][j]*(ypredi-self.y[i]))
                    Dc.append(ypredi-self.y[i])
            dm = sum(Dm)/len(Dm)
            dc = sum(Dc)/len(Dc)
            self.m = self.m - self.L * dm
            self.c = self.c - self.L * dc
        return(self.m,self.c)
    
    def predict(self,x_new):
       # add your code here 
        arr = []
        for i in (x_new):
            ypredi = (i *self.m) + self.c
            arr.append(ypredi)
        return(arr)





#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
# Credit Transaction data(30 points)

#Reading CSVs Files
df_main = pd.read_csv("./res_purchase_2014.csv")

#Clean Data only numerical values
# Convert to string
df = df_main['Amount'].astype(str)

# Remove all the unwanted characters
df = df.map(lambda x: x.replace('$','').replace(')','').replace('zero',''))

# Remove the Bracket and negate the value
df = df.map(lambda x: x.replace('(', '-')) 

# Convert the String to Numeric Value
df = df.apply(pd.to_numeric)
TotalAmount = df.sum()
print("Total amount spending captured in this dataset", TotalAmount)


######## WW GRAINER
df_grainer = df_main[df_main['Vendor'].str.contains("WW GRAINGER")]

# Data Cleaning from above
df = df_grainer['Amount'].astype(str)

# Remove all the unwanted characters
df = df.map(lambda x: x.replace('$','').replace(')','').replace('zero',''))

# Remove the Bracket and negate the value
df = df.map(lambda x: x.replace('(', '-')) 

# Convert the String to Numeric Value
df = df.apply(pd.to_numeric)
TotalAmount = df.sum()
print("Total amount spend at WW GRAINGER", TotalAmount)

###### WM SUPERCENTER

df_supercenter = df_main[df_main['Vendor'].str.contains("WM SUPERCENTER")]

# Data Cleaning from above
df = df_supercenter['Amount'].astype(str)

# Remove all the unwanted characters
df = df.map(lambda x: x.replace('$','').replace(')','').replace('zero',''))

# Remove the Bracket and negate the value
df = df.map(lambda x: x.replace('(', '-')) 

# Convert the String to Numeric Value
df = df.apply(pd.to_numeric)
TotalAmount = df.sum()
print("Total amount spend at WM SUPERCENTER", TotalAmount)


####### GROCERY STORES
df_main['Merchant Category Code (MCC)'] = df_main['Merchant Category Code (MCC)'].str.replace(',',' ')
df_grocery = df_main[df_main['Merchant Category Code (MCC)'].str.contains("GROCERY STORES")]

# Data Cleaning from above
df = df_grocery['Amount'].astype(str)

# Remove all the unwanted characters
df = df.map(lambda x: x.replace('$','').replace(')','').replace('zero',''))

# Remove the Bracket and negate the value
df = df.map(lambda x: x.replace('(', '-')) 

# Convert the String to Numeric Value
df = df.apply(pd.to_numeric)
TotalAmount = df.sum()
print("Total amount spend at GROCERY STORES", TotalAmount)

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#Data Processing with Pandas (40 points)

#1 Reading Excel Files
BalanceSheet = pd.read_excel('./Energy.xlsx')
Ratings = pd.read_excel('./EnergyRating.xlsx')

#2  drop the column if more than 30% value in this colnmn ismissing value, see how many features are remaining.
BalanceSheet = BalanceSheet.loc[:, BalanceSheet.isnull().mean() < 0.3]
print(BalanceSheet.head(10))

#3drop the column if more than 90% value in this colnmn is 0,see how many features are remaining.

BalanceSheet = BalanceSheet.drop(columns=BalanceSheet.columns[((BalanceSheet==0).mean()>0.9)],axis=1)
print(BalanceSheet.head(10))


#4 Replace all None or NaN with average value of each column.
BalanceSheet.fillna((BalanceSheet.mean()))

# 5  Normalize the table

BalanceSheetNums = BalanceSheet.select_dtypes([np.number]) #selecting numeric columns only to normalize

normalBalanceSheet = BalanceSheetNums.apply(lambda x: (x-x.min())/(x.max()-x.min()))

print(normalBalanceSheet.head(10))



# 6 Correlation

correaltion_BalanceSheet = normalBalanceSheet[['Current Assets - Other - Total', 'Current Assets - Total', 'Other Long-term Assets', 'Assets Netting & Other Adjustments']]

print("Correaltion Matrix ::\n\n",correaltion_BalanceSheet.corr())

# 7 Merge (inner) Ratings and BalanceSheet based on ’datadate’ and ’Global Com-pany Key’, and name merged dataset ’Matched’.

Matched = pd.merge(Ratings, BalanceSheet, on=['Data Date', 'Global Company Key'], how='inner') #inner join on three keys
print(Matched)



# 8 Mapping 

dict_ratings = { "AAA" : 0,
                "AA+" : 1,
                "AA" : 2,
                "AA-" : 3,
                "A+" : 4,
                "A" : 5,
                "A-" : 6,
                "BBB+" : 7,
                "BBB": 8,
                "BBB-" : 9,
                "BB+" : 10,
                "BB" : 11,
                "others" : 12 }


Matched['Rate'] = Matched['S&P Domestic Long Term Issuer Credit Rating'].map(dict_ratings)
print(Matched.head(10))

# 9
# 
# Linear_model = Linear_regression(Matched['Interest and Related Expense- Total'],Matched['Rate'],0,0,500,0.001)

