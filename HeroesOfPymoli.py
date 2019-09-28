### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()

## Player Count

* Display the total number of players


#PLAYER COUNT

players = purchase_data["SN"].nunique()
players

## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


uni = purchase_data["Item ID"].nunique()
avg = purchase_data["Price"].mean()
IDcount = purchase_data["Purchase ID"].count()
total = purchase_data["Price"].sum()

summary = pd.DataFrame({"Number of Unique Items":[uni], "Average Purchase Price ($)": [avg], "Total Number of Purchases": [IDcount], "Total Revenue ($)": [total]})
summary

## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed









## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

PercCalc = purchase_data.loc[:, ["Gender", "SN", "Age"]]
forpercCalc = PercCalc.drop_duplicates()
rand = pd.DataFrame(forpercCalc.count())
percCount = rand[0][0]

genderCount = forpercCalc["Gender"].value_counts()
genderPerc = (genderCount / percCount)*100
percFrame = pd.DataFrame({"Count": genderCount, "Percentage of Total (%)": genderPerc})

percFrame


# PURCHASING ANALYSIS #

genGrp = purchase_data.groupby(["Gender"])
genCount = genGrp.count()["Price"]
countgen = genCount.rename("Purchase Count")

genMean = genGrp.mean()["Price"]
meangen = genMean.rename("Average Purchase Price ($)")

genGrpPrice = genGrp.sum()["Price"]
sumgen = genGrpPrice.rename("Total Purchase Value ($)")

genAvg = genGrpPrice / percFrame["Count"]
avggen = genAvg.rename("Average Purchase Total per Person by Gender ($)")

genFrame = pd.DataFrame([countgen, meangen, sumgen, avggen]).round(2)
genFrame.transpose()



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


#forpercCalc["Age"].max()
age = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 100]
ageTitle = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-45"]

forpercCalc["Range"] = pd.cut(forpercCalc["Age"], age, labels=ageTitle)
ttlCount = forpercCalc["Range"].value_counts()
perc = (ttlCount/percCount)*100

ageFrame = pd.DataFrame({"Total Count": ttlCount, "Percentage of Players (%)": perc})
ageFrame.sort_index().round(2)

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

purchase_data["Range"] = pd.cut(purchase_data["Age"], age, labels=ageTitle)
rangeGrp = purchase_data.groupby(["Range"])
rangeCount = rangeGrp.count()["Price"]
rangeCount = rangeCount.rename("Purchase Count")

rangeMean = rangeGrp.mean()["Price"]
rangeMean = rangeMean.rename("Average Purchase Price ($)")

rangeSum = rangeGrp.sum()["Price"]
rangeSum = rangeSum.rename("Total Purchase Value ($)")

rangeAvg = rangeSum / ageFrame["Total Count"]
rangeAvg = rangeAvg.rename("Average Purchase Total per Person by Age ($)")

rangeFrame = pd.DataFrame([rangeCount, rangeMean, rangeSum, rangeAvg]).round(2)
rangeFrame.transpose().sort_index()

## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



snGrp = purchase_data.groupby(["SN"])
snCount = snGrp.count()["Price"]
snCount = snCount.rename("Purchase Count")

snMean = snGrp.mean()["Price"]
snMean = snMean.rename("Average Purchase Price ($)")

snSum = snGrp.sum()["Price"]
snSum = snSum.rename("Total Purchase Value ($)")

snFrame = pd.DataFrame([snCount, snMean, snSum]).round(2)
snFrame.transpose().sort_values("Total Purchase Value ($)", ascending=False).head()

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



item = purchase_data.loc[:, ["Item ID", "Item Name", "Price"]]

itemGrp = purchase_data.groupby(["Item ID", "Item Name"])
itemCount = itemGrp.count()["Price"]
itemCount = itemCount.rename("Purchase Count")

itemMean = itemGrp.mean()["Price"]
itemMean = itemMean.rename("Item Price ($)")

itemSum = itemGrp.sum()["Price"]
itemSum = itemSum.rename("Total Purchase Value ($)")

itemFrame = pd.DataFrame([itemCount, itemMean, itemSum]).round(2)
itemFrame.transpose().sort_values("Purchase Count", ascending=False).head()

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



itemFrame.transpose().sort_values("Total Purchase Value ($)", ascending=False).head()