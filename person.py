class Person:
    count = 0
    def __init__(self, name, age, address):
        self.name = name #인스턴스 변수
        self.age = age
        self.address = address
        self.weight = [65, 70, 75, 78]
        self.height = 170
        print("{} 객체가 생성됨".format(self.name))
        Person.count += 1 #클래스 변수의 증가

    @classmethod ###decorator
    def printing(cls):
        print("객체 수는 {}".format(cls.count))

    def __len__(self):
        return len(self.weight)

    def __str__(self): #Person 객체 출력 시 필요
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    

    def __eq__(self, other):
        return self.address == other.address
    
    #클래스의 객체도 호출하게 만들어주는 메서드
    # def __call__(self): #머신러닝, 딥러닝
    #     return self.weight / self.height**2

    def __getitem__(self, indx):
        return self.weight[indx]
    
    # def __del__(self):
    #     print("객체 {}이 소멸됨.".format(self.name))

#가리키는 대상이 없어서 붕 떠있어 > 바로 삭제
Person("guest", 11, "jeju") 
new_person = Person("lee", 20, "Busan") #new_person 참조변수 > 다 쓰이고 소멸
other_person = Person("kim", 30, "Busan")

Person.printing() ##클래스 메서드 호출
new_person.printing()

print(f"person 객체의 나이는 {new_person.age:5}") #최소너비 지정 > 예) 두자릿수라면 3칸 띄우고 입력됨
print("객체의 타입은 {}".format(isinstance(new_person, Person)))
print(new_person == other_person) #return true or false

print(f"현재 체중은 {new_person[2]}")
print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision))

print(new_person.__str__())
print(str(new_person))
# print(new_person) : print함수는 string을 요구하므로 자동적으로 __str__ 호출해서 출력O
# print(f"체질량 지수는 {new_person()}") ##__call__

my_list = [1, 2, 3, 4]
print(len(my_list))
print(f"{Person.count} 객체가 생성됨")
print(f"{other_person.count} 객체가 생성됨")
