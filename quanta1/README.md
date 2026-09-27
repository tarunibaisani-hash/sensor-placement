# FloodGuard Quantum AI 🌊⚡
### AI & Quantum Powered Flood Forecasting and Smart Sensor Placement for Krishna and Godavari River Basins

FloodGuard Quantum AI is a state-of-the-art government-grade disaster management and hydrologic intelligence dashboard engineered for the **Krishna and Godavari River Basins** across **Andhra Pradesh** and **Telangana**.

---

## 🌟 Key Architecture & Modules

1. **🏛️ Module 1: Home Dashboard** — Real-time telemetry overview, river basin status, live KPI cards (Total Sensors, Flood Alerts, Districts Monitored, Active Shelters, System Status).
2. **🧠 Module 2: Flood Prediction** — AI predictive engine powered by `flood_model.pkl` evaluating 17 hydrologic, infrastructural, and ecological parameters with Plotly gauges, probability meters, and feature contribution charts.
3. **🗺️ Module 3: Krishna & Godavari Map** — Interactive GIS mapping across 12 Andhra Pradesh & Telangana districts with layer toggles for flood risk heatmaps, sensors, relief shelters, and barrages.
4. **⚛️ Module 4: Quantum Sensor Placement** — Quantum Approximate Optimization Algorithm (QAOA) and QUBO Hamiltonian formulation via **Qiskit** and **qBraid** to maximize coverage and eliminate deadzones.
5. **🌊 Module 5: River Monitoring** — Live gauge heights, discharge rates, spillway gates, and safe/watch/alert/danger classifications for major barrages (Prakasam, Dowleswaram, Bhadrachalam, Srisailam, Nagarjuna Sagar, Polavaram, etc.).
6. **🚨 Module 6: Disaster Response** — Emergency resource calculator automatically computing NDRF/SDRF rescue teams, inflatable boats, medical units, food supplies, and SOP action directives.
7. **🏠 Module 7: Shelter Management** — Live occupancy tracker and directory for 13 relief centers across AP & Telangana with Green/Yellow/Red availability indicators.
8. **🌐 Module 8: Multilingual Alert System** — Citizen broadcast generator supporting **Telugu (తెలుగు)**, **English**, **Hindi (हिन्दी)**, **Tamil (தமிழ்)**, and **Kannada (ಕನ್ನಡ)** with CAP protocol compliance.
9. **📈 Module 9: Analytics & Insights** — Multi-day temporal hydrographs, district risk vulnerability indices, and sensor performance metrics.
10. **🎛️ Module 10: Government Command Center** — Unified single-screen mission-control view with top situational metrics, live operations map, and AI decision support.

---

## 🎨 Design Theme
- **Dark Charcoal Background** (`#0e1117` / `#151921`)
- **Emerald Green** (`#10B981` / `#00D084`)
- **Gold Highlights** (`#F59E0B` / `#FFD700`)
- **Crisp White Text** & **Glassmorphism Cards**
- **Permanent Wide Sidebar** with icons and highlighted active tabs.

---

## 🚀 How to Run the Application

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train / verify model (already generated)
python train_model.py

# 3. Launch Streamlit Application
streamlit run app.py
```
