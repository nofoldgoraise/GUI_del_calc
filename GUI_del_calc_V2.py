from tkinter import *

window = Tk()

# 디자인 변수
bg_color = "#2B3240"      # 창 배경
label_bg = "#2B3240"      # label 배경
frame_bg = "#2B3240"      # 프레임 배경
font_color = "#1DB584"    # 기본 글자색
button_bg = "#1DB584"      # 버튼 배경 (계산 버튼 등 primary action)
highlight_color = "#5FFFD4"  # 순수익 등 강조용
error_color = "#FF6B6B"   # 오류 문구용 (민트 배경에 빨강 계열이 잘 띔)

# 창 설정
window.title("배달 일당 계산기")
window.geometry("500x600")
window.config(bg = bg_color)
window.option_add("*font", "나눔고딕, 15")

# 변수
title_label_text = "배달 일당 계산기" # Label 텍스트 (제목)
work_time_label_text = "총 운행시간:" # Label 텍스트 (총 운행시간)
rest_time_label_text = "총 휴식시간:" # Label 텍스트 (총 휴식시간)
today_pay_label_text = "지출 금액:" # Label 텍스트 (지출)
today_money_label_text = "매출 금액:" # Label 텍스트 (매출)
today_count_label_text = "건 수:" # Label 텍스트 (건 수)

hello_label_text = "☆오늘도 안전운전 하세요☆" # Label 텍스트 (인사문구)
hello_label_text_font = ("나눔고딕", 15, "bold")

info_label_text = "[안내] 값을 입력후 계산버튼을 누르세요" # 안내 문구 텍스트
info_label_text_font = ("나눔고딕", 15, "bold")

error_text = "[오류] 잘못입력하셨습니다!" # 오류 안내 텍스트

file_save_text = "" # 파일저장할 값 저장 변수
file_save_info_text = "[안내] 파일이 저장되었습니다."

calc_button_info_text = "[안내] 계산이 완료되었습니다."

calc_button_text = "계산" # Button 텍스트 (계산)
reset_button_text = "초기화" # Button 텍스트 (초기화)
save_button_text = "저장" # Button 텍스트 (저장)
close_button_text = "종료" # Button 텍스트 (종료)

# Label 기본 텍스트 (결과)
real_work_time_result_default_text = "실 운행시간: "
today_pay_result_default_text = "지출 금액: "
today_count_result_default_text = "완료 건 수: "
hour_count_result_default_text = "시간당 건 수: "
today_money_result_default_text = "매출 금액: "
count_price_result_default_text = "건 당 단가: "
profit_result_default_text = "★순수익 금액: "

title_label_font = ("나눔고딕", 20, "bold") # Label 폰트 (제목)

# 함수
def make_label(frame, label_text, label_font = None, label_row = None, label_column = None, label_sticky = None): # Label 생성 함수
  label = Label(frame)
  label.config(text = label_text, font = label_font, bg = label_bg, fg = font_color)
  label.grid(row = label_row, column = label_column, sticky = label_sticky, padx = 5, pady = 5)
  return label

def make_button(frame, button_text, button_command = None, button_row = None, button_column = None): # Button 생성 함수
  button = Button(frame)
  button.config(text = button_text, command = button_command, bg = button_bg)
  button.grid(row = button_row, column = button_column, padx = 5, pady = 5)
  return button

def make_entry(frame, entry_row = None, entry_column = None, entry_sticky = None): # Entry 생성 함수
  entry = Entry(frame)
  entry.grid(row = entry_row, column = entry_column, sticky = entry_sticky, padx = 5, pady = 5)
  return entry

def calc_button_command(event = None): # Button 함수 (계산)
  global file_save_text
  try:
    # Entry 입력값 추출 변수
    work_time = int(work_time_entry.get()) # 총 운행시간
    rest_time = int(rest_time_entry.get()) # 총 휴식시간
    today_pay = int(today_pay_entry.get()) # 지출 ★ 그대로 출력
    today_money = int(today_money_entry.get()) # 매출 ★ 그대로 출력
    today_count = int(today_count_entry.get()) # 건수 ★ 그대로 출력
    # 출력값 계산
    real_work_time = work_time - rest_time # 실 운행시간
    hour_count = today_count / real_work_time # 시간당 건 수
    count_price = int(today_money / today_count) # 건 당 단가
    profit = today_money - today_pay # 순수익 금액
    # 출력
    real_work_time_result_text = f"실 운행시간: {real_work_time}시간"
    today_pay_result_text = f"지출 금액: {today_pay:,}원"
    today_count_result_text = f"완료 건 수: {today_count}건"
    hour_count_result_text = f"시간당 건 수: {hour_count:.1f}건"
    today_money_result_text = f"매출 금액: {today_money:,}원"
    count_price_result_text = f"건 당 단가: {count_price:,}원"
    profit_result_text = f"★순수익 금액: {profit:,}원"
    
    real_work_time_result_label.config(text = real_work_time_result_text)
    today_pay_result_label.config(text = today_pay_result_text)
    today_count_result_label.config(text = today_count_result_text)
    hour_count_result_label.config(text = hour_count_result_text)
    today_money_result_label.config(text = today_money_result_text)
    count_price_result_label.config(text = count_price_result_text)
    profit_result_label.config(text = profit_result_text, fg = highlight_color)
    
    info_label.config(text = calc_button_info_text)
    
    file_save_text = f"""실 운행시간: {real_work_time}시간
지출 금액: {today_pay:,}원
완료 건 수: {today_count}건
시간당 건 수: {hour_count:.1f}건
매출 금액: {today_money:,}원
건 당 단가: {count_price:,}원
★순수익 금액: {profit:,}원
===================="""
  except (ValueError, ZeroDivisionError):
    info_label.config(text = error_text)

def reset_button_command(): # Button 함수 (초기화)
  work_time_entry.delete(0, "end")
  rest_time_entry.delete(0, "end")
  today_pay_entry.delete(0, "end")
  today_money_entry.delete(0, "end")
  today_count_entry.delete(0, "end")
  real_work_time_result_label.config(text = real_work_time_result_default_text)
  today_pay_result_label.config(text = today_pay_result_default_text)
  today_count_result_label.config(text = today_count_result_default_text)
  hour_count_result_label.config(text = hour_count_result_default_text)
  today_money_result_label.config(text = today_money_result_default_text)
  count_price_result_label.config(text = count_price_result_default_text)
  profit_result_label.config(text = profit_result_default_text, fg = font_color)
  info_label.config(text = info_label_text)
  work_time_entry.focus()
  
def save_button_command(): # Button 함수 (저장)
  file_save = open("배달 정산.txt", "a", encoding = "utf-8")
  file_save.write(file_save_text)
  file_save.close()
  info_label.config(text = file_save_info_text)

def close_button_command(): # Button 함수 (종료)
  window.destroy()

# GUI 설정
frame1 = Frame(window) # Frame 생성 (제목)
frame1.config(bg = frame_bg)
frame1.pack()

title_label = make_label(frame1, title_label_text, title_label_font) # Label 생성 (제목)

frame2 = Frame(window) # Frame 생성 (Label, Entry)
frame2.config(bg = frame_bg)
frame2.pack()

work_time_label = make_label(frame2, work_time_label_text, label_row = 0, label_column = 0, label_sticky = "w") # Label 생성 (총 운행시간)
work_time_entry = make_entry(frame2, entry_row = 0, entry_column = 1, entry_sticky = "w") # Entry 생성 (총 운행시간)

rest_time_label = make_label(frame2, rest_time_label_text, label_row = 1, label_column = 0, label_sticky = "w") # Label 생성 (총 휴식시간)
rest_time_entry = make_entry(frame2, entry_row = 1, entry_column = 1, entry_sticky = "w") # Entry 생성 (총 휴식시간)

today_pay_label = make_label(frame2, today_pay_label_text, label_row = 2, label_column = 0, label_sticky = "w") # Label 생성 (지출)
today_pay_entry = make_entry(frame2, entry_row = 2, entry_column = 1, entry_sticky = "w") # Entry 생성 (지출)

today_money_label = make_label(frame2, today_money_label_text, label_row = 3, label_column = 0, label_sticky = "w") # Label 생성 (매출)
today_money_entry = make_entry(frame2, entry_row = 3, entry_column = 1, entry_sticky = "w") # Entry 생성 (총 운행시간)

today_count_label = make_label(frame2, today_count_label_text, label_row = 4, label_column = 0, label_sticky = "w") # Label 생성 (건 수)
today_count_entry = make_entry(frame2, entry_row = 4, entry_column = 1, entry_sticky = "w") # Entry 생성 (건 수)

frame3 = Frame(window) # Frame 생성 (Button)
frame3.config(bg = frame_bg)
frame3.pack()

calc_button = make_button(frame3, calc_button_text, calc_button_command, button_row = 0, button_column = 0) # Button 생성 (계산)
reset_button = make_button(frame3, reset_button_text, reset_button_command, button_row = 0, button_column = 1) # Button 생성 (초기화)
save_button = make_button(frame3, save_button_text, save_button_command, button_row = 0, button_column = 2) # Button 생성 (저장)
close_button = make_button(frame3, close_button_text, close_button_command, button_row = 0, button_column = 3) # Button 생성 (종료)

frame4 = Frame(window) # Frame 생성 (결과창)
frame4.config(bg = frame_bg)
frame4.pack()

real_work_time_result_label = make_label(frame4, real_work_time_result_default_text) # Label 생성 (결과)
today_pay_result_label = make_label (frame4, today_pay_result_default_text)
today_count_result_label = make_label (frame4, today_count_result_default_text)
hour_count_result_label = make_label (frame4, hour_count_result_default_text)
today_money_result_label = make_label (frame4, today_money_result_default_text)
count_price_result_label = make_label (frame4, count_price_result_default_text)
profit_result_label = make_label (frame4, profit_result_default_text) # Label 생성 (결과)

hello_label = make_label(frame4, hello_label_text, hello_label_text_font, label_row = 8, label_column = 0) # Label 생성 (인사문구)

info_label = make_label(frame4, info_label_text, info_label_text_font, label_row = 9, label_column = 0) # Label 생성 (안내)

window.bind("<Return>", calc_button_command)

window.mainloop()