import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="4th Grade Math: Dimensional Thinking with a Pencil", 
    layout="centered"
)

# Header
st.markdown("#### Honablue M.Ed International")
st.title("📝 4th Grade Math: Dimensional Thinking with a Pencil")

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

# Update responses
st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective
st.markdown("---")
st.markdown("""
### 🧠 Learning Objective
Use estimation, drawing, and measurement to explore **dimensions, area, and circumference** with a pencil and yellow tape.

*In 1st grade, students described a pencil by its length and weight. Some said 'yellow' — today, we explore what that really means in mathematical terms.*
""")

# Step 1: Estimation
st.markdown("---")
st.markdown("### 📏 Step 1: Make Your Estimate")
st.markdown("Look at your pencil. How many strips of yellow tape do you think it will take to cover the entire length?")

estimation = st.slider(
    "My Estimate (number of strips):", 
    min_value=1, 
    max_value=10, 
    value=4,
    help="Move the slider to make your best guess!"
)

# Visual representation of estimate
fig1, ax1 = plt.subplots(figsize=(6, 3))
for i in range(10):
    color = "gold" if i < estimation else "lightgray"
    ax1.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor='black'))
    ax1.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold')

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1)
ax1.set_title(f"Your Estimate: {estimation} strips")
ax1.set_xlabel("Strip Number")
ax1.axis('off')
st.pyplot(fig1)

st.session_state.responses["Estimate"] = estimation

# Step 2: Actual Measurement
st.markdown("---")
st.markdown("### 📐 Step 2: Measure with Real Tape")
st.markdown("Now use yellow tape to actually measure your pencil. Count how many strips it takes!")

actual_strips = st.number_input(
    "Actual number of strips used:", 
    min_value=1, 
    max_value=10, 
    value=1,
    help="Count each strip of tape you used"
)

# Visual comparison
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(10, 3))

# Estimate visualization
for i in range(10):
    color = "gold" if i < estimation else "lightgray"
    ax2.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor='black'))
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 1)
ax2.set_title(f"Estimate: {estimation} strips")
ax2.axis('off')

# Actual visualization
for i in range(10):
    color = "orange" if i < actual_strips else "lightgray"
    ax3.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor='black'))
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 1)
ax3.set_title(f"Actual: {actual_strips} strips")
ax3.axis('off')

st.pyplot(fig2)

st.session_state.responses["Actual_Strips"] = actual_strips

# Comparison Analysis
difference = abs(estimation - actual_strips)
st.markdown("### 🤔 How Did You Do?")
if estimation == actual_strips:
    st.success("🎯 Perfect! Your estimate matched exactly!")
else:
    st.info(f"Your estimate was off by {difference} strip(s). That's still great estimation practice!")

# Step 3: Ruler Measurements
st.markdown("---")
st.markdown("### 📏 Step 3: Measure with a Ruler")
st.markdown("Use a real ruler to measure your pencil in both inches and centimeters.")

col1, col2 = st.columns(2)
with col1:
    inches = st.number_input("Length in inches:", min_value=0.0, step=0.1, format="%.1f")
with col2:
    centimeters = st.number_input("Length in centimeters:", min_value=0.0, step=0.1, format="%.1f")

st.session_state.responses.update({"Inches": inches, "Centimeters": centimeters})

if inches > 0 and centimeters > 0:
    ratio = centimeters / inches
    st.info(f"📊 Conversion: 1 inch ≈ {ratio:.1f} centimeters")

# Step 4: Cross Section Exploration
st.markdown("---")
st.markdown("### ⭕ Step 4: Explore the Pencil's Cross Section")
st.markdown("If you cut your pencil like a slice of bread, you'd see a circle. How many tape pieces would it take to go around?")

circumference_estimate = st.slider(
    "Estimate: tape pieces around the circumference:",
    min_value=1,
    max_value=8,
    value=6
)

# Draw cross section
fig3, ax4 = plt.subplots(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='#DEB887', alpha=0.7)
ax4.add_patch(circle)

# Add segments around the circle
for i in range(8):
    theta1 = i * 45
    theta2 = (i + 1) * 45
    color = "gold" if i < circumference_estimate else "lightgray"
    
    wedge = mpatches.Wedge(
        (0, 0), 1.2, theta1, theta2, 
        width=0.15, facecolor=color, 
        edgecolor='black', alpha=0.8
    )
    ax4.add_patch(wedge)

ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_aspect('equal')
ax4.set_title(f"Pencil Cross Section - {circumference_estimate} tape pieces around edge")
ax4.axis('off')
st.pyplot(fig3)

st.session_state.responses["Circumference_Estimate"] = circumference_estimate

# Step 5: Area Concept
st.markdown("---")
st.markdown("### 📦 Step 5: Understanding Area")
st.markdown("""
If you could unwrap all the tape from your pencil and lay it flat, you'd get a rectangle!
- **Length** = length of your pencil
- **Width** = how many strips went around
- **Area** = Length × Width
""")

if actual_strips > 0 and inches > 0:
    area_estimate = actual_strips * inches
    st.metric("Estimated Tape Area", f"{area_estimate:.1f} square inches")

# Reflection Questions
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

# Submit Section
st.markdown("---")
if st.button("✅ Submit My Work", type="primary"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success("Great work! Your responses have been saved.")
        
        # Show summary
        st.markdown("### 📊 Your Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Estimate", f"{estimation} strips")
        with col2:
            st.metric("Actual", f"{actual_strips} strips")
        with col3:
            st.metric("Difference", f"{difference} strips")
    else:
        st.error("Please fill in your name and date before submitting!")

# Vocabulary Section
with st.expander("📚 Vocabulary Helper"):
    vocab_terms = {
        "Estimation": "A careful, educated guess about a number or measurement",
        "Measurement": "Finding the exact size, length, or amount of something using tools",
        "Length": "How long something is from end to end",
        "Width": "How wide something is from side to side", 
        "Area": "The amount of space inside a shape (Length × Width for rectangles)",
        "Circumference": "The distance all the way around a circle",
        "Cross Section": "What you see when you cut straight through an object",
        "Conversion": "Changing from one unit of measurement to another"
    }
    
    for term, definition in vocab_terms.items():
        st.markdown(f"**{term}**: {definition}")

# Teacher's Data View
if st.checkbox("🏫 Teacher View: Show All Student Data"):
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        
        # Quick stats
        if len(df) > 0:
            st.markdown("### 📈 Class Statistics")
            col1, col2, col3 = st.columns(3)
            with col1:
                avg_estimate = df['Estimate'].mean() if 'Estimate' in df.columns else 0
                st.metric("Average Estimate", f"{avg_estimate:.1f}")
            with col2:
                avg_actual = df['Actual_Strips'].mean() if 'Actual_Strips' in df.columns else 0
                st.metric("Average Actual", f"{avg_actual:.1f}")
            with col3:
                completion_rate = (df['Name'].notna().sum() / len(df)) * 100
                st.metric("Completion Rate", f"{completion_rate:.0f}%")
    else:
        st.info("No student responses yet.")

# Footer
st.markdown("---")
st.markdown("*Happy learning! Remember: estimation is a superpower that gets better with practice! 🌟*")
