from clickhouse_driver import Client
from trader import Trader
from Strategy_BoostVolume import Strategy_BoostVolume
from datetime import timedelta,datetime

def main():
    trader = Strategy_BoostVolume()
    
    for swap in swaps:
        table_name = swap.replace("-", "_").lower()
        query = f"SELECT * FROM {table_name} ORDER BY timestamp ASC"
        result = client.execute(query)
        print(f"Contents of {table_name} sorted by timestamp:")
        for row in result:
            timestamp, open_price, high_price, low_price, close_price, volume = row
            previous_time = timestamp - timedelta(hours=1)

            query_current = f"SELECT * FROM {table_name} WHERE timestamp = {previous_time}" 
            trader.update(timestamp, open_price, high_price, low_price, close_price, volume)
            print(trader)



