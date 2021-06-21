# Yahoo Finance Python API


This api supports **Intraday Data** upto 1 minute granularity which a lots of free api doesn't support

## Usage

This command returns a dataframe which can be further modified to add new columns , exported to excel etc

``` python
tata_power = YahooFinance('TATAPOWER.NS', result_range='1mo', interval='15m', dropna='True').result
```

## Installation

``` bash
git clone https://github.com/Ashish-003/Reinforcement_Learning_for_Stock_Prediction-master.git
cd yahoo_finance_api
python setup.py install
```

### Requirements

- Pandas
- Request

### Note

Make sure to use TICKER symbol from yahoo finance website
https://in.finance.yahoo.com/ 
