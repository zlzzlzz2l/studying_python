class agePackage:
    def detail(self):
        print("24")
        
if __name__ == "__main__":
    print("agePackage 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때에만 실행된다.")
    name_to = agePackage()
    name_to.detail()
else:
    print("agePackage 외부에서 모듈 호출")