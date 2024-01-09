import os

from scapy.utils import wrpcap, rdpcap


class PcapHandler:
    @staticmethod
    def savePackets(packets, filename):
        filepath = f"../../../temp/pcap/{filename}.pcap"
        wrpcap(filepath, packets)

    @staticmethod
    def loadPackets(filename):
        filepath = f"../../../temp/pcap/{filename}.pcap"
        return rdpcap(filepath)

    @staticmethod
    def deletePackets(filename):
        filepath = f"../../../../temp/pcap/{filename}.pcap"
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
            except OSError as e:
                print(f"Error: {filepath} - {e}")
