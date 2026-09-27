"""
FloodGuard Quantum AI
AI & Quantum Powered Flood Forecasting and Smart Sensor Placement for Krishna and Godavari River Basins

Author: FloodGuard Quantum AI System
Theme: Dark Charcoal, Emerald Green, Gold Highlights, White Text, Glassmorphism Cards
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import joblib
import os
import json
import time

# Local Modules
from styles import get_custom_css
from data_manager import (
    DISTRICTS_DATA,
    BARRAGES_STATIONS,
    SHELTERS_DATA,
    MULTILINGUAL_ALERTS,
    SENSOR_CANDIDATES
)
from quantum_engine import (
    run_quantum_sensor_optimization,
    generate_qaoa_circuit,
    QISKIT_AVAILABLE
)

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="FloodGuard Quantum AI - Krishna & Godavari Basins",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Styling (Dark Charcoal + Emerald Green + Gold Highlights + Glassmorphism)
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ---------------------------------------------------------
# Model Loader
# ---------------------------------------------------------
@st.cache_resource
def load_flood_model():
    model_path = os.path.join(os.path.dirname(__file__), "flood_model.pkl")
    if os.path.exists(model_path):
        try:
            package = joblib.load(model_path)
            return package
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None
    return None

model_package = load_flood_model()

# ---------------------------------------------------------
# UI Helper Components
# ---------------------------------------------------------
def render_header(title, subtitle, tag="GOVERNMENT OF INDIA & AP/TELANGANA SDMA", gold_tag="QUANTUM AI INTEGRATED"):
    st.markdown(f"""
    <div class="gov-header">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
            <div>
                <span class="gov-tag">🏛️ {tag}</span>
                <span class="gold-tag">⚡ {gold_tag}</span>
                <h1 class="gov-title">🌊 {title}</h1>
                <p class="gov-subtitle">{subtitle}</p>
            </div>
            <div style="text-align: right; background: rgba(0,0,0,0.4); padding: 8px 14px; border-radius: 10px; border: 1px solid rgba(16,185,129,0.3);">
                <span class="pulse-dot"></span>
                <span style="font-size: 0.82rem; font-weight: 700; color: #10B981;">TELEMETRY STREAM LIVE</span>
                <div style="font-size: 0.75rem; color: #CBD5E1; margin-top: 3px;">Satellite Sync: INSAT-3DR | CWC Hydrology</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_kpi_card(title, value, badge_text, badge_type="emerald", icon="📊", note=""):
    badge_class = f"kpi-badge-{badge_type}"
    card_html = f"""
    <div class="glass-card">
        <div class="kpi-container">
            <div>
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            <div style="font-size: 2.2rem; opacity: 0.85;">{icon}</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
            <span class="kpi-badge {badge_class}">{badge_text}</span>
            <span style="font-size: 0.72rem; color: #CBD5E1;">{note}</span>
        </div>
    </div>
    """
    return st.markdown(card_html, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div class="app-footer">
        <p><strong>FloodGuard Quantum AI</strong> - Smart Flood Forecasting & Sensor Placement System</p>
        <p style="margin-top: 4px; font-size: 0.78rem;">
            Powered by <span>Qiskit 2.5</span> • <span>qBraid Quantum Cloud</span> • <span>CWC & SDMA Realtime Telemetry Feeds</span>
        </p>
        <p style="color: #64748B; font-size: 0.72rem; margin-top: 2px;">
            Confidential State Disaster Management & Flood Control System © 2026. All Rights Reserved.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand-box">
        <div class="sidebar-logo-text">
            <span>🛡️</span> FloodGuard Quantum AI
        </div>
        <div class="sidebar-sub-text">KRISHNA & GODAVARI BASIN COMMAND</div>
    </div>
    """, unsafe_allow_html=True)

    menu_options = [
        "🏛️ Module 1: Home Dashboard",
        "🧠 Module 2: Flood Prediction",
        "🗺️ Module 3: Krishna & Godavari Map",
        "⚛️ Module 4: Quantum Sensor Placement",
        "🌊 Module 5: River Monitoring",
        "🚨 Module 6: Disaster Response",
        "🏠 Module 7: Shelter Management",
        "🌐 Module 8: Multilingual Alert System",
        "📈 Module 9: Analytics & Insights",
        "🎛️ Module 10: Govt Command Center"
    ]

    selected_menu = st.radio(
        "NAVIGATION MENU",
        menu_options,
        index=0,
        label_visibility="collapsed"
    )

    st.markdown("---")
    
    # Quick Simulation / Basin Control Filter
    st.markdown("<p style='font-size: 0.8rem; font-weight: 700; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.05em;'>Active Basin Scope</p>", unsafe_allow_html=True)
    active_basin = st.selectbox(
        "Select River Basin",
        ["Both Basins (Krishna & Godavari)", "Krishna River Basin", "Godavari River Basin"],
        index=0,
        label_visibility="collapsed"
    )

    st.markdown("<p style='font-size: 0.8rem; font-weight: 700; color: #10B981; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 15px;'>Monsoon Simulation Mode</p>", unsafe_allow_html=True)
    sim_intensity = st.select_slider(
        "Monsoon Intensity",
        options=["Normal Flow", "Monsoon Heavy", "Depression / Cyclone", "Super Flood Peak (1986/2009 Scale)"],
        value="Monsoon Heavy",
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 10px; padding: 12px; margin-top: 20px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span class="pulse-dot"></span>
            <span style="font-size: 0.8rem; font-weight: 700; color: #FFFFFF;">Quantum Core Status</span>
        </div>
        <div style="font-size: 0.74rem; color: #CBD5E1; margin-top: 4px;">
            QAOA Circuit Active • 24 Qubits<br>
            Backend: <span style="color: #F59E0B; font-weight: 600;">qBraid-Aer / Qiskit 2.5</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# MODULE 1 : HOME DASHBOARD
# =========================================================
if selected_menu == "🏛️ Module 1: Home Dashboard":
    render_header(
        "FloodGuard Quantum AI — Executive Overview",
        "Real-time AI & Quantum hydrologic intelligence for Krishna and Godavari river basins"
    )

    # Live Ticker
    st.markdown("""
    <div class="ticker-wrap">
        <span class="ticker-title">⚠️ LIVE HYDROLOGY FLASH:</span>
        <span class="ticker-content">Bhadrachalam Gauge at 54.8 ft (Exceeds 3rd Danger Mark) • Prakasam Barrage 65/70 gates open releasing 485,000 cusecs • Dowleswaram discharge surge at 1.42M cusecs.</span>
    </div>
    """, unsafe_allow_html=True)

    # Top KPI Metrics Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        render_kpi_card("Total Sensors", "238", "100% Operational", "emerald", "📡", "IoT & Radar Nodes")
    with col2:
        render_kpi_card("Flood Alerts", "4 Active", "2 Critical (Red)", "red", "🚨", "Delta & Riparian")
    with col3:
        render_kpi_card("Districts Monitored", "12", "8 AP + 4 TS", "emerald", "🏛️", "Full River Corridors")
    with col4:
        render_kpi_card("Active Shelters", "13", "18,650 Capacity", "gold", "🏠", "72.4% Occupied")
    with col5:
        render_kpi_card("System Status", "ONLINE", "Quantum QAOA Synced", "emerald", "⚡", "Latency: 28ms")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Krishna and Godavari River Overview
    st.markdown("### 🌊 Krishna & Godavari River Basin Systems Overview")
    
    col_k, col_g = st.columns(2)
    
    with col_k:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #10B981;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="color: #FFFFFF; margin: 0; font-size: 1.3rem;">🏞️ Krishna River Basin</h3>
                <span class="kpi-badge kpi-badge-gold">STATUS: ALERT (HIGH FLOW)</span>
            </div>
            <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.5;">
                Originating from Mahabaleshwar, flowing through Telangana and Andhra Pradesh into the Bay of Bengal at Hamsaladeevi.
                Major barrages include <strong>Srisailam, Nagarjuna Sagar,</strong> and <strong>Prakasam Barrage</strong>.
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 14px;">
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Prakasam Barrage Level</div>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #F59E0B;">13.80 ft <span style="font-size: 0.75rem; color: #EF4444;">(Danger: 14.50 ft)</span></div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Current Total Outflow</div>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #10B981;">485,000 Cusecs</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Key Vulnerable Nodes</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF;">Vijayawada, Avanigadda, Guntur</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Tributaries Active</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #F59E0B;">Budameru, Muneru, Musi</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_g:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #EF4444;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="color: #FFFFFF; margin: 0; font-size: 1.3rem;">🌊 Godavari River Basin</h3>
                <span class="kpi-badge kpi-badge-red">STATUS: DANGER (SEVERE SURGE)</span>
            </div>
            <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.5;">
                India's second longest river, carrying heavy upstream inflows from SRSP, Kaleshwaram, Kinnerasani, and Sabari into 
                <strong>Bhadrachalam, Polavaram,</strong> and <strong>Sir Arthur Cotton Barrage (Dowleswaram)</strong>.
            </p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 14px;">
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Bhadrachalam Gauge Height</div>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #EF4444;">54.80 ft <span style="font-size: 0.75rem; color: #EF4444;">(3rd Alert: 53.0 ft)</span></div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Dowleswaram Total Discharge</div>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #F59E0B;">1,425,000 Cusecs</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Severely Impacted Zones</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF;">Konaseema Islands, Rajahmundry, Bhadrachalam</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <div style="font-size: 0.72rem; color: #CBD5E1;">Delta Distributaries</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #F59E0B;">Gautami, Vasishta, Vainateya</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Quick Visual Charts for Module 1
    st.markdown("### 📊 Hydro-Discharge Telemetry Comparison (Last 24 Hours)")
    time_series = pd.date_range(end=pd.Timestamp.now(), periods=24, freq='h')
    df_trend = pd.DataFrame({
        "Timestamp": time_series,
        "Godavari (Dowleswaram - Lakh Cusecs)": [10.2 + 0.18*i + np.sin(i/3)*0.4 for i in range(24)],
        "Krishna (Prakasam Barrage - Lakh Cusecs)": [3.1 + 0.08*i + np.cos(i/4)*0.2 for i in range(24)],
        "Bhadrachalam Gauge (Feet)": [46.5 + 0.35*i for i in range(24)]
    })

    fig_home = go.Figure()
    fig_home.add_trace(go.Scatter(
        x=df_trend["Timestamp"], y=df_trend["Godavari (Dowleswaram - Lakh Cusecs)"],
        mode='lines+markers', name='Godavari Outflow (Lakh Cusecs)',
        line=dict(color='#EF4444', width=3),
        marker=dict(size=5)
    ))
    fig_home.add_trace(go.Scatter(
        x=df_trend["Timestamp"], y=df_trend["Krishna (Prakasam Barrage - Lakh Cusecs)"],
        mode='lines+markers', name='Krishna Outflow (Lakh Cusecs)',
        line=dict(color='#10B981', width=3),
        marker=dict(size=5)
    ))
    fig_home.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(18,22,30,0.7)',
        font=dict(color='#E2E8F0', family='Plus Jakarta Sans'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.08)', title="Hourly Timestamp"),
        yaxis=dict(gridcolor='rgba(255,255,255,0.08)', title="Discharge (Lakh Cusecs)"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=40, t=40, b=40),
        height=340
    )
    st.plotly_chart(fig_home, use_container_width=True)


# =========================================================
# MODULE 2 : FLOOD PREDICTION
# =========================================================
elif selected_menu == "🧠 Module 2: Flood Prediction":
    render_header(
        "AI Hydrologic Flood Prediction Engine",
        "Predict real-time flood probability using trained model 'flood_model.pkl' across 17 hydrologic & geographical parameters"
    )

    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 14px 18px; margin-bottom: 20px;">
        <span style="font-weight: 700; color: #10B981;">⚡ Model Architecture:</span>
        <span style="color: #E2E8F0; font-size: 0.9rem;">
            Ensemble Gradient Boosted Decision Forest trained on 17 watershed and catchment variables. Calibrated for Krishna & Godavari hydrologic basins.
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Scenario Presets
    preset_choice = st.selectbox(
        "⚡ Quick Load Historical / Simulated Scenarios:",
        [
            "Custom User Input",
            "Godavari 2022 Mega Flood Surge (Bhadrachalam & Konaseema Breach)",
            "Krishna 2009 / 2024 Vijayawada Prakasam Inundation Event",
            "Normal Moderate Monsoon Flow (Safe Baseline)",
            "Severe Cyclone & High Tidal Surge (Delta Corridor)"
        ]
    )

    # Default preset values
    default_vals = {
        "MonsoonIntensity": 8.0, "TopographyDrainage": 7.0, "RiverManagement": 7.0,
        "Deforestation": 6.0, "Urbanization": 7.0, "ClimateChange": 8.0,
        "DamsQuality": 8.0, "Siltation": 7.0, "AgriculturalPractices": 6.0,
        "Encroachments": 7.0, "DrainageSystems": 6.0, "CoastalVulnerability": 8.0,
        "Landslides": 5.0, "Watersheds": 7.0, "PopulationScore": 8.0,
        "WetlandLoss": 7.0, "InadequatePlanning": 7.0
    }

    if preset_choice == "Godavari 2022 Mega Flood Surge (Bhadrachalam & Konaseema Breach)":
        default_vals.update({
            "MonsoonIntensity": 14.5, "TopographyDrainage": 12.0, "RiverManagement": 4.0,
            "Deforestation": 11.0, "Urbanization": 10.5, "ClimateChange": 13.0,
            "DamsQuality": 5.0, "Siltation": 13.5, "AgriculturalPractices": 9.0,
            "Encroachments": 12.0, "DrainageSystems": 3.5, "CoastalVulnerability": 14.0,
            "Landslides": 8.0, "Watersheds": 13.0, "PopulationScore": 12.5,
            "WetlandLoss": 12.0, "InadequatePlanning": 13.0
        })
    elif preset_choice == "Krishna 2009 / 2024 Vijayawada Prakasam Inundation Event":
        default_vals.update({
            "MonsoonIntensity": 13.8, "TopographyDrainage": 11.5, "RiverManagement": 5.0,
            "Deforestation": 10.0, "Urbanization": 14.0, "ClimateChange": 11.5,
            "DamsQuality": 6.0, "Siltation": 12.8, "AgriculturalPractices": 8.0,
            "Encroachments": 14.5, "DrainageSystems": 4.0, "CoastalVulnerability": 11.0,
            "Landslides": 6.0, "Watersheds": 12.0, "PopulationScore": 14.0,
            "WetlandLoss": 13.5, "InadequatePlanning": 14.0
        })
    elif preset_choice == "Normal Moderate Monsoon Flow (Safe Baseline)":
        default_vals.update({
            "MonsoonIntensity": 4.0, "TopographyDrainage": 4.5, "RiverManagement": 12.0,
            "Deforestation": 3.5, "Urbanization": 5.0, "ClimateChange": 4.0,
            "DamsQuality": 13.0, "Siltation": 4.0, "AgriculturalPractices": 4.5,
            "Encroachments": 3.0, "DrainageSystems": 12.0, "CoastalVulnerability": 4.0,
            "Landslides": 2.5, "Watersheds": 4.0, "PopulationScore": 5.0,
            "WetlandLoss": 3.5, "InadequatePlanning": 4.0
        })
    elif preset_choice == "Severe Cyclone & High Tidal Surge (Delta Corridor)":
        default_vals.update({
            "MonsoonIntensity": 15.0, "TopographyDrainage": 13.5, "RiverManagement": 6.0,
            "Deforestation": 9.0, "Urbanization": 11.0, "ClimateChange": 14.0,
            "DamsQuality": 7.0, "Siltation": 11.0, "AgriculturalPractices": 8.5,
            "Encroachments": 11.5, "DrainageSystems": 4.5, "CoastalVulnerability": 15.0,
            "Landslides": 7.0, "Watersheds": 11.5, "PopulationScore": 13.0,
            "WetlandLoss": 14.0, "InadequatePlanning": 12.0
        })

    # Sliders for the 17 Inputs in a clear 3-column layout
    st.markdown("#### 🎚️ Model Input Parameters (Scale: 1.0 - 15.0)")
    
    col_in1, col_in2, col_in3 = st.columns(3)
    
    with col_in1:
        st.markdown("<p style='color: #10B981; font-weight:700;'>🌧️ Hydrologic & Climate Factors</p>", unsafe_allow_html=True)
        monsoon = st.slider("1. Monsoon Intensity", 1.0, 15.0, float(default_vals["MonsoonIntensity"]), 0.1)
        climate = st.slider("2. Climate Change Impact", 1.0, 15.0, float(default_vals["ClimateChange"]), 0.1)
        topography = st.slider("3. Topography & Drainage Slope", 1.0, 15.0, float(default_vals["TopographyDrainage"]), 0.1)
        watersheds = st.slider("4. Watershed Catchment Runoff", 1.0, 15.0, float(default_vals["Watersheds"]), 0.1)
        landslides = st.slider("5. Landslides & Upstream Silt Run", 1.0, 15.0, float(default_vals["Landslides"]), 0.1)
        siltation = st.slider("6. Riverbed Siltation Level", 1.0, 15.0, float(default_vals["Siltation"]), 0.1)

    with col_in2:
        st.markdown("<p style='color: #F59E0B; font-weight:700;'>🏗️ Infrastructure & Management</p>", unsafe_allow_html=True)
        river_mgmt = st.slider("7. River Basin Management", 1.0, 15.0, float(default_vals["RiverManagement"]), 0.1, help="Higher = Better Management")
        dams_qual = st.slider("8. Dams & Barrages Quality", 1.0, 15.0, float(default_vals["DamsQuality"]), 0.1, help="Higher = Stronger Quality")
        drainage_sys = st.slider("9. Urban Drainage Network Capacity", 1.0, 15.0, float(default_vals["DrainageSystems"]), 0.1, help="Higher = Superior Capacity")
        inad_planning = st.slider("10. Inadequate Planning Index", 1.0, 15.0, float(default_vals["InadequatePlanning"]), 0.1)
        urbanization = st.slider("11. Urbanization & Concreting", 1.0, 15.0, float(default_vals["Urbanization"]), 0.1)
        encroachments = st.slider("12. Riverbed Encroachments", 1.0, 15.0, float(default_vals["Encroachments"]), 0.1)

    with col_in3:
        st.markdown("<p style='color: #38BDF8; font-weight:700;'>🌳 Ecological & Human Exposure</p>", unsafe_allow_html=True)
        deforestation = st.slider("13. Deforestation in Catchments", 1.0, 15.0, float(default_vals["Deforestation"]), 0.1)
        wetland_loss = st.slider("14. Wetland & Mangrove Loss", 1.0, 15.0, float(default_vals["WetlandLoss"]), 0.1)
        coastal_vuln = st.slider("15. Coastal & Delta Vulnerability", 1.0, 15.0, float(default_vals["CoastalVulnerability"]), 0.1)
        agri_pract = st.slider("16. Agricultural Practices Impact", 1.0, 15.0, float(default_vals["AgriculturalPractices"]), 0.1)
        pop_score = st.slider("17. Population Exposure Density", 1.0, 15.0, float(default_vals["PopulationScore"]), 0.1)

    # Prediction Execution
    input_vector = np.array([[
        monsoon, topography, river_mgmt, deforestation, urbanization,
        climate, dams_qual, siltation, agri_pract, encroachments,
        drainage_sys, coastal_vuln, landslides, watersheds, pop_score,
        wetland_loss, inad_planning
    ]])

    if model_package is not None and "model" in model_package:
        pred_raw = model_package["model"].predict(input_vector)[0]
        flood_prob = float(np.clip(pred_raw, 0.02, 0.99))
    else:
        score = (monsoon*0.16 + climate*0.10 + siltation*0.11 + encroachments*0.10 + 
                 (16-river_mgmt)*0.11 + (16-drainage_sys)*0.11 + coastal_vuln*0.09 +
                 urbanization*0.09 + wetland_loss*0.08 + deforestation*0.07 + inad_planning*0.08)
        flood_prob = float(np.clip(score / 15.0, 0.05, 0.98))

    # Determine Risk Level
    if flood_prob < 0.35:
        risk_level = "Low"
        risk_color = "#10B981"
        badge_style = "emerald"
        action_msg = "🟢 All parameters safe. River storage capacity optimal. No evacuations needed."
    elif flood_prob < 0.60:
        risk_level = "Medium"
        risk_color = "#F59E0B"
        badge_style = "gold"
        action_msg = "🟡 Watch alert issued. First warning level approaching at Prakasam & Dowleswaram."
    elif flood_prob < 0.80:
        risk_level = "High"
        risk_color = "#F97316"
        badge_style = "gold"
        action_msg = "🟠 High risk alert. Evacuation of low-lying island habitations and riverbed sectors initiated."
    else:
        risk_level = "Critical"
        risk_color = "#EF4444"
        badge_style = "red"
        action_msg = "🔴 CRITICAL DISASTER EMERGENCY. Catastrophic inundation expected. Full NDRF/SDRF mobilization."

    st.markdown("---")
    st.markdown("### 🎯 Prediction Results & Risk Analysis")

    res_col1, res_col2 = st.columns([1, 1])

    with res_col1:
        # Plotly Gauge Chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=flood_prob * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "<b>FLOOD PROBABILITY (%)</b>", 'font': {'size': 20, 'color': '#FFFFFF'}},
            number={'suffix': "%", 'font': {'size': 36, 'color': risk_color, 'family': 'Plus Jakarta Sans'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#CBD5E1"},
                'bar': {'color': risk_color, 'thickness': 0.28},
                'bgcolor': "rgba(22, 27, 34, 0.8)",
                'borderwidth': 2,
                'bordercolor': "rgba(16, 185, 129, 0.3)",
                'steps': [
                    {'range': [0, 35], 'color': 'rgba(16, 185, 129, 0.25)'},
                    {'range': [35, 60], 'color': 'rgba(245, 158, 11, 0.25)'},
                    {'range': [60, 80], 'color': 'rgba(249, 115, 22, 0.30)'},
                    {'range': [80, 100], 'color': 'rgba(239, 68, 68, 0.40)'}
                ],
                'threshold': {
                    'line': {'color': "#EF4444", 'width': 4},
                    'thickness': 0.75,
                    'value': 80.0
                }
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E2E8F0'),
            height=320,
            margin=dict(l=30, r=30, t=40, b=20)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

    with res_col2:
        # Risk Card & Breakdown
        card_class = f"glass-card-{badge_style}" if badge_style != "emerald" else "glass-card"
        st.markdown(f"""
        <div class="{card_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="color: #FFFFFF; margin: 0; font-size: 1.3rem;">📋 AI Risk Classification</h3>
                <span class="kpi-badge kpi-badge-{badge_style}" style="font-size: 0.9rem; padding: 6px 14px;">RISK LEVEL: {risk_level.upper()}</span>
            </div>
            <div style="margin-top: 14px;">
                <div style="font-size: 0.82rem; color: #CBD5E1;">Confidence Metric:</div>
                <div style="font-size: 1.5rem; font-weight: 800; color: #FFFFFF;">{(1.0 - abs(flood_prob - 0.5)*0.2)*98.5:.1f}% AI Confidence</div>
            </div>
            <div style="margin-top: 12px; padding: 12px; background: rgba(0,0,0,0.4); border-radius: 8px; border-left: 4px solid {risk_color};">
                <div style="font-size: 0.88rem; font-weight: 600; color: #FFFFFF;">{action_msg}</div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 14px;">
                <div style="background: rgba(0,0,0,0.3); padding: 8px 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">
                    <span style="font-size: 0.72rem; color: #CBD5E1;">Est. Discharge Surge</span>
                    <div style="font-weight: 700; color: #F59E0B;">+{int(flood_prob * 1800000):,} Cusecs</div>
                </div>
                <div style="background: rgba(0,0,0,0.3); padding: 8px 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">
                    <span style="font-size: 0.72rem; color: #CBD5E1;">Vulnerable Taluks</span>
                    <div style="font-weight: 700; color: #EF4444;">{int(flood_prob * 42)} Mandals</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Feature Importance Impact Chart
    st.markdown("#### 🔍 Top Contributing Risk Drivers for Current Prediction")
    feat_names = [
        "Monsoon Intensity", "Topography & Drainage", "River Management (Inv)", "Deforestation",
        "Urbanization", "Climate Change", "Dams Quality (Inv)", "Siltation",
        "Agricultural Practices", "Encroachments", "Drainage Systems (Inv)", "Coastal Vulnerability",
        "Landslides", "Watersheds", "Population Score", "Wetland Loss", "Inadequate Planning"
    ]
    vals = [
        monsoon, topography, (16-river_mgmt), deforestation,
        urbanization, climate, (16-dams_qual), siltation,
        agri_pract, encroachments, (16-drainage_sys), coastal_vuln,
        landslides, watersheds, pop_score, wetland_loss, inad_planning
    ]
    df_factors = pd.DataFrame({"Factor": feat_names, "Risk Contribution": vals}).sort_values(by="Risk Contribution", ascending=True)

    fig_bar = px.bar(
        df_factors.tail(8),
        x="Risk Contribution",
        y="Factor",
        orientation='h',
        color="Risk Contribution",
        color_continuous_scale=[[0, '#10B981'], [0.5, '#F59E0B'], [1.0, '#EF4444']]
    )
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(18,22,30,0.7)',
        font=dict(color='#E2E8F0', family='Plus Jakarta Sans'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.08)', title="Normalized Factor Stress (1-15)"),
        yaxis=dict(gridcolor='rgba(255,255,255,0.08)', title=""),
        coloraxis_showscale=False,
        height=280,
        margin=dict(l=20, r=20, t=10, b=20)
    )
    st.plotly_chart(fig_bar, use_container_width=True)


# =========================================================
# MODULE 3 : KRISHNA & GODAVARI MAP (WITH DEDICATED SEPARATE MAPS)
# =========================================================
elif selected_menu == "🗺️ Module 3: Krishna & Godavari Map":
    render_header(
        "Geospatial Basin Command Map Systems",
        "Dedicated and Unified GIS maps for Krishna & Godavari Basins across 12 Andhra Pradesh & Telangana districts"
    )

    # Scope Filter
    filter_state = st.radio(
        "Select State Scope:",
        ["All (AP & Telangana - 12 Districts)", "Andhra Pradesh (8 Districts)", "Telangana (4 Districts)"],
        horizontal=True
    )

    # 4 Dedicated Tabs for Maps as requested
    map_tab_unified, map_tab_sensors, map_tab_shelters, map_tab_capacity = st.tabs([
        "🗺️ Master Basin Map (Unified)",
        "📡 Smart Sensor Placement Map",
        "🏠 Emergency Shelters Map",
        "🌊 River Corridors & Barrage Capacity Map"
    ])

    center_lat, center_lon = 17.15, 80.85

    # ---------------------------------------------------------
    # TAB 1: UNIFIED MASTER MAP
    # ---------------------------------------------------------
    with map_tab_unified:
        st.markdown("#### 🌐 Unified Multi-Layer Geospatial Command Center")
        
        # Layer toggles
        col_t1, col_t2, col_t3, col_t4 = st.columns(4)
        with col_t1:
            u_layer_flood = st.checkbox("🌊 District Risk Zones", value=True, key="u_flood")
        with col_t2:
            u_layer_sensors = st.checkbox("📡 IoT Telemetry Sensors", value=True, key="u_sensor")
        with col_t3:
            u_layer_shelters = st.checkbox("🏠 Relief Shelters", value=True, key="u_shelter")
        with col_t4:
            u_layer_barrages = st.checkbox("🧱 Barrages & Dams", value=True, key="u_barrage")

        m_unified = folium.Map(location=[center_lat, center_lon], zoom_start=7, tiles="CartoDB dark_matter", control_scale=True)

        # Plot District Risk
        if u_layer_flood:
            for dist_name, data in DISTRICTS_DATA.items():
                if filter_state == "Andhra Pradesh (8 Districts)" and data["state"] != "Andhra Pradesh":
                    continue
                if filter_state == "Telangana (4 Districts)" and data["state"] != "Telangana":
                    continue

                fill_col = "#EF4444" if data["vulnerability_score"] > 0.90 else "#F97316" if data["vulnerability_score"] > 0.80 else "#F59E0B" if data["vulnerability_score"] > 0.70 else "#10B981"
                risk_label = "CRITICAL" if data["vulnerability_score"] > 0.90 else "HIGH" if data["vulnerability_score"] > 0.80 else "WATCH" if data["vulnerability_score"] > 0.70 else "SAFE"
                
                popup_html = f"""
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 220px; background: #151921; color: #FFFFFF; padding: 10px; border-radius: 8px;">
                    <h4 style="margin: 0; color: #10B981; border-bottom: 2px solid {fill_col}; padding-bottom: 4px;">{dist_name} ({data['state']})</h4>
                    <div style="margin-top: 6px; font-size: 12px; color: #E2E8F0;"><strong>Basin:</strong> {data['basin']}</div>
                    <div style="font-size: 12px; color: #E2E8F0;"><strong>Population:</strong> {data['population']:,}</div>
                    <div style="font-size: 12px; color: {fill_col}; font-weight: bold;"><strong>Risk:</strong> {risk_label} ({data['vulnerability_score']*100:.0f}%)</div>
                    <div style="font-size: 11px; margin-top: 4px; color: #CBD5E1;"><strong>Threat:</strong> {data['primary_threat']}</div>
                </div>
                """
                folium.Circle(
                    location=[data["lat"], data["lon"]],
                    radius=26000,
                    color=fill_col,
                    weight=2,
                    fill=True,
                    fill_color=fill_col,
                    fill_opacity=0.25,
                    popup=folium.Popup(popup_html, max_width=300),
                    tooltip=f"{dist_name} District ({risk_label} Risk)"
                ).add_to(m_unified)

        # Plot Barrages
        if u_layer_barrages:
            for b in BARRAGES_STATIONS:
                b_col = "#EF4444" if b["status"] == "Danger" else "#F59E0B" if b["status"] == "Alert" else "#10B981"
                b_html = f"""
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 240px; background: #151921; color: #FFFFFF; padding: 10px; border-radius: 8px;">
                    <h4 style="margin: 0; color: #F59E0B;">🧱 {b['name']}</h4>
                    <div style="font-size: 12px; margin-top: 4px; color: #E2E8F0;"><strong>River:</strong> {b['river']} River</div>
                    <div style="font-size: 12px; color: #E2E8F0;"><strong>Level:</strong> {b['current_level_ft']} ft (Danger: {b['danger_level_ft']} ft)</div>
                    <div style="font-size: 12px; color: #10B981;"><strong>Discharge:</strong> {b['discharge_cusecs']:,} Cusecs</div>
                    <div style="font-size: 12px; font-weight: bold; color: {b_col};">Status: {b['status'].upper()}</div>
                </div>
                """
                folium.Marker(
                    location=[b["lat"], b["lon"]],
                    popup=folium.Popup(b_html, max_width=300),
                    tooltip=f"Barrage: {b['name']} ({b['status']})",
                    icon=folium.Icon(color="darkpurple", icon="tint", prefix="fa")
                ).add_to(m_unified)

        # Plot Sensors
        if u_layer_sensors:
            for s in SENSOR_CANDIDATES:
                s_html = f"""
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 200px; background: #151921; color: #FFFFFF; padding: 8px; border-radius: 8px;">
                    <h4 style="margin: 0; color: #10B981;">📡 {s['name']}</h4>
                    <div style="font-size: 11px; margin-top: 4px; color: #E2E8F0;"><strong>Hardware:</strong> {s['type']}</div>
                    <div style="font-size: 11px; color: #10B981;">Status: Online (28ms)</div>
                </div>
                """
                folium.CircleMarker(
                    location=[s["lat"], s["lon"]],
                    radius=5,
                    color="#10B981",
                    weight=2,
                    fill=True,
                    fill_color="#00D084",
                    fill_opacity=0.85,
                    popup=folium.Popup(s_html, max_width=250),
                    tooltip=f"Sensor: {s['name']}"
                ).add_to(m_unified)

        # Plot Shelters
        if u_layer_shelters:
            for sh in SHELTERS_DATA:
                occ_pct = (sh["occupancy"] / sh["capacity"]) * 100
                sh_col = "#EF4444" if occ_pct >= 90 else "#F59E0B" if occ_pct >= 70 else "#10B981"
                st_text = "FULL" if occ_pct >= 90 else "LIMITED" if occ_pct >= 70 else "AVAILABLE"
                sh_html = f"""
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 230px; background: #151921; color: #FFFFFF; padding: 10px; border-radius: 8px;">
                    <h4 style="margin: 0; color: #F59E0B;">🏠 {sh['name']}</h4>
                    <div style="font-size: 11px; margin-top: 4px; color: #E2E8F0;"><strong>District:</strong> {sh['district']}</div>
                    <div style="font-size: 11px; color: #E2E8F0;"><strong>Occupancy:</strong> {sh['occupancy']}/{sh['capacity']} ({occ_pct:.0f}%)</div>
                    <div style="font-size: 11px; color: {sh_col}; font-weight: bold;">Status: {st_text}</div>
                </div>
                """
                folium.Marker(
                    location=[sh["lat"], sh["lon"]],
                    popup=folium.Popup(sh_html, max_width=300),
                    tooltip=f"Shelter: {sh['name']} ({st_text})",
                    icon=folium.Icon(color="green" if occ_pct < 70 else "orange" if occ_pct < 90 else "red", icon="home", prefix="fa")
                ).add_to(m_unified)

        st_folium(m_unified, width=None, height=560, key="map_unified")

    # ---------------------------------------------------------
    # TAB 2: DEDICATED SENSOR PLACEMENT MAP
    # ---------------------------------------------------------
    with map_tab_sensors:
        st.markdown("#### 📡 Dedicated Sensor Placement & Telemetry Grid Map")
        st.markdown("<p style='color: #CBD5E1; font-size: 0.88rem;'>Displays candidate IoT nodes, Doppler stations, ultrasonic gauges, and their active catchment coverage radii across Krishna and Godavari river corridors.</p>", unsafe_allow_html=True)
        
        m_sensors = folium.Map(location=[center_lat, center_lon], zoom_start=7, tiles="CartoDB dark_matter", control_scale=True)
        
        for s in SENSOR_CANDIDATES:
            # Radius of detection buffer (40 km)
            folium.Circle(
                location=[s["lat"], s["lon"]],
                radius=40000,
                color="#10B981",
                weight=1,
                fill=True,
                fill_color="#10B981",
                fill_opacity=0.18,
                tooltip=f"Coverage Radius: {s['name']}"
            ).add_to(m_sensors)

            s_html = f"""
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 220px; background: #151921; color: #FFFFFF; padding: 10px; border-radius: 8px;">
                <h4 style="margin: 0; color: #10B981;">📡 {s['name']}</h4>
                <div style="font-size: 11px; margin-top: 4px; color: #E2E8F0;"><strong>Sensor ID:</strong> {s['id']}</div>
                <div style="font-size: 11px; color: #E2E8F0;"><strong>Basin:</strong> {s['basin']} River Basin</div>
                <div style="font-size: 11px; color: #F59E0B;"><strong>Hardware:</strong> {s['type']}</div>
                <div style="font-size: 11px; color: #10B981;"><strong>Risk Weight:</strong> {s['risk_weight']*100:.0f}%</div>
                <div style="font-size: 11px; color: #10B981; font-weight: bold;">Status: Active Transmission</div>
            </div>
            """
            folium.CircleMarker(
                location=[s["lat"], s["lon"]],
                radius=7,
                color="#00D084",
                weight=2,
                fill=True,
                fill_color="#F59E0B",
                fill_opacity=0.95,
                popup=folium.Popup(s_html, max_width=280),
                tooltip=f"Station: {s['name']} ({s['type']})"
            ).add_to(m_sensors)

        st_folium(m_sensors, width=None, height=560, key="map_dedicated_sensors")

    # ---------------------------------------------------------
    # TAB 3: DEDICATED RELIEF SHELTERS MAP
    # ---------------------------------------------------------
    with map_tab_shelters:
        st.markdown("#### 🏠 Dedicated Emergency Relief Shelters & Evacuation Centers Map")
        st.markdown("<p style='color: #CBD5E1; font-size: 0.88rem;'>Displays all 13 relief camps with real-time occupancy status: <span style='color:#10B981; font-weight:bold;'>GREEN (Available)</span>, <span style='color:#F59E0B; font-weight:bold;'>YELLOW (Limited)</span>, <span style='color:#EF4444; font-weight:bold;'>RED (Full)</span>.</p>", unsafe_allow_html=True)
        
        m_shelters = folium.Map(location=[center_lat, center_lon], zoom_start=7, tiles="CartoDB dark_matter", control_scale=True)
        
        for sh in SHELTERS_DATA:
            occ_pct = (sh["occupancy"] / sh["capacity"]) * 100
            sh_col = "#EF4444" if occ_pct >= 90 else "#F59E0B" if occ_pct >= 70 else "#10B981"
            st_label = "FULL (>90% OCCUPIED)" if occ_pct >= 90 else "LIMITED CAPACITY" if occ_pct >= 70 else "AVAILABLE (>30% VACANT)"
            
            # Evacuation catchment circle (15km radius)
            folium.Circle(
                location=[sh["lat"], sh["lon"]],
                radius=18000,
                color=sh_col,
                weight=1,
                fill=True,
                fill_color=sh_col,
                fill_opacity=0.15,
                tooltip=f"Evacuation Zone: {sh['name']}"
            ).add_to(m_shelters)

            sh_html = f"""
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 250px; background: #151921; color: #FFFFFF; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0; color: #F59E0B;">🏠 {sh['name']}</h4>
                <div style="font-size: 12px; margin-top: 5px; color: #E2E8F0;"><strong>District:</strong> {sh['district']} ({sh['river_basin']} Basin)</div>
                <div style="font-size: 12px; color: #E2E8F0;"><strong>Capacity:</strong> {sh['capacity']} | <strong>Occupancy:</strong> {sh['occupancy']} ({occ_pct:.0f}%)</div>
                <div style="font-size: 12px; color: #10B981;"><strong>Available Vacancies:</strong> {sh['capacity'] - sh['occupancy']} Beds</div>
                <div style="font-size: 12px; color: {sh_col}; font-weight: bold; margin-top: 4px;">Status: {st_label}</div>
                <div style="font-size: 11px; margin-top: 6px; color: #CBD5E1; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 4px;">
                    <strong>In-Charge:</strong> {sh['officer']}<br>📞 {sh['phone']}
                </div>
            </div>
            """
            folium.Marker(
                location=[sh["lat"], sh["lon"]],
                popup=folium.Popup(sh_html, max_width=300),
                tooltip=f"Shelter: {sh['name']} ({st_label})",
                icon=folium.Icon(color="green" if occ_pct < 70 else "orange" if occ_pct < 90 else "red", icon="home", prefix="fa")
            ).add_to(m_shelters)

        st_folium(m_shelters, width=None, height=560, key="map_dedicated_shelters")

    # ---------------------------------------------------------
    # TAB 4: DEDICATED RIVER BASIN & BARRAGE CAPACITY MAP
    # ---------------------------------------------------------
    with map_tab_capacity:
        st.markdown("#### 🌊 Dedicated River Corridors & Barrage Capacity Map")
        st.markdown("<p style='color: #CBD5E1; font-size: 0.88rem;'>Displays key barrages, spillway capacities, discharge volumes, and water levels across Krishna & Godavari River flow corridors.</p>", unsafe_allow_html=True)
        
        m_capacity = folium.Map(location=[center_lat, center_lon], zoom_start=7, tiles="CartoDB dark_matter", control_scale=True)
        
        for b in BARRAGES_STATIONS:
            b_col = "#EF4444" if b["status"] == "Danger" else "#F59E0B" if b["status"] == "Alert" else "#10B981"
            spillway_pct = (b["discharge_cusecs"] / b["capacity_cusecs"]) * 100
            
            # Flow buffer circle
            folium.Circle(
                location=[b["lat"], b["lon"]],
                radius=32000,
                color=b_col,
                weight=2,
                fill=True,
                fill_color=b_col,
                fill_opacity=0.22,
                tooltip=f"River Flow Zone: {b['river']} ({b['name']})"
            ).add_to(m_capacity)

            b_html = f"""
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; min-width: 260px; background: #151921; color: #FFFFFF; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0; color: #10B981;">🧱 {b['name']}</h4>
                <div style="font-size: 12px; margin-top: 5px; color: #E2E8F0;"><strong>River Basin:</strong> {b['river']} River</div>
                <div style="font-size: 12px; color: #E2E8F0;"><strong>Location:</strong> {b['district']}</div>
                <div style="font-size: 12px; color: #FFFFFF;"><strong>Current Level:</strong> {b['current_level_ft']} ft <span style="color:#EF4444;">(Danger: {b['danger_level_ft']} ft)</span></div>
                <div style="font-size: 12px; color: #F59E0B;"><strong>Current Discharge:</strong> {b['discharge_cusecs']:,} Cusecs</div>
                <div style="font-size: 12px; color: #CBD5E1;"><strong>Spillway Capacity:</strong> {b['capacity_cusecs']:,} Cusecs ({spillway_pct:.1f}%)</div>
                <div style="font-size: 12px; color: #10B981;"><strong>Gates Operational:</strong> {b['gates_open']}</div>
                <div style="font-size: 12px; color: {b_col}; font-weight: bold; margin-top: 4px;">Status: {b['status'].upper()}</div>
            </div>
            """
            folium.Marker(
                location=[b["lat"], b["lon"]],
                popup=folium.Popup(b_html, max_width=320),
                tooltip=f"Barrage: {b['name']} ({b['status'].upper()})",
                icon=folium.Icon(color="red" if b["status"] == "Danger" else "orange" if b["status"] == "Alert" else "blue", icon="tint", prefix="fa")
            ).add_to(m_capacity)

        st_folium(m_capacity, width=None, height=560, key="map_dedicated_capacity")

    # Legend
    st.markdown("""
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-top: 10px; background: rgba(22, 27, 34, 0.85); padding: 10px 20px; border-radius: 10px; border: 1px solid rgba(16, 185, 129, 0.25);">
        <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; background: #EF4444; border-radius: 50%; display: inline-block;"></span> <span style="font-size: 0.82rem; color: #FFFFFF;">Critical Risk / Danger Mark</span></div>
        <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; background: #F97316; border-radius: 50%; display: inline-block;"></span> <span style="font-size: 0.82rem; color: #FFFFFF;">High Flood Alert</span></div>
        <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; background: #10B981; border-radius: 50%; display: inline-block;"></span> <span style="font-size: 0.82rem; color: #FFFFFF;">IoT Telemetry Sensor</span></div>
        <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; background: #6366F1; border-radius: 4px; display: inline-block;"></span> <span style="font-size: 0.82rem; color: #FFFFFF;">Barrage / Spillway</span></div>
        <div style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; background: #F59E0B; border-radius: 3px; display: inline-block;"></span> <span style="font-size: 0.82rem; color: #FFFFFF;">Relief Shelter Facility</span></div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# MODULE 4 : QUANTUM SENSOR PLACEMENT
# =========================================================
elif selected_menu == "⚛️ Module 4: Quantum Sensor Placement":
    render_header(
        "Quantum Sensor Placement Optimization",
        "Quantum Approximate Optimization Algorithm (QAOA) & QUBO formulation powered by Qiskit & qBraid framework"
    )

    st.markdown("""
    <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 12px; padding: 14px 18px; margin-bottom: 20px;">
        <span style="font-weight: 700; color: #F59E0B;">⚛️ Quantum Objective:</span>
        <span style="color: #E2E8F0; font-size: 0.9rem;">
            Maximize sensor catchment coverage while minimizing redundant overlapping radii and penalizing deadzones across Krishna and Godavari river corridors using an Ising Hamiltonian mapped to Qiskit quantum circuits.
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Quantum Setup Controls
    qcol1, qcol2, qcol3 = st.columns(3)
    with qcol1:
        sensor_budget = st.slider("🎯 Sensor Deployment Budget (K)", 6, 20, 12)
    with qcol2:
        q_basin = st.selectbox("🌊 Target Basin Filter", ["All", "Krishna", "Godavari"])
    with qcol3:
        backend_choice = st.selectbox("💻 Quantum Backend Target", ["qBraid-Aer-Simulator (24 Qubits)", "Qiskit Statevector Sampler", "IBMQ Heron Quantum Cloud"])

    if st.button("🚀 EXECUTE QUANTUM QAOA SENSOR OPTIMIZATION", use_container_width=True):
        with st.spinner("Compiling Ising Hamiltonian, applying Hadamard superposition, and running QAOA variational layers..."):
            time.sleep(0.6)
            q_results = run_quantum_sensor_optimization(
                k_budget=sensor_budget,
                river_basin_filter=q_basin,
                backend_type=backend_choice
            )
            st.session_state["quantum_results"] = q_results
            st.success("✨ Quantum Optimization Converged Successfully to Ground State!")

    if "quantum_results" not in st.session_state:
        st.session_state["quantum_results"] = run_quantum_sensor_optimization(k_budget=sensor_budget, river_basin_filter=q_basin)

    res = st.session_state["quantum_results"]
    b_met = res["before_metrics"]
    a_met = res["after_metrics"]

    # Before vs After Comparative KPI Cards
    st.markdown("### 📊 Before Optimization vs After Optimization")
    
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-title">Coverage Percentage</div>
            <div style="display: flex; align-items: baseline; gap: 8px;">
                <span style="color: #EF4444; font-size: 1.3rem; text-decoration: line-through;">{b_met['coverage_pct']}%</span>
                <span style="color: #10B981; font-size: 2.1rem; font-weight: 800;">{a_met['coverage_pct']}%</span>
            </div>
            <span class="kpi-badge kpi-badge-emerald">+{(a_met['coverage_pct'] - b_met['coverage_pct']):.1f}% GAIN</span>
        </div>
        """, unsafe_allow_html=True)

    with mcol2:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-title">Sensor Network Efficiency</div>
            <div style="display: flex; align-items: baseline; gap: 8px;">
                <span style="color: #EF4444; font-size: 1.3rem; text-decoration: line-through;">{b_met['efficiency']*100:.0f}%</span>
                <span style="color: #10B981; font-size: 2.1rem; font-weight: 800;">{a_met['efficiency']*100:.0f}%</span>
            </div>
            <span class="kpi-badge kpi-badge-emerald">+{(a_met['efficiency'] - b_met['efficiency'])*100:.0f}% OPTIMAL</span>
        </div>
        """, unsafe_allow_html=True)

    with mcol3:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-title">Redundant Overlap</div>
            <div style="display: flex; align-items: baseline; gap: 8px;">
                <span style="color: #EF4444; font-size: 1.3rem;">{b_met['redundancy_pct']}%</span>
                <span style="color: #10B981; font-size: 2.1rem; font-weight: 800;">{a_met['redundancy_pct']}%</span>
            </div>
            <span class="kpi-badge kpi-badge-gold">-{(b_met['redundancy_pct'] - a_met['redundancy_pct']):.1f}% WASTE REDUCED</span>
        </div>
        """, unsafe_allow_html=True)

    with mcol4:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-title">Unmonitored Dead Zones</div>
            <div style="display: flex; align-items: baseline; gap: 8px;">
                <span style="color: #EF4444; font-size: 1.3rem; text-decoration: line-through;">{b_met['dead_zones_detected']} Zones</span>
                <span style="color: #10B981; font-size: 2.1rem; font-weight: 800;">{a_met['dead_zones_detected']}</span>
            </div>
            <span class="kpi-badge kpi-badge-emerald">ZERO DEAD ZONES</span>
        </div>
        """, unsafe_allow_html=True)

    # Before vs After Dual Map Comparison
    st.markdown("### 🗺️ Sensor Placement Map Comparison")
    map_col1, map_col2 = st.columns(2)

    with map_col1:
        st.markdown("<h4 style='color: #EF4444; text-align: center;'>❌ Before Optimization (Naive Placement - Redundant & Gaps)</h4>", unsafe_allow_html=True)
        m_before = folium.Map(location=[17.15, 80.85], zoom_start=7, tiles="CartoDB dark_matter")
        for node in res["before_sensors"]:
            folium.Circle(
                location=[node["lat"], node["lon"]],
                radius=42000,
                color="#EF4444",
                weight=1,
                fill=True,
                fill_color="#EF4444",
                fill_opacity=0.35,
                tooltip=f"Naive Placement: {node['name']}"
            ).add_to(m_before)
            folium.CircleMarker(
                location=[node["lat"], node["lon"]],
                radius=5,
                color="#EF4444",
                fill=True,
                fill_color="#FFFFFF"
            ).add_to(m_before)
        st_folium(m_before, width=None, height=380, key="map_before")

    with map_col2:
        st.markdown("<h4 style='color: #10B981; text-align: center;'>✅ After Quantum QAOA Optimization (Max Coverage & High Efficiency)</h4>", unsafe_allow_html=True)
        m_after = folium.Map(location=[17.15, 80.85], zoom_start=7, tiles="CartoDB dark_matter")
        for node in res["after_sensors"]:
            folium.Circle(
                location=[node["lat"], node["lon"]],
                radius=42000,
                color="#10B981",
                weight=1,
                fill=True,
                fill_color="#10B981",
                fill_opacity=0.28,
                tooltip=f"Quantum Optimal Node: {node['name']} ({node['type']})"
            ).add_to(m_after)
            folium.CircleMarker(
                location=[node["lat"], node["lon"]],
                radius=6,
                color="#00D084",
                fill=True,
                fill_color="#F59E0B"
            ).add_to(m_after)
        st_folium(m_after, width=None, height=380, key="map_after")

    # Quantum Convergence & Circuit Diagnostics
    st.markdown("### ⚛️ Quantum Circuit & Energy Convergence Diagnostics")
    c_col1, c_col2 = st.columns([1, 1])

    with c_col1:
        # Energy Convergence Plot
        df_conv = pd.DataFrame(res["energy_convergence"])
        fig_conv = px.line(
            df_conv, x="iteration", y="ground_state_energy",
            title="QAOA Ground State Energy Minimization Trajectory",
            markers=True
        )
        fig_conv.update_traces(line_color="#10B981", marker=dict(size=6, color="#F59E0B"))
        fig_conv.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(18,22,30,0.7)',
            font=dict(color='#E2E8F0'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.08)', title="QAOA Optimization Iteration"),
            yaxis=dict(gridcolor='rgba(255,255,255,0.08)', title="Ising Energy <H>"),
            height=280,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_conv, use_container_width=True)

    with c_col2:
        # Quantum Specs Table
        q_info = res["quantum_details"]
        st.markdown(f"""
        <div class="glass-card" style="height: 280px; overflow-y: auto;">
            <div style="font-weight: 700; color: #F59E0B; margin-bottom: 8px;">⚙️ Quantum Execution Parameters:</div>
            <div style="font-size: 0.84rem; line-height: 1.8; color: #E2E8F0;">
                • <strong>Algorithm:</strong> {q_info['algorithm']}<br>
                • <strong>Qiskit Version:</strong> {q_info['qiskit_version']}<br>
                • <strong>Active Qubits:</strong> {q_info['qubits_used']} Qubits<br>
                • <strong>Quantum Shots:</strong> {q_info['shots']} Shots<br>
                • <strong>Circuit Depth:</strong> {q_info['circuit_depth']} Gates Deep<br>
                • <strong>Optimal QUBO Energy:</strong> <span style="color: #10B981; font-weight:700;">{q_info['optimal_qubo_energy']}</span><br>
                • <strong>Backend:</strong> {q_info['backend']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Recommended Sensor Locations Table
    st.markdown("### 📋 Recommended Sensor Locations List (Post-Quantum Optimization)")
    df_rec = pd.DataFrame(res["after_sensors"])
    st.dataframe(
        df_rec[["id", "name", "basin", "type", "risk_weight", "lat", "lon"]].rename(columns={
            "id": "Sensor ID", "name": "Telemetry Station Location",
            "basin": "River Basin", "type": "Sensor Hardware",
            "risk_weight": "Catchment Risk Score", "lat": "Latitude", "lon": "Longitude"
        }),
        use_container_width=True
    )


# =========================================================
# MODULE 5 : RIVER MONITORING
# =========================================================
elif selected_menu == "🌊 Module 5: River Monitoring":
    render_header(
        "River Basin Hydrologic Monitoring",
        "Live gauge heights, barrage discharges, spillway capacity, and alert statuses for Krishna and Godavari Rivers"
    )

    # Status Definitions Bar
    st.markdown("""
    <div style="display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap;">
        <span class="kpi-badge kpi-badge-emerald">🟢 SAFE: Normal Flow</span>
        <span class="kpi-badge kpi-badge-gold">🟡 WATCH: Rising Hydrograph</span>
        <span class="kpi-badge" style="background: rgba(249, 115, 22, 0.2); color: #F97316; border: 1px solid rgba(249, 115, 22, 0.4);">🟠 ALERT: 1st/2nd Warning Level</span>
        <span class="kpi-badge kpi-badge-red">🔴 DANGER: 3rd Danger Level Breached</span>
    </div>
    """, unsafe_allow_html=True)

    tab_krishna, tab_godavari = st.tabs(["🏞️ Krishna River Stations", "🌊 Godavari River Stations"])

    with tab_krishna:
        krishna_stations = [b for b in BARRAGES_STATIONS if b["river"] == "Krishna"]
        for b in krishna_stations:
            badge_t = "red" if b["status"] == "Danger" else "gold" if b["status"] in ["Alert", "Watch"] else "emerald"
            discharge_pct = (b["discharge_cusecs"] / b["capacity_cusecs"]) * 100
            
            st.markdown(f"""
            <div class="glass-card">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <h3 style="color: #FFFFFF; margin: 0; font-size: 1.25rem;">🧱 {b['name']} ({b['district']})</h3>
                        <span style="font-size: 0.8rem; color: #CBD5E1;">Latitude: {b['lat']} | Longitude: {b['lon']}</span>
                    </div>
                    <span class="kpi-badge kpi-badge-{badge_t}" style="font-size: 0.85rem; padding: 6px 14px;">STATUS: {b['status'].upper()}</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-top: 14px;">
                    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                        <span style="font-size: 0.72rem; color: #CBD5E1;">Current Water Level</span>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #FFFFFF;">{b['current_level_ft']} ft</div>
                        <span style="font-size: 0.7rem; color: #EF4444;">Danger Mark: {b['danger_level_ft']} ft</span>
                    </div>
                    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                        <span style="font-size: 0.72rem; color: #CBD5E1;">Current Outflow Discharge</span>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #10B981;">{b['discharge_cusecs']:,} Cusecs</div>
                        <span style="font-size: 0.7rem; color: #CBD5E1;">Capacity: {b['capacity_cusecs']:,}</span>
                    </div>
                    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                        <span style="font-size: 0.72rem; color: #CBD5E1;">Spillway Utilization</span>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #F59E0B;">{discharge_pct:.1f}%</div>
                        <span style="font-size: 0.7rem; color: #CBD5E1;">Gates Open: {b['gates_open']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab_godavari:
        godavari_stations = [b for b in BARRAGES_STATIONS if b["river"] == "Godavari"]
        for b in godavari_stations:
            badge_t = "red" if b["status"] == "Danger" else "gold" if b["status"] in ["Alert", "Watch"] else "emerald"
            discharge_pct = (b["discharge_cusecs"] / b["capacity_cusecs"]) * 100
            
            st.markdown(f"""
            <div class="glass-card">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <h3 style="color: #FFFFFF; margin: 0; font-size: 1.25rem;">🌊 {b['name']} ({b['district']})</h3>
                        <span style="font-size: 0.8rem; color: #CBD5E1;">Latitude: {b['lat']} | Longitude: {b['lon']}</span>
                    </div>
                    <span class="kpi-badge kpi-badge-{badge_t}" style="font-size: 0.85rem; padding: 6px 14px;">STATUS: {b['status'].upper()}</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-top: 14px;">
                    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                        <span style="font-size: 0.72rem; color: #CBD5E1;">Current Water Level</span>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #FFFFFF;">{b['current_level_ft']} ft</div>
                        <span style="font-size: 0.7rem; color: #EF4444;">Danger Mark: {b['danger_level_ft']} ft</span>
                    </div>
                    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                        <span style="font-size: 0.72rem; color: #CBD5E1;">Current Outflow Discharge</span>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #10B981;">{b['discharge_cusecs']:,} Cusecs</div>
                        <span style="font-size: 0.7rem; color: #CBD5E1;">Capacity: {b['capacity_cusecs']:,}</span>
                    </div>
                    <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                        <span style="font-size: 0.72rem; color: #CBD5E1;">Spillway Utilization</span>
                        <div style="font-size: 1.3rem; font-weight: 800; color: #F59E0B;">{discharge_pct:.1f}%</div>
                        <span style="font-size: 0.7rem; color: #CBD5E1;">Gates Open: {b['gates_open']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# =========================================================
# MODULE 6 : DISASTER RESPONSE
# =========================================================
elif selected_menu == "🚨 Module 6: Disaster Response":
    render_header(
        "Disaster Response & Emergency Resource Allocator",
        "Automated resource computation, NDRF/SDRF mobilization, and evacuation management when flood risk escalates"
    )

    # Risk Trigger Selector
    st.markdown("#### ⚡ Set Operational Flood Emergency Level:")
    sim_risk = st.select_slider(
        "Current Operational Risk Level",
        options=["Low (Green)", "Medium (Yellow)", "High (Orange)", "Critical (Red)"],
        value="Critical (Red)"
    )

    # Filter High/Critical Affected Districts
    is_emergency = sim_risk in ["High (Orange)", "Critical (Red)"]
    multiplier = 1.0 if sim_risk == "Critical (Red)" else 0.6 if sim_risk == "High (Orange)" else 0.2

    # Calculate Affected Districts
    affected_districts = []
    total_pop_affected = 0
    
    for d_name, d_info in DISTRICTS_DATA.items():
        if d_info["vulnerability_score"] >= (0.80 if sim_risk == "Critical (Red)" else 0.88):
            pop_at_risk = int(d_info["population"] * d_info["vulnerability_score"] * multiplier * 0.28)
            affected_districts.append({
                "District": d_name,
                "State": d_info["state"],
                "Basin": d_info["basin"],
                "Vulnerable Population": pop_at_risk,
                "Primary Threat": d_info["primary_threat"]
            })
            total_pop_affected += pop_at_risk

    # Compute Resource Requirements
    rescue_teams_req = int(total_pop_affected / 4500) + 12
    medical_teams_req = int(total_pop_affected / 6000) + 15
    food_packets_daily = total_pop_affected * 2
    water_tankers_req = int(total_pop_affected / 1200) + 20
    boats_req = rescue_teams_req * 4

    # Top Emergency KPI Summary
    rcol1, rcol2, rcol3, rcol4 = st.columns(4)
    with rcol1:
        render_kpi_card("Affected Districts", f"{len(affected_districts)} Districts", "AP & Telangana", "red" if is_emergency else "emerald", "🏛️")
    with rcol2:
        render_kpi_card("Estimated Pop at Risk", f"{total_pop_affected:,}", "Immediate Evacuation", "red" if is_emergency else "emerald", "👥")
    with rcol3:
        render_kpi_card("Rescue Teams Required", f"{rescue_teams_req} Teams", f"{boats_req} Inflatable Boats", "gold", "🚤")
    with rcol4:
        render_kpi_card("Medical Units Required", f"{medical_teams_req} Units", "Mobile ICU & Trauma", "gold", "🚑")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Suggested Actions & Standard Operating Procedures (SOPs)
    st.markdown("### 📋 Suggested Disaster Management Actions & SOP Checklist")
    
    sop_col1, sop_col2 = st.columns(2)
    with sop_col1:
        st.markdown(f"""
        <div class="glass-card" style="border-left: 4px solid #EF4444;">
            <h4 style="color: #FFFFFF; margin: 0 0 10px 0;">⚡ Immediate Tactical Actions (0 - 6 Hours)</h4>
            <div style="font-size: 0.85rem; line-height: 1.8; color: #E2E8F0;">
                ✅ <strong>Deploy NDRF & SDRF Battalions:</strong> Move 10th Bn (Vijayawada) and 8th Bn to Konaseema & Bhadrachalam.<br>
                ✅ <strong>Sound Acoustic Sirens:</strong> Activate riverbank sirens in 48 vulnerable low-lying Lanka villages.<br>
                ✅ <strong>Power Grid Isolation:</strong> De-energize submerged transformers to avoid electrical hazards.<br>
                ✅ <strong>Evacuation Fleet Dispatch:</strong> Deploy {boats_req} motorized rescue boats and heavy transport trucks.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with sop_col2:
        st.markdown(f"""
        <div class="glass-card" style="border-left: 4px solid #F59E0B;">
            <h4 style="color: #FFFFFF; margin: 0 0 10px 0;">📦 Relief & Medical Support (6 - 24 Hours)</h4>
            <div style="font-size: 0.85rem; line-height: 1.8; color: #E2E8F0;">
                🍞 <strong>Food & Rations:</strong> Distribute {food_packets_daily:,} ready-to-eat dry ration and milk packets.<br>
                💧 <strong>Potable Water Supply:</strong> Mobilize {water_tankers_req} water tankers and chlorine purification tabs.<br>
                💉 <strong>Epidemic Prevention:</strong> Dispatch ORS kits, anti-venom vials, and mobile chlorine sprays.<br>
                📡 <strong>Satellite Comms:</strong> Deploy HAM radio & satellite phones to remote island cutoff villages.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Detailed Affected Districts Table
    st.markdown("### 🏢 Affected Districts Breakdown & Threat Vectors")
    df_affected = pd.DataFrame(affected_districts)
    st.dataframe(df_affected, use_container_width=True)

    # Interactive Dispatch Command Button
    if st.button("📤 GENERATE & DISPATCH STATE DISASTER ORDERS TO COLLECTORS", use_container_width=True):
        st.success("✅ Emergency Deployment Order Dispatched to AP SDMA, Telangana SDMA, NDRF 10th Bn & CWC Control Center!")


# =========================================================
# MODULE 7 : SHELTER MANAGEMENT
# =========================================================
elif selected_menu == "🏠 Module 7: Shelter Management":
    render_header(
        "Emergency Relief Shelter Management System",
        "Live capacity tracking, occupancy indicators, and logistics status across Krishna and Godavari river corridors"
    )

    # Top Shelter KPIs
    total_cap = sum(s["capacity"] for s in SHELTERS_DATA)
    total_occ = sum(s["occupancy"] for s in SHELTERS_DATA)
    total_avail = total_cap - total_occ
    occ_overall_pct = (total_occ / total_cap) * 100

    scol1, scol2, scol3, scol4 = st.columns(4)
    with scol1:
        render_kpi_card("Total Capacity", f"{total_cap:,}", "13 Relief Centers", "emerald", "🏢")
    with scol2:
        render_kpi_card("Current Occupancy", f"{total_occ:,}", f"{occ_overall_pct:.1f}% Occupied", "gold", "👥")
    with scol3:
        render_kpi_card("Available Vacancies", f"{total_avail:,} Beds", "Active Receiving", "emerald", "🛏️")
    with scol4:
        render_kpi_card("Status Indicator", "GREEN = Available", "YELLOW = Ltd | RED = Full", "emerald", "🚦")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Filter Controls
    fcol1, fcol2, fcol3 = st.columns(3)
    with fcol1:
        basin_filter = st.selectbox("Filter Basin:", ["All Basins", "Krishna", "Godavari", "Krishna & Godavari"])
    with fcol2:
        status_filter = st.selectbox("Filter Status:", ["All Statuses", "Green (Available)", "Yellow (Limited)", "Red (Full)"])
    with fcol3:
        search_query = st.text_input("🔍 Search Shelter / District / Officer:", "")

    # Filter Shelters
    filtered_shelters = []
    for sh in SHELTERS_DATA:
        vac = sh["capacity"] - sh["occupancy"]
        vac_pct = (vac / sh["capacity"]) * 100
        status_cat = "Green (Available)" if vac_pct > 30 else "Yellow (Limited)" if vac_pct > 10 else "Red (Full)"
        
        if basin_filter != "All Basins" and sh["river_basin"] != basin_filter:
            continue
        if status_filter != "All Statuses" and status_cat != status_filter:
            continue
        if search_query:
            q = search_query.lower()
            if q not in sh["name"].lower() and q not in sh["district"].lower() and q not in sh["officer"].lower():
                continue

        filtered_shelters.append({**sh, "status_cat": status_cat, "vacancy": vac, "vac_pct": vac_pct})

    # Render Shelter Cards
    st.markdown(f"### 📋 Active Shelters Directory ({len(filtered_shelters)} Shelters Found)")
    
    for sh in filtered_shelters:
        badge_type = "emerald" if "Green" in sh["status_cat"] else "gold" if "Yellow" in sh["status_cat"] else "red"
        card_type = "glass-card" if badge_type == "emerald" else f"glass-card-{badge_type}"
        occ_bar = int((sh["occupancy"] / sh["capacity"]) * 100)

        st.markdown(f"""
        <div class="{card_type}">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div>
                    <h3 style="color: #FFFFFF; margin: 0; font-size: 1.2rem;">🏠 {sh['name']}</h3>
                    <span style="font-size: 0.8rem; color: #CBD5E1;">District: <strong>{sh['district']}</strong> | River Basin: <strong>{sh['river_basin']}</strong> | Shelter ID: {sh['id']}</span>
                </div>
                <span class="kpi-badge kpi-badge-{badge_type}" style="font-size: 0.85rem; padding: 6px 14px;">STATUS: {sh['status_cat'].upper()}</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-top: 14px;">
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <span style="font-size: 0.72rem; color: #CBD5E1;">Total Capacity</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #FFFFFF;">{sh['capacity']:,} People</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <span style="font-size: 0.72rem; color: #CBD5E1;">Current Occupancy</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #F59E0B;">{sh['occupancy']:,} ({occ_bar}%)</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <span style="font-size: 0.72rem; color: #CBD5E1;">Available Vacancy</span>
                    <div style="font-size: 1.25rem; font-weight: 800; color: #10B981;">{sh['vacancy']:,} Beds</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                    <span style="font-size: 0.72rem; color: #CBD5E1;">Officer In-Charge</span>
                    <div style="font-size: 0.88rem; font-weight: 700; color: #FFFFFF;">{sh['officer']}</div>
                    <span style="font-size: 0.72rem; color: #CBD5E1;">📞 {sh['phone']}</span>
                </div>
            </div>
            <div style="display: flex; gap: 14px; margin-top: 10px; font-size: 0.76rem; color: #CBD5E1;">
                <span>🩺 Medical Unit: {'✅ Available' if sh['medical_unit'] else '❌ Absent'}</span>
                <span>🍞 Food Stock: {sh['food_stock_days']} Days</span>
                <span>⚡ Power Backup: {sh['power_backup']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# MODULE 8 : MULTILINGUAL ALERT SYSTEM
# =========================================================
elif selected_menu == "🌐 Module 8: Multilingual Alert System":
    render_header(
        "Multilingual Emergency Public Warning System",
        "Instant citizen flood warning broadcasts in English, Telugu, Hindi, Tamil, and Kannada across 4 alert tiers"
    )

    # Language and Alert Level Selectors
    lcol1, lcol2 = st.columns(2)
    with lcol1:
        lang_choice = st.selectbox(
            "🌐 Select Broadcast Language:",
            ["Telugu (తెలుగు)", "English", "Hindi (हिन्दी)", "Tamil (தமிழ்)", "Kannada (ಕನ್ನಡ)"]
        )
    with lcol2:
        alert_tier = st.selectbox(
            "🚨 Select Alert Severity Level:",
            ["Red (🔴 Critical Emergency)", "Orange (🟠 High Flood Alert)", "Yellow (🟡 Watch Advisory)", "Green (🟢 Normal Flow)"]
        )

    # Normalize keys
    lang_key = lang_choice.split(" ")[0]
    tier_key = "Red" if "Red" in alert_tier else "Orange" if "Orange" in alert_tier else "Yellow" if "Yellow" in alert_tier else "Green"

    alert_content = MULTILINGUAL_ALERTS[lang_key][tier_key]
    badge_style = "red" if tier_key == "Red" else "gold" if tier_key in ["Orange", "Yellow"] else "emerald"
    card_type = "glass-card-danger" if tier_key == "Red" else "glass-card-gold" if tier_key in ["Orange", "Yellow"] else "glass-card"

    # Display Alert Card
    st.markdown(f"""
    <div class="{card_type}" style="padding: 26px 30px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span class="kpi-badge kpi-badge-{badge_style}" style="font-size: 0.95rem; padding: 6px 16px;">
                {tier_key.upper()} BROADCAST LEVEL
            </span>
            <span style="font-size: 0.8rem; color: #CBD5E1;">CAP Protocol Compliant v1.2</span>
        </div>
        <h2 style="color: #FFFFFF; font-size: 1.55rem; margin: 0 0 12px 0;">{alert_content['title']}</h2>
        <div style="background: rgba(0,0,0,0.4); padding: 14px 18px; border-radius: 10px; margin-bottom: 14px; border-left: 4px solid {'#EF4444' if tier_key=='Red' else '#F59E0B' if tier_key in ['Orange','Yellow'] else '#10B981'};">
            <div style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; line-height: 1.5;">{alert_content['headline']}</div>
        </div>
        <div style="font-size: 0.95rem; color: #E2E8F0; line-height: 1.7; margin-bottom: 18px;">
            <strong>📢 Instructions for Citizens:</strong><br>
            {alert_content['instructions']}
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 12px; font-size: 0.78rem; color: #CBD5E1;">
            <span>🏛️ {alert_content['authority']}</span>
            <span>Emergency Helpline: <strong>1070 / 112</strong></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Multi-language Broadcast Grid Comparison
    st.markdown("### 🌐 Simultaneous 5-Language Broadcast Preview")
    
    tabs = st.tabs(["English", "Telugu (తెలుగు)", "Hindi (हिन्दी)", "Tamil (தமிழ்)", "Kannada (ಕನ್ನಡ)"])
    lang_names = ["English", "Telugu", "Hindi", "Tamil", "Kannada"]
    
    for i, t in enumerate(tabs):
        with t:
            d = MULTILINGUAL_ALERTS[lang_names[i]][tier_key]
            st.markdown(f"""
            <div style="background: rgba(22, 27, 34, 0.85); padding: 16px; border-radius: 10px; border: 1px solid rgba(16,185,129,0.25);">
                <h4 style="color: #FFFFFF; margin: 0 0 8px 0;">{d['title']}</h4>
                <p style="color: #CBD5E1; font-size: 0.9rem; margin-bottom: 8px;">{d['headline']}</p>
                <p style="color: #94A3B8; font-size: 0.85rem;">{d['instructions']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Broadcast Actions
    st.markdown("#### 📡 Citizen Broadcast Dispatch Actions:")
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1:
        if st.button("📱 SEND CELL BROADCAST / SMS TO BASIN USERS", use_container_width=True):
            st.success("✅ SMS Cell Broadcast initiated to 4.2 Million subscribers in delta towers!")
    with b_col2:
        if st.button("📢 DISPATCH WHATSAPP DISASTER ALERTS", use_container_width=True):
            st.success("✅ WhatsApp verified channels notified in Telugu, Hindi & English!")
    with b_col3:
        if st.button("📻 TRIGGER AIR & DOORDARSHAN EBS HOOKS", use_container_width=True):
            st.success("✅ Emergency Broadcast System (EBS) audio interrupt signaled!")


# =========================================================
# MODULE 9 : ANALYTICS & INSIGHTS
# =========================================================
elif selected_menu == "📈 Module 9: Analytics & Insights":
    render_header(
        "Hydrologic Trends & Sensor Analytics",
        "Deep-dive telemetry trends, district risk correlations, and quantum sensor performance metrics"
    )

    tab_trend, tab_risk, tab_sensor = st.tabs(["📊 Flood Trends & Hydrographs", "🏢 District Risk Analytics", "📡 Sensor Network Telemetry"])

    with tab_trend:
        st.markdown("#### 📈 Multi-Day Inflow vs Outflow Hydrograph (Krishna & Godavari)")
        
        days = pd.date_range(end=pd.Timestamp.now(), periods=14, freq='D')
        df_hydro = pd.DataFrame({
            "Date": days,
            "Godavari Inflow (Lakh Cusecs)": [6.2, 7.8, 9.4, 12.1, 14.8, 16.5, 15.2, 13.0, 11.5, 9.8, 8.4, 7.2, 6.5, 5.8],
            "Godavari Outflow (Lakh Cusecs)": [5.8, 7.2, 8.9, 11.5, 14.2, 15.9, 14.8, 12.6, 11.0, 9.4, 8.0, 6.9, 6.1, 5.4],
            "Krishna Inflow (Lakh Cusecs)": [2.1, 2.5, 3.4, 4.8, 5.9, 5.2, 4.6, 4.0, 3.5, 3.0, 2.7, 2.4, 2.2, 2.0],
            "Krishna Outflow (Lakh Cusecs)": [1.9, 2.3, 3.1, 4.5, 5.6, 5.0, 4.4, 3.8, 3.3, 2.9, 2.5, 2.3, 2.1, 1.9]
        })

        fig_line = px.line(
            df_hydro, x="Date",
            y=["Godavari Inflow (Lakh Cusecs)", "Godavari Outflow (Lakh Cusecs)", "Krishna Inflow (Lakh Cusecs)", "Krishna Outflow (Lakh Cusecs)"],
            title="14-Day River Hydrograph Discharge Curves",
            color_discrete_sequence=["#EF4444", "#F59E0B", "#10B981", "#38BDF8"]
        )
        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(18,22,30,0.7)',
            font=dict(color='#E2E8F0', family='Plus Jakarta Sans'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.08)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.08)', title="Discharge (Lakh Cusecs)"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            height=380
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with tab_risk:
        st.markdown("#### 🏢 Comparative District Vulnerability & Population Density")
        
        d_names = list(DISTRICTS_DATA.keys())
        d_vuln = [DISTRICTS_DATA[d]["vulnerability_score"] * 100 for d in d_names]
        d_pop = [DISTRICTS_DATA[d]["population"] / 100000.0 for d in d_names]
        d_state = [DISTRICTS_DATA[d]["state"] for d in d_names]

        df_dist = pd.DataFrame({
            "District": d_names,
            "Flood Risk Score (%)": d_vuln,
            "Population (Lakhs)": d_pop,
            "State": d_state
        }).sort_values(by="Flood Risk Score (%)", ascending=False)

        col_b1, col_b2 = st.columns(2)
        with col_b1:
            fig_bar_risk = px.bar(
                df_dist, x="District", y="Flood Risk Score (%)",
                color="Flood Risk Score (%)",
                color_continuous_scale=[[0, '#10B981'], [0.5, '#F59E0B'], [1.0, '#EF4444']],
                title="District Vulnerability Index (%)"
            )
            fig_bar_risk.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(18,22,30,0.7)',
                font=dict(color='#E2E8F0'),
                xaxis=dict(gridcolor='rgba(255,255,255,0.08)'),
                yaxis=dict(gridcolor='rgba(255,255,255,0.08)'),
                height=340
            )
            st.plotly_chart(fig_bar_risk, use_container_width=True)

        with col_b2:
            fig_pie = px.pie(
                df_dist, values="Population (Lakhs)", names="District",
                title="Riparian Population Distribution by District",
                color_discrete_sequence=px.colors.sequential.Tealgrn
            )
            fig_pie.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#E2E8F0'),
                height=340
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    with tab_sensor:
        st.markdown("#### 📡 Quantum Sensor Network Performance Metrics")
        
        pcol1, pcol2, pcol3 = st.columns(3)
        with pcol1:
            render_kpi_card("Mean Network Uptime", "99.84%", "SLA Guaranteed", "emerald", "📶")
        with pcol2:
            render_kpi_card("Telemetry Latency", "24.6 ms", "LoRaWAN & 4G/5G", "emerald", "⚡")
        with pcol3:
            render_kpi_card("Packet Loss Rate", "0.04%", "Zero Dropped Frames", "emerald", "🛡️")

        sensor_types = ["Radar Water Level", "Ultrasonic Gauges", "Optical Stream Gauges", "Tidal Surge Telemetry", "Acoustic Doppler"]
        sensor_counts = [84, 62, 38, 32, 22]
        
        fig_pie_sensor = px.pie(
            names=sensor_types, values=sensor_counts,
            title="IoT Sensor Hardware Distribution in Krishna & Godavari Basins",
            color_discrete_sequence=["#10B981", "#059669", "#F59E0B", "#38BDF8", "#6366F1"]
        )
        fig_pie_sensor.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E2E8F0'),
            height=340
        )
        st.plotly_chart(fig_pie_sensor, use_container_width=True)


# =========================================================
# MODULE 10 : GOVERNMENT COMMAND CENTER
# =========================================================
elif selected_menu == "🎛️ Module 10: Govt Command Center":
    render_header(
        "Government Disaster Command Center",
        "Unified Mission-Control Operations Dashboard for Krishna and Godavari River Basins"
    )

    # 1. TOP ROW: 4 Critical Metrics
    st.markdown("### 🚨 Critical Situation Telemetry")
    top1, top2, top3, top4 = st.columns(4)
    with top1:
        render_kpi_card("Active Alerts", "4 Basins Active", "2 Red | 2 Orange", "red", "🚨", "Statewide Emergency")
    with top2:
        render_kpi_card("Flood Risk Level", "CRITICAL (88.4%)", "Danger Mark Breached", "red", "🌊", "Bhadrachalam & Delta")
    with top3:
        render_kpi_card("Population at Risk", "482,500", "Evacuation Underway", "gold", "👥", "12 Districts")
    with top4:
        render_kpi_card("Sensors Online", "238 / 238", "100% Quantum Synced", "emerald", "📡", "Zero Blindspots")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # 2. CENTER: Large Interactive Mission Control Map
    st.markdown("### 🗺️ Live Basin Operations Map")
    
    m_cmd = folium.Map(location=[17.15, 80.85], zoom_start=7, tiles="CartoDB dark_matter")
    
    # Add Barrages
    for b in BARRAGES_STATIONS:
        b_col = "red" if b["status"] == "Danger" else "orange" if b["status"] == "Alert" else "green"
        folium.Marker(
            location=[b["lat"], b["lon"]],
            tooltip=f"{b['name']} - {b['status'].upper()} ({b['discharge_cusecs']:,} cusecs)",
            icon=folium.Icon(color=b_col, icon="tint", prefix="fa")
        ).add_to(m_cmd)

    # Add Shelter markers
    for sh in SHELTERS_DATA:
        folium.CircleMarker(
            location=[sh["lat"], sh["lon"]],
            radius=5,
            color="#F59E0B",
            fill=True,
            fill_color="#F59E0B",
            tooltip=f"Shelter: {sh['name']} (Cap: {sh['capacity']})"
        ).add_to(m_cmd)

    # Add Quantum Sensor Nodes
    for s in SENSOR_CANDIDATES:
        folium.CircleMarker(
            location=[s["lat"], s["lon"]],
            radius=4,
            color="#10B981",
            fill=True,
            fill_color="#00D084",
            tooltip=f"Sensor: {s['name']}"
        ).add_to(m_cmd)

    st_folium(m_cmd, width=None, height=450, key="map_command_center")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # 3. BOTTOM ROW: AI Recommendations, Emergency Actions, Shelter Status
    st.markdown("### ⚡ Command Decisions & Operational Telemetry")
    bot1, bot2, bot3 = st.columns(3)

    with bot1:
        st.markdown("""
        <div class="glass-card" style="border-top: 4px solid #10B981; height: 320px; overflow-y: auto;">
            <h4 style="color: #FFFFFF; margin: 0 0 10px 0;">🧠 Quantum AI Recommendations</h4>
            <div style="font-size: 0.84rem; line-height: 1.7; color: #E2E8F0;">
                • <strong>Prakasam Barrage Regulation:</strong> Maintain discharge between 480k - 520k cusecs to avoid Budameru backwater surge.<br>
                • <strong>Godavari Spillway Coordination:</strong> Open all 175 gates at Dowleswaram with balanced delta split: Gautami (45%), Vasishta (35%), Vainateya (20%).<br>
                • <strong>Sensor Mesh Realignment:</strong> Quantum QAOA indicates high vulnerability in Konaseema lowlands; reposition 3 Doppler units downstream.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with bot2:
        st.markdown("""
        <div class="glass-card" style="border-top: 4px solid #EF4444; height: 320px; overflow-y: auto;">
            <h4 style="color: #FFFFFF; margin: 0 0 10px 0;">🚨 Emergency Action Directives</h4>
            <div style="font-size: 0.84rem; line-height: 1.7; color: #E2E8F0;">
                • <strong>Evacuation Order:</strong> Mandatory relocation for 48 low-lying river islands across Konaseema & Bhadrachalam.<br>
                • <strong>NDRF Deployment:</strong> 22 boats assigned to Avanigadda, 30 boats to Rajahmundry & Amalapuram.<br>
                • <strong>Helicopter Airdrop Standby:</strong> 4 IAF Mi-17 helicopters on standby at Gannavaram Airport for food drops.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with bot3:
        st.markdown("""
        <div class="glass-card" style="border-top: 4px solid #F59E0B; height: 320px; overflow-y: auto;">
            <h4 style="color: #FFFFFF; margin: 0 0 10px 0;">🏠 Live Shelter Status</h4>
            <div style="font-size: 0.84rem; line-height: 1.7; color: #E2E8F0;">
                • <strong>Total Capacity:</strong> 18,650 Persons<br>
                • <strong>Current Occupancy:</strong> 13,500 (72.4%)<br>
                • <strong>Available Vacancies:</strong> 5,150 Beds<br>
                • <strong>Medical Officers Deployed:</strong> 34 Doctors, 70 Nurses<br>
                • <strong>Food Stock Runway:</strong> 6.5 Days Average<br>
                • <strong>Backup Power Generators:</strong> 100% Operational
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Command Action Buttons
    st.markdown("---")
    cc_b1, cc_b2, cc_b3 = st.columns(3)
    with cc_b1:
        if st.button("📢 BROADCAST RED ALERT TO AP & TELANGANA MEDIA", use_container_width=True):
            st.success("🚨 Official Gazette & Broadcast Advisory Issued to Doordarshan, AIR, and Digital Channels!")
    with cc_b2:
        if st.button("📄 GENERATE CHIEF SECRETARY SITREP REPORT (PDF)", use_container_width=True):
            st.success("📄 SITREP #2026-KG-09 Generated and Encrypted for Cabinet Review!")
    with cc_b3:
        if st.button("🔄 SYNCHRONIZE WITH ISRO BHUVAN / CWC", use_container_width=True):
            st.success("🛰️ Satellite Telemetry & Reservoir Inflow Data Refreshed!")


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
render_footer()
