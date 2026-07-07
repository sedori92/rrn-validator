import streamlit as st
from rrn_checker import check_rrn

st.title("세무사무실 특급 AI 에이전트")

st.write("""
세무사무실의 반복적인 문서 확인 업무를 줄이기 위한 AI 전처리 도구입니다.

현재 Version 1.1에서는 주민등록번호 직접 입력 검증 기능을 제공하며,
앞으로 사진, 이미지, PDF 업로드 및 OCR 분석 기능으로 확장할 예정입니다.
""")

st.divider()

input_method = st.radio(
    "입력 방법을 선택하세요",
    ["직접 입력", "사진 촬영", "이미지 업로드", "PDF 업로드"]
)

st.divider()

if input_method == "직접 입력":
    st.subheader("주민등록번호 직접 입력 검증")

    rrn = st.text_input("주민등록번호를 입력하세요", placeholder="예: 900101-1234568")

    if st.button("검사하기"):
        if rrn.strip() == "":
            st.warning("주민등록번호를 입력해 주세요.")
        else:
            result = check_rrn(rrn)
            st.subheader("검사 결과")
            st.text(result)

elif input_method == "사진 촬영":
    st.subheader("사진 촬영 입력")
    st.info("사진 촬영 기능은 다음 버전에서 OCR 기능과 함께 추가할 예정입니다.")

elif input_method == "이미지 업로드":
    st.subheader("이미지 업로드")
    uploaded_image = st.file_uploader(
        "이미지 파일을 업로드하세요",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:
        st.success("이미지 파일이 업로드되었습니다.")
        st.image(uploaded_image, caption="업로드한 이미지", use_container_width=True)
        st.info("OCR 문자 추출 기능은 다음 단계에서 연결할 예정입니다.")

elif input_method == "PDF 업로드":
    st.subheader("PDF 업로드")
    uploaded_pdf = st.file_uploader(
        "PDF 파일을 업로드하세요",
        type=["pdf"]
    )

    if uploaded_pdf is not None:
        st.success("PDF 파일이 업로드되었습니다.")
        st.info("PDF 문자 추출 기능은 다음 단계에서 연결할 예정입니다.")

st.divider()

st.info("※ 이 프로그램은 번호의 형식 오류 가능성을 1차 확인하는 도구이며, 실제 존재 여부를 확인하지 않습니다.")
