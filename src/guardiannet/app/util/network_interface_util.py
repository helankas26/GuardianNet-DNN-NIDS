import psutil


class NetworkInterfaceUtil:
    @staticmethod
    def getNetworkInterfaces():
        return list(psutil.net_if_addrs().keys())
