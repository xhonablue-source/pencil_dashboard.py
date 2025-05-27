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

st.title("📐 4th Grade Math: Area and Measurement with a Pencil")

# Michigan Learning Standards
st.markdown("---")
st.markdown("### 📚 Michigan Learning Standards Addressed")
with st.expander("Click to view aligned standards"):
    st.markdown("""
    **4.MD.1** - Know relative sizes of measurement units within one system of units including km, m, cm; kg, g; lb, oz.; l, ml; hr, min, sec.
    **4.MD.2** - Use the four operations to solve word problems involving measurements.
    **4.MD.3** - Apply the area and perimeter formulas for rectangles.
    **4.OA.3** - Solve multistep word problems using the four operations.
    **Mathematical Practices:**
    - **MP.1** - Make sense of problems and persevere in solving them
    - **MP.5** - Use appropriate tools strategically  
    - **MP.6** - Attend to precision
    """)
st.markdown("---")

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student Information Section
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
Use estimation, measurement tools, and mathematical reasoning to explore **area, perimeter, and measurement conversions** with a pencil and white correction tape.

*Students will apply measurement skills and area concepts while practicing estimation strategies and using both standard and non-standard units of measure.*

### 📦 Materials Needed
- 📝 **Wood pencil**
- ⚪ **BIC Wite-Out EZ Correct** tape
- 📏 **Ruler**
""")

# Step 1: Estimation
st.markdown("---")
st.markdown("### 📏 Step 1: Make Your Estimate")
st.markdown("Look at your pencil. How many strips of white correction tape do you think it will take to cover the **entire length on all sides of the pencil**?")

estimation = st.slider("My Estimate (number of strips):", 1, 10, 4)

# Estimate visual
fig1, ax1 = plt.subplots(figsize=(6, 3))
for i in range(10):
    color = "gold" if i < estimation else "lightgray"
    ax1.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor='black'))
    ax1.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1)
ax1.axis('off')
ax1.set_title(f"Your Estimate: {estimation} strips")
st.pyplot(fig1)
st.session_state.responses["Estimate"] = estimation

# Step 2: Actual Measurement
st.markdown("---")
st.markdown("### 📐 Step 2: Measure with Real Tape")
st.markdown("Now use correction tape to measure your pencil. Count how many strips it actually takes.")

actual_strips = st.number_input("Actual number of strips used:", 1, 10, 1)
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(10, 3))
for i in range(10):
    ax2.add_patch(plt.Rectangle((i, 0), 0.8, 1, color="gold" if i < estimation else "lightgray", edgecolor='black'))
    ax3.add_patch(plt.Rectangle((i, 0), 0.8, 1, color="orange" if i < actual_strips else "lightgray", edgecolor='black'))
for ax in [ax2, ax3]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.axis('off')
ax2.set_title(f"Estimate: {estimation} strips")
ax3.set_title(f"Actual: {actual_strips} strips")
st.pyplot(fig2)
st.session_state.responses["Actual_Strips"] = actual_strips

# Comparison
difference = abs(estimation - actual_strips)
st.markdown("### 🤔 How Did You Do?")
if estimation == actual_strips:
    st.success("🎯 Perfect! Your estimate matched exactly!")
else:
    st.info(f"Your estimate was off by {difference} strip(s). That's still great estimation practice!")

# Step 3: Ruler Measurement
st.markdown("---")
st.markdown("### 📏 Step 3: Measure with a Ruler")
col1, col2 = st.columns(2)
with col1:
    inches = st.number_input("Length in inches:", min_value=0.0, step=0.1, format="%.1f")
with col2:
    centimeters = st.number_input("Length in centimeters:", min_value=0.0, step=0.1, format="%.1f")
st.session_state.responses.update({"Inches": inches, "Centimeters": centimeters})
if inches > 0 and centimeters > 0:
    st.info(f"📊 Conversion: 1 inch ≈ {centimeters / inches:.1f} cm")

# Step 4: Cross Section
st.markdown("---")
st.markdown("### ⭕ Step 4: Explore the Pencil's Cross Section")
circumference_estimate = st.slider("Estimate: white tape pieces around the circumference:", 1, 8, 6)
fig3, ax4 = plt.subplots(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='#DEB887', alpha=0.7)
ax4.add_patch(circle)
deg = 360 / circumference_estimate
for i in range(circumference_estimate):
    ax4.add_patch(mpatches.Wedge((0, 0), 1.2, i * deg, (i + 1) * deg, width=0.15, facecolor="white", edgecolor='black', alpha=0.8))
ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_aspect('equal')
ax4.axis('off')
ax4.set_title(f"{circumference_estimate} white tape pieces around edge")
st.pyplot(fig3)
st.session_state.responses["Circumference_Estimate"] = circumference_estimate

# Step 5: Area
st.markdown("---")
st.markdown("### 📦 Step 5: Understanding Area")
col1, col2, col3 = st.columns(3)
with col1:
    calc_length = st.number_input("Length (inches):", 0.0, step=0.1, value=float(inches) if inches > 0 else 0.0, format="%.1f")
with col2:
    calc_width = st.number_input("Correction tape width (inches):", 0.0, step=0.1, value=0.2, format="%.1f")
with col3:
    calc_strips = st.number_input("Number of strips around:", 1, 12, value=circumference_estimate if circumference_estimate > 0 else 1)
if calc_length > 0 and calc_width > 0 and calc_strips > 0:
    total_area = calc_length * calc_width * calc_strips
    st.success(f"🎯 Total Surface Area: **{total_area:.2f} square inches**")
    st.session_state.responses.update({
        "Calculated_Area": total_area,
        "Calc_Length": calc_length,
        "Calc_Width": calc_width,
        "Calc_Strips": calc_strips
    })

# Reflection
st.markdown("---")
st.markdown("### 💭 Reflection Questions")
reflection1 = st.text_area("1. What surprised you most about measuring your pencil?")
reflection2 = st.text_area("2. Why might estimation be a useful skill in real life?")
reflection3 = st.text_area("3. Which measurement (inches or centimeters) felt more natural to you? Why?")
st.session_state.responses.update({
    "Reflection_1": reflection1,
    "Reflection_2": reflection2,
    "Reflection_3": reflection3
})

# Submit
st.markdown("---")
if st.button("✅ Submit My Work", type="primary"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success("Great work! Your responses have been saved.")
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Estimate", f"{estimation} strips")
        with col2: st.metric("Actual", f"{actual_strips} strips")
        with col3: st.metric("Difference", f"{difference} strips")
    else:
        st.error("Please fill in your name and date before submitting!")

# Vocabulary
with st.expander("📚 Vocabulary Helper"):
    vocab = {
        "Estimation": "A careful, educated guess",
        "Measurement": "Finding exact size/length using tools",
        "Length": "How long something is end-to-end",
        "Width": "How wide something is side-to-side", 
        "Area": "Amount of surface space",
        "Circumference": "Distance around a circle",
        "Cross Section": "Flat face of a 3D object after cutting",
        "Conversion": "Changing between measurement units"
    }
    for term, definition in vocab.items():
        st.markdown(f"**{term}**: {definition}")

# Teacher view
if st.checkbox("🏫 Teacher View: Show All Student Data"):
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Average Estimate", f"{df['Estimate'].mean():.1f}")
        with col2: st.metric("Average Actual", f"{df['Actual_Strips'].mean():.1f}")
        with col3: st.metric("Completion Rate", f"{(df['Name'].notna().sum() / len(df)) * 100:.0f}%")
    else:
        st.info("No student responses yet.")

# Footer
st.markdown("---")
st.markdown("*Happy learning! Remember: estimation is a superpower that gets better with practice! 🌟*")
