import streamlit as st
import pandas as pd

from src.ai.llm_agent import analyze_data

st.title("🧠 CommerceDoctor AI")

# Upload file FIRST
file = st.file_uploader("Upload Orders JSON")

if file:
    df = pd.read_json(file)

    st.subheader("📊 Raw Data")
    st.dataframe(df)

    # Sample for AI
    sample = df.head(5).to_dict()

    # AI button
    if st.button("Run AI Analysis"):
        result = analyze_data(sample)
        st.subheader("🧠 AI Analysis")
        st.write(result)

    # Fix button
    if st.button("⚡ Auto Fix Data"):
        df = df[df["amount"] >= 0]
        df = df[df["customer_id"].notna()]
        df = df.drop_duplicates("order_id")

        st.subheader("✅ Fixed Data")
        st.dataframe(df)

        st.subheader("📊 KPIs")
        st.metric("Total Revenue", df["amount"].sum())
        st.metric("Total Orders", len(df))