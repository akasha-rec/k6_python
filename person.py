class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.weight = 70
        self.height = 170
        self.__vision = 1.0 #private 속성
    
    def __len__(self):
        return len(self.weight)

    def __str__(self): #Person 객체 출력 시 필요
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    

    def __eq__(self, other):
        return self.address == other.address
    
    #클래스의 객체도 호출하게 만들어주는 메서드
    def __call__(self): #머신러닝, 딥러닝
        return self.weight / self.height**2

    # def show_person_vision(self):
    #     print("시력은 {}".format(self.__vision))
new_person = Person("lee", 20, "Busan")
other_person = Person("kim", 30, "Busan")
print(new_person == other_person) #return true or false

print(f"체질량 지수는 {new_person()}") ##__call__

print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision))

#private 속성이라서 출력/변경 > 함수 만들어서
# new_person.show_person_vision()

print(new_person.__str__())
print(str(new_person))
# print(new_person) : print함수는 string을 요구하므로 자동적으로 __str__ 호출해서 출력O

my_list = [1, 2, 3, 4]
print(len(my_list))