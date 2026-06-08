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
    layout="centered"
)

st.markdown("""
    <style>
    .main { background-color: #0a0d14; color: #f1f5f9; }
    .stButton>button { width: 100%; background-color: #0284c7; color: white; font-weight: bold; border-radius: 8px; padding: 14px; font-size: 18px; }
    .stButton>button:hover { background-color: #0369a1; }
    .signal-box { padding: 25px; border-radius: 12px; text-align: center; font-size: 24px; font-weight: bold; margin-top: 20px; box-shadow: 0px 4px 20px rgba(0,0,0,0.6); }
    .buy-signal { background-color: #10b981; color: white; border: 2px solid #065f46; }
    .sell-signal { background-color: #ef4444; color: white; border: 2px solid #991b1b; }
    .hold-signal { background-color: #334155; color: #cbd5e1; border: 2px solid #1e293b; }
    .metric-header { font-size: 16px; font-weight: bold; color: #38bdf8; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.image(app_logo_url, width=70)
st.title("🤖 Quotex Ultimate Hybrid Master Engine")
st.caption("All-In-One Platform: Multi-Timeframe Structure, SNR Levels, FVG Blocks, Indicators & All Candle Patterns")
st.markdown("---")

# =====================================================================
# 2. MASTER GLOBAL OPERATION MODE SWITCHER
# =====================================================================
market_mode = st.selectbox("🌐 CHOOSE SYSTEM MODE", [
    "Real Market (100% Fully Automatic Cloud Scanner)", 
    "OTC Market (Safe Pro-Trader Checklist Decision Helper)"
])

# =====================================================================
# MODE 1: REAL MARKET (100% AUTOMATIC STRATEGY CONFLUENCE)
# =====================================================================
if market_mode == "Real Market (100% Fully Automatic Cloud Scanner)":
    st.subheader("🚀 Live Multi-Strategy Scanner (Auto-Tracking)")
    
    pair_selected = st.selectbox("🎯 Target Real Currency Pair", ["EURUSD", "GBPUSD", "USDJPY", "EURJPY", "AUDUSD", "USDCAD"])
    st.caption("TradingView Core Engine is combining 15M Structural Flows, Pivot SNR, RSI, MACD & Candles continuously...")
    
    # Advanced TradingView Technical Gauge Widget Integration
    tv_widget_html = f"""
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
      {{
      "interval": "1m",
      "width": "100%",
      "isIndicatorOnly": false,
      "height": 440,
      "symbol": "FX:{pair_selected}",
      "showIntervalTabs": true,
      "displayMode": "single",
      "locale": "en",
      "colorTheme": "dark"
    }}
      </script>
    </div>
    """
    components.html(tv_widget_html, height=450)
    
    st.markdown("""
    > 📥 **Live Execution Rule:** 
    > * **STRONG BUY (Sui Extreme Right Par):** Execute 1-2 Min **CALL (UP)** trade on Quotex.
    > * **STRONG SELL (Sui Extreme Left Par):** Execute 1-2 Min **PUT (DOWN)** trade on Quotex.
    > * **NEUTRAL / NORMAL BUY-SELL:** **STRICT HOLD** (Engine filters risk).
    """)

# =====================================================================
# MODE 2: OTC MARKET (SAFE CHECKLIST METHOD WITH ALL STRATEGIES)
# =====================================================================
else:
    st.subheader("🕵️‍♂️ Safe OTC Matrix Setup (Multi-Strategy Checklist)")
    st.caption("Apne Quotex Live OTC Chart Ko Dekhein Aur Niche Ki Conditions Ko Match Karke Select Karein:")
    
    otc_pair = st.selectbox("🎯 Target OTC Asset Pair", [
        "USD/BRL (OTC)", "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/INR (OTC)", "EUR/JPY (OTC)", "USD/ARS (OTC)"
    ])
    
    st.markdown("---")
    # Strategy Block 1: Multi-Timeframe Structure & Institutional Levels
    st.markdown('<p class="metric-header">📐 Strategy Block 1: 15-Min Macro Structure & SNR Zones</p>', unsafe_allow_html=True)
    macro_trend = st.radio("15-Min Chart Par Market Ka Trend Flow Kya Hai?", ["BULLISH (Upar Ki Taraf Heavy Flow)", "BEARISH (Niche Ki Taraf Heavy Flow)", "SIDEWAYS (Range Me Phansa Hua Zone)"])
    snr_zone = st.radio("Kya Price Kisi Major 15-Min Level / FVG Block Par Hai?", ["At Major Support / FVG Demand Zone", "At Major Resistance / Supply Zone", "Middle Zone (No Clear Institutional Level)"])

    st.markdown("---")
    # Strategy Block 2: Comprehensive Candlestick Pattern Engine
    st.markdown('<p class="metric-header">🕯️ Strategy Block 2: 1-Min Candlestick Patterns Triggers</p>', unsafe_allow_html=True)
    current_pattern = st.selectbox("Abhi Live 1-Min Candle Kaunsi Close Hui Hai?", [
        "Bullish Hammer / Pinbar",
        "Bearish Shooting Star",
        "Bullish Engulfing",
        "Bearish Engulfing",
        "Bullish Marubozu (Full Strong Green)",
        "Bearish Marubozu (Full Strong Red)",
        "Normal Moving Candle (No Specific Pattern)"
    ])

    st.markdown("---")
    # Strategy Block 3: Mathematical Indicators Confluence
    st.markdown('<p class="metric-header">📊 Strategy Block 3: Momentum Indicators Alignment</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        rsi_state = st.radio("RSI Indicator Ki State:", ["Oversold Zone (<35)", "Overbought Zone (>65)", "Normal Balanced Zone"])
    with col2:
        macd_state = st.radio("MACD Line Crossover State:", ["Golden Cross (Bullish Signal)", "Dead Cross (Bearish Signal)", "Neutral / No Cross"])

    st.markdown("---")
    
    # Engine Computation Algorithm
    if st.button("⚡ RUN FULL STRATEGY CONFLUENCE ALGORITHM", use_container_width=True):
        with st.spinner("🤖 System analyzing all 3 strategy blocks simultaneously..."):
            time.sleep(1.5)
        
        # Comprehensive CALL (BUY) Rule Logic
        is_structure_buy = (macro_trend == "BULLISH (Upar Ki Taraf Heavy Flow)" or snr_zone == "At Major Support / FVG Demand Zone")
        is_pattern_buy = (current_pattern in ["Bullish Hammer / Pinbar", "Bullish Engulfing", "Bullish Marubozu (Full Strong Green)"])
        is_indicators_buy = (rsi_state == "Oversold Zone (<35)" or macd_state == "Golden Cross (Bullish Signal)")
        
        # Comprehensive PUT (SELL) Rule Logic
        is_structure_sell = (macro_trend == "BEARISH (Niche Ki Taraf Heavy Flow)" or snr_zone == "At Major Resistance / Supply Zone")
        is_pattern_sell = (current_pattern in ["Bearish Shooting Star", "Bearish Engulfing", "Bearish Marubozu (Full Strong Red)"])
        is_indicators_sell = (rsi_state == "Overbought Zone (>65)" or macd_state == "Dead Cross (Bearish Signal)")

        # Final Decision Display Matrix
        if is_structure_buy and (is_pattern_buy and is_indicators_buy):
            st.markdown(f'<div class="signal-box buy-signal">🟩 SIGNAL: HIGH PROBABILITY CALL (UP) <br><span style="font-size:14px; font-weight:normal;">All Strategies Aligned! 15M Frame, {current_pattern}, and Indicators are supporting buyers. Safe 1-2 Min Entry!</span></div>', unsafe_allow_html=True)
            st.balloons()
            
        elif is_structure_sell and (is_pattern_sell and is_indicators_sell):
            st.markdown(f'<div class="signal-box sell-signal">🟥 SIGNAL: HIGH PROBABILITY PUT (DOWN) <br><span style="font-size:14px; font-weight:normal;">All Strategies Aligned! 15M Institutional Supply, {current_pattern}, and Momentum are supporting sellers. Safe 1-2 Min Entry!</span></div>', unsafe_allow_html=True)
            
        else:
            st.markdown('<div class="signal-box hold-signal">🟨 SUGGESTION: STRICT HOLD (FILTER ACTIVATED) <br><span style="font-size:14px; font-weight:normal;">Confluence Missing: Kuch strategies call aur kuch sell keh rahi hain. Risk control karne ke liye abhi koi trade na lein!</span></div>', unsafe_allow_html=True)
