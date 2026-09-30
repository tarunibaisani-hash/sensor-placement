"""
FloodGuard Quantum AI - Custom CSS & Styling Module
Implements Dark Charcoal, Emerald Green, Gold Highlights, White Text, Glassmorphism,
Hover animations, high-contrast selectbox controls, and Government Command Center UI aesthetics.
"""

def get_custom_css():
    return """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    /* Global Root Variables */
    :root {
        --bg-main: #0e1117;
        --bg-charcoal: #151921;
        --bg-card: rgba(22, 27, 34, 0.92);
        --emerald-primary: #10B981;
        --emerald-glow: rgba(16, 185, 129, 0.35);
        --gold-primary: #F59E0B;
        --gold-glow: rgba(245, 158, 11, 0.35);
        --text-white: #FFFFFF;
        --text-light: #F1F5F9;
        --text-muted: #94A3B8;
        --border-glass: rgba(16, 185, 129, 0.3);
        --danger-red: #EF4444;
        --danger-glow: rgba(239, 68, 68, 0.35);
    }

    /* Base App Styling */
    html, body, [class*="st-emotion"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: var(--text-light) !important;
    }

    .stApp {
        background: radial-gradient(circle at 50% 0%, #17202a 0%, #0e1117 65%, #080a0d 100%) !important;
        color: var(--text-light) !important;
    }

    /* Keep Sidebar ALWAYS Visible & High-Contrast */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #12161f 0%, #0d1017 100%) !important;
        border-right: 1px solid rgba(16, 185, 129, 0.3) !important;
        min-width: 320px !important;
        width: 320px !important;
        box-shadow: 4px 0 24px rgba(0, 0, 0, 0.6) !important;
    }

    /* Sidebar text high contrast override */
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] p {
        color: #F8FAFC !important;
    }

    /* Hide sidebar collapse button */
    [data-testid="stSidebarCollapseButton"], 
    button[kind="header"], 
    [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* Top Header Bar */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Glassmorphism Cards with high contrast */
    .glass-card {
        background: rgba(21, 26, 35, 0.92) !important;
        backdrop-filter: blur(14px) !important;
        -webkit-backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        border-radius: 14px !important;
        padding: 20px 22px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-bottom: 16px !important;
        color: #F1F5F9 !important;
    }

    .glass-card:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(16, 185, 129, 0.6) !important;
        box-shadow: 0 14px 38px rgba(16, 185, 129, 0.2), 0 8px 20px rgba(0, 0, 0, 0.6) !important;
    }

    .glass-card-gold {
        background: rgba(26, 26, 33, 0.92) !important;
        backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(245, 158, 11, 0.4) !important;
        border-radius: 14px !important;
        padding: 20px 22px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45) !important;
        transition: all 0.3s ease !important;
        margin-bottom: 16px !important;
        color: #F1F5F9 !important;
    }

    .glass-card-gold:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(245, 158, 11, 0.8) !important;
        box-shadow: 0 14px 38px rgba(245, 158, 11, 0.25), 0 8px 20px rgba(0, 0, 0, 0.6) !important;
    }

    .glass-card-danger {
        background: rgba(32, 18, 24, 0.92) !important;
        backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(239, 68, 68, 0.45) !important;
        border-radius: 14px !important;
        padding: 20px 22px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45) !important;
        transition: all 0.3s ease !important;
        margin-bottom: 16px !important;
        color: #F1F5F9 !important;
    }

    .glass-card-danger:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(239, 68, 68, 0.85) !important;
        box-shadow: 0 14px 38px rgba(239, 68, 68, 0.3), 0 8px 20px rgba(0, 0, 0, 0.6) !important;
    }

    /* KPI Metric Cards */
    .kpi-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .kpi-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--text-muted);
        margin-bottom: 4px;
    }

    .kpi-value {
        font-size: 2.1rem;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }

    .kpi-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-top: 8px;
    }

    .kpi-badge-emerald {
        background: rgba(16, 185, 129, 0.2);
        color: #10B981 !important;
        border: 1px solid rgba(16, 185, 129, 0.45);
    }

    .kpi-badge-gold {
        background: rgba(245, 158, 11, 0.2);
        color: #F59E0B !important;
        border: 1px solid rgba(245, 158, 11, 0.45);
    }

    .kpi-badge-red {
        background: rgba(239, 68, 68, 0.2);
        color: #EF4444 !important;
        border: 1px solid rgba(239, 68, 68, 0.45);
    }

    /* Header Banner Styling - Government Public Safety Aesthetics */
    .gov-header {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.18) 0%, rgba(245, 158, 11, 0.12) 45%, rgba(18, 22, 30, 0.96) 100%);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 16px;
        padding: 24px 30px;
        margin-bottom: 24px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.55);
    }

    .gov-title {
        font-size: 1.95rem;
        font-weight: 800;
        color: #FFFFFF !important;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
        letter-spacing: -0.01em;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }

    .gov-subtitle {
        font-size: 0.98rem;
        color: #E2E8F0 !important;
        margin-top: 6px;
        font-weight: 500;
        line-height: 1.4;
    }

    .gov-tag {
        display: inline-block;
        background: linear-gradient(90deg, #10B981, #059669);
        color: #0F172A !important;
        font-weight: 800;
        font-size: 0.74rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 6px;
        margin-right: 8px;
    }

    .gold-tag {
        display: inline-block;
        background: linear-gradient(90deg, #F59E0B, #D97706);
        color: #0F172A !important;
        font-weight: 800;
        font-size: 0.74rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 6px;
    }

    /* Sidebar Logo & Branding */
    .sidebar-brand-box {
        padding: 16px 12px 20px 12px;
        border-bottom: 1px solid rgba(16, 185, 129, 0.25);
        margin-bottom: 18px;
    }

    .sidebar-logo-text {
        font-size: 1.35rem;
        font-weight: 800;
        color: #FFFFFF !important;
        letter-spacing: -0.01em;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .sidebar-sub-text {
        font-size: 0.78rem;
        color: var(--gold-primary) !important;
        font-weight: 700;
        letter-spacing: 0.05em;
        margin-top: 4px;
    }

    /* Sidebar Radio Menu Styling */
    div[data-testid="stRadio"] > div {
        gap: 6px;
    }

    div[data-testid="stRadio"] label {
        background: rgba(25, 30, 40, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
        margin-bottom: 4px !important;
        transition: all 0.25s ease !important;
        cursor: pointer !important;
    }

    div[data-testid="stRadio"] label:hover {
        background: rgba(16, 185, 129, 0.18) !important;
        border-color: rgba(16, 185, 129, 0.5) !important;
        transform: translateX(4px) !important;
    }

    div[data-testid="stRadio"] label[data-checked="true"],
    div[data-testid="stRadio"] label:has(input:checked) {
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.28) 0%, rgba(245, 158, 11, 0.18) 100%) !important;
        border-color: var(--emerald-primary) !important;
        border-left: 4px solid var(--emerald-primary) !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3) !important;
    }

    div[data-testid="stRadio"] label span {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
    }

    /* Streamlit Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(16, 185, 129, 0.5) !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.02em !important;
        padding: 10px 24px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35) !important;
        transition: all 0.25s ease !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        box-shadow: 0 6px 22px rgba(16, 185, 129, 0.5) !important;
        transform: translateY(-2px) !important;
    }

    /* Live Pulsing Dot */
    .pulse-dot {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #10B981;
        box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
        animation: pulse 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
        margin-right: 8px;
    }

    .pulse-dot-red {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #EF4444;
        box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7);
        animation: pulse-red 1.5s infinite cubic-bezier(0.66, 0, 0, 1);
        margin-right: 8px;
    }

    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { transform: scale(1.15); box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }

    @keyframes pulse-red {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
        70% { transform: scale(1.15); box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
    }

    /* Custom Ticker Bar */
    .ticker-wrap {
        width: 100%;
        overflow: hidden;
        background: rgba(18, 22, 30, 0.92);
        border: 1px solid rgba(245, 158, 11, 0.4);
        border-radius: 8px;
        padding: 8px 14px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }

    .ticker-title {
        color: var(--gold-primary) !important;
        font-weight: 800;
        font-size: 0.82rem;
        letter-spacing: 0.05em;
        white-space: nowrap;
        margin-right: 14px;
    }

    .ticker-content {
        color: #F1F5F9 !important;
        font-size: 0.86rem;
        font-weight: 500;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(18, 22, 30, 0.7);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(16, 185, 129, 0.25);
    }

    .stTabs [data-baseweb="tab"] {
        color: #94A3B8 !important;
        font-weight: 600;
        padding: 10px 18px;
        border-radius: 8px;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(16, 185, 129, 0.22) !important;
        color: #10B981 !important;
        font-weight: 700 !important;
        border: 1px solid rgba(16, 185, 129, 0.45) !important;
    }

    /* =========================================================
       COMPLETE HIGH-CONTRAST FIX FOR SELECTBOX & DROPDOWNS (MODULE 8 & GLOBAL)
       ========================================================= */
    .stSelectbox label, 
    div[data-testid="stSelectbox"] label,
    .stMultiSelect label {
        color: #F8FAFC !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        margin-bottom: 6px !important;
        display: block !important;
    }

    div[data-baseweb="select"] {
        background-color: #1a222d !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #1a222d !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(16, 185, 129, 0.45) !important;
        border-radius: 10px !important;
        min-height: 44px !important;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #10B981 !important;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.3) !important;
    }

    div[data-baseweb="select"] svg {
        fill: #10B981 !important;
    }

    div[data-baseweb="select"] span, 
    div[data-baseweb="select"] div,
    div[data-baseweb="select"] input {
        color: #FFFFFF !important;
        background-color: transparent !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* Dropdown Popover List Container */
    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"],
    [data-baseweb="popover"] > div {
        background-color: #151921 !important;
        border: 1px solid rgba(16, 185, 129, 0.5) !important;
        border-radius: 10px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85) !important;
        color: #FFFFFF !important;
    }

    /* Dropdown Option Items */
    li[role="option"],
    div[role="option"],
    div[data-baseweb="option"],
    [data-baseweb="menu"] li {
        background-color: #151921 !important;
        color: #F8FAFC !important;
        font-weight: 600 !important;
        font-size: 0.94rem !important;
        padding: 12px 16px !important;
        cursor: pointer !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* Option Hover & Active States */
    li[role="option"]:hover,
    li[role="option"][aria-selected="true"],
    div[role="option"]:hover,
    div[data-baseweb="option"]:hover,
    [data-baseweb="menu"] li:hover,
    [data-baseweb="menu"] li[aria-selected="true"] {
        background-color: rgba(16, 185, 129, 0.25) !important;
        color: #10B981 !important;
        font-weight: 800 !important;
        border-left: 4px solid #10B981 !important;
    }

    /* Leaflet Popups and Map Layers */
    .leaflet-popup-content-wrapper, .leaflet-popup-tip {
        background: #151921 !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(16, 185, 129, 0.5) !important;
        border-radius: 10px !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.75) !important;
    }

    .leaflet-popup-content {
        color: #F1F5F9 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        line-height: 1.5 !important;
    }

    .leaflet-popup-content h4, .leaflet-popup-content strong {
        color: #FFFFFF !important;
    }

    .leaflet-container a.leaflet-popup-close-button {
        color: #94A3B8 !important;
    }
    .leaflet-container a.leaflet-popup-close-button:hover {
        color: #10B981 !important;
    }

    /* Streamlit DataFrame / Table Dark High-Contrast Styling */
    [data-testid="stDataFrame"], [data-testid="stTable"] {
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }

    div[data-testid="stDataFrame"] table {
        background-color: #151921 !important;
        color: #F8FAFC !important;
    }

    div[data-testid="stDataFrame"] th {
        background-color: #1a222d !important;
        color: #10B981 !important;
        font-weight: 700 !important;
        border-bottom: 1px solid rgba(16, 185, 129, 0.3) !important;
    }

    div[data-testid="stDataFrame"] td {
        background-color: #151921 !important;
        color: #E2E8F0 !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    input, textarea {
        background-color: #151921 !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(16, 185, 129, 0.4) !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
    }

    /* Footer styling */
    .app-footer {
        text-align: center;
        padding: 24px 10px 12px 10px;
        margin-top: 40px;
        border-top: 1px solid rgba(16, 185, 129, 0.25);
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 500;
    }

    .app-footer span {
        color: var(--gold-primary);
        font-weight: 700;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0b0e14;
    }
    ::-webkit-scrollbar-thumb {
        background: #1e2634;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #10B981;
    }
    </style>
    """
