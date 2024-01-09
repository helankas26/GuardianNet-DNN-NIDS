import sys
import time
from collections import Counter
from threading import Thread

from PyQt6.QtWidgets import QApplication

from src.guardiannet.app.controller import Alert
from src.guardiannet.app.core.util import PcapHandler, CsvHandler


class DetectionNotifier(Thread):
    def __init__(self, prediction_queue, filename_queue):
        super(DetectionNotifier, self).__init__()
        self.prediction_queue = prediction_queue
        self.filename_queue = filename_queue
        self.lastAlertTime = {}
        self.suppressionTime = 60
        self.labelMapping = {
            0: "BENIGN",
            1: "Bot",
            2: "DDoS",
            3: "DoS GoldenEye",
            4: "DoS Hulk",
            5: "DoS Slowhttptest",
            6: "DoS slowloris",
            7: "FTP-Patator",
            8: "PortScan",
            9: "SSH-Patator"
        }

    def run(self):
        predictions = self.prediction_queue.get()
        filename = self.filename_queue.get()

        while predictions is not None:
            higherCountAttack = self.__getAttackType(predictions)

            if higherCountAttack == 0:
                predictions = self.prediction_queue.get()
                continue

            attackLabel = self.__getAttackLabel(higherCountAttack)
            self.__triggerAlert(higherCountAttack, attackLabel)

            predictions = self.prediction_queue.get()

            PcapHandler.deletePackets(filename)
            CsvHandler.deleteCsv(filename)

            filename = self.filename_queue.get()

    @staticmethod
    def __getAttackType(predictions):
        attackGroup = Counter(predictions)

        return max(attackGroup, key=attackGroup.get)

    def __getAttackLabel(self, attack):
        return self.labelMapping.get(attack, None)

    def __triggerAlert(self, higherCountAttack, attackLabel):
        currentTime = time.time()

        if higherCountAttack in self.lastAlertTime and (currentTime - self.lastAlertTime[higherCountAttack]) < self.suppressionTime:
            return
        else:
            self.lastAlertTime[higherCountAttack] = currentTime
            app = QApplication(sys.argv)
            alert = Alert()
            alert.ui.lblAttcak.setText(attackLabel)
            sys.exit(app.exec())


