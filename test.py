from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from openvibe_tool import *
from private_tool import *
from CSP import CSPFilter
import numpy as np
    
lsl = LSL()
lsl.connect()
signal_ls = []

while True:
    print(1)
    # signal1, t1 = lsl.collectDataByTime(5000)
    # signal2, t2 = lsl.collectDataByTime(5000)
    # signal3, t3 = lsl.collectDataByTime(5000)
    # signal = lsl.receiveData()
    # print(signal)
    print(lsl.inlet)
    # amp, freq = fft(signal1, t1)
    break
    # print(1)
    # print(signal1)
    # csp = CSPFilter(signal1, signal2, signal3)
    # csp = CSPFilter(*[[lsl.collectDataByTime(1000)[0] for _ in range(3)] for _ in range(3)])
    # covariance matrix 구하는 과정에서 오류 생김
    # 리스트 차원이 모자르는 듯
    # print(s_fft)
    # print(len(s_fft[0]), len(s_fft[1]))
    # print(csp)
    # break
    
    # 기본 실습에 사용할 간단한 가상 데이터

    X = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])
    y = np.array([1,1,1,2,2,2])
    # 기본적인 LDA 구현

    clf = LinearDiscriminantAnalysis()
    clf.fit(X,y)