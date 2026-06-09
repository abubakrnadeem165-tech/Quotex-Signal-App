import streamlit as st
import streamlit.components.v1 as components
import time

# =====================================================================
# 1. PREMIUM INSTITUTIONAL INTERFACE SETUP
# =====================================================================
app_logo_url = "https://cdn-icons-png.flaticon.com/512/2422/2422796.png"
st.set_page_config(
    page_title="Quotex Ultimate Hybrid Master Engine", 
    page_icon=app_logo_url, 
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #0a0d14; color: #f1f5f9; }
    .stButton>button { width: 100%; background-color: #0284c7; color: white; font-weight: bold; border-radius: 8px; padding: 14px; font-size: 18px; }
    .stButton>button:hover { background-color: #0369a1; }
    .signal-box { padding: 25px; border-radius: 12px; text-align: center; font-size: 24px; font-weight: bold; margin-top: 20px; box-shadow: 0px 4px 20px rgba(0,0,0,0.6); }
    .metric-header { font-size: 16px; font-weight: bold; color: #38bdf8; margin-top: 15px; }
    .money-box { background-color: #1e293b; padding: 12px; border-radius: 6px; border-left: 4px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .rule-box { background-color: #0f172a; padding: 15px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. SIDEBAR: EMERGENCY ACCOUNT RECOVERY MODE
# =====================================================================
st.sidebar.image(app_logo_url, width=50)
st.sidebar.title("🧮 Account Recovery Manager")
st.sidebar.markdown("---")

capital = st.sidebar.number_input("💵 Live Balance ($)", min_value=0.0, value=1.36, step=0.01)

st.sidebar.error("🚨 LAST HOPE MODE ACTIVE")
st.sidebar.markdown(f"""
<div class="money-box">
    🔥 <b>Next Fixed Trade:</b> <span style="color:#f87171; font-size:16px;"><b>$1.00 Only</b></span><br>
    ⚠️ <b>Strict Expiry Rule:</b> Quotex par trade ka time strictly <b>00:01:00 (1 Minute)</b> hona chahiye! 2 min par kabhi nahi jana.
</div>
""", unsafe_allow_html=True)

# =====================================================================
# 3. MAIN DASHBOARD & MONITORING ENGINE
# =====================================================================
st.title("🤖 Quotex Ultimate Hybrid Master Engine")
st.caption("Strict 1-Minute Radar Dashboard - Built for Recovery Protection")
st.markdown("---")

# Cheat Sheet for the user to detect FRESH vs OLD signals
st.markdown("""
<div class="rule-box">
    <h3 style="color:#fbbf24; margin-top:0;">🛑 FRESH vs OLD SIGNAL SECRETS (Loss Se Bachne Ka Tareeqa)</h3>
    <p><b>1. FRESH SIGNAL (🟢 Safe Entry):</b> Agar aap meter ke niche dekh rahay ho aur <b>Buy ka number achanak 13-14 se jump kar ke 18, 20, ya 22</b> par chala jaye aur sui Strong Buy par aa jaye. Iska matlab hai naya jhatka aaya hai, furan entry lo!</p>
    <p><b>2. OLD SIGNAL (❌ Dangerous Entry - DO NOT TOUCH):</b> Agar aapne dashboard khola aur wahan pehle se hi <b>Buy 22 ya 24</b> par khara hai aur sui extreme corner par chipki hui hai. Aapne 30 seconds wait kiya aur number wahi ruka hua hai, toh enter mat hona. Market wahan se direct reverse ho kar loss de gi.</p>
</div>
""", unsafe_allow_html=True)

# Grid Layout for 4 Major Pairs
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💱 EUR/USD (Strict 1-Min)")
    components.html("""
    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
    {"interval": "1m", "width": "100%", "isIndicatorOnly": false, "height": 380, "symbol": "FX:EURUSD", "showIntervalTabs": false, "displayMode": "single", "locale": "en", "colorTheme": "dark"}
    </script></div>""", height=390)
    
with col2:
    st.markdown("### 💱 GBP/USD (Strict 1-Min)")
    components.html("""
    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
    {"interval": "1m", "width": "100%", "isIndicatorOnly": false, "height": 380, "symbol": "FX:GBPUSD", "showIntervalTabs": false, "displayMode": "single", "locale": "en", "colorTheme": "dark"}
    </script></div>""", height=390)

st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 💱 USD/JPY (Strict 1-Min)")
    components.html("""
    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
    {"interval": "1m", "width": "100%", "isIndicatorOnly": false, "height": 380, "symbol": "FX:USDJPY", "showIntervalTabs": false, "displayMode": "single", "locale": "en", "colorTheme": "dark"}
    </script></div>""", height=390)
    
with col4:
    st.markdown("### 💱 EUR/JPY (Strict 1-Min)")
    components.html("""
    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
    {"interval": "1m", "width": "100%", "isIndicatorOnly": false, "height": 380, "symbol": "FX:EURJPY", "showIntervalTabs": false, "displayMode": "single", "locale": "en", "colorTheme": "dark"}
    </script></div>""", height=390)
