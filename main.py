# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
import time
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers

llm = CTransformers(
    model = "llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type = "llama"
)

st.title('AI 시인 - powered by gKim')

content = st.text_input('시의 주제를 제시해주세요')

if st.button('시 작성 요청하기'):
    with st.spinner('Wait for it...'):
        # time.sleep(3)
        result = llm.predict("write a poem about " + content + ": ")
        st.write(result)
