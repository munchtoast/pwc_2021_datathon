# First Place PWC 2021 Datathon Competition

Python with Pandas used to solve and estimate the financial concerns of large, and small corporations from pre-COVID19 to present day. We have utilized financial models concerning valuations, profitability, operating costs, liquidity, and debt to track trends.

## Description

We have used this program to make API calls using the "Request" library to https://financialmodelingprep.com/, to utilize their software and tools in extracting data from corporations. Data would propogate from the API call, and we will then extract only the JSON component of the return call. This is then used to parse out information, based on the Stock Ticker, and Financial Year that is supplied to the call arguments. 

## Getting Started

### Dependencies

* Python 3.6+
* Pandas
* Requests
* Json
* Windows 10

### Installing

* You can install the latest version of Python by navigating to this link: https://www.python.org/
* For installing the required libraries for Python, execute these commands in a terminal:
    * pip install pandas
    * pip install requests
    * Json is included natively!

### Executing program

* Running the program can be done by opening up a terminal on your computer:
    * Navigate to the directory of the file
    * Run "**python Datathon-DataTest.py**"

* To make modifications, to track other stock tickers:
    * Open "**Datathon-DataTest.py**" with an IDE or Text Editor, and modify the "**listofstocks**" variable (line 55) with the tickers of stocks.
    * Disclaimer: Some stock tickers may not work with the API call as financialmodelingprep only supports stocks from the more popular exchanges.

* Subsequently, you can modify the output file name on "f" and "x.to_csv" (lines 65, and 66) to match your desired file name.

## Help

* If "**python Datathon-DataTest.py**" does not run properly try: "**python3 Datathon-DataTest.py**"
* If there are errors with importing the libraries, try these steps below:
    * Open a file explorer, navigate to the "**site-packages**", and copy the directory location
    * Open up the Environment Variables, and insert this into the **PATH**
    * You may also be missing the packages, which you can do by following "**Installing**" section above

## Version History

* 0.2
    * Various bug fixes and optimizations
    * Modified API call, and renamed output CSV file
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [inancialmodelingprep.com](https://financialmodelingprep.com/)