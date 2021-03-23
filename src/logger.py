import datetime

# System Logger
def write_system_log(log_message) :
    stream_system_log = open("log/system_log.txt", 'a')

    log_refined = f"{datetime.datetime.now()}\t{log_message}\n"
    stream_system_log.write(log_refined)

    print("Log\t", log_refined, end='')

    stream_system_log.close()

# Trade Logger
def write_trade_log(log_message) :
    stream_trade_log = open("log/trade_log", 'a')

    log_refined = f"{datetime.datetime.now()}\t{log_message}\n"
    stream_trade_log.write(log_refined)

    print("Log\t", log_refined, end='')

    stream_trade_log.close()

