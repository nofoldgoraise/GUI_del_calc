from tkinter import * # tkinter 라이브러리 함수 전체 호출

window = Tk() # 창 생성

calc_output_text = f"""실 운행시간: 시간
지출: 원
건 수: 건
매 출: 원
시간당 건 수: 건
평균 단가: 원
순수익: 원"""

# 변수 설정
double_bars = "=" * 20

result_text = ""


# 함수 설정
def all_calc(event = None): # 계산 버튼 함수
  try:
    global result_text
    working_time = int(work_time_entry.get()) # 총 운행시간
    resting_time = int(rest_time_entry.get()) # 총 휴식시간
    real_total_time = working_time - resting_time # 실 운행시간
    
    today_oil = int(oil_price_entry.get()) # 기름값
    today_food = int(food_price_entry.get()) # 식비
    today_pay = today_oil + today_food # 총 지출 (기름값 + 식비)
    
    today_count = int(delivery_count_entry.get()) # 건 수
    
    today_price = int(total_cash_entry.get()) # 매 출
    
    avr_count = f"{today_count / real_total_time:.1f}" # 시간당 건 수 (건 수 / 실운행시간 = 소수점 1번째 까지 출력)
    
    avr_price = today_price // today_count # 평균 단가 (매출 // 건수 = 몫만 출력)
    
    get_money = today_price - today_pay # 순수익 (매 출 - 지 출)
    
    result_text = f"""실 운행시간: {real_total_time}시간
지출: {today_pay:,}원
건 수: {today_count}건
매 출: {today_price:,}원
시간당 건 수: {avr_count}건
평균 단가: {avr_price:,}원
★순 수익: {get_money:,}원"""
    calc_output_label.config(text = result_text)
    calc_reset()
    work_time_entry.focus()
    
  except (ZeroDivisionError, ValueError): # 문자입력, 계산안됨, 공백 등 오류발생시 결과Label에 오류문구 출력.
    calc_output_label.config(text = "[오류] 잘못 입력하셨습니다!")
    
def calc_reset(): # 계산 버튼 누르면 입력창 초기화 함수
  work_time_entry.delete(0, "end") # 운행시간 입력창 초기화
  rest_time_entry.delete(0, "end") # 휴식시간 입력창 초기화
  oil_price_entry.delete(0, "end") # 기름값 입력창 초기화
  food_price_entry.delete(0, "end") # 식비 입력창 초기화
  total_cash_entry.delete(0, "end") # 매출 입력창 초기화
  delivery_count_entry.delete(0, "end") # 건수 입력창 초기화  

def input_reset(): # 초기화 버튼 함수 (결과 Label 초기화)
  result_text = """실 운행시간: 시간
지출: 원
건 수: 건
매 출: 원
시간당 건 수: 건
평균 단가: 원
순 수익: 원"""
  calc_output_label.config(text = result_text) # 결과 출력창 초기화
  
def user_exit(): # 종료 버튼 함수
  window.destroy()
  
def make_label(label_text, label_font, label_color):
  label = Label(window) # Label 생성 함수
  label.config(text = label_text, font = label_font, bg = label_color)
  label.pack() # Label 배치
  return label
  
def make_entry(): # 입력창 생성 함수
  entry = Entry(window) # 입력창 생성
  entry.pack() # 입력창 배치
  return entry

def make_btn(text, color, str_font, cmd): # 버튼 만들기 함수
  btn = Button(window) # 버튼 생성
  btn.config(text = text, bg = color, font = str_font, command = cmd)
  btn.pack() # 버튼 배치
  
def save_txt(): # 파일 저장 함수
  file_name = save_entry.get() # 파일명 입력값 가져오기
  f = open(f"{file_name}.txt", "a") # 입력값에따른 파일명 새로만들기 or 이어쓰기 실행
  f.write(result_text + f"\n{double_bars}\n")
  f.close()

# 창 설정
window.title("GUI 배달 일당 계산기") # 창 제목
window.geometry("600x750") # 창 크기
window.config(bg = "gray") # 창 배경색
window.option_add("*font", "나눔고딕 20")

# Label 설정 (프로그램 제목)
program_name = Label(window) # Label 설정 (프로그램 제목)
program_name.config(text = "★ GUI 배달 일당 계산기 ★")
program_name.pack() # Label 배치 (프로그램 제목)

# Label, 입력창 함수 호출 변수
work_time_label = make_label("총 운행시간(시간)", ("궁서", 15), "orange") # Label 생성
work_time_entry = make_entry() # 입력창 생성

rest_time_label = make_label("총 휴식시간(시간)", ("궁서", 15), "orange") # Label 생성
rest_time_entry = make_entry() # 입력창 생성

oil_price_label = make_label("기름값", ("궁서", 15), "orange") # Label 생성
oil_price_entry = make_entry() # 입력창 생성

food_price_label = make_label("식비", ("궁서", 15), "orange") # Label 생성
food_price_entry = make_entry() # 입력창 생성

total_cash_label = make_label("매출", ("궁서", 15), "orange") # Label 생성
total_cash_entry = make_entry() # 입력창 생성

delivery_count_label = make_label("건 수", ("궁서", 15), "orange") # Label 생성
delivery_count_entry = make_entry() # 입력창 생성

# 버튼 생성 (계산, 초기화)
calc_btn = make_btn("계 산", "lime", "나눔고딕, 15", all_calc) # 버튼 생성 (계산)
reset_btn = make_btn("초기화", "pink", "나눔고딕, 15", input_reset) # 버튼 생성 (초기화)

# Label 설정 (최종 계산결과 출력)
calc_output_label = make_label(calc_output_text, "나눔고딕, 15", "skyblue")

# Label 설정 (파일명 저장 Label)
file_save_label = make_label("저장할 파일명 입력", ("궁서", 15), "yellow")

# 입력창 설정 (저장할 파일명 입력창)
save_entry = make_entry()

# 버튼 설정 (저장)
save_btn = make_btn(".txt 저장", "yellow", "나눔고딕, 15", save_txt) # 임시로 user_exit 지정

# 버튼 설정 (종료)
exit_btn = make_btn("종 료", "red", "나눔고딕, 20", user_exit)

window.bind("<Return>", all_calc) # 계산버튼 창 전체에 bind

window.mainloop() # 창 배치