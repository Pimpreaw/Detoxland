# -*- coding: utf-8 -*-
"""Detoxland and detoxme plz

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RLRHjDY8Zvk2c0GBqaPh-VQgvPoFpf_U
"""



import streamlit as st
import time

# --- ตั้งค่า UI ---
st.set_page_config(page_title="Detoxland: The Self Battle", page_icon="", layout="wide")

# --- CSS สำหรับตกแต่ง ---
st.markdown('''
    <style>
    body {
        background-color: #f4f4f4;
    }
    .big-title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .sub-title {
        font-size: 20px;
        color: #555;
        text-align: center;
    }
    .button-style {
        background-color: #4CAF50;
        color: white;
        padding: 15px 25px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
    </style>
''', unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="big-title">Detoxland: The Self Battle</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">ช่วยให้คุณโฟกัสและลดการใช้โซเชียลมีเดียอย่างมีสุขภาพจิตที่ดี</p>', unsafe_allow_html=True)

# --- Layout ของหน้า UI ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # ปุ่มเริ่ม Pomodoro Timer
    if st.button("⏳ Start Pomodoro (25 min)", key="pomodoro"):
        st.session_state["end_time"] = time.time() + (25 * 60)
        st.success("✅ Pomodoro เริ่มแล้ว! ตั้งใจทำงานนะ ")

    # แสดงเวลาที่เหลือ
    if "end_time" in st.session_state:
        remaining_time = st.session_state["end_time"] - time.time()
        if remaining_time > 0:
            st.info(f"⏳ เวลาที่เหลือ: {int(remaining_time // 60)} นาที {int(remaining_time % 60)} วินาที")
        else:
            st.success(" Pomodoro เสร็จแล้ว! พักสักหน่อยนะ ️")

    # ระบบบันทึกอารมณ์ (Mental Health Tracker)
    st.subheader(" บันทึกอารมณ์ของคุณวันนี้")
    mood = st.selectbox("วันนี้คุณรู้สึกอย่างไร?", [" Happy", " Neutral", " Sad", " Anxious"])
    if st.button(" บันทึกอารมณ์"):
        st.success("✅ บันทึกอารมณ์สำเร็จ!")

    # ฟีเจอร์จัดการอาการแพนิค
    st.subheader(" จัดการอาการแพนิค")
    if st.button(" ฉันรู้สึกเครียด"):
        st.warning("✨ ลองใช้ 5-4-3-2-1 เทคนิค หรือหายใจลึก ๆ นะ ✨")
        st.write("หากยังรู้สึกไม่ดีขึ้น ลองพูดคุยกับผู้เชี่ยวชาญหรือคนใกล้ตัว")

    # แบบสอบถามวัดระดับอาการติดโซเชียล
    st.subheader(" แบบสอบถาม: คุณติดโซเชียลแค่ไหน?")
    questions = [
        "1. คุณใช้โซเชียลมีเดียเป็นสิ่งแรกหลังตื่นนอนหรือไม่?",
        "2. คุณรู้สึกว่าต้องเช็คโซเชียลตลอดเวลาไหม?",
        "3. คุณใช้โซเชียลจนกระทบเวลานอนหรือไม่?",
        "4. คุณรู้สึกกังวลเมื่อไม่ได้ใช้โซเชียลมีเดียหรือไม่?",
        "5. คุณเคยพยายามลดการใช้โซเชียลแต่ทำไม่ได้หรือไม่?"
    ]
    responses = []
    for q in questions:
        responses.append(st.radio(q, ["ใช่", "ไม่ใช่"], index=1))

    if st.button(" วิเคราะห์ผล"):
        score = responses.count("ใช่")
        if score <= 1:
            st.success("✅ คุณใช้โซเชียลมีเดียอย่างสมดุล ดีมาก!")
        elif score <= 3:
            st.warning("⚠️ คุณอาจใช้โซเชียลมากเกินไป ลองกำหนดเวลาให้ตัวเอง")
        else:
            st.error(" คุณอาจติดโซเชียลอย่างมาก! ลองหากิจกรรมอื่นแทนการใช้โซเชียล")

st.write("---")  # เส้นคั่น
st.markdown("<p style='text-align: center;'> Detoxland ช่วยให้คุณลดความเครียดและโฟกัสกับชีวิตมากขึ้น</p>", unsafe_allow_html=True)