from datetime import datetime
from threading import Thread

from scapy.sendrecv import sniff

from src.guardiannet.app.core.util import PcapHandler
from src.guardiannet.app.util import ConfigurationManager


class PacketCapturer(Thread):
    def __init__(self, pcap_queue):
        super(PacketCapturer, self).__init__()
        self.pcap_queue = pcap_queue

    def run(self):
        while True:
            packets = self.__capture()
            filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            PcapHandler.savePackets(packets, filename)
            self.pcap_queue.put(filename)

    @staticmethod
    def __capture():
        config = ConfigurationManager.loadConfiguration()
        count = config.get('setting').get('batchSize')
        iface = config.get('setting').get('iface')

        if iface is None:
            return sniff(count=count, store=True)
        else:
            return sniff(iface=iface, count=count, store=True)
