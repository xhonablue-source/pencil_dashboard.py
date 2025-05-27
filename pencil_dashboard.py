import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches  # Fixed import!
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MathCraft | 4th Grade Area & Measurement", 
    layout="centered",
    page_icon="🧮"
)

# Header with logo-style branding
st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;">
    <h2 style="color: white; margin: 0; font-weight: bold;">🧮 MathCraft</h2>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">Hands-On Mathematical Thinking</p>
    <p style="color: #e0e0e0; margin: 0; font-size: 0.8rem; margin-top: 0.5rem;">© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

st.title("📀 4th Grade Math: Area and Measurement with a Pencil")

# Michigan Learning Standards
st.markdown("---")
st.markdown("### 📚 Michigan Learning Standards Addressed")
with st.expander("Click to view aligned standards"):
    st.markdown("""
    **4.MD.1** - Know relative sizes of measurement units within one system of units including km, m, cm; kg, g; lb, oz.; l, ml; hr, min, sec.
    
    **4.MD.2** - Use the four operations to solve word problems involving distances, intervals of time, liquid volumes, masses of objects, and money.

    **4.MD.3** - Apply the area and perimeter formulas for rectangles.

    **4.OA.3** - Solve multistep word problems using the four operations.

    **Mathematical Practices:**
    - **MP.1** - Make sense of problems and persevere
    - **MP.5** - Use appropriate tools strategically
    - **MP.6** - Attend to precision
    """)
st.markdown("---")

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student Info
st.markdown("---")
st.markdown("### 👨‍🎓 Student Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name:", key="student_name")
with col2:
    date = st.text_input("Date:", key="student_date")
st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective
st.markdown("---")
st.markdown("""
### 🧠 Learning Objective
Use estimation, measurement tools, and reasoning to explore **area, perimeter, and measurement conversions**.

### 📦 Materials Needed
- 📝 **Wood pencil**
- ⚪ **Correction tape**
- 📏 **Ruler**
""")

# Step 1: Estimation
st.markdown("---")
st.markdown("### 📏 Step 1: Make Your Estimate")
st.markdown("Look at your pencil. How many strips of correction tape to cover the length?")

estimation = st.slider("My Estimate (number of strips):", 1, 10, 4)

fig1, ax1 = plt.subplots(figsize=(6, 3))
for i in range(10):
    color = "gold" if i < estimation else "lightgray"
    ax1.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor='black'))
    ax1.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1)
ax1.set_title(f"Your Estimate: {estimation} strips")
ax1.axis('off')
st.pyplot(fig1)

st.session_state.responses["Estimate"] = estimation

# Analytical Thinking Step
st.markdown("### 🧠 Analytical Thinking Step 1: Reasoning About Estimates")
st.markdown("""
- Why is **zero** not a valid option?
- Is **10** a good maximum estimate? Why or why not?
- Why might it be unhelpful to allow higher numbers?
- What would **your** maximum estimate be?
- How did you decide that number?

Write or discuss your ideas below before moving on:
""")
analysis_response = st.text_area("Write your thoughts here:", key="analytical_estimate")
st.session_state.responses["Estimate_Analysis"] = analysis_response

# Step 2: Actual Measurement
st.markdown("---")
st.markdown("### 📀 Step 2: Measure with Real Tape")
st.markdown("Now use white correction tape to measure your pencil.")

actual_strips = st.number_input("Actual number of strips used:", 1, 10, 1)

f
