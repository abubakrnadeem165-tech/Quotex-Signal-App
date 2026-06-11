import streamlit as st
import streamlit.components.v1 as components
import time

# =====================================================================
# 1. PREMIUM INSTITUTIONAL INTERFACE SETUP
# =====================================================================
app_logo_url = "https://cdn-icons-png.flaticon.com/512/2422/2422796.png"
st.set_page_config(page_title="Quotex Ultimate Hybrid Master Engine", page_icon=app_logo_url, layout="wide")

st.markdown("""
<style>
    .main { background-color: #0a0d14; color: #f1f5f9; }
    .stButton>button { width: 100%; background-color: #0284c7; color: white; font-weight: bold; border-radius: 8px; padding: 14px; font-size: 18px; }
    .stButton>button:hover { background-color: #0369a1; }
    .signal-box { padding: 25px; border-radius: 12px; text-align: center; font-size: 24px; font-weight: bold; margin-top: 20px; box-shadow: 0px 4px 20px rgba(0,0,0,0.6); }
    .buy-signal { background-color: #10b981; color: white; border: 2px solid #065f46; }
    .sell-signal { background-color: #ef4444; color: white; border: 2px solid #991b1b; }
    .hold-signal { background-color: #334155; color: #cbd5e1; border: 2px solid #1e293b; }
    .money-box { background-color: #1e293b; padding: 12px; border-radius: 6px; border-left: 4px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .rule-box { background-color: #0f172a; padding: 12px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 15px; }
    h4 { color: #38bdf8; font-weight: bold; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. SIDEBAR: EMERGENCY ACCOUNT RECOVERY MODE
# =====================================================================
st.sidebar.image(app_logo_url, width=50)
st.sidebar.title("🧮 Account Recovery")
st.sidebar.markdown("---")
# Live balance perfectly matches your screen ($2.20)
capital = st.sidebar.number_input("💵 Live Balance ($)", min_value=0.0, value=2.20, step=0.01)
st.sidebar.error("🚨 RECOVERY MODE ACTIVE")
st.sidebar.markdown(f"""
<div class="money-box">
    🔥 <b>Next Fixed Trade:</b> <span style="color:#f87171; font-size:16px;"><b>$1.00 Only</b></span><br>
    ⚠️ <b>Strict Expiry Rule:</b> Quotex par trade ka time strictly <b>00:01:00 (1 Minute)</b> hona chahiye!
</div>
""", unsafe_allow_html=True)

# =====================================================================
# 3. MAIN DASHBOARD & GLOBAL MODE SWITCHER
# =====================================================================
st.title("🤖 Quotex Ultimate Hybrid Master Engine")
st.caption("Lag-Free Multi-Pair Radar Engine - Built for High Speed Precision")
st.markdown("---")

market_mode = st.selectbox("🌐 CHOOSE SYSTEM MODE", [
    "Real Market (Multi-Pair Live Radar Dashboard)",
    "OTC Market (Safe Pro-Trader Checklist Decision Helper)"
])

# =====================================================================
# MODE A: REAL MARKET (OPTIMIZED DROP-DOWN FOR MAXIMUM SPEED 🚀)
# =====================================================================
if market_mode == "Real Market (Multi-Pair Live Radar Dashboard)":
    st.markdown("""
    <div class="rule-box">
        <h3 style="color:#fbbf24; margin-top:0; font-size:16px; margin-bottom:5px;">🛑 FRESH vs OLD SIGNAL SECRETS (Loss Se Bachne Ka Tareeqa)</h3>
        <span style="font-size:13px; color:#cbd5e1;">
            <b>1. FRESH SIGNAL (🟢 Safe):</b> Sui achanak jhatke se ghoom kar <b>Strong</b> par jaye aur niche buy/sell ka count barhay $\rightarrow$ <b>Furan entry lo!</b><br>
            <b>2. OLD SIGNAL (❌ Dangerous):</b> Sui pehle se extreme corner par chipki ho ya candle khatam hone wali ho $\rightarrow$ <b>Skip kar do.</b>
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # Dropdown system memory load ko 90% kam kar deta hai tabs ke muqable me
    selected_pair = st.selectbox("🎯 SELECT ACTIVE TRADING PAIR TO MONITOR", [
        "EUR/USD", "GBP/USD", "USD/JPY", "EUR/JPY", "AUD/USD", "USD/CAD"
    ])
    
    # Mapping pair names to TradingView Symbols
    pair_symbols = {
        "EUR/USD": "FX:EURUSD",
        "GBP/USD": "FX:GBPUSD",
        "USD/JPY": "FX:USDJPY",
        "EUR/JPY": "FX:EURJPY",
        "AUD/USD": "FX:AUDUSD",
        "USD/CAD": "FX:USDCAD"
    }
    
    active_symbol = pair_symbols[selected_pair]
    widget_height = 380

    st.markdown(f"<h4>💱 {selected_pair} Technical Gauge (1m)</h4>")
    
    # Super-cleaned standalone injection to completely remove browser freezing
    components.html(f"""
    <div class="tradingview-widget-container" style="width:100%; height:{widget_height}px;">
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
        {{
            "interval": "1m",
            "width": "100%",
            "isIndicatorOnly": false,
            "height": {widget_height},
            "symbol": "{active_symbol}",
            "showIntervalTabs": false,
            "displayMode": "single",
            "locale": "en",
            "colorTheme": "dark"
        }}
        </script>
    </div>
    """, height=widget_height+20)

    st.markdown("---")

# =====================================================================
# MODE B: OTC MARKET (SAFE CHECKLIST METHOD)
# =====================================================================
else:
    st.subheader("🕵️‍♂️ Safe OTC Matrix Setup (Multi-Strategy Checklist)")
    st.info("💡 Note: OTC market me indicators direct kaam nahi karte. Pehle Quotex ka chart dekhein, phir niche details check karein:")
    
    col_otc1, col_otc2 = st.columns(2)
    
    with col_otc1:
        macro_trend = st.radio("📈 1. Market Macro Trend (15M Flow)", ["Bullish (Up Trend)", "Bearish (Down Trend)", "Ranging (Sideways)"])
        snr_zone = st.radio("🎯 2. Price Position near SNR Zone", ["At Strong Support (Bottom)", "At Strong Resistance (Top)", "In Middle of the Zone"])
        current_pattern = st.selectbox("🕯️ 3. Current Active Candlestick Pattern", [
            "None / Standard Candle", "Hammer (Bullish Reversal)", "Shooting Star (Bearish Reversal)", 
            "Bullish Engulfing", "Bearish Engulfing", "Marubozu Strong Candle"
        ])
        
    with col_otc2:
        rsi_state = st.radio("📊 4. RSI (14) Condition", ["Overbought (>70)", "Oversold (<30)", "Normal Middle Zone"])
        macd_state = st.radio("📉 5. MACD (12, 26, 9) Cross", ["Bullish Cross (Green Line Up)", "Bearish Cross (Red Line Up)", "No Clear Cross"])
        
    st.markdown("---")
    
    if st.button("⚡ RUN FULL STRATEGY CONFLUENCE ALGORITHM"):
        score = 0
        if macro_trend == "Bullish (Up Trend)": score += 1
        if snr_zone == "At Strong Support (Bottom)": score += 2
        if current_pattern in ["Hammer (Bullish Reversal)", "Bullish Engulfing"]: score += 2
        if rsi_state == "Oversold (<30)": score += 1.5
        if macd_state == "Bullish Cross (Green Line Up)": score += 1.5
        
        if macro_trend == "Bearish (Down Trend)": score -= 1
        if snr_zone == "At Strong Resistance (Top)": score -= 2
        if current_pattern in ["Shooting Star (Bearish Reversal)", "Bearish Engulfing"]: score -= 2
        if rsi_state == "Overbought (>70)": score -= 1.5
        if macd_state == "Bearish Cross (Red Line Up)": score -= 1.5
        
        if score >= 3.5:
            st.markdown(f'<div class="signal-box buy-signal">🟩 SIGNAL: CALL (UP) <br><span style="font-size:14px;">Confluence Score: +{score} | Expiry: 1-2 Min</span></div>', unsafe_allow_html=True)
        elif score <= -3.5:
            st.markdown(f'<div class="signal-box sell-signal">🟥 SIGNAL: PUT (DOWN) <br><span style="font-size:14px;">Confluence Score: {score} | Expiry: 1-2 Min</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="signal-box hold-signal">🟨 STRICT HOLD: NO CONFIDENCE <br><span style="font-size:14px;">Market clear nahi hai. Sabar karein!</span></div>', unsafe_allow_html=True)
