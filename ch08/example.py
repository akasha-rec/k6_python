# 메시지

def show_messages(messages):
    """인사말 출력"""
    for message in messages:
        print(message)

# messages= ["안녕", "잘가", "식사했어?"]
# show_messages(messages)

#메시지 전송

def send_messages(messages, sent_messages):
    """리스트 이동"""
    print("\n모든 메시지 보내는 중")
    while messages: #보내기 전 메시지
        current_message = messages.pop() #마지막부터 1개씩 꺼내서
        print(current_message)
        sent_messages.append(current_message) #리스트 이동

messages= ["안녕", "잘가", "식사했어?"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)
# send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

#샌드위치 만들기
def make_sandwich(*items): #가변위치인수. 튜플 형태로 전달
    """주문받은 샌드위치 만들기"""
    print("\n 주문 받았습니다.")
    for item in items:
        print(f"주문하신 {item}을 샌드위치에 넣어드리겠습니다.")
    print("완성됐습니다.")

make_sandwich("햄", "양상추", "피클", "랜치 소스")
make_sandwich("스크램블 에그", "토마토", "양배추")
make_sandwich("베이컨", "양상추 많이")

#사용자 프로필 #** > 가변키워드 인수. 딕셔너리 형태로 전달
def build_profile(first, last, **user_info):
    """사용자 정보를 딕셔너리로 저장"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    user_info["배우고 있는 것"] = "파이썬"
    user_info["좋아하는 것"] = "책"
    user_info["싫어하는 것"] = "해산물"
    return user_info

user_profile = build_profile("이름", "성")
print(user_profile)

# 자동차
def make_car(factory, model, **options):
    """자동차 정보를 딕셔너리에 저장하기"""
    car_dict = {
        "factory" : factory.title(),
        "model" : model.title(),
    } #options.items() : 모든 키-값 쌍을 반환하는 메서드
    for option, value in options.items():
        car_dict[option] = value #car_dict[]에 키-값쌍을 넣는 것

    return car_dict

car = make_car("subaru", "outback", color = "blue", two_package=True)
print(car)