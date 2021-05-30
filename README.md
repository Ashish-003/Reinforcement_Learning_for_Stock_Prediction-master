# Reinforcement_Learning_for_Stock_Prediction-master
This is the code for "Reinforcement Learning for Stock Prediction".Inspiration from Siraj Raval on Youtube
## Running the Code

To train the model, download a training and test csv files from [Yahoo! Finance](https://ca.finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC) into `data/`
```
mkdir models
python train.py ^GSPC 10 1000
```

Then when training finishes (minimum 200 episodes for results):
```
python evaluate.py ^GSPC_2011 model_ep1000
````
To fetch csv files 
run in the yahoo api directory
```
python3 main.py
```
