"""
FloodGuard Quantum AI - Data Management & Constants Module
Contains geospatial datasets, sensors, shelters, barrages, river paths,
and multilingual translations for Krishna and Godavari River Basins.
"""

# Districts data with coordinates, population, base risk, shelters, river basins
DISTRICTS_DATA = {
    # Andhra Pradesh Districts
    "Krishna": {
        "state": "Andhra Pradesh",
        "basin": "Krishna",
        "lat": 16.1800,
        "lon": 81.1300,
        "population": 1735000,
        "vulnerability_score": 0.85,
        "primary_threat": "River Outflow & Tidal Surge (Machilipatnam / Avanigadda)",
        "elevation_m": 8,
        "base_sensors": 18,
        "key_rivers": ["Krishna", "Budameru"]
    },
    "NTR": {
        "state": "Andhra Pradesh",
        "basin": "Krishna",
        "lat": 16.5062,
        "lon": 80.6480,
        "population": 2218000,
        "vulnerability_score": 0.92,
        "primary_threat": "Prakasam Barrage Backwater & Budameru Diversion Breach",
        "elevation_m": 19,
        "base_sensors": 24,
        "key_rivers": ["Krishna", "Budameru Rivulet"]
    },
    "Guntur": {
        "state": "Andhra Pradesh",
        "basin": "Krishna",
        "lat": 16.3067,
        "lon": 80.4365,
        "population": 2090000,
        "vulnerability_score": 0.78,
        "primary_threat": "Right Canal Inundation & Downstream Krishna Floodplain",
        "elevation_m": 33,
        "base_sensors": 16,
        "key_rivers": ["Krishna", "Guntur Channel"]
    },
    "Eluru": {
        "state": "Andhra Pradesh",
        "basin": "Krishna & Godavari",
        "lat": 16.7107,
        "lon": 81.0952,
        "population": 2071000,
        "vulnerability_score": 0.82,
        "primary_threat": "Kolleru Lake Overflow & Tammileru Flood Inundation",
        "elevation_m": 22,
        "base_sensors": 15,
        "key_rivers": ["Tammileru", "Yerrakaluva", "Kolleru Outflow"]
    },
    "East Godavari": {
        "state": "Andhra Pradesh",
        "basin": "Godavari",
        "lat": 17.0005,
        "lon": 81.7800,
        "population": 1832000,
        "vulnerability_score": 0.88,
        "primary_threat": "Rajahmundry & Dowleswaram Heavy Discharge Overflows",
        "elevation_m": 14,
        "base_sensors": 22,
        "key_rivers": ["Godavari (Akhanda Godavari)"]
    },
    "West Godavari": {
        "state": "Andhra Pradesh",
        "basin": "Godavari",
        "lat": 16.5449,
        "lon": 81.5212,
        "population": 1779000,
        "vulnerability_score": 0.84,
        "primary_threat": "Vasishta Godavari Inundation & Delta Lowlands",
        "elevation_m": 11,
        "base_sensors": 19,
        "key_rivers": ["Godavari (Vasishta)", "Yerrakaluva"]
    },
    "Konaseema": {
        "state": "Andhra Pradesh",
        "basin": "Godavari",
        "lat": 16.5800,
        "lon": 81.9900,
        "population": 1719000,
        "vulnerability_score": 0.95,
        "primary_threat": "Gautami / Vainateya Island Inundation & High Tide Lock",
        "elevation_m": 4,
        "base_sensors": 20,
        "key_rivers": ["Gautami Godavari", "Vainateya", "Vashishta"]
    },
    "Kakinada": {
        "state": "Andhra Pradesh",
        "basin": "Godavari",
        "lat": 16.9891,
        "lon": 82.2475,
        "population": 2092000,
        "vulnerability_score": 0.79,
        "primary_threat": "Coastal Godavari Canal Surges & Yeleru Reservoir Release",
        "elevation_m": 5,
        "base_sensors": 17,
        "key_rivers": ["Yeleru", "Godavari Delta Canals"]
    },

    # Telangana Districts
    "Khammam": {
        "state": "Telangana",
        "basin": "Krishna & Godavari",
        "lat": 17.2473,
        "lon": 80.1514,
        "population": 1401000,
        "vulnerability_score": 0.86,
        "primary_threat": "Muneru River Flash Floods & Wyra Overflow",
        "elevation_m": 107,
        "base_sensors": 14,
        "key_rivers": ["Muneru", "Akeru", "Wyra"]
    },
    "Bhadradri Kothagudem": {
        "state": "Telangana",
        "basin": "Godavari",
        "lat": 17.5500,
        "lon": 80.6200,
        "population": 1069000,
        "vulnerability_score": 0.96,
        "primary_threat": "Bhadrachalam 1st/2nd/3rd Warning Levels (Godavari Inundation)",
        "elevation_m": 89,
        "base_sensors": 25,
        "key_rivers": ["Godavari", "Kinnerasani", "Sabarí"]
    },
    "Karimnagar": {
        "state": "Telangana",
        "basin": "Godavari",
        "lat": 18.4386,
        "lon": 79.1288,
        "population": 1005000,
        "vulnerability_score": 0.72,
        "primary_threat": "Manair Dam Inflows & Lower Manair Basin Inundation",
        "elevation_m": 265,
        "base_sensors": 13,
        "key_rivers": ["Manair", "Godavari Sub-basin"]
    },
    "Nizamabad": {
        "state": "Telangana",
        "basin": "Godavari",
        "lat": 18.6725,
        "lon": 78.0941,
        "population": 1571000,
        "vulnerability_score": 0.76,
        "primary_threat": "Sri Ram Sagar Project (SRSP) Heavy Inflows & Backwater",
        "elevation_m": 395,
        "base_sensors": 15,
        "key_rivers": ["Godavari", "Phulang"]
    }
}

# Key Barrages and Monitoring Stations
BARRAGES_STATIONS = [
    {
        "name": "Prakasam Barrage",
        "river": "Krishna",
        "district": "NTR / Guntur",
        "lat": 16.5074,
        "lon": 80.6062,
        "warning_level_ft": 12.0,
        "danger_level_ft": 14.5,
        "current_level_ft": 13.8,
        "discharge_cusecs": 485000,
        "capacity_cusecs": 1190000,
        "status": "Alert",
        "gates_open": "65 / 70"
    },
    {
        "name": "Srisailam Dam",
        "river": "Krishna",
        "district": "Nandyal / Nagarkurnool",
        "lat": 16.0886,
        "lon": 78.8972,
        "warning_level_ft": 880.0,
        "danger_level_ft": 885.0,
        "current_level_ft": 882.4,
        "discharge_cusecs": 390000,
        "capacity_cusecs": 1320000,
        "status": "Watch",
        "gates_open": "8 / 12"
    },
    {
        "name": "Nagarjuna Sagar Dam",
        "river": "Krishna",
        "district": "Palnadu / Nalgonda",
        "lat": 16.5772,
        "lon": 79.3134,
        "warning_level_ft": 585.0,
        "danger_level_ft": 590.0,
        "current_level_ft": 587.2,
        "discharge_cusecs": 420000,
        "capacity_cusecs": 1050000,
        "status": "Watch",
        "gates_open": "18 / 26"
    },
    {
        "name": "Sir Arthur Cotton Barrage (Dowleswaram)",
        "river": "Godavari",
        "district": "East Godavari",
        "lat": 16.9408,
        "lon": 81.7694,
        "warning_level_ft": 13.75,
        "danger_level_ft": 17.75,
        "current_level_ft": 16.40,
        "discharge_cusecs": 1425000,
        "capacity_cusecs": 3000000,
        "status": "Alert",
        "gates_open": "175 / 175"
    },
    {
        "name": "Bhadrachalam Gauge Station",
        "river": "Godavari",
        "district": "Bhadradri Kothagudem",
        "lat": 17.6689,
        "lon": 80.8936,
        "warning_level_ft": 48.0,
        "danger_level_ft": 53.0,
        "current_level_ft": 54.8,
        "discharge_cusecs": 1580000,
        "capacity_cusecs": 2500000,
        "status": "Danger",
        "gates_open": "River Gauge Active"
    },
    {
        "name": "Polavaram Project (Spillway)",
        "river": "Godavari",
        "district": "Eluru / East Godavari",
        "lat": 17.2567,
        "lon": 81.6567,
        "warning_level_ft": 42.0,
        "danger_level_ft": 45.7,
        "current_level_ft": 43.1,
        "discharge_cusecs": 1490000,
        "capacity_cusecs": 5000000,
        "status": "Alert",
        "gates_open": "48 / 48"
    },
    {
        "name": "Sri Ram Sagar Project (SRSP)",
        "river": "Godavari",
        "district": "Nizamabad",
        "lat": 18.9667,
        "lon": 78.3333,
        "warning_level_ft": 1088.0,
        "danger_level_ft": 1091.0,
        "current_level_ft": 1087.5,
        "discharge_cusecs": 120000,
        "capacity_cusecs": 900000,
        "status": "Safe",
        "gates_open": "6 / 42"
    },
    {
        "name": "Medigadda (Laxmi) Barrage - Kaleshwaram",
        "river": "Godavari",
        "district": "Jayashankar Bhupalpally",
        "lat": 18.7917,
        "lon": 79.9481,
        "warning_level_ft": 99.0,
        "danger_level_ft": 102.0,
        "current_level_ft": 98.4,
        "discharge_cusecs": 350000,
        "capacity_cusecs": 2825000,
        "status": "Watch",
        "gates_open": "42 / 85"
    }
]

# Relief Shelters Across the 12 Districts
SHELTERS_DATA = [
    {
        "id": "SH-AP-01",
        "name": "Vijayawada Municipal High School Relief Center",
        "district": "NTR",
        "river_basin": "Krishna",
        "capacity": 1500,
        "occupancy": 1280,
        "lat": 16.5186,
        "lon": 80.6341,
        "officer": "R. Sudhakar (Tahasildar)",
        "phone": "+91 94401 23456",
        "medical_unit": True,
        "food_stock_days": 6,
        "power_backup": "Solar + 120kVA DG Set"
    },
    {
        "id": "SH-AP-02",
        "name": "Avanigadda Cyclone & Flood Shelter #4",
        "district": "Krishna",
        "river_basin": "Krishna",
        "capacity": 850,
        "occupancy": 420,
        "lat": 16.0210,
        "lon": 80.9180,
        "officer": "K. Venkatesh (Revenue Insp.)",
        "phone": "+91 94401 78901",
        "medical_unit": True,
        "food_stock_days": 8,
        "power_backup": "DG Set 75kVA"
    },
    {
        "id": "SH-AP-03",
        "name": "Machilipatnam ZP Indoor Stadium Shelter",
        "district": "Krishna",
        "river_basin": "Krishna",
        "capacity": 2200,
        "occupancy": 890,
        "lat": 16.1850,
        "lon": 81.1390,
        "officer": "M. Lakshmi (DRO)",
        "phone": "+91 94402 11223",
        "medical_unit": True,
        "food_stock_days": 10,
        "power_backup": "Dual Grid + DG Set"
    },
    {
        "id": "SH-AP-04",
        "name": "Rajahmundry Arts College Mega Shelter Camp",
        "district": "East Godavari",
        "river_basin": "Godavari",
        "capacity": 3000,
        "occupancy": 2890,
        "lat": 17.0050,
        "lon": 81.7780,
        "officer": "V. Ramana Murthy (RDO)",
        "phone": "+91 94403 33445",
        "medical_unit": True,
        "food_stock_days": 5,
        "power_backup": "250kVA Emergency DG"
    },
    {
        "id": "SH-AP-05",
        "name": "Amalapuram Coastal & Delta Relief Pavilion",
        "district": "Konaseema",
        "river_basin": "Godavari",
        "capacity": 1800,
        "occupancy": 1750,
        "lat": 16.5780,
        "lon": 82.0050,
        "officer": "P. Srinivasa Rao (DMHO Lead)",
        "phone": "+91 94404 55667",
        "medical_unit": True,
        "food_stock_days": 4,
        "power_backup": "100kVA DG Set"
    },
    {
        "id": "SH-AP-06",
        "name": "Narsapur Flood Evacuation Center",
        "district": "West Godavari",
        "river_basin": "Godavari",
        "capacity": 1200,
        "occupancy": 680,
        "lat": 16.4380,
        "lon": 81.6980,
        "officer": "B. Anjaneyulu (Tahasildar)",
        "phone": "+91 94405 66778",
        "medical_unit": True,
        "food_stock_days": 7,
        "power_backup": "Solar Microgrid"
    },
    {
        "id": "SH-AP-07",
        "name": "Guntur Collectorate Community Relief Wing",
        "district": "Guntur",
        "river_basin": "Krishna",
        "capacity": 1600,
        "occupancy": 520,
        "lat": 16.3120,
        "lon": 80.4420,
        "officer": "D. Anitha (Sub-Collector)",
        "phone": "+91 94406 77889",
        "medical_unit": True,
        "food_stock_days": 12,
        "power_backup": "Central Power Grid + DG"
    },
    {
        "id": "SH-AP-08",
        "name": "Eluru Tammileru Catchment Relief Base",
        "district": "Eluru",
        "river_basin": "Krishna & Godavari",
        "capacity": 1400,
        "occupancy": 1150,
        "lat": 16.7180,
        "lon": 81.1020,
        "officer": "C. Suresh Babu (Revenue Div)",
        "phone": "+91 94407 88990",
        "medical_unit": True,
        "food_stock_days": 5,
        "power_backup": "125kVA Generator"
    },
    {
        "id": "SH-AP-09",
        "name": "Kakinada Port Emergency Transit Camp",
        "district": "Kakinada",
        "river_basin": "Godavari",
        "capacity": 2000,
        "occupancy": 640,
        "lat": 16.9920,
        "lon": 82.2530,
        "officer": "S. Durga Prasad (Port Trust EO)",
        "phone": "+91 94408 99001",
        "medical_unit": True,
        "food_stock_days": 9,
        "power_backup": "Marine Industrial Gen"
    },
    {
        "id": "SH-TG-01",
        "name": "Bhadrachalam Temple Choultry Emergency Relief Shelter",
        "district": "Bhadradri Kothagudem",
        "river_basin": "Godavari",
        "capacity": 2500,
        "occupancy": 2480,
        "lat": 17.6710,
        "lon": 80.8900,
        "officer": "G. Satyanarayana (ITDA Project Lead)",
        "phone": "+91 94411 22334",
        "medical_unit": True,
        "food_stock_days": 3,
        "power_backup": "200kVA High Capacity DG"
    },
    {
        "id": "SH-TG-02",
        "name": "Khammam SR&BGNR College Multi-Purpose Shelter",
        "district": "Khammam",
        "river_basin": "Krishna & Godavari",
        "capacity": 1800,
        "occupancy": 1620,
        "lat": 17.2510,
        "lon": 80.1470,
        "officer": "T. Madhavi (Municipal Comm.)",
        "phone": "+91 94412 33445",
        "medical_unit": True,
        "food_stock_days": 6,
        "power_backup": "150kVA Generator"
    },
    {
        "id": "SH-TG-03",
        "name": "Manair River Corridor Disaster Center",
        "district": "Karimnagar",
        "river_basin": "Godavari",
        "capacity": 1200,
        "occupancy": 410,
        "lat": 18.4410,
        "lon": 79.1320,
        "officer": "Y. Rajeshwar (Tahsildar)",
        "phone": "+91 94413 44556",
        "medical_unit": True,
        "food_stock_days": 10,
        "power_backup": "100kVA DG Set"
    },
    {
        "id": "SH-TG-04",
        "name": "Nizamabad SRSP Catchment Emergency Facility",
        "district": "Nizamabad",
        "river_basin": "Godavari",
        "capacity": 1500,
        "occupancy": 380,
        "lat": 18.6780,
        "lon": 78.0980,
        "officer": "E. Pradeep (Disaster Mgmt Off)",
        "phone": "+91 94414 55667",
        "medical_unit": True,
        "food_stock_days": 14,
        "power_backup": "Dual DG Backup"
    }
]

# Multilingual Alerts Templates for the 4 Alert Levels
MULTILINGUAL_ALERTS = {
    "English": {
        "Green": {
            "title": "🟢 NORMAL STATUS - KRISHNA & GODAVARI BASINS",
            "headline": "All river flows are within safe carrying capacities.",
            "instructions": "Normal monitoring in effect. No evacuation necessary. Farmers and coastal fishermen may operate regular activities.",
            "authority": "Issued by Disaster Management Authority (SDMA / NDMA)"
        },
        "Yellow": {
            "title": "🟡 WATCH ADVISORY - ELEVATED DISCHARGE",
            "headline": "Moderate river swells recorded. First warning levels approached at key barrages.",
            "instructions": "Low-lying riverbank communities should remain vigilant. Keep emergency documents, batteries, and drinking water secure.",
            "authority": "Issued by State Flood Control Cell & CWC"
        },
        "Orange": {
            "title": "🟠 FLOOD ALERT - IMMINENT HIGH INUNDATION",
            "headline": "Severe discharge surges from upstream catchments. Secondary danger mark breached.",
            "instructions": "Immediate evacuation preparations required. Move livestock and elderly to designated relief shelters. Avoid riverbed crossings.",
            "authority": "Issued by State Emergency Operations Center (SEOC)"
        },
        "Red": {
            "title": "🔴 CRITICAL DISASTER ALERT - SEVERE FLOOD EMERGENCY",
            "headline": "Catastrophic river overflows exceeding 3rd danger mark. Flash floods active across delta corridors.",
            "instructions": "EVACUATE IMMEDIATELY to designated government relief shelters. Follow NDRF/SDRF boat rescue instructions. Do not attempt road travel.",
            "authority": "AP & Telangana Disaster Response Force - EMERGENCY BROADCAST"
        }
    },
    "Telugu": {
        "Green": {
            "title": "🟢 సాధారణ స్థితి - కృష్ణా & గోదావరి పరీవాహక ప్రాంతాలు",
            "headline": "నదీ ప్రవాహాలు సురక్షిత స్థాయిలోనే ఉన్నాయి.",
            "instructions": "పరిస్థితి ప్రశాంతంగా ఉంది. తరలింపు అవసరం లేదు. రైతులు మరియు మత్స్యకారులు తమ సాధారణ కార్యకలాపాలను కొనసాగించవచ్చు.",
            "authority": "రాష్ట్ర విపత్తు నిర్వహణ సంస్థ (SDMA) ద్వారా జారీ చేయబడింది"
        },
        "Yellow": {
            "title": "🟡 పర్యవేక్షణ హెచ్చరిక (వాచ్) - నదీ ప్రవాహాల్లో పెరుగుదల",
            "headline": "ఎగువ ప్రాంతాల నుండి నీటి ప్రవాహం పెరుగుతోంది. మొదటి ప్రమాద హెచ్చరిక సమీపిస్తోంది.",
            "instructions": "నదీ తీర గ్రామాల ప్రజలు అప్రమత్తంగా ఉండాలి. ముఖ్యమైన పత్రాలు, మందులు మరియు సురక్షిత తాగునీరు అందుబాటులో ఉంచుకోండి.",
            "authority": "కేంద్ర జల సంఘం మరియు విపత్తు నివారణ విభాగం"
        },
        "Orange": {
            "title": "🟠 ముందస్తు హెచ్చరిక (అలర్ట్) - వరద ఉధృతి ప్రమాదం",
            "headline": "బ్యారేజీల వద్ద రెండవ ప్రమాద హెచ్చరిక జారీ. లంక గ్రామాలు జలదిగ్బంధంలో చిక్కుకునే అవకాశం.",
            "instructions": "తక్షణమే సహాయ పునరావాస కేంద్రాలకు వెళ్లడానికి సిద్ధం కావాలి. పశువులను ఎత్తైన ప్రదేశాలకు తరలించండి. వాగులు దాటవద్దు.",
            "authority": "రాష్ట్ర అత్యవసర ఆపరేషన్ల కేంద్రం (SEOC)"
        },
        "Red": {
            "title": "🔴 అత్యవసర ప్రమాద హెచ్చరిక (రెడ్ అలర్ట్) - తీవ్ర వరద విపత్తు",
            "headline": "మూడవ ప్రమాద హెచ్చరిక దాటి రికార్డు స్థాయి వరద నీరు ప్రవహిస్తోంది. లోతట్టు ప్రాంతాలు నీటమునిగాయి.",
            "instructions": "వెంటనే సురక్షిత ప్రభుత్వ సహాయ శిబిరాలకు తరలి వెళ్లండి! NDRF / SDRF బోట్ సిబ్బంది సూచనలను పాటించండి. అత్యవసర హెల్ప్‌లైన్: 1070/112.",
            "authority": "ఆంధ్రప్రదేశ్ & తెలంగాణ విపత్తు స్పందన దళం - అత్యవసర సందేశం"
        }
    },
    "Hindi": {
        "Green": {
            "title": "🟢 सामान्य स्थिति - कृष्णा एवं गोदावरी बेसिन",
            "headline": "सभी नदियों में जलस्तर सुरक्षित सीमा के भीतर है।",
            "instructions": "सामान्य निगरानी जारी है। किसी निकासी की आवश्यकता नहीं है। सामान्य दैनिक कार्य जारी रख सकते हैं।",
            "authority": "राज्य आपदा प्रबंधन प्राधिकरण (SDMA) द्वारा जारी"
        },
        "Yellow": {
            "title": "🟡 सतर्कता चेतावनी (वॉच) - जलस्तर में वृद्धि",
            "headline": "ऊपरी जलग्रहण क्षेत्रों से पानी की आवक बढ़ रही है। प्रथम चेतावनी स्तर के निकट।",
            "instructions": "तटीय व निचले इलाकों के निवासी सतर्क रहें। जरूरी दस्तावेज, दवाइयां व सुरक्षित पेयजल तैयार रखें।",
            "authority": "केंद्रीय जल आयोग एवं राज्य बाढ़ नियंत्रण प्रकोष्ठ"
        },
        "Orange": {
            "title": "🟠 बाढ़ चेतावनी (अलर्ट) - जलभराव का तीव्र खतरा",
            "headline": "बैराजों पर दूसरा चेतावनी स्तर पार। बाढ़ का पानी निचले इलाकों में प्रवेश कर सकता है।",
            "instructions": "राहत शिविरों में जाने की तत्काल तैयारी करें। मवेशियों को सुरक्षित ऊंचे स्थानों पर पहुंचाएं। जलमग्न रास्तों पर न जाएं।",
            "authority": "राज्य आपातकालीन संचालन केंद्र (SEOC)"
        },
        "Red": {
            "title": "🔴 गंभीर आपदा चेतावनी (रेड अलर्ट) - भीषण बाढ़ आपातकाल",
            "headline": "तीसरे खतरे के निशान को पार करते हुए रिकॉर्ड जलप्रवाह। भारी जलप्लावन जारी।",
            "instructions": "तत्काल प्रभाव से नामित राहत शिविरों में स्थानांतरित हों। एनडीआरएफ/एसडीआरएफ बचाव दल के निर्देशों का पालन करें।",
            "authority": "आपदा प्रतिक्रिया बल - आपातकालीन प्रसारण"
        }
    },
    "Tamil": {
        "Green": {
            "title": "🟢 இயல்பு நிலை - கிருஷ்ணா & கோதாவரி படுகைகள்",
            "headline": "அனைத்து நதிகளின் நீர்மட்டமும் பாதுகாப்பு வரம்பிற்குள் உள்ளது.",
            "instructions": "வழக்கமான கண்காணிப்பு தொடர்கிறது. வெளியேற்றம் தேவையில்லை. பொதுமக்கள் வழக்கம் போல் செயல்படலாம்.",
            "authority": "மாநில பேரிடர் மேலாண்மை ஆணையம் (SDMA) வழங்கியது"
        },
        "Yellow": {
            "title": "🟡 கண்காணிப்பு எச்சரிக்கை - நதி நீர் வரத்து அதிகரிப்பு",
            "headline": "நீர் வரத்து அதிகரித்துள்ளது. முதல் எச்சரிக்கை நிலையை நதிகள் எட்டுகின்றன.",
            "instructions": "தாழ்வான பகுதிகளில் உள்ள மக்கள் விழிப்புடன் இருக்கவும். அத்தியாவசிய பொருட்கள் மற்றும் குடிநீரை தயார் நிலையில் வைக்கவும்.",
            "authority": "மத்திய நீர் ஆணையம் & பேரிடர் மேலாண்மை பிரிவு"
        },
        "Orange": {
            "title": "🟠 வெள்ள எச்சரிக்கை (ஆரஞ்சு அலர்ட்) - தீவிர நீர் வரத்து",
            "headline": "இரண்டாவது அபாயக் குறியீட்டைத் தாண்டியது. கரையோரப் பகுதிகளில் நீர் புகும் அபாயம்.",
            "instructions": "உடனடியாக நிவாரண முகாம்களுக்குச் செல்ல தயாராகுங்கள். கால்நடைகளை மேடான பகுதிகளுக்கு நகர்த்தவும்.",
            "authority": "மாநில அவசரக்கால செயல்பாட்டு மையம் (SEOC)"
        },
        "Red": {
            "title": "🔴 அவசர பேரிடர் எச்சரிக்கை (ரெட் அலர்ட்) - மிகக் கடுமையான வெள்ளம்",
            "headline": "மூன்றாவது அபாய அளவைத் தாண்டி பெரும் வெள்ளப்பெருக்கு ஏற்பட்டுள்ளது.",
            "instructions": "உடனடியாக அரசு நிவாரண முகாம்களுக்கு செல்லவும்! NDRF மீட்புக் குழுவினரின் வழிமுறைகளைப் பின்பற்றவும்.",
            "authority": "பேரிடர் மீட்புப் படை - அவசர அறிவிப்பு"
        }
    },
    "Kannada": {
        "Green": {
            "title": "🟢 ಸಾಮಾನ್ಯ ಸ್ಥಿತಿ - ಕೃಷ್ಣಾ ಮತ್ತು ಗೋದಾವರಿ ಕಣಿವೆಗಳು",
            "headline": "ಎಲ್ಲಾ ನದಿಗಳ ನೀರಿನ ಮಟ್ಟವು ಸುರಕ್ಷಿತ ಮಿತಿಯಲ್ಲಿದೆ.",
            "instructions": "ಸಾಮಾನ್ಯ ನಿಗಾ ವಹಿಸಲಾಗಿದೆ. ಸ್ಥಳಾಂತರ ಅಗತ್ಯವಿಲ್ಲ. ದೈನಂದಿನ ಚಟುವಟಿಕೆಗಳು ಎಂದಿನಂತೆ ಮುಂದುವರಿಯಬಹುದು.",
            "authority": "ರಾಜ್ಯ ವಿಪತ್ತು ನಿರ್ವಹಣಾ ಪ್ರಾಧಿಕಾರ (SDMA)"
        },
        "Yellow": {
            "title": "🟡 ನಿಗಾ ಎಚ್ಚರಿಕೆ (ವಾಚ್) - ನೀರಿನ ಒಳಹರಿವು ಹೆಚ್ಚಳ",
            "headline": "ಮೇಲ್ಭಾಗದ ಪ್ರದೇಶಗಳಿಂದ ಒಳಹರಿವು ಹೆಚ್ಚುತ್ತಿದೆ. ಮೊದಲ ಎಚ್ಚರಿಕೆಯ ಮಟ್ಟ ಸಮೀಪಿಸುತ್ತಿದೆ.",
            "instructions": "ನದಿತೀರದ ಜನರು ಎಚ್ಚರದಿಂದಿರಬೇಕು. ಅಗತ್ಯ ದಾಖಲೆಗಳು, ಔಷಧಗಳು ಮತ್ತು ಕುಡಿಯುವ ನೀರನ್ನು ಸಿದ್ಧವಾಗಿಡಿ.",
            "authority": "ಕೇಂದ್ರ ಜಲ ಆಯೋಗ ಮತ್ತು ಪ್ರವಾಹ ನಿಯಂತ್ರಣ ಕೊಠಡಿ"
        },
        "Orange": {
            "title": "🟠 ಪ್ರವಾಹ ಎಚ್ಚರಿಕೆ (ಆರೆಂಜ್ ಅಲರ್ಟ್) - ತೀವ್ರ ಪ್ರವಾಹದ ಭೀತಿ",
            "headline": "ಎರಡನೇ ಅಪಾಯದ ಮಟ್ಟವನ್ನು ಮೀರಿದೆ. ತಗ್ಗು ಪ್ರದೇಶಗಳು ಜಲಾವೃತಗೊಳ್ಳುವ ಸಾಧ್ಯತೆ.",
            "instructions": "ತಕ್ಷಣವೇ ಪರಿಹಾರ ಶಿಬಿರಗಳಿಗೆ ತೆರಳಲು ಸಿದ್ಧರಾಗಿ. ಜಾನುವಾರುಗಳನ್ನು ಸುರಕ್ಷಿತ ಎತ್ತರದ ಪ್ರದೇಶಗಳಿಗೆ ಸ್ಥಳಾಂತರಿಸಿ.",
            "authority": "ರಾಜ್ಯ ತುರ್ತು ಕಾರ್ಯಾಚರಣೆ ಕೇಂದ್ರ (SEOC)"
        },
        "Red": {
            "title": "🔴 ತುರ್ತು ಅಪಾಯದ ಎಚ್ಚರಿಕೆ (ರೆಡ್ ಅಲರ್ಟ್) - ಭೀಕರ ಪ್ರವಾಹ ವಿಪತ್ತು",
            "headline": "ಮೂರನೇ ಅಪಾಯದ ಮಟ್ಟ ಮೀರಿ ದಾಖಲೆ ಪ್ರಮಾಣದ ಪ್ರವಾಹ ನೀರು ಹರಿಯುತ್ತಿದೆ.",
            "instructions": "ತಕ್ಷಣವೇ ನಿಗದಿತ ಸರ್ಕಾರಿ ಪರಿಹಾರ ಶಿಬಿರಗಳಿಗೆ ತೆರಳಿ! NDRF / SDRF ರಕ್ಷಣಾ ಸಿಬ್ಬಂದಿಯ ಸೂಚನೆಗಳನ್ನು ಕಡ್ಡಾಯವಾಗಿ ಪಾಲಿಸಿ.",
            "authority": "ವಿಪತ್ತು ಸ್ಪಂದನಾ ಪಡೆ - ತುರ್ತು ಪ್ರಕಟಣೆ"
        }
    }
}

# Candidate Sensor Coordinates for Quantum Sensor Placement Module (24 nodes across Godavari & Krishna)
SENSOR_CANDIDATES = [
    {"id": "NODE-01", "name": "Srisailam Reservoir Forebay", "basin": "Krishna", "lat": 16.082, "lon": 78.889, "risk_weight": 0.88, "type": "Radar Gauge"},
    {"id": "NODE-02", "name": "Nagarjuna Sagar Tailpond", "basin": "Krishna", "lat": 16.581, "lon": 79.324, "risk_weight": 0.82, "type": "Ultrasonic Telemetry"},
    {"id": "NODE-03", "name": "Prakasam Barrage Inflow", "basin": "Krishna", "lat": 16.512, "lon": 80.601, "risk_weight": 0.96, "type": "Multi-Param Hydro Station"},
    {"id": "NODE-04", "name": "Vijayawada Budameru Inundation Confluence", "basin": "Krishna", "lat": 16.529, "lon": 80.648, "risk_weight": 0.94, "type": "Optical Water Level Sensor"},
    {"id": "NODE-05", "name": "Avanigadda Delta Outfall", "basin": "Krishna", "lat": 16.015, "lon": 80.925, "risk_weight": 0.91, "type": "Tidal Surge Gauge"},
    {"id": "NODE-06", "name": "Hamsaladeevi Krishna Sea Estuary", "basin": "Krishna", "lat": 15.820, "lon": 80.950, "risk_weight": 0.89, "type": "Ocean Hydro Gauge"},
    {"id": "NODE-07", "name": "Guntur Right Canal Head Sluice", "basin": "Krishna", "lat": 16.321, "lon": 80.450, "risk_weight": 0.74, "type": "Acoustic Doppler"},
    {"id": "NODE-08", "name": "Khammam Muneru Inundation Point", "basin": "Krishna", "lat": 17.240, "lon": 80.145, "risk_weight": 0.92, "type": "Flash Flood Radar"},
    {"id": "NODE-09", "name": "Wyra Catchment Confluence", "basin": "Krishna", "lat": 17.200, "lon": 80.350, "risk_weight": 0.79, "type": "Ultrasonic Gauge"},
    {"id": "NODE-10", "name": "Jaggayyapet Krishna Entry Point", "basin": "Krishna", "lat": 16.890, "lon": 80.090, "risk_weight": 0.83, "type": "Flow Telemetry"},
    {"id": "NODE-11", "name": "Repalle Lowland Tidal Sensor", "basin": "Krishna", "lat": 16.020, "lon": 80.840, "risk_weight": 0.85, "type": "Salinity & Level Sensor"},
    {"id": "NODE-12", "name": "Nandigama Flood Spillway", "basin": "Krishna", "lat": 16.780, "lon": 80.290, "risk_weight": 0.77, "type": "Precipitation & Stage"},

    {"id": "NODE-13", "name": "Bhadrachalam Ghat Main Telemetry", "basin": "Godavari", "lat": 17.669, "lon": 80.893, "risk_weight": 0.98, "type": "Dual Radar Level Sensor"},
    {"id": "NODE-14", "name": "Kunavaram Sabari Confluence", "basin": "Godavari", "lat": 17.580, "lon": 81.260, "risk_weight": 0.95, "type": "Multi-Tributary Gauge"},
    {"id": "NODE-15", "name": "Polavaram Upstream Coffer Dam", "basin": "Godavari", "lat": 17.265, "lon": 81.645, "risk_weight": 0.97, "type": "Satellite IoT Hydro Station"},
    {"id": "NODE-16", "name": "Dowleswaram Barrage Head", "basin": "Godavari", "lat": 16.942, "lon": 81.771, "risk_weight": 0.96, "type": "Multi-Beam Acoustic Flow"},
    {"id": "NODE-17", "name": "Rajahmundry Pushkar Ghat", "basin": "Godavari", "lat": 17.008, "lon": 81.775, "risk_weight": 0.93, "type": "Submersible Level Sensor"},
    {"id": "NODE-18", "name": "Amalapuram Gautami Branch Point", "basin": "Godavari", "lat": 16.582, "lon": 82.003, "risk_weight": 0.90, "type": "Delta Flow Transducer"},
    {"id": "NODE-19", "name": "Narsapur Vasishta Estuary", "basin": "Godavari", "lat": 16.442, "lon": 81.701, "risk_weight": 0.87, "type": "Tidal Wave Telemetry"},
    {"id": "NODE-20", "name": "Kakinada Yeleru Outfall Sluice", "basin": "Godavari", "lat": 16.985, "lon": 82.240, "risk_weight": 0.81, "type": "Optical Stream Gauge"},
    {"id": "NODE-21", "name": "Eluru Kolleru Lake Surge Node", "basin": "Godavari", "lat": 16.650, "lon": 81.250, "risk_weight": 0.86, "type": "Wetland Hydro Station"},
    {"id": "NODE-22", "name": "Manair Dam Outflow Karimnagar", "basin": "Godavari", "lat": 18.420, "lon": 79.110, "risk_weight": 0.78, "type": "Reservoir Level Transmitter"},
    {"id": "NODE-23", "name": "SRSP Dam Forebay Nizamabad", "basin": "Godavari", "lat": 18.970, "lon": 78.330, "risk_weight": 0.84, "type": "Ultrasonic Telemetry"},
    {"id": "NODE-24", "name": "Kaleshwaram Medigadda Inflow Point", "basin": "Godavari", "lat": 18.790, "lon": 79.950, "risk_weight": 0.89, "type": "High-Volume Doppler Station"}
]
