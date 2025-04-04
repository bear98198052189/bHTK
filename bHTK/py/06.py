class User:
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공 환영합니다")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

    def __str__(self):
        return f"사용자: {self.name}, 이메일 {self.email}"
            
user1 = User("임정훈","imjeonghun642@gmail.com", "asdhq1w")
user2 = User("강태훈","gantaehun624@gmail.com","qhbw312bg")

print(user1)
print(user2)