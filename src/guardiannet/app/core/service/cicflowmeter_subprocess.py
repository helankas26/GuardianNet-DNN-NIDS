import os
import platform
import subprocess
from threading import Thread


class CICFlowMeter(Thread):
    def __init__(self, pcap_queue, csv_queue):
        super(CICFlowMeter, self).__init__()
        self.pcap_queue = pcap_queue
        self.csv_queue = csv_queue

    def run(self):
        filename = self.pcap_queue.get()

        while filename is not None:
            self.__convertPcapToCsv(filename)

            filepath = f"../../../temp/csv/{filename}.pcap_Flow.csv"
            if os.path.exists(filepath):
                self.csv_queue.put(filename)

            filename = self.pcap_queue.get()

    @staticmethod
    def __convertPcapToCsv(filename):
        outputDir = f"../../../temp/csv/"
        filepath = f"../../../temp/pcap/{filename}.pcap"
        command = None

        try:
            operating_system = platform.system()

            if operating_system == 'Windows':
                command = f"core\\util\\cicflowmeterutil\\bin\\cfm.bat {filepath} {outputDir}"
            elif operating_system == 'Linux':
                command = f".core/util/cicflowmeterutil/bin/cfm {filepath} {outputDir}"

            subprocess.run(command, check=True, shell=True, text=True)

        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with error code {e.returncode}.")
            print("Error:", e.stderr)
        except Exception as e:
            print("An error occurred:", e)
