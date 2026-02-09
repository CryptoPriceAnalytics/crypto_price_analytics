import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crypto Analytics Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/processed_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Project Overview",
        "Market Overview",
        "Sentiment Analysis",
        "Model Forecast Comparison",
        "Best Model Selection",
        "7-Day Forecast",
        "30-Day Forecast",
        "Trading & Backtesting",
        "Final Insights"
    ]
)

# ------------------ PAGE 1 ------------------
if page == "Project Overview":
    st.title("📌 Project Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Cryptos Tracked", df["coin"].nunique())
    col2.metric("Models Used", "ARIMA, Prophet, LSTM")
    col3.metric("Forecast Horizons", "7D, 30D")

    st.subheader("Insight")
    st.info(
        "Initial analysis indicates correlation between sentiment spikes "
        "and short-term crypto price movements for major coins."
    )

# ------------------ PAGE 2 ------------------
elif page == "Market Overview":
    st.title("📈 Market Overview")

    coin = st.selectbox("Select Coin", sorted(df["coin"].unique()))
    filtered = df[df["coin"] == coin]

    fig, ax = plt.subplots()
    ax.plot(filtered["date"], filtered["close"])
    ax.set_title(f"{coin} Price Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    ax.grid(True)
    st.pyplot(fig)

# ------------------ PAGE 3 ------------------
elif page == "Sentiment Analysis":
    st.title("💬 Sentiment Analysis")

    st.subheader("Sentiment Overview")
    st.info("Sentiment analysis results integrated from NLP pipeline.")

    # Placeholder visuals
    st.write("• Sentiment over time")
    st.write("• Sentiment distribution")
    st.write("• Avg sentiment score")

# ------------------ PAGE 4 ------------------
elif page == "Model Forecast Comparison":
    st.title("📊 Model Forecast Comparison")
    st.info("Forecast comparison between ARIMA, Prophet, and LSTM models.")

# ------------------ PAGE 5 ------------------
elif page == "Best Model Selection":
    st.title("🏆 Best Model Selection")
    st.info("Model ranking based on RMSE, MAE, MAPE, and R².")

# ------------------ PAGE 6 ------------------
elif page == "7-Day Forecast":
    st.title("🔮 7-Day Forecast")
    st.info("7-day forecast with confidence intervals.")

# ------------------ PAGE 7 ------------------
elif page == "30-Day Forecast":
    st.title("📆 30-Day Forecast")
    st.info("Longer horizon forecast highlighting uncertainty.")

# ------------------ PAGE 8 ------------------
elif page == "Trading & Backtesting":
    st.title("📉 Trading Strategy & Backtesting")
    st.info("Buy/Sell signals and strategy performance vs market.")

# ------------------ PAGE 9 ------------------
elif page == "Final Insights":
    st.title("🧠 Final Insights")
    st.success(
        "The dashboard integrates price, sentiment, and forecasting insights "
        "to support informed crypto investment decisions."
    )
