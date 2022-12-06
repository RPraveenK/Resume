# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:56:45 2022

@author: z013012
"""
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume - Praveen Kumar.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Praveen Kumar Renganathan"
PAGE_ICON = ":wave:"
NAME = "Praveen Kumar Renganathan"
DESCRIPTION = """
Senior Production Engineer - PowerTrain IoT Data Analysis and Tooling Activities
"""
ADDRESS="""
🏠 ADDRESS: \n
Villa 312 GF, Avigna Celeste, \n
Eachankaranai Village, Kunnavakkam Post, \n
Chengalpattu, Tamil Nadu - 603002
"""
MOBILE="📲 CONTACT: +91-9500214154"

EMAIL = "pravinpforpolite@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/praveen-kumar-r-b28a3998/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(ADDRESS)
    st.write(MOBILE)
    st.write("📫", EMAIL)
    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ► 8 Years 2 Months in Power Train Projects 
    - @ RENAULT NISSAN TECHNOLOGY BUSINESS CENTER INDIA ➡️ Sept'14 to Till Date
- ► Holding a bachelor's Degree in Mechanical Engineering with 7.71 CGPA
    - @ KCG College of Technology, Karapakkam, Chennai -97
- ► Strong hands-on experience and knowledge in Python, Excel and AutoCAD
- ► Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ►  👩‍💻 Programming: Python (Pandas, PysimpleGUI), Microsoft Excel VBA
- ►  📊 Data Visualization: MS Excel, Matplotlib
- ►  ✍ Drafting: AutoCAD
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**SENIOR PRODUCTION ENGINEER | RENAULT NISSAN TECHNOLOGY BUSINESS CENTER INDIA**")
st.write("05/2021 - Present ➡️ POWER TRAIN IOT DATA ANALYSIS AND TOOLING PROJECTS")
st.write(
    """
- ► Created Excel VBA Program to Automate Nissan JATCO Gearbox Cost Reduction Results for Easy Customer Interpretation
- ► Using Excel VBA Program and MS Access created a Tooling Drawing Database
- ► Created a Standalone XIGMA Dashboard for Easy Data Interpretation and Analysis the Individual Testbench Overall Status and Monitoring using Self Learned Python Programming using Python Pandas and Matplotlib libraries and delivered to Nissan Yokohama Plant.
- ► Using Python PysimpleGUI Created an application to Prepare Tooling Standardisation Sheet as per the Input Machining Condition
"""
)

# --- JOB 2
st.write('\n')
st.write("07/2017 - 05/2021 ➡️ Gasoline Engine Assembly and Testing Process Engineering Activity") 
st.write(
    """
- ► Process Designer for New Engine Assembly Projects, Including Proto Engine Assembly and Testing
- ► Operating Standard Creation, Process Sequence Derivation, Cycle Time Calculations, Job allocation and Line balancing activities for New Engine Assembly Models and Projects
- ► Responsible for Serial Life Product Changes Implementation and Handover
- ► Process Responsible for Cylinder Head Sub Assembly Line, Short Engine Monitoring Test Bench and Variable Valve Timing Checking Machine
- ► Responsible for Engine Testing bed Wiring Harness Development and Proving both Industrial and Vehicle Wiring Harness
- ► Knowledge on Industrial Type Wiring Harness
- ► Engine Assembly Production and Process Documentation Creation
- ► Engine Assembly Line Poka-Yoke and Assembly Jigs and Tools Planning and Implementation for New and Serial Life Engine Models.
- ► New Facility RFQ Creation, SAP PR Creation, Technical and Commercial validation, Delivery, and Installation follow-ups with Suppliers, Trial Completion, Machine Proving and Handover for Mass Production
- ► Experienced in Assembly Line Process Capability improvement activity
- ► Experienced in Engine Malfunction Check and Assembly Line Process Improvement
"""
)

# --- JOB 3
st.write('\n')
st.write("08/2014 - 06/2017 ➡️ Power Train Project Management Activities")
st.write(
    """
- ► Project Management Activities for Power Train Projects
- ► Purchase and Finance Coordination for Power Train activity
- ► Budget Framing, Shopping List Creation and Follow-up for both CAPITAL EXPENSES and OPERATIONAL EXPENSES
- ► Manpower and related cost Calculations for New Projects
- ► Product wise COST PER UNIT Calculations and over all Power Train COST PER UNIT Calculations activity
- ► Workload and Work Force management for Team
- ► Regular Tracking of Project Budget and Cash out Tracking for Power Train Activity
- ► Project Scheduling and Follow-up
"""
)

# --- PROJECTS HANDLED ---
st.write('\n')
st.subheader("Projects Handled")
st.write(
    """
- ► Power Train Project Management (BR Engine Models, Sxx Gearbox Models)
- ►  Engine Assembly and Engine Testing Process Engineering \n
    - Renault – KWID, TRIBER and KIGER \n
    - Nissan – MAGNITE \n
    - Datsun – Redi-GO \n
"""
)

# --- Project Accomplishments ---
st.write('\n')
st.subheader("Project Accomplishments")
st.write(
    """
- ► BR Engine Models Emission Norms Upgradation \n
    - Worked individually for BS IV to BS VI Step 1 Engine Emission Norms Upgradation and got appreciation from RNTBCI MD and Received Gold Special Award for the same
- ► XIGMA Dashboard using Python Programming \n
    - Concept and Algorithm Created using Python Software for an Automated Dashboard for Data Analysis Activity from Scratch using Self Learned Knowledge on Python Programming Software \n
    - Department Vice President Appreciated and recognized as Individual Achiever for the Month
"""
)

# --- Skill Set ---
st.write('\n')
st.subheader("Additional Skill Set")
st.write(
    """
- ► SIEMENS PLC Ladder and SCADA Programming – Certified by LiveWire \n
    - Basic Knowledge in SIEMENS Step 7 PLC Ladder Programming \n
    - Basic Knowledge in WinCC SCADA Programming \n
- ► Microsoft Office \n
    - Strong Knowledge in MS Excel Pivot and VBA Macro Program Creation \n
- ► AutoCAD \n
    - 2D Sketching and Tool and Tool Holder Assembly Drawings \n
- ► Python Programming \n
    - Basic Boot Camp Couse Completed through Udemy – Course Completed Certified \n
    - On Going a Certification Course on Python Through NPTEL \n
- ► MATLAB Programming \n
    - Basic Couse Ongoing through Udemy  
"""
)
