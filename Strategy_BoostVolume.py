class Strategy_BoostVolume(Trader):
    def should_enter(self, kline):
        # 另一种入场逻辑
        pass

    def should_exit(self, kline, stop_loss):
        # 另一种出场逻辑
        pass

    def set_stop_loss(self, kline):
        # 另一种止损逻辑
        pass