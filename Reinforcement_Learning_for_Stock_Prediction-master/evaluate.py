import keras
from keras.models import load_model
import time
from agent.agent import Agent
from functions import *
import sys
import numpy as np

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
e1_buy = []
e1_sell = []
e2_buy= []
e2_sell = []


if len(sys.argv) != 3:
	print ("Usage: python evaluate.py [stock] [model]")
	exit()
print("yolo")

stock_name, model_name = sys.argv[1], sys.argv[2]
print("aaya")
model = load_model("models/" + model_name)

window_size = model.layers[0].input.shape.as_list()[1]

agent = Agent(window_size, True, model_name)

data = getStockDataVec(stock_name)
print("yoooooooooo")
print(data)
l = len(data) - 1
batch_size = 32
print("lis " + str(l))

state = getState(data, 0, window_size + 1)
total_profit = 0
agent.inventory = []

# Setup our plot
fig, ax = plt.subplots()
timeseries_iter = 0
number = 0
credit = 0
#plt_data = []
t = 1
while(t<l):
	action = agent.act(state)

	# sit
	next_state = getState(data, t + 1, window_size + 1)
	reward = 0

	if action == 1: # buy
		agent.inventory.append(data[t])
		#plt_data.append((timeseries_iter, data[t], 'Buy'))
		print (str(t)+" Buy: " + formatPrice(data[t]))
		e1_buy.append(t)
		e2_buy.append(formatPrice(data[t]))
		number+=1
		credit +=(data[t])

	elif action == 2 and len(agent.inventory) > 0: # sell
		bought_price = agent.inventory.pop(0)
		reward = max(data[t] - bought_price, 0)
		total_profit += data[t] - bought_price
		#plt_data.append((timeseries_iter, data[t], 'Sell'))
		number -=1
		print (str(t)+" Sell: " + formatPrice(data[t]) + " | Profit: " + formatPrice(data[t] - bought_price))
		e1_sell.append(t)
		e2_sell.append(formatPrice(data[t]))
		credit -= (data[t])
	else:
		print(str(t))
	#timeseries_iter += 1
	
	done = True if t == l - 1 else False
	agent.memory.append((state, action, reward, next_state, done))
	state = next_state
	while(t == l-1):
		time.sleep(30)
		print("dafaq")
		data = getStockDataVec(stock_name)
		l = len(data) -1
		print("t is " + str(t)) 

 
	if done:
		print ("--------------------------------")
		print (stock_name + " Total Profit: " + formatPrice(total_profit))
		print ("--------------------------------")
		print("Stocks left : " + str(number))
		print("Money left : " + str(credit))
		plt.figure(figsize=(100,100))
		plt.plot([i for i in range(len(data))], data)
		plt.scatter(e1_buy, e2_buy, marker="^", color="g", label="buy")
		plt.scatter(e1_sell, e2_sell, marker="v", color="r", label="sell")
		plt.legend(loc="upper right")
		plt.xlabel("time")
		plt.ylabel("$ price")
		plt.savefig("EV" + ".png")
	
	if len(agent.memory) > batch_size:
			agent.expReplay(batch_size)
	t+=1 

#plt_data = np.array(plt_data)/
#ax.plot(plt_data[:, 0], plt_data[:, 1])
#Display our plots
#plt.show()


print("bye")

print("escaped")
exit()