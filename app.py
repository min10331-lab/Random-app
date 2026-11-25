import random
import streamlit as st

# 웹 페이지 제목 및 아이콘 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱")

st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("무엇을 먹을지 고민될 때 아래 버튼을 눌러보세요!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가하거나 수정할 수 있습니다)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "초밥",
    "짜장면",
    "짬뽕",
    "햄버거",
    "파스타",
    "쌀국수",
    "비빔밥",
    "국밥",
    "마라탕",
    "떡볶이",
    "샌드위치",
]

# 버튼을 누르면 실행되는 코드
if st.button("🎲 오늘의 메뉴 뽑기", use_container_width=True):
  today_menu = random.choice(lunch_menus)
  st.success(f"오늘의 추천 점심 메뉴는 **{today_menu}**입니다!")
  st.balloons()  # 화면에 풍선이 날아오르는 시각 효과
