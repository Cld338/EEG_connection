from local_libs.openvibe_tool import *
from local_libs.private_tool import *

lsl = LSL()
lsl.connect()
while True:
    print(lsl.receiveData())