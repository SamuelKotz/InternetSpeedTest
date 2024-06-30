import speedtest


def test():
    speed = speedtest.Speedtest()
    download = '{:.2f}'.format(speed.download() / 1024 / 1024)
    upload = '{:.2f}'.format(speed.upload() / 1024 / 1024)

