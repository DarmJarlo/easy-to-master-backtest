# This is a self-made easy-to-master backtest for your trading.

I have good experience with using this backtest framework developed by myself. This design aims to facilitate the backtest by establishing an instance of "Trader" class, which will acquire the market data at every moment and make decisions according to trading strategy. 

## The main framework contains:  
### Data collection and storage in your own database
Depending on the exchange you are using, collect the data by using API or downloading directly

### Feed market data

Update market data at each moment in chronological order, including key metrics such as price, trading volume, and other relevant indicators. The base class includes critical market data members, while you can customize your own derived class including additional members specific to your strategy. Feed the market data according to the timestamp.

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

I am an experienced professional programmer and independent trading system developer. I have helped develop various trading robots based on machine learning or traditional indicators. I can also help build customized visualization systems, monitoring and messaging systems, and backtesting systems. If you need my help in these areas, you can contact me at huoxiaqu@yahoo.com



