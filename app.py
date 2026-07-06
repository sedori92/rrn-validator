import streamlit as st
from rrn_checker import check_rrn

st.title("주민번호 오기 검증기")

st.write("계약서, 확인서, 진술서 등에 기재된 주민등록번호의 오기 가능성을 1차적으로 확인하는 프로그램입니다.")

rrn = st.text_input("주민등록번호를 입력하세요", placeholder="예: 900101-1234568")

if st.button("검사하기"):
    if rrn.strip() == "":
        st.warning("주민등록번호를 입력해 주세요.")
    else:
        result = check_rrn(rrn)
        st.subheader("검사 결과")
        st.text(result)

st.info("※ 이 프로그램은 주민등록번호의 실제 존재 여부를 확인하지 않습니다.")
