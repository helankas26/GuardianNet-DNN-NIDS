from multiprocessing import Process, Queue

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model


class AttacksPredictor(Process):
    def __init__(self, csv_queue):
        super(AttacksPredictor, self).__init__()
        self.model = load_model("model/DNN_Model_nids.h5")
        self.csv_queue = csv_queue
        self.dataset = None
        self.selectedDataFrame = None
        self.prediction_queue = Queue()

    def run(self):
        filename = self.csv_queue.get()

        while filename is not None:
            self.__loadDataset(filename)
            predictions = self.__predict()
            self.prediction_queue.put(predictions)

            filename = self.csv_queue.get()

    def __predict(self):
        predictionsResult = []

        self.__preprocessing()

        dataToPredict = self.selectedDataFrame.iloc[:, :].values
        predictions = self.model.predict(dataToPredict)

        for prediction in predictions:
            predictionsResult.append(np.argmax(prediction))

        return predictionsResult

    def __loadDataset(self, filename):
        filepath = f"../../../../temp/csv/{filename}.pcap_Flow.csv"
        self.dataset = pd.read_csv(filepath)

    def __preprocessing(self):
        self.__selectFeature()
        self.__replaceInfiniteValuesNaN()
        self.__scaleData()

    def __selectFeature(self):
        colsToSelect = ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
                        'Total Length of Fwd Packets', 'Total Length of Bwd Packets',
                        'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Fwd Packet Length Mean',
                        'Fwd Packet Length Std', 'Bwd Packet Length Max', 'Bwd Packet Length Min',
                        'Bwd Packet Length Mean', 'Bwd Packet Length Std', 'Flow Bytes/s',
                        'Flow Packets/s', 'Flow IAT Mean', 'Flow IAT Std', 'Flow IAT Max',
                        'Flow IAT Min', 'Fwd IAT Total', 'Fwd IAT Mean', 'Fwd IAT Std',
                        'Fwd IAT Max', 'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean',
                        'Bwd IAT Std', 'Bwd IAT Max', 'Bwd IAT Min', 'Fwd Header Length',
                        'Bwd Header Length', 'Fwd Packets/s', 'Bwd Packets/s',
                        'Min Packet Length', 'Max Packet Length', 'Packet Length Mean',
                        'Packet Length Std', 'Packet Length Variance', 'Average Packet Size',
                        'Avg Fwd Segment Size', 'Avg Bwd Segment Size', 'Subflow Fwd Packets',
                        'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes',
                        'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd',
                        'min_seg_size_forward', 'Active Mean', 'Active Std', 'Active Max',
                        'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min']

        self.dataset.columns = self.dataset.columns.str.strip()

        missingCols = [col for col in colsToSelect if col not in self.dataset.columns]
        if missingCols:
            raise ValueError(f"Missing columns in the dataset: {missingCols}")

        self.selectedDataFrame = self.dataset[colsToSelect].copy()

    def __replaceInfiniteValuesNaN(self):
        self.selectedDataFrame.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.selectedDataFrame.fillna(0, inplace=True)

    def __scaleData(self):
        scaler = MinMaxScaler()
        self.selectedDataFrame = pd.DataFrame(scaler.fit_transform(self.selectedDataFrame), columns=self.selectedDataFrame.columns)
