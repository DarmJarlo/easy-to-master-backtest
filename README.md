# This is a self-made easy-to-master backtest for your trading

I have good experience with using this backtest framework developed by myself. And it‘s quite easy to adapt your own startegy to it. This design aims to simulate a trader by establishing an instance of "Trader" class, which will acquire the market data at every moment and make decisions according to trading strategy. 

## The main framework contains:  
### Data collection and storage in your own database
Depending on the exchange you are using, collect the data by using API or downloading directly

### Feed market data

Update market data at each moment in chronological order, includmming key metrics such as price, trading volume, and other relevant indicators. The base class includes critical market data members, while you can customize your own derived class including additional members specific to your strategy. Feed the market data according to the timestamp.

### Define entry and exit conditions
Based on the current market data, calculate indicators as per your strategy to determine entry and exit points for trades.

### Run the backtest in a loop
Execute the backtest by iterating through the data, simulating trades according to your strategy. Record each trade in a file, generate a report, and create graphs to illustrate profit and loss variations over time.

### Time delay mode
To account for potential time delays in real trading, here 3 kinds of methods to simulate the real trade price are considered

1. using the momentum to simulate real prices : real price = current price + momentum * assumed latency
2. the mid price of next second
3. the lowest/highest price of next second.

### About me

I am an experienced professional programmer and independent trading system developer. I have helped develop various trading robots based on machine learning or traditional indicators. I can also help build customized visualization systems, monitoring and messaging systems, and backtesting systems. If you need my work in these areas, you can contact me at huoxiaqu@yahoo.com

-------Chinese below-------------------------------------------------------------------------------------------------------

# 这是一个易于掌握的交易回测程序

这是个自己开发的傻瓜级回测框架，非常容易掌握，并且便于实施自己的策略，。此设计旨在通过建立“Trader”类的实例来模拟交易员，Trader将在每个时刻获取市场数据并根据交易策略做出决策。

## 主要框架包含：
### 数据收集和存储在您自己的数据库中
根据您使用的交易所，使用 API 或直接下载收集数据

### 提供市场数据

按时​​间顺序更新每个时刻的市场数据，包括价格、交易量和其他相关指标等关键指标。基类已经包括关键的市场数据成员，而您可以自定义自己的派生类，包括特定于您的策略的其他成员。根据时间戳提供市场数据。

### 定义进入和退出条件
根据当前市场数据，根据您的策略计算指标以确定交易的进入和退出点。

### 循环运行回测
通过遍历数据执行回测，根据您的策略模拟交易。将每笔交易记录在一个csv中，并生成报告，画图以说明利润和损失随时间的变化。

### 时间延迟模式
为了考虑实际交易中可能出现的时间延迟，这里考虑了 3 种模拟实际交易价格的方法

1. 使用动量模拟实际价格：实际价格 = 当前价格 + 动量 * 假设延迟
2. 下一时间粒度的中间价格
3. 下一时间粒度的最低/最高价格。

### 关于我

我是一名经验丰富的专业程序员和独立交易系统开发人员。我曾帮助开发过各种基于机器学习或传统指标的交易机器人。我还可以帮助构建定制的可视化系统、监控和消息传递系统以及回测系统。如果您需要我在这方面的工作，可以通过 huoxiaqu@yahoo.com 与我联系，依照工作量商议价格



