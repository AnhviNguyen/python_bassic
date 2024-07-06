import random
import sys
from enum import Enum

class RBS(Enum):
    BÚA = 2
    BAO = 3
    kÉO = 1

# print(RBS(1))
# print(RBS.BAO)

playerChoice = input("Bạn hãy chọn \n 1. Kéo \n 2. Búa \n 3. Bao \n")
player = int(playerChoice)

if (player <1 or player >3):
    print("Bạn đã chọn sai, vui lòng chọn lại")
    sys.exit()

computer = random.randint(1, 3)
print("Bạn chọn: ", RBS(player).name)
print("Máy tính chọn: ",RBS(computer).name)
if player == 1 and computer == 3 or player ==2 and computer == 1 or player == 3 and computer == 2 :
    print("Bạn thắng")
# elif player == 1 and computer == 2 or player ==2 and computer ==3 or player ==3 and computer == 1:
elif player == computer:
    print("Bạn hòa")
else:
    print("Bạn thua")