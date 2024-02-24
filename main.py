# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
import time

st.title('Goo Kim')
content = st.text_input('시의 주제를 제시해주세요')

if st.button('시 작성 요청하기'):
    with st.spinner('Wait for it...'):
        time.sleep(3)
        result = content + "에 대한 시를 써줘"
        st.write(result)
