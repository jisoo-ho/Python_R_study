#번호, 제목, 작성자, 조회수 메인에 출력
#메뉴 선택 시 (글쓰기, 수정, 삭제, 조회, 종료) 중 선택
#글 번호 자동 주입
#조회시 조회수 추가

class Gesipan:
    def __init__(self, no, title, name, contents, hit):
        self.no = no
        self.title = title
        self.name = name
        self.contents = contents
        self.hit = hit

    def print_info(self):
        print(self.no,"\t\t", self.title,"\t", self.name,"\t", self.hit)

    def print_all(self):
        self.hit = int(self.hit)+1 # 5번 종료 후 글이 저장된 후 조회수 증가 가능
        print("글 번호 : " , self.no)
        print("글 제목 : " , self.title)
        print("글 작성자 : ", self.name)
        print("글 내용 : ",self.contents)
        print("글 조회수 : ",self.hit)
    
    def getHit(self):
        return self.hit
#------------ class gesipan : END--------------

#메인
def print_menu(gesipan_list):
    print("글 번호 \t 글 제목 \t 작성자 \t 조회수")
    print("--------------------------------------------------------")
    for i in range(1, len(gesipan_list)+1):
        gesipan_list[-i].print_info()
    print("--------------------------------------------------------")
    print("1. 글 작성")
    print("2. 글 조회")
    print("3. 글 삭제")
    print("4. 글 수정")
    print("5. 종료")
    menu = input("메뉴선택 : ")
    return int(menu)
# ------- def print_menu() : END ---------------

#글 번호부여
def setNo(gesipan_list):
    noList = []
    maxNo = 0
    for i in gesipan_list:
        noList.append(int(i.no))
    if len(noList) !=0:
        maxNo = max(noList)
    return maxNo
#-------def setNo() : END --------------

#데이터 입력받기
def set_gesipan(gesipan_list):
    title = input("글 제목 : ")
    name = input("작성자 : ")
    contents = input("글 내용 : ")
    no = setNo(gesipan_list)+1
    hit = 0
    gesipan = Gesipan(no, title, name, contents, hit)
    return gesipan
# ---------def set_gesipan() : END -------------

#글 내용 출력하기
def print_gesipan(gesipan_list, no):
    for i, gesipan in enumerate(gesipan_list):
        if gesipan.no == no:
            gesipan_list[i].print_all()
#-----------def print_gesipan() : END ---------

#글 수정(수정하려면 5번으로 종료한번해서 저장하고 다시 실행해야한다.)
def mod_gesipan(gesipan_list, no):
    title = input("수정할 제목 : ")
    name = input("수정할 이름 : ")
    contents = input("수정할 내용 : ")

    for i, gesipan in enumerate(gesipan_list):
        if gesipan.no == no:
            gesipan_list[i].__init__(no, title, name, contents, hit=gesipan_list[0].getHit())
#------------def mod_gesipan() : END ----------

#글 삭제하기(한번 종료해서 저장 후에 삭제할 수 있다.)
def delete_gesipan(gesipan_list, no):
    for i, gesipan in enumerate(gesipan_list):
        if gesipan.no == no:
            del gesipan_list[i]
#-----------def delete_gesipan() : END -----------------

#게시판 파일로 만들기
def store_gesipan(gesipan_list):
    f = open("gesipan_db.txt", "wt")
    for gesipan in gesipan_list:
        f.write(str(gesipan.no) + "\n")
        f.write(gesipan.title + "\n")
        f.write(gesipan.name + "\n")
        f.write(gesipan.contents + "\n")
        f.write(str(gesipan.hit) + "\n")
    f.close()
# ----------- store_gesipan END --------------------

#글 불러들이기
def load_gesipan(gesipan_list):
    try:
        f = open("gesipan_db.txt", "rt")
        lines = f.readlines()
        num = len(lines)/5 
        num = int(num)     

        for i in range(num):
            no = lines[5*i].rstrip("\n")
            title = lines[5*i+1].rstrip("\n") # rstrip('\n') : 맨 오른쪽 '\n'을 제거
            name = lines[5*i+2].rstrip('\n') # lstrip('\n') : 맨 왼쪽 '\n' 을 제거
            contents = lines[5*i+3].rstrip('\n') # strip('\n') : 양쪽 끝의 '\n'을 제거
            hit = lines[5*i+4].rstrip('\n')
            gesipan = Gesipan(no, title, name, contents, hit)
            gesipan_list.append(gesipan)
        f.close()
    except FileNotFoundError:
        pass
#----------- load_gesipan END --------------------


#모듈 자체 테스트 시, 호출할 함수
def run():
    gesipan_list = []
    load_gesipan(gesipan_list)
    while 1:
        menu = print_menu(gesipan_list)
        # 1. 글 쓰기
        if menu == 1:
            gesipan = set_gesipan(gesipan_list)
            gesipan_list.append(gesipan)

        # 2. 글 조회
        elif menu == 2:
            no = input("번호입력 : ")
            print_gesipan(gesipan_list,no)

        # 3. 글 삭제
        elif menu == 3:
            no = input("번호입력 : ")
            delete_gesipan(gesipan_list, no)

        # 4. 글 수정
        elif menu == 4:
            no = input("번호입력 : ")
            mod_gesipan(gesipan_list, no)

        # 5. 종료
        elif menu == 5:
            store_gesipan(gesipan_list)
            break


if __name__ == "__main__":
    run()
# -------------- if __name__ END -----------------