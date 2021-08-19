ALPHA_VANTAGE_API_KEY = 'FYZYKB0Z8EV8YL69'
TELEGRAM_API_KEY = '1813854902:AAHdpcHSAuElxu3HskhPXaPftNVDGrQxBVM'

__developer_mode = False

__bot_name = 'Dot Coin Bot'
__telegrm_interval = 10

if not __developer_mode:
    telegram_hour = __telegrm_interval * 60
else:
    telegram_hour = 310

ticker = 'DOT'
time_frames = {'1': '1min', '5': '5min', '15': '15min',
               '30': '30min', '60': '60min'}  # bars
selected_tf = '5min'

notify_when_there_is_no_signal = True


# telegram bot mesajlari
start_message = (f"Merhaba, {__bot_name} botuna hoş geldiniz. Bu bot ile belirlediğiniz mum preiyotları ile {ticker} / USD üzerinden her {__telegrm_interval} dakikada bir 10 günlük ortalamaya ne kadar yaklaşıldığını öğrenebilirsiniz."
                 "Dilerserniz /stop yazarak bu botu durdurabilirsiniz."
                 )

help_message = ("/help: Komut listesi \n"
                "/start botu başlatır \n"
                "/stop botu durdur \n"
                )

stop_message = "Bot durduruldu."
off_message = "Bot zaten kapalı."

get_ticker_message = "Ticker: "

non = 'Sinyal tespit edilemedi'
