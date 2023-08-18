from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from local_libs.openvibe_tool import *
from local_libs.private_tool import *
from local_libs.CSP import CSPFilter
import numpy as np


def process_receive():
    while flag:
        signal = lsl.receiveData()
        print(signal)
        signal_ls.append(signal)

def process_classification():
    while flag:
        return


lsl = LSL()
lsl.connect()
signal_ls = []

flag = True

# while True:
    # signal1, t1 = lsl.collectDataByTime(5000)
    # signal2, t2 = lsl.collectDataByTime(5000)
    # signal3, t3 = lsl.collectDataByTime(5000)
    
    # print(lsl.inlet)
    # amp, freq = fft(signal1, t1)
    # break
    # print(1)
    # print(signal1)
    # csp = CSPFilter(signal1, signal2, signal3)
    # csp = CSPFilter(*[[lsl.collectDataByTime(1000)[0] for _ in range(3)] for _ in range(3)])
    # covariance matrix 구하는 과정에서 오류 생김
    # 리스트 차원이 모자르는 듯
    # print(s_fft)
    # print(len(s_fft[0]), len(s_fft[1]))
    # print(csp)