import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MathCraft | 4th Grade Area & Measurement", 
    layout="centered",
    page_icon="🧫"
)

# Header
st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;">
    <h2 style="color: white; margin: 0; font-weight: bold;">🧫 MathCraft</h2>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">Hands-On Mathematical Thinking</p>
    <p style="color: #e0e0e0; margin: 0; font-size: 0.8rem; margin-top: 0.5rem;">© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

st.title("📀 4th Grade Math: Area and Measurement with a Pencil")

# Standards
st.markdown("---")
st.markdown("### 📚 Michigan Learning Standards Addressed")
with st.expander("Click to view aligned standards"):
    st.markdown("""
    **4.MD.1** - Know relative sizes of measurement units.
    **4.MD.2** - Solve word problems involving measurements.
    **4.MD.3** - Apply area and perimeter formulas.
    **4.OA.3** - Solve multistep problems using the four operations.
    **MP.1** - Make sense of problems
    **MP.5** - Use tools strategically
    **MP.6** - Attend to precision
    """)
st.markdown("---")

# State init
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student info
st.markdown("### 👨‍🎓 Student Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name:")
with col2:
    date = st.text_input("Date:")
st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective
st.markdown("---")
st.markdown("""
### 🧠 Learning Objective
Explore area and measurement by estimating how many white tape strips are needed to cover the entire length on all sides of a pencil.

### 🛆 Materials Needed
- 📝 Pencil
- ⚪ BIC Wite-Out EZ Correct tape
- 📏 Ruler
""")

# Step 1: Estimate
st.markdown("---")
st.markdown("### 📏 Step 1: Make Your Estimate")
st.markdown("How many strips of white correction tape will it take to cover the entire length on all sides of your pencil?")
estimation = st.slider("My Estimate:", 1, 10, 4)
fig1, ax1 = plt.subplots(figsize=(6, 3))
for i in range(10):
    color = "gold" if i < estimation else "lightgray"
    ax1.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor='black'))
    ax1.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold')
ax1.axis('off')
ax1.set_title(f"Your Estimate: {estimation} strips")
st.pyplot(fig1)
st.session_state.responses["Estimate"] = estimation

# Step 2: Actual
st.markdown("---")
st.markdown("### 📀 Step 2: Measure with Tape")
actual = st.number_input("Actual number of strips:", 1, 10, 1)
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(10, 3))
for i in range(10):
    ax2.add_patch(plt.Rectangle((i, 0), 0.8, 1, color="gold" if i < estimation else "lightgray", edgecolor='black'))
    ax3.add_patch(plt.Rectangle((i, 0), 0.8, 1, color="orange" if i < actual else "lightgray", edgecolor='black'))
for ax in [ax2, ax3]:
    ax.set_xlim(0, 10)
    ax.axis('off')
ax2.set_title(f"Estimate: {estimation}")
ax3.set_title(f"Actual: {actual}")
st.pyplot(fig2)
st.session_state.responses["Actual_Strips"] = actual

# Step 3: Length & Width
st.markdown("---")
st.markdown("### 📏 Step 3: Measure Pencil Length and Tape Width")
col1, col2 = st.columns(2)
with col1:
    inches = st.number_input("Length of pencil (in inches):", 0.0, 20.0, 0.0, step=0.1)
with col2:
    width_str = st.selectbox("Tape width (fraction of an inch):", ["1/8", "1/4", "1/3", "3/8", "1/2", "2/3", "3/4", "7/8", "1"], index=4)
fraction_map = {"1/8": 0.125, "1/4": 0.25, "1/3": 1/3, "3/8": 0.375, "1/2": 0.5, "2/3": 2/3, "3/4": 0.75, "7/8": 0.875, "1": 1.0}
tape_width = fraction_map[width_str]
st.session_state.responses.update({"Inches": inches, "Tape_Width": tape_width, "Tape_Width_Fraction": width_str})

# Step 4: Cross section
st.markdown("---")
st.markdown("### ⭕ Step 4: Estimate Tape Pieces Around the Pencil")
circumference = st.slider("Estimated number of strips around:", 1, 8, 6)
fig3, ax4 = plt.subplots(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='#DEB887', alpha=0.7)
ax4.add_patch(circle)
deg = 360 / circumference
for i in range(circumference):
    ax4.add_patch(mpatches.Wedge((0, 0), 1.2, i * deg, (i + 1) * deg, width=0.15, facecolor="white", edgecolor='black'))
ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.axis('off')
ax4.set_title(f"{circumference} strips around pencil")
st.pyplot(fig3)
st.session_state.responses["Circumference_Estimate"] = circumference

# Step 5: Area
st.markdown("---")
st.markdown("### 🛆 Step 5: Calculate Surface Area")
if inches > 0 and tape_width > 0 and circumference > 0:
    area = inches * tape_width * circumference
    st.success(f"Total Surface Area: {area:.2f} square inches")
    st.session_state.responses.update({"Calculated_Area": area})

# Analytical Thinking
st.markdown("---")
st.markdown("### 🧠 Analytical Thinking")
q1 = st.selectbox("If you doubled the tape width...", ["It would stay the same", "It would double", "It would be cut in half", "It would increase a little"])
q2 = st.selectbox("Why might your estimate differ...", ["I misjudged the pencil", "Didn't consider all sides", "Tape stretched", "All of the above"])
q3 = st.selectbox("Which would NOT affect surface area?", ["Number of tape strips", "Width of tape", "Color of tape", "Pencil length"])
q4 = st.selectbox("Friend's pencil is twice as long...", ["About the same", "Twice as much", "Half as much", "Need tape width to know"])
q5 = st.selectbox("If you wrapped diagonally...", ["Perimeter", "Area", "Length", "None"])
st.session_state.responses.update({"Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5})

# Reflection
st.markdown("---")
st.markdown("### 💭 Reflection")
r1 = st.text_area("1. What surprised you most?")
r2 = st.text_area("2. Why is estimation useful?")
r3 = st.text_area("3. Which measurement felt more natural?")
st.session_state.responses.update({"Reflection_1": r1, "Reflection_2": r2, "Reflection_3": r3})

# Submit
if st.button("✅ Submit My Work"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success("Responses saved!")
    else:
        st.error("Please enter your name and date.")

# Teacher View
if st.checkbox("🏫 Teacher View"):
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df)
    else:
        st.info("No submissions yet.")

# Footer
st.markdown("---")
st.markdown("*Keep estimating, measuring, and improving. Great math thinkers build through practice!* 🌟")
