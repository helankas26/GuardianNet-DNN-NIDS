from queue import Queue as ThreadQueue
from multiprocessing import Queue as MultiProcessingQueue, Process

from src.guardiannet.app.core.service import PacketCapturer, CICFlowMeter, AttacksPredictor


class NIDSEngine(Process):
    def __init__(self):
        super(NIDSEngine, self).__init__()

    def run(self):
        pcap_queue = ThreadQueue()
        csv_queue = MultiProcessingQueue()

        packetCapturer = PacketCapturer(pcap_queue)
        cicFlowMeter = CICFlowMeter(pcap_queue, csv_queue)
        attacksPredictor = AttacksPredictor(csv_queue)

        packetCapturer.start()
        cicFlowMeter.start()
        attacksPredictor.start()

        # packetCapturer.join()
        # cicFlowMeter.join()
        # attacksPredictor.join()
