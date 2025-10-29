
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Samarth Insight Demo", layout="wide")

st.title("Samarth Insight — Agri & Climate Q&A (Demo)")
st.markdown("""Small demo focused on **Gujarat** and **Rice**. Data sources: sample CSVs (representative).""")

@st.cache_data
def load_data():
    crop = pd.read_csv("crop_data.csv")
    rain = pd.read_csv("rainfall_data.csv")
    return crop, rain

crop_data, rain_data = load_data()

st.sidebar.header("Quick actions")
choice = st.sidebar.selectbox("Demo questions", [
    "Compare average rainfall: Gujarat vs Maharashtra (last 3 years)",
    "Top crops in Gujarat (latest year)",
    "Gujarat rice production trend (2019-2022)",
    "Identify district placeholder (not in sample)"
])

def compare_rainfall(s1, s2, years=3):
    max_year = rain_data["Year"].max()
    min_year = max_year - (years - 1)
    df = rain_data[rain_data["Year"].between(min_year, max_year)]
    avg = df.groupby("State", as_index=False)["Rainfall_mm"].mean()
    sel = avg[avg["State"].isin([s1, s2])]
    return sel

def top_crops_in_state(state):
    latest = crop_data["Year"].max()
    df = crop_data[(crop_data["State"]==state) & (crop_data["Year"]==latest)]
    top = df.groupby("Crop", as_index=False)["Production"].sum().sort_values("Production", ascending=False)
    return top

def rice_trend(state):
    df = crop_data[(crop_data["State"]==state) & (crop_data["Crop"].str.lower()=="rice")]
    return df.sort_values("Year")

if st.button("Run selected demo"):
    if choice.startswith("Compare average rainfall"):
        res = compare_rainfall("Gujarat","Maharashtra", years=3)
        st.subheader("Average rainfall (last 3 years)")
        st.table(res)
        st.caption("Source: IMD (sample data) — rainfall_data.csv")
    elif choice.startswith("Top crops in Gujarat"):
        st.subheader("Top crops in Gujarat (latest year)")
        res = top_crops_in_state("Gujarat")
        st.table(res)
        st.caption("Source: Ministry of Agriculture (sample) — crop_data.csv")
    elif choice.startswith("Gujarat rice production trend"):
        st.subheader("Gujarat — Rice production trend (2019-2022)")
        res = rice_trend("Gujarat")
        st.line_chart(res.set_index("Year")["Production"])
        st.dataframe(res)
        st.caption("Source: Ministry of Agriculture (sample) — crop_data.csv")
    else:
        st.warning("District-level data is not included in this small sample. Full project would include district CSVs.")

st.markdown("---")
st.header("Ask a simple question (limited demo parsing)")
q = st.text_input("Type question (try: 'show rice trend in Gujarat' or 'compare rainfall Gujarat Maharashtra')")

if q:
    ql = q.lower()
    if "rainfall" in ql and "compare" in ql:
        out = compare_rainfall("Gujarat","Maharashtra", years=3)
        st.write(out)
        st.caption("Source: rainfall_data.csv")
    elif "top" in ql and "crops" in ql and "gujarat" in ql:
        out = top_crops_in_state("Gujarat")
        st.write(out)
        st.caption("Source: crop_data.csv")
    elif "rice" in ql and "trend" in ql and "gujarat" in ql:
        out = rice_trend("Gujarat")
        st.line_chart(out.set_index("Year")["Production"])
        st.write(out)
        st.caption("Source: crop_data.csv")
    else:
        st.info("Demo parser could not understand. Use the quick actions or try simple queries like 'compare rainfall Gujarat Maharashtra'")
