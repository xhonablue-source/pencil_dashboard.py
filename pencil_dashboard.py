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

st.title("📐 4th Grade Math: Area and Measurement with a Pencil")

# Michigan Learning Standards
st.markdown("---")
st.markdown("### 📚 Michigan Learning Standards Addressed")
with st.expander("Click to view aligned standards"):
    st.markdown("""
    **4.MD.1** - Know relative sizes of measurement units within one system of units including km, m, cm; kg, g; lb, oz.; l, ml; hr, min, sec. Within a single system of measurement, express measurements in a larger unit in terms of a smaller unit.
    
    **4.MD.2** - Use the four operations to solve word problems involving distances, intervals of time, liquid volumes, masses of objects, and money, including problems involving simple fractions or decimals.
    
    **4.MD.3** - Apply the area and perimeter formulas for rectangles in real world and mathematical problems.
    
    **4.OA.3** - Solve multistep word problems posed with whole numbers and having whole-number answers using the four operations, including problems in which remainders must be interpreted.
    
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

# Update responses
st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective
st.markdown("---")
st.markdown("""
### 🧠 Learning Objective
Use estimation, measurement tools, and mathematical reasoning to explore **area, perimeter, and measurement conversions** with a pencil and white correction tape.

*Students will apply measurement skills and area concepts while practicing estimation strategies and using both standard and non-standard units of measure.*

### 📦 Materials Needed
Before we begin, make sure you have these items:
- 📝 **Wood pencil** (standard #2 pencil)
- ⚪ **BIC Wite-Out EZ Correct** correction tape dispenser
- 📏 **Ruler** (with both inches and centimeters)

*Teacher note: Each student or pair of students will need their own set of materials.*
""")

# Step 1: Estimation
st.markdown("---")
st.markdown("### 📏 Step 1: Make Your Estimate")
st.markdown("Look at your pencil. How many strips of white correction tape do you think it will take to cover the entire length?")

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
st.markdown("Now use white correction tape to actually measure your pencil. Count how many strips it takes!")

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
    "Estimate: white tape pieces around the circumference:",
    min_value=1,
    max_value=8,
    value=6
)

# Draw cross section
fig3, ax4 = plt.subplots(figsize=(6, 6))
circle = plt.Circle((0, 0), 1, color='#DEB887', alpha=0.7)
ax4.add_patch(circle)

# Add segments around the circle - divide into circumference_estimate sections
degrees_per_section = 360 / circumference_estimate
for i in range(circumference_estimate):
    theta1 = i * degrees_per_section
    theta2 = (i + 1) * degrees_per_section
    
    wedge = mpatches.Wedge(
        (0, 0), 1.2, theta1, theta2, 
        width=0.15, facecolor="white", 
        edgecolor='black', alpha=0.8
    )
    ax4.add_patch(wedge)

ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_aspect('equal')
ax4.set_title(f"Pencil Cross Section - {circumference_estimate} white tape pieces around edge")
ax4.axis('off')
st.pyplot(fig3)

st.session_state.responses["Circumference_Estimate"] = circumference_estimate

# Step 5: Area Concept
st.markdown("---")
st.markdown("### 📦 Step 5: Understanding Area")
st.markdown("""
If you could unwrap all the correction tape from your pencil and lay it flat, you'd get a rectangle!
- **Length** = length of your pencil
- **Width** = width of one tape strip
- **Number of strips** = how many strips went around (from cross section)
- **Total Area** = Length × Width × Number of strips around
""")

# Area Calculator Section
st.markdown("#### 🧮 Area Calculator")
st.markdown("Enter your measurements to calculate the total surface area:")

col1, col2, col3 = st.columns(3)
with col1:
    calc_length = st.number_input(
        "Length (inches):", 
        min_value=0.0, 
        step=0.1, 
        value=float(inches) if inches > 0 else 0.0,
        format="%.1f",
        key="calc_length"
    )
with col2:
    calc_width = st.number_input(
        "Correction tape width (inches):", 
        min_value=0.0, 
        step=0.1, 
        value=0.2,
        format="%.1f",
        key="calc_width",
        help="White-out correction tape is typically about 0.2 inches wide"
    )
with col3:
    calc_strips = st.number_input(
        "Number of strips around:", 
        min_value=1, 
        max_value=12, 
        value=circumference_estimate if circumference_estimate > 0 else 1,
        key="calc_strips"
    )

# Calculate and display result
if calc_length > 0 and calc_width > 0 and calc_strips > 0:
    total_area = calc_length * calc_width * calc_strips
    
    # Display calculation
    st.markdown("#### 📊 Your Calculation:")
    st.markdown(f"""
    **{calc_length}** inches (length) × **{calc_width}** inches (width) × **{calc_strips}** strips = **{total_area:.2f} square inches**
    """)
    
    # Show result prominently
    st.success(f"🎯 Total Surface Area: **{total_area:.2f} square inches**")
    
    # Save to responses
    st.session_state.responses.update({
        "Calculated_Area": total_area,
        "Calc_Length": calc_length,
        "Calc_Width": calc_width,
        "Calc_Strips": calc_strips
    })
else:
    st.info("Enter all measurements above to calculate the area!")

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

# Word Problems Section
st.markdown("---")
st.markdown("### 📝 Challenge Word Problems")
st.markdown("*Apply what you've learned to solve these problems:*")

# Problem 1
st.markdown("#### 📚 **Problem 1: Classroom Pencils**")
st.markdown("""
**Ms. Garcia** has 4 new pencils for her reading group. Each pencil is 8 inches long. 
She uses correction tape that is 0.2 inches wide, and it takes 6 strips of tape to go around each pencil.

**Question:** How much correction tape area is needed to cover all 4 pencils?
""")

problem1_answer = st.text_area(
    "Show your work:",
    height=100,
    key="problem1",
    placeholder="Step 1: Find the area for 1 pencil\nStep 2: Multiply by 4 pencils\nStep 3: Write your answer"
)

# Problem 2  
st.markdown("#### 🎨 **Problem 2: Art Supply**")
st.markdown("""
**Tommy** is decorating a pencil for an art project. His pencil is 7 inches long, and he uses tape that is 0.5 inches wide. 
He estimates it will take 5 strips to go around his pencil.

**Question:** What is the surface area Tommy will cover with tape?
""")

problem2_answer = st.text_area(
    "Show your calculation:",
    height=100,
    key="problem2",
    placeholder="Use the formula: Length × Width × Number of strips = ?"
)

# Problem 3
st.markdown("#### 🏫 **Problem 3: Pencil Comparison**")
st.markdown("""
**Sarah** has a short pencil that is 5 inches long. **Alex** has a long pencil that is 10 inches long. 
Both pencils need 6 strips of 0.2-inch wide tape to be covered.

**Question:** How much more tape area does Alex need than Sarah?
""")

problem3_answer = st.text_area(
    "Find the difference:",
    height=100,
    key="problem3",
    placeholder="Sarah's pencil area = ?\nAlex's pencil area = ?\nDifference = ?"
)

# Store word problem responses
st.session_state.responses.update({
    "Word_Problem_1": problem1_answer,
    "Word_Problem_2": problem2_answer,
    "Word_Problem_3": problem3_answer
})

# Simplified hints
with st.expander("💡 Need help? Click for hints"):
    hint_col1, hint_col2, hint_col3 = st.columns(3)
    
    with hint_col1:
        st.markdown("**Problem 1:**\n8 × 0.2 × 6 = ? \nThen × 4 pencils")
    
    with hint_col2:
        st.markdown("**Problem 2:**\n7 × 0.5 × 5 = ?")
    
    with hint_col3:
        st.markdown("**Problem 3:**\nFind each area first, then subtract!")

# Submit Section
st.markdown("---")
st.markdown("### ✅ Submit Your Complete Work")
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
