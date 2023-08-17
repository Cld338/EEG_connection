from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import multiprocessing as mp 
from openvibe_tool import *
from private_tool import *
from CSP import CSPFilter
import numpy as np
import time

def process_receive():
    while True:
        signal = lsl.receiveData()
        print("received")
        signal_ls.append(signal)


def process_classification():
    while True:
        print("process_classification running")
        time.sleep(0.0001)


lsl = LSL()
lsl.connect()
signal_ls = []

if __name__ == "__main__":
    p1 = mp.Process(target=process_receive, name="receiver", daemon=True)
    # print("Status: ", p.is_alive())
    p2 = mp.Process(target=process_classification, name="classifier", daemon=True)

    p1.start()
    p2.start()

    while True:
        print(len(signal_ls))


    # time.sleep(5)   # 메인 프로세스 3초 대기
    # p.kill()        # 서브 프로세스 종료
    # print("Status: ", p.is_alive())

    # p.join()        # 메인 프로세스는 서브 프로세스가 종료될 때까지 블록됨    
    # print("Status: ", p.is_alive())