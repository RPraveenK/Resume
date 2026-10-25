import base64
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="R. Praveen Kumar | Industrial IoT Developer", page_icon="🏭", layout="wide")

HERE = Path(__file__).parent

# ---------- Background: IoT machines drawn as line art (SVG) ----------
BG_SVG = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1400 900'>
<g fill='none' stroke='#3fd0c9' stroke-width='2' opacity='.5'>
<!-- CNC machine -->
<rect x='60' y='520' width='380' height='260' rx='8'/><rect x='90' y='550' width='230' height='170' rx='4'/>
<line x1='205' y1='550' x2='205' y2='720'/><rect x='340' y='550' width='70' height='110'/>
<circle cx='375' cy='690' r='14'/><path d='M200 580 v40 m-12 0 h24 l-12 24 z'/>
<!-- PLC rack -->
<rect x='1010' y='560' width='320' height='170' rx='6'/>
<rect x='1030' y='580' width='60' height='130'/><rect x='1100' y='580' width='60' height='130'/>
<rect x='1170' y='580' width='60' height='130'/><rect x='1240' y='580' width='70' height='60'/>
<circle cx='1060' cy='600' r='5'/><circle cx='1130' cy='600' r='5'/><circle cx='1200' cy='600' r='5'/>
<!-- Robot arm -->
<rect x='620' y='700' width='140' height='30'/><path d='M690 700 L660 560 L780 470 L860 520'/>
<circle cx='660' cy='560' r='16'/><circle cx='780' cy='470' r='14'/><path d='M860 520 l20 20 m-20 -20 l-24 14'/>
<!-- Camera on stand (vision) -->
<rect x='500' y='200' width='90' height='50' rx='6'/><circle cx='545' cy='225' r='14'/><path d='M545 250 v90 m-30 0 h60'/>
<path d='M545 225 L430 330 M545 225 L660 330' stroke-dasharray='6 8'/>
<!-- Edge gateway + cloud -->
<rect x='980' y='160' width='150' height='90' rx='8'/><circle cx='1000' cy='180' r='5'/>
<path d='M1210 240 a30 30 0 0 1 10 -58 a42 42 0 0 1 80 10 a28 28 0 0 1 -6 48 z'/>
</g>
<g fill='none' stroke='#ffb020' stroke-width='1.6' stroke-dasharray='4 10' opacity='.5'>
<path d='M250 520 C250 400 400 300 500 225'/><path d='M590 225 C760 190 880 200 980 205'/>
<path d='M1130 205 L1215 215'/><path d='M1170 560 C1170 400 1130 300 1060 250'/>
<path d='M780 470 C860 400 900 300 980 230'/>
</g>
<g fill='#ffb020' opacity='.7'>
<circle cx='250' cy='520' r='6'/><circle cx='1060' cy='250' r='6'/><circle cx='780' cy='470' r='6'/><circle cx='545' cy='225' r='6'/>
</g></svg>"""
bg = base64.b64encode(BG_SVG.encode()).decode()

# ---------- Profile photo: put profile.jpg / .jpeg / .png next to app.py ----------
photo_html = '<div class="avatar">PK</div>'
for name in ("profile.jpg", "profile.jpeg", "profile.png"):
    p = HERE / name
    if p.exists():
        mime = "png" if name.endswith("png") else "jpeg"
        b64 = base64.b64encode(p.read_bytes()).decode()
        photo_html = f'<img class="avatar" src="data:image/{mime};base64,{b64}" alt="R. Praveen Kumar">'
        break

st.markdown(
    f"""
<style>
.stApp {{
  background: linear-gradient(rgba(13,24,33,.86), rgba(13,24,33,.93)),
              url("data:image/svg+xml;base64,{bg}") center / cover fixed no-repeat;
}}
header[data-testid="stHeader"] {{ background: transparent; }}
.stApp {{ color-scheme: dark; }}
.stApp :where(h1, h2, h3, h4, p, li, label, span, div[data-testid="stMarkdownContainer"]) {{ color: #e6eef3; }}
.stApp a {{ color: #3fd0c9 !important; }}
[data-testid="stMetricLabel"] *, [data-testid="stMetricLabel"] {{ color: #9bb0bf !important; }}
[data-testid="stMetricValue"], [data-testid="stMetricValue"] * {{ color: #e6eef3 !important; }}
button[data-baseweb="tab"] {{ color: #9bb0bf !important; }}
button[data-baseweb="tab"][aria-selected="true"] {{ color: #ffb020 !important; }}
[data-baseweb="tab-highlight"] {{ background-color: #ffb020 !important; }}
[data-testid="stBaseButton-primary"] {{ background: #ffb020 !important; border-color: #ffb020 !important; }}
[data-testid="stBaseButton-primary"], [data-testid="stBaseButton-primary"] * {{ color: #1a1200 !important; }}
div[role="radiogroup"] label * {{ color: #e6eef3 !important; }}
.block-container {{ max-width: 1000px; padding-top: 2.5rem; }}
h1, h2, h3 {{ letter-spacing: -.01em; }}
.avatar {{ width: 190px; height: 190px; border-radius: 50%; object-fit: cover;
  border: 3px solid #ffb020; box-shadow: 0 0 0 6px rgba(255,176,32,.15), 0 0 40px rgba(63,208,201,.25);
  display: flex; align-items: center; justify-content: center; font-size: 64px; font-weight: 700;
  color: #ffb020; background: #142431; }}
.role {{ color: #3fd0c9; font-size: 1.3rem; margin: -.4rem 0 .8rem; }}
.lead {{ color: #b9c9d4; max-width: 60ch; }}
div[data-testid="stMetric"] {{ background: rgba(20,36,49,.8); border-left: 3px solid #ffb020;
  padding: 10px 14px; border-radius: 6px; }}
.chip {{ display: inline-block; background: rgba(20,36,49,.9); border: 1px solid #25394a;
  padding: 5px 12px; margin: 0 6px 8px 0; border-radius: 6px; font-size: .95rem; }}
.card {{ background: rgba(20,36,49,.85); border: 1px solid #25394a; border-radius: 10px; padding: 16px 18px; height: 100%; }}
.card b {{ font-size: 1.1rem; }} .card p {{ color: #9bb0bf; margin: .3rem 0 .5rem; }}
.card em {{ color: #ffb020; font-style: normal; font-size: .9rem; }}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- Hero ----------
c1, c2 = st.columns([1, 2.4], gap="large", vertical_alignment="center")
with c1:
    st.markdown(photo_html, unsafe_allow_html=True)
with c2:
    st.title("R. Praveen Kumar")
    st.markdown('<div class="role">Industrial IoT & Software Developer</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="lead">I build C++, C#, Python and Qt/QML software that reads CNCs and PLCs, '
        "shows operators what is happening, and stops errors before they leave the machine. "
        "Over 2 years in Industrial IoT, including a year at Nissan Yokohama, Japan, on top of "
        "12+ years in powertrain manufacturing.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "📍 Chengalpattu, Tamil Nadu  ·  ✉️ [pravinpforpolite@gmail.com](mailto:pravinpforpolite@gmail.com)"
        "  ·  📞 [+91 95002 14154](tel:+919500214154)"
    )
    st.markdown(
        "🔗 [LinkedIn](https://www.linkedin.com/in/praveen-kumar-renganathan-b28a3998)"
        "  ·  💻 [GitHub](https://github.com/RPraveenK)"
    )

resume = HERE / "Praveen_Kumar_Resume.pdf"
if resume.exists():
    st.download_button(
        "Download resume (PDF)",
        data=resume.read_bytes(),
        file_name="Praveen_Kumar_Resume.pdf",
        mime="application/pdf",
        type="primary",
        icon=":material/download:",
    )

m = st.columns(4)
m[0].metric("Industrial IoT", "2+ yrs")
m[1].metric("Manufacturing", "12+ yrs")
m[2].metric("On-site at Nissan Japan", "1 yr")
m[3].metric("Nissan F-Pilot", "Certified")

# ---------- Experience ----------
st.header("Experience")
ROLES = {
    "IoT Developer, Assistant Manager (2025 – now)": (
        "RNTBCI, MWC, Chengalpattu",
        [
            "Develop IIoT apps in C++, C#, Python and VB for NC/PLC/PMC data logging and real-time production monitoring.",
            "Build edge-computing systems and Qt/QML HMIs for machine diagnostics and operator interfaces.",
            "Develop vision-based Poka-Yoke with OpenCV and YOLO, integrated with machines through OEM SDKs.",
            "Certified to develop and maintain F-Pilot systems under Nissan standards: architecture, testing, defect investigation, performance tuning.",
            "Own IoT edge-device deployment end to end, from RFQ and specification to installation.",
            "Create dashboards for production decisions and lead plant-wide digital transformation.",
        ],
    ),
    "IoT Developer, NPTP Trainee (2024 – 2025)": (
        "Nissan Motor Corporation, Yokohama, Japan",
        [
            "Selected for the Nissan Production Technology Partnership programme to specialise in Industrial IoT.",
            "Designed and deployed a Quality Gate IoT application that improved inspection accuracy and cycle time.",
            "Built CNC/PLC data acquisition with FANUC FOCAS and Keyence KVCom+ over factory networks.",
            "Earned Business Digital Engineer (BDE) certification.",
        ],
    ),
    "IoT Data Analyst & RPA Developer (2021 – 2024)": (
        "RNTBCI, MWC (Senior Production Engineer)",
        [
            "Built and deployed the Python XIGMA Dashboard at Nissan Yokohama.",
            "Built a Tooling Drawing Management System (VBA + MS Access), Excel-VBA tools and PySimpleGUI apps.",
            "Developed MATLAB automated error-judgment and real-time alerts for NC machining during a 3-month assignment in Japan.",
            "Used data analysis and prediction to reduce failures and improve machining quality.",
        ],
    ),
    "Manufacturing Engineering (2014 – 2021)": (
        "RNTBCI",
        [
            "Engine Assembly & Testing Process Engineer: prototype engine processes, line balancing, test-bed wiring harnesses, RFQ and machine proving.",
            "Project Management Engineer: CAPEX/OPEX budgets, schedules and supplier coordination for powertrain programmes.",
        ],
    ),
}
tabs = st.tabs(list(ROLES.keys()))
for tab, (org, points) in zip(tabs, ROLES.values()):
    with tab:
        st.markdown(f"**{org}**")
        for p in points:
            st.markdown(f"- {p}")

# ---------- Skills ----------
st.header("Skills")
SKILLS = {
    "Languages": ["C++17+", "Embedded C/C++", "C#", "Python", "VB", "MATLAB", "Excel VBA"],
    "Embedded": ["Modern Embedded C++", "FreeRTOS"],
    "GUI & HMI": ["Qt/QML", "PySimpleGUI", "Diagnostic screens", "Operator interfaces"],
    "IoT & protocols": ["FANUC FOCAS", "Keyence KVCom+", "NC/PLC/PMC", "Edge computing", "Device SDKs", "Factory networks"],
    "Vision & AI": ["OpenCV", "Ultralytics YOLO", "Pandas", "Matplotlib", "Vision Poka-Yoke"],
    "Automation": ["Siemens Step 7", "Ladder Logic", "Delta PLC", "WinCC SCADA"],
    "Tooling": ["CMake", "qmake", "Visual Studio", "MS Access"],
}
area = st.radio("Area", ["All"] + list(SKILLS), horizontal=True, label_visibility="collapsed")
items = [s for k, v in SKILLS.items() if area in ("All", k) for s in v]
st.markdown("".join(f'<span class="chip">{s}</span>' for s in items), unsafe_allow_html=True)

# ---------- Projects ----------
st.header("Projects and recognition")
PROJECTS = [
    ("XIGMA Python Dashboard", "Production dashboard built and deployed at Nissan Yokohama.", "Individual Achiever of the Month, by the Department VP"),
    ("Quality Gate IoT Application", "Inspection app for a new-technology machine, with better accuracy and cycle time.", "Earned Business Digital Engineer certification"),
    ("Automated error-judgment system", "MATLAB and vision-based judgment with real-time alerts for NC machining in Japan.", "Improved defect-detection accuracy"),
    ("BR Engine BS IV to BS VI upgrade", "Step-1 upgrade of the engine programme.", "Gold Special Award, RNTBCI Managing Director"),
]
cols = st.columns(2)
for i, (t, d, r) in enumerate(PROJECTS):
    cols[i % 2].markdown(f'<div class="card"><b>{t}</b><p>{d}</p><em>{r}</em></div>', unsafe_allow_html=True)
    cols[i % 2].write("")

# ---------- Certifications and education ----------
st.header("Certifications")
st.markdown(
    "- **F-Pilot Crew System Developer**, Nissan (Oct 2026)\n"
    "- **Modern Embedded C++ with FreeRTOS**, Future Shock Technologies (May 2026)\n"
    "- **Business Digital Engineer (BDE)**, Nissan (2025)\n"
    "- **PLC and SCADA course**, LIVEWIRE India (Feb 2020)"
)
st.header("Education and languages")
st.markdown(
    "B.E. Mechanical Engineering, KCG College of Technology, Chennai (CGPA 7.71, 2010 – 2014).  \n"
    "Tamil (native), English (professional), Japanese (basic, studying for JLPT N5)."
)
