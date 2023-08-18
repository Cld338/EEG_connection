from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import multiprocessing as mp 
from openvibe_tool import *
from private_tool import *
from CSP import CSPFilter
import numpy as np
import time

def process_receive():
    n_trials = 0
    while True:
        signal = lsl.receiveData()
        # print("received")
        signal_ls.append(signal)
        n_trials += 1
        print(len(signal_ls))


def process_classification():
    while True:
        print("process_classification running")
        time.sleep(1)


lsl = LSL()
lsl.connect()
processManager = mp.Manager()
signal_ls = processManager.list()

windowWidth = 256
windowOverlap = round(windowWidth*0.5)

if __name__ == "__main__":
    mp.freeze_support()
    p1 = mp.Process(target=process_receive, name="receiver")
    # print("Status: ", p.is_alive())
    p2 = mp.Process(target=process_classification, name="classifier")
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()


    # time.sleep(5)   # 메인 프로세스 3초 대기
    # p.kill()        # 서브 프로세스 종료
    # print("Status: ", p.is_alive())

    # p.join()        # 메인 프로세스는 서브 프로세스가 종료될 때까지 블록됨    
    # print("Status: ", p.is_alive())