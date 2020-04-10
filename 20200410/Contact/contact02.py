class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name : ", self.name)
        print("Phone Number : ", self.phone_number)
        print("E-mail : ", self.e_mail)
        print("Address : ", self.addr)
#------------ class Contact : END--------------


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택 : ")
    return int(menu)
# ------- def print_menu() : END ---------------

#사용자로부터 데이터 입력받기
def set_contact():
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E-mail : ")
    addr = input("Address : ")
#   2단계 : print(name, phone_number, e_mail, addr)
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
# ---------def set_contact() : END -------------

#연락처 출력하기
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()
#-----------def print_contact() : END -----------------


#연락처 삭제하기
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]
#-----------def delete_contact() : END -----------------

#연락처 파일로 만들기
def store_contact(contact_list):
    f = open("C:/rStudy/20200410/Contact/contact_db.txt", "wt")

    for contact in contact_list:
        f.write(contact.name + "\n")
        f.write(contact.phone_number + "\n")
        f.write(contact.e_mail + "\n")
        f.write(contact.addr + "\n")
    f.close()
# ----------- store_contact END --------------------

#연락처 불러들이기
def load_contact(contact_list):
    f = open("C:/rStudy/20200410/Contact/contact_db.txt", "rt")
    # 파일에서 읽어들인 전체 라인 수를 4로 나누어, 몇 개의 데이터가 존재하는지 확인
    lines = f.readlines()
    num = len(lines)/4 # 나눗셈 연산을 수행하면 num 값이 실수가 되는데,
    num = int(num)     # 이 값을 int() 내장 함수를 사용해 정수형으로 형 변환

    for i in range(num):
        name = lines[4*i].rstrip("\n") # rstrip('\n') : 맨 오른쪽 '\n'을 제거
        phone = lines[4*i+1].rstrip('\n') # lstrip('\n') : 맨 왼쪽 '\n' 을 제거
        email = lines[4*i+2].rstrip('\n') # strip('\n') : 양쪽 끝의 '\n'을 제거
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()
#----------- load_contact END --------------------


#모듈 자체 테스트 시, 호출할 함수
def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        # 1. 연락처 입력 선택
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        # 2. 연락처 출력
        elif menu == 2:
            print_contact(contact_list)

        # 3. 연락처 삭제
        elif menu == 3:
            name = input("Name : ")
            delete_contact(contact_list, name)

        # 4. 종료
        elif menu == 4:
            store_contact(contact_list)
            break
# 3단계 : while 1:
# 3단계 :      menu = print_menu()
# 3단계 :      if menu == 4:
# 3단계 :          break
#    2단계 : set_contact()
#    1단계 : kim = Contact("김일구", "010-8812-1193", "ilgu@python.com", "Seoul")
#    1단계 : kim.print_info()
# ---------------def run() : END --------------------


if __name__ == "__main__":
    run()
# -------------- if __name__ END -----------------
