import pandas as pd
import requests         #Required in order to use API 
import json             #Required to parse contents

#Global Variables:
#You can create an account at https://financialmodelingprep.com/ in order to use their API key
api_key=''

#Input: Array of integers
#Output: Print out the array of integers, separated by a space
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

#Input: Stock ticker, and specified year for analyzing
#Output: Return the result of the Pandas API call, as a pandas dataframe
def financialratios(quote, year):
    fr = requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/{quote}?apikey={api_key}")
    fr = fr.json()  #Get json contents
    #print(fr)  #DEBUG, print out json contents

    #Compare the date entries first, and save an index value
    index = 0
    for element in fr['ratios']:
        date = element['date'].split('-')
        if int(date[0]) == year:
            break
        index += 1

    #print(index) #Debug

    #Parse out contents of fr
    valuation = fr['ratios'][index]['investmentValuationRatios']
    profitability = fr['ratios'][index]['profitabilityIndicatorRatios']
    operating = fr['ratios'][index]['operatingPerformanceRatios']
    liquidity = fr['ratios'][index]['liquidityMeasurementRatios']
    debt = fr['ratios'][index]['debtRatios']

    #Put objects into pandas dataframe
    valuation = pd.DataFrame(list(valuation.items()),columns=['Ratio', quote])
    profitability = pd.DataFrame(list(profitability.items()),columns=['Ratio', quote])
    operating = pd.DataFrame(list(operating.items()),columns=['Ratio', quote])
    liquidity = pd.DataFrame(list(liquidity.items()),columns=['Ratio', quote])
    debt = pd.DataFrame(list(debt.items()),columns=['Ratio', quote])
    
    #Combine into a list for concat into pd
    frames = [valuation,profitability,operating,liquidity,debt]
    result = pd.concat(frames)
    return result

def main():
    #f=open("data.txt", 'w')
    year = 2020 #This changes the year you want to look for
    listofstocks = ['CTRN','ANF','AEO','URBN','BKE','JWN','DXLG','TJX','GPS','ROST','PLCE'] #List of stocks
    x = financialratios('GOOGL', year) #Must initialize a single object

    for item in listofstocks:
        print(item)
        y = financialratios(item, year)
        x = x.merge(y,on='Ratio')
    
    #print(x) #Debug

    f=open("datathonQ1.csv", "w+")
    x.to_csv("datathonQ1.csv")

    f.close()


# Driver Code:
if __name__ == '__main__':
    main()