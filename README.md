# Description

---

### KETI 와 함께 출전했던 K-사이버 시큐리티 챌린지에서 사용한 코드입니다.



### attack generator

* 공격 데이터 주입 코드입니다. Kviser api 를 사용하여 만들었습니다.

* python 코드로 작성되었습니다.

> ### 시나리오 3
>
> 계기판 내 모든 경고등 점등 공격
>
> 초기요청상태(우리공격전주최측에요청할셋팅):기어 단수P or N
>
> 초기상황(시나리오상 필요한 상황 가정) : 도로 위 주행 상
>
> 미션을 D 단으로 체결 후 RPM 값을 올리며 주행 상황을 만든다. TODO: 2ms 원래 20ms 10까지는 어느정도 가능
>
> 이때, 시동이 곧 꺼진다는 문구가 등장하게 되면서 카운트 다운을 시작하고(실제 카운트 다운 가능)
>
> 시동이 꺼졌다는 화면(실제 시동이 꺼졌다는 화면 점등 가능)을 점등시킨다. TODO: 시동꺼짐 알림 원래(200)은 10 기어는 1 단위로 줄 수 있으면 좋다.
>
> 운전자는 비상등을 켜고 차량을 세우려고 할 것이다. (이때, 주최측에 깜빡이를 켜달라고 요청) TODO: 비상등 깜빡이 5ms
>
>  공격팀은 비상등이 들어오지 않도록 OFF 신호를 지속적으로 주입하여 비상등을 켤 수 없게 한다.
>
> 이때, 차량의 근접 및 안전 관련 센서들이 에러 또는 종료된다는 경고등을 반복적으로 주입하여,

> ### 공격 시나리오 4
>
> 조도 센서기반의 라이트 마비 공격 (물리적 공격 포함)
>
> 초기요청상태(우리공격전주최측에요청할셋팅):기어단수 P or N,라이트 모드 ON
>
> 초기상황(시나리오상 필요한 상황 가정) : 어두운 골목길 주행 상황
>
> 라이트가 켜진 상태에서 주행하는 차량에 짧은 주기로 라이트가 깜빡이는 공격을 주입한다.
>
> 이때, 운전자는 라이트에 문제가 생겼다는 점을 인지하고 라이트를 조작하려하지만, 우리가 정해놓은 라이트 모드
>
> 가 유지되도록 공격을 지속적으로 주입하여 손 쓸수 없도록 만든다.
>
> 어두운 길에서 라이트가 비정상적으로 작동하면 운전자의 시야 확보에 문제가 생기며 마주보고 오는 운전자의 시야또한 방해할 수 있는 공격이다.
>
> 운전자가 외부의 환경으로부터 보호받지 못하고 침착한 대응을 할 수 없도록 공격을 주입한다.



### Data argumentation

* 학습데이터 증강 코드입니다.
* 주피터 노트북으로 작성되었습니다.
* 10진수 인코딩 파일의 경우 CAN-ID 의 16진수를 10진수로 학습하기 위해 제작되었습니다.



