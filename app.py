import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Stock Data Analyzer", layout="wide")

st.title("📈 Stock Data Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    selected_cols = st.multiselect("Select columns to analyze", df.columns.tolist())

    if selected_cols:
        st.subheader("Summary Statistics")
        st.write(df[selected_cols].describe())

        for col in selected_cols:
            st.markdown(f"### 📊 Visualization for `{col}`")

            if pd.api.types.is_numeric_dtype(df[col]):
                fig, ax = plt.subplots()
                sns.histplot(df[col].dropna(), kde=True, ax=ax, color="skyblue")
                ax.set_title(f"Histogram of {col}")
                st.pyplot(fig)

            elif pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
                fig, ax = plt.subplots()
                df[col].value_counts().head(10).plot(kind='bar', ax=ax, color='orange')
                ax.set_title(f"Top 10 Categories in {col}")
                st.pyplot(fig)

            else:
                st.warning(f"Unsupported column type for `{col}`")
    else:
        st.warning("Please select at least one column to analyze.")
else:
    st.info("Please upload a CSV file to get started.")
