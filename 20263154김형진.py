
grades = {}

while True:
    print("\n== 성적 계산기 ==")
    print("1: 점수 넣기")
    print("2: 결과 보기")
    print("3: 종료하기")
    
    select = input("번호를 고르시오: ")
    
    if select == "1":
        subject = input("과목명: ")
        score_input = input("점수 (0~100): ")
      
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                grades[subject] = score
                print(subject + " " + str(score) + "점 저장됨!")
            else:
                print("점수는 0에서 100 사이로 입력하시오.")
        else:
            print("숫자로 입력하시오.")
            
    elif select == "2":
        if len(grades) == 0:
            print("저장된 점수가 없습니다.")
        else:
            print("\n--- 내 성적표 ---")
            total_sum = 0
            
            for sub in grades:
                print(sub + " : " + str(grades[sub]) + "점")
                total_sum = total_sum + grades[sub]
                
            avg = total_sum / len(grades)
            print("----------------")
            print("총점:", total_sum)
            print("평균:", round(avg, 2))
          
            if avg >= 90:
                print("이번 학기 목표 달성! (A학점)")
            elif avg >= 80:
                print("조금만 더 하면 A입니다! (B학점)")
            else:
                print("다음 학기에 더 열심히 합시다!")
  
          
            
    elif select == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("1, 2, 3 중에서 다시 고르시오.")
