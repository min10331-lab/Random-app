import pandas as pd
import streamlit as st


# 1. 함수(def)와 조건문(if-elif-else)을 활용한 추천 교재 반환 함수
def get_recommended_books(subject):
  if subject == "국어":
    return ["매삼비", "자습서"]
  elif subject == "수학":
    return ["마더텅", "올림포스"]
  elif subject == "영어":
    return ["올림포스"]
  elif subject == "과학":
    return ["완자", "마더텅"]
  elif subject == "사회":
    return ["완자", "자습서"]
  else:  # 역사
    return ["자습서", "완자"]


# 2. 함수(def), 반복문(for), 조건문(if-elif-else)을 활용한 주간 공부 계획표 생성 함수
def create_study_plan(books):
  days = ["월", "화", "수", "목", "금", "토", "일"]
  tasks = []
  times = []

  first_book = books[0]
  second_book = books[1] if len(books) > 1 else f"{books[0]} 심화"

  # 반복문(for)으로 월~일요일까지의 계획 생성
  for day in days:
    if day in ["월", "수"]:
      tasks.append(f"{first_book} - 개념 학습 및 기본 문제 풀이")
      times.append("1시간 30분")
    elif day in ["화", "목"]:
      tasks.append(f"{second_book} - 유형별 집중 문제 풀이")
      times.append("1시간 30분")
    elif day == "금":
      tasks.append(f"{first_book} & {second_book} - 주간 오답 정리")
      times.append("2시간")
    elif day == "토":
      tasks.append("실전 모의 테스트 및 시간 배분 연습")
      times.append("2시간")
    else:  # 일요일
      tasks.append("이번 주 핵심 개념 총복습 및 휴식")
      times.append("1시간")

  plan_data = {"요일": days, "주요 학습 내용": tasks, "권장 시간": times}
  return pd.DataFrame(plan_data)


# --- 메인 화면 UI 구성 ---
st.set_page_config(page_title="공부 계획표 맞춤 가이드", page_icon="📚")

st.title("📚 공부 계획표 맞춤 가이드")
st.write(
    "나이와 과목을 선택하면 적합한 문제집과 맞춤 공부 계획표를 만들어 드립니다."
)

# 나이 입력 슬라이더 (17세 ~ 19세)
age = st.slider("나이를 선택하세요", min_value=17, max_value=19, value=17)

# 과목 선택 상자
subjects = ["국어", "수학", "영어", "과학", "사회", "역사"]
selected_subject = st.selectbox("공부할 과목을 선택하세요", subjects)

if st.button("맞춤 가이드 생성하기", use_container_width=True):
  # 정의한 함수 호출
  books = get_recommended_books(selected_subject)

  # 추천 교재 텍스트 출력 (조건문 if-else)
  if len(books) == 2:
    st.info(
        f"**{selected_subject}**을(를) 공부할땐 **'{books[0]}'**과"
        f" **'{books[1]}'** 교재가 적합합니다."
    )
  else:
    st.info(
        f"**{selected_subject}**을(를) 공부할땐 **'{books[0]}'** 교재가"
        " 적합합니다."
    )

  # 맞춤 공부 계획표 표 출력
  st.subheader(f"🗓️ {age}세 맞춤 {selected_subject} 주간 공부 계획표")
  plan_df = create_study_plan(books)
  st.table(plan_df)

  # 나이가 19세일 때 응원 메시지 출력
  if age == 19:
    st.success(
        "🔥 고3 수험생 여러분, 지금까지 달려온 노력이 분명 빛을 발할 거예요."
        " 마지막까지 응원합니다!"
    )
