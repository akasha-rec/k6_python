# 메시지

# def show_message(unsend_messages):
#     """인사말 출력"""
#     for msg in msg_lst:
#         print(msg)

# show_message(unsend_messages)

#메시지 전송
unsend_messages= ["안녕", "잘가", "식사했어?"]
sent_messages = []
def show_messages(unsend_messages, sent_messages):
    """리스트 이동"""
    while unsend_messages: #보내기 전 메시지
        current_message = unsend_messages.pop() #마지막부터 1개씩 꺼내서
        print(f"현재 메시지: {current_message}")
        sent_messages.append(current_message) #리스트 이동

def finish_message(sent_messages): #보낸 메시지
    for sent_message in sent_messages:
        print(f"보낸 메시지 : {sent_message}")

show_messages(unsend_messages, sent_messages)
finish_message(sent_messages)


