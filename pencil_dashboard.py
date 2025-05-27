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
    **4.MD.1** - Know relative sizes of measurement units within one system of units including km, m, cm; kg, g; lb, oz.; l, ml; hr, min, sec. Within a single system of measurement, express measurements in a larger unit in terms of a smaller unit.
    *Applied through: Converting between inches and centimeters, understanding fractions of an inch (3/16), decimal conversions*
    
    **4.MD.2** - Use the four operations to solve word problems involving distances, intervals of time, liquid volumes, masses of objects, and money, including problems involving simple fractions or decimals.
    *Applied through: Multi-step word problems using surface area calculations, working with fractions (3/16 inch), estimation error calculations*
    
    **4.MD.3** - Apply the area and perimeter formulas for rectangles in real world and mathematical problems.
    *Applied through: Surface area formula (Length × Width × Number of strips), calculating area of tape strips, real-world application to pencil covering*
    
    **4.OA.3** - Solve multistep word problems posed with whole numbers and having whole-number answers using the four operations, including problems in which remainders must be interpreted.
    *Applied through: Estimation vs. actual comparisons, error ratio calculations, multi-step area problems*
    
    **4.NF.6** - Use decimal notation for fractions with denominators 10 or 100.
    *Applied through: Converting 3/16 to decimal form (0.1875), understanding decimal representations*
    
    **Mathematical Practices:**
    - **MP.1** - Make sense of problems and persevere in solving them
    - **MP.2** - Reason abstractly and quantitatively *(error ratios, percent calculations)*
    - **MP.3** - Construct viable arguments and critique reasoning *(analytical thinking about estimates)*
    - **MP.4** - Model with mathematics *(surface area formula, real-world applications)*
    - **MP.5** - Use appropriate tools strategically *(rulers, fraction visualization, correction tape)*
    - **MP.6** - Attend to precision *(fraction measurements, decimal accuracy)*
    """)
st.markdown("---")

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student Information Section
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
Use estimation, measurement tools, and mathematical reasoning to explore **area and measurement** with a pencil and white correction tape.

### 📦 Materials Needed
- 📝 **Wood pencil** (standard #2 pencil)
- ⚪ **BIC Wite-Out EZ Correct** correction tape dispenser
- 📏 **Ruler** (with both inches and centimeters)
""")

# Area Formula Introduction
st.markdown("---")
st.markdown("### 🌟 **KEY FORMULA FOR THIS LESSON**")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; margin: 1rem 0;">
    <h3 style="color: white; margin: 0; font-size: 1.5rem;">Surface Area Formula</h3>
    <h2 style="color: white; margin: 0.5rem 0; font-family: monospace; font-size: 2rem;">Area = Length × Width × Strips</h2>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">Length of pencil × Width of tape × Number of strips around</p>
</div>
""", unsafe_allow_html=True)

# Plan view of tape strip with dimensions
st.markdown("### 📋 Meet Your BIC Wite-Out EZ Correct Strip")
st.markdown("**This is what ONE strip of your correction tape looks like from above (Plan View):**")

fig_tape, ax_tape = plt.subplots(figsize=(10, 4))

tape_length = 6.5
tape_width = 3/16
scale_factor = 15  # Make it bigger for visibility

rect = plt.Rectangle((0, 0), tape_length, tape_width * scale_factor, 
                    facecolor='white', edgecolor='black', linewidth=3)
ax_tape.add_patch(rect)

# Add dimensions with better arrows
ax_tape.annotate('', xy=(0, -0.4), xytext=(tape_length, -0.4),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=3))
ax_tape.text(tape_length/2, -0.7, f'{tape_length}" long', 
            ha='center', va='top', fontsize=14, color='blue', fontweight='bold')

ax_tape.annotate('', xy=(-0.5, 0), xytext=(-0.5, tape_width * scale_factor),
                arrowprops=dict(arrowstyle='<->', color='red', lw=3))
ax_tape.text(-0.8, (tape_width * scale_factor)/2, f'3/16" wide', 
            ha='center', va='center', fontsize=12, color='red', fontweight='bold', rotation=90)

# Add area calculation
ax_tape.text(tape_length/2, (tape_width * scale_factor)/2, 
            f'Area = {tape_length}" × 3/16" = {tape_length * (3/16):.4f} square inches', 
            ha='center', va='center', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))

ax_tape.set_xlim(-1.2, tape_length + 0.5)
ax_tape.set_ylim(-1, tape_width * scale_factor + 0.5)
ax_tape.set_aspect('equal')
ax_tape.set_title('📋 Plan View: ONE BIC Wite-Out EZ Correct Strip\n(Actual dimensions)', 
                 fontsize=16, fontweight='bold', pad=20)
ax_tape.axis('off')

st.pyplot(fig_tape)

st.markdown("""
**Why these measurements matter:**
- **Length: 6.5 inches** - This is how long each strip is when you pull it from the dispenser
- **Width: 3/16 inch** - This is how wide the tape is (we'll learn about this fraction below!)
- **Area of ONE strip: 1.2188 square inches** - This is the area each strip covers

📐 **Plan View** means looking down from directly above, showing length and width. Later we'll see a **cross-section** view!
""")

# Interactive Fraction Tutorial - NOW CONNECTED TO TAPE WIDTH
st.markdown("---")
st.markdown("### 📏 Understanding 3/16 Inch (Your Tape Width!)")
st.markdown("**Your BIC Wite-Out tape is 3/16 inch wide. Let's understand what that means!**")

# Create ruler showing sixteenths
fig_ruler, ax_ruler = plt.subplots(figsize=(10, 4))
ruler_length = 1  # Show just 1 inch for clarity
ax_ruler.add_patch(plt.Rectangle((0, 0), ruler_length, 0.5, facecolor='lightgray', edgecolor='black'))

# Add inch marks
for i in range(2):
    ax_ruler.plot([i, i], [0, 0.5], 'k-', linewidth=3)
    ax_ruler.text(i, -0.1, f'{i}"', ha='center', va='top', fontweight='bold', fontsize=12)

# Add sixteenth marks with special highlighting for 3/16
for i in range(ruler_length * 16 + 1):
    x = i / 16
    if i % 16 == 0:
        continue
    elif i % 8 == 0:
        ax_ruler.plot([x, x], [0, 0.4], 'k-', linewidth=2)
    elif i % 4 == 0:
        ax_ruler.plot([x, x], [0, 0.35], 'k-', linewidth=1.5)
    elif i % 2 == 0:
        ax_ruler.plot([x, x], [0, 0.25], 'k-', linewidth=1)
    else:
        ax_ruler.plot([x, x], [0, 0.15], 'k-', linewidth=0.5)

# Highlight 3/16 specifically
tape_width_pos = 3/16
ax_ruler.plot([tape_width_pos, tape_width_pos], [0, 0.5], 'r-', linewidth=4)
ax_ruler.text(tape_width_pos, 0.7, '3/16"\n(Your tape width!)', ha='center', va='bottom', 
             fontweight='bold', color='red', fontsize=12,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))

ax_ruler.set_xlim(-0.1, 1.1)
ax_ruler.set_ylim(-0.3, 1.0)
ax_ruler.set_title('Ruler Showing Your Tape Width: 3/16 Inch', fontsize=14, fontweight='bold')
ax_ruler.axis('off')
st.pyplot(fig_ruler)

# Interactive fraction calculator - focused on understanding 3/16
st.markdown("#### 🧮 Fraction Calculator: Explore Different Sixteenths")
st.markdown("**Try different fractions to see how 3/16 compares to other measurements:**")

col1, col2 = st.columns(2)

with col1:
    numerator = st.selectbox(
        "Choose the numerator (top number):",
        options=list(range(1, 17)),
        index=2,  # Default to 3 for 3/16
        key="fraction_num"
    )

with col2:
    st.markdown("**Denominator (bottom number):** 16")
    st.markdown(f"**Your fraction:** {numerator}/16")

decimal_result = numerator / 16
st.markdown(f"**Decimal equivalent:** {numerator}/16 = {decimal_result:.4f} inches")

# Special callout when 3/16 is selected
if numerator == 3:
    st.success(f"🎯 **Perfect! This is your tape width: 3/16 = {decimal_result:.4f} inches**")
else:
    st.info(f"Compare this to your tape width: 3/16 = {3/16:.4f} inches")

# Visual representation focused on the selected fraction
fig_frac, (ax_whole, ax_zoom) = plt.subplots(1, 2, figsize=(12, 3))

# Show whole inch divided into 16 parts
ax_whole.add_patch(plt.Rectangle((0, 0), 1, 0.5, facecolor='lightblue', edgecolor='black'))
for i in range(17):
    x = i / 16
    ax_whole.plot([x, x], [0, 0.5], 'k-', linewidth=0.5)

# Highlight the selected fraction
for i in range(numerator):
    x1 = i / 16
    x2 = (i + 1) / 16
    ax_whole.add_patch(plt.Rectangle((x1, 0), x2 - x1, 0.5, facecolor='red', alpha=0.7))

# Always show where 3/16 is for comparison
if numerator != 3:
    for i in range(3):
        x1 = i / 16
        x2 = (i + 1) / 16
        ax_whole.add_patch(plt.Rectangle((x1, 0), x2 - x1, 0.5, facecolor='yellow', alpha=0.5))
    ax_whole.text(3/32, 0.6, 'Tape width\n(3/16)', ha='center', va='bottom', fontsize=8, color='orange')

ax_whole.set_xlim(-0.05, 1.05)
ax_whole.set_ylim(-0.1, 0.8)
ax_whole.set_title(f'One Inch Showing {numerator}/16', fontweight='bold')
ax_whole.text(0.5, -0.05, '1 inch = 16/16', ha='center', va='top', fontsize=10)
ax_whole.axis('off')

# Zoomed view
zoom_start = max(0, (numerator - 2) / 16)
zoom_end = min(1, (numerator + 2) / 16)
ax_zoom.add_patch(plt.Rectangle((zoom_start, 0), zoom_end - zoom_start, 0.5, facecolor='lightblue', edgecolor='black'))

for i in range(int(zoom_start * 16), int(zoom_end * 16) + 1):
    x = i / 16
    if zoom_start <= x <= zoom_end:
        ax_zoom.plot([x, x], [0, 0.5], 'k-', linewidth=1)
        if i == numerator:
            ax_zoom.plot([x, x], [0, 0.5], 'r-', linewidth=3)
            ax_zoom.text(x, 0.6, f'{i}/16', ha='center', va='bottom', fontweight='bold', color='red')
        elif i == 3:  # Always mark the tape width
            ax_zoom.plot([x, x], [0, 0.5], 'orange', linewidth=2)
            ax_zoom.text(x, -0.1, 'Tape', ha='center', va='top', fontsize=8, color='orange')

ax_zoom.set_xlim(zoom_start - 0.02, zoom_end + 0.02)
ax_zoom.set_ylim(-0.2, 0.8)
ax_zoom.set_title(f'Zoomed View: {numerator}/16 = {decimal_result:.4f}"', fontweight='bold')
ax_zoom.axis('off')

st.pyplot(fig_frac)

st.markdown("""
### 🔗 **Connecting Fractions to Area Calculation**

Now you understand that your BIC Wite-Out **strip** is **3/16 inch wide**!

Each strip has TWO measurements:
- **Length of the strip**: 6.5 inches (how long it is)
- **Width of the strip**: 3/16 inch (how wide it is)

When we calculate the surface area of your pencil, we'll use:
- **Length**: How long your pencil is (you'll measure this)
- **Strip width**: 3/16 inch (0.1875 inches) - how wide each strip is
- **Number of strips**: How many strips go around the pencil

**Area = Pencil length × Strip width × Number of strips around**
**Area = Pencil length × 0.1875 × Number of strips around**
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
ax1.axis('off')
st.pyplot(fig1)

st.session_state.responses["Estimate"] = estimation

# Analytical Thinking about Estimates
st.markdown("### 🧠 Analytical Thinking: Reasoning About Estimates")
st.markdown("Think about your estimation process:")
st.markdown("""
- Why is **zero** not a valid option?
- Is **10** a good maximum estimate? Why or why not?
- Why might it be unhelpful to allow higher numbers?
- What would your maximum estimate be?
- How did you decide that number?
""")

estimation_reasoning = st.text_area(
    "Write your thoughts:",
    height=120,
    key="estimation_reasoning",
    placeholder="Think about: What makes a good estimate? Why do we set limits?"
)

st.session_state.responses["Estimation_Reasoning"] = estimation_reasoning

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

# Error Ratio Tutorial - Auto Calculator
st.markdown("### 💡 Estimation Tutorial: Understanding Your Estimation Error")
st.markdown("Now let's analyze your **estimation** compared to the actual number:")

st.markdown("""
**Step 1:** Find the **difference** between your **estimation** and the actual value.

**Step 2:** Divide that difference by the actual number of strips to get your **estimation error ratio**.

**Step 3:** Use this formula: 

`Estimation Error Ratio = |Estimation - Actual| / Actual`

This helps us understand how close your **estimation** was. Smaller ratios mean better **estimation** accuracy!
""")

if actual_strips > 0:
    # Auto-calculate based on their responses
    error_ratio = round(difference / actual_strips, 2)
    percent_error = round((difference / actual_strips) * 100, 1)
    percent_accuracy = round(100 - percent_error, 1)
    over_under = "above" if estimation > actual_strips else ("below" if estimation < actual_strips else "exact")
    
    # Create auto-output calculator display
    st.markdown("#### 🧮 **Your Automatic Estimation Error Calculator Results**")
    
    # Step-by-step calculation display
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        **Step 1 - Find the difference:**
        - Your **estimation**: **{estimation}** strips
        - Actual count: **{actual_strips}** strips  
        - Difference: |{estimation} - {actual_strips}| = **{difference}** strips
        
        **Step 2 - Calculate estimation error ratio:**
        - **Estimation Error Ratio** = {difference} ÷ {actual_strips} = **{error_ratio}**
        
        **Step 3 - Convert to percentages:**
        - **Estimation Error**: {difference} ÷ {actual_strips} × 100 = **{percent_error}%**
        - **Estimation Accuracy**: 100 - {percent_error} = **{percent_accuracy}%**
        """)
    
    with col2:
        # Visual summary box
        st.markdown(f"""
        <div style="padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white; text-align: center;">
            <h4 style="margin: 0; color: white;">📊 Your Estimation Results</h4>
            <p style="margin: 0.5rem 0; font-size: 1.2rem;"><strong>Error Ratio: {error_ratio}</strong></p>
            <p style="margin: 0.5rem 0;"><strong>Accuracy: {percent_accuracy}%</strong></p>
            <p style="margin: 0.5rem 0;"><strong>You estimated {over_under}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Interpretation with feedback
    st.markdown("#### 🎯 **What This Means for Your Estimation Skills:**")
    
    if over_under != "exact":
        st.markdown(f"Your **estimation** was **{over_under}** the actual amount by **{difference}** strips.")
    else:
        st.markdown("🌟 Your **estimation** was exact! Perfect **estimation** precision!")
    
    # Performance feedback
    if error_ratio == 0:
        st.success("🌟 **Perfect estimation!** Your estimation error ratio = 0 - You nailed it!")
    elif error_ratio <= 0.2:
        st.success(f"🎯 **Excellent estimation skills!** Your estimation error ratio = {error_ratio} (≤ 0.2 is great!)")
    elif error_ratio <= 0.5:
        st.info(f"👍 **Good estimation skills!** Your estimation error ratio = {error_ratio} (≤ 0.5 is solid work!)")
    elif error_ratio <= 1.0:
        st.warning(f"📈 **Keep practicing your estimation!** Your estimation error ratio = {error_ratio} - Estimation gets better with practice!")
    else:
        st.warning(f"🎯 **Estimation challenge!** Your estimation error ratio = {error_ratio} - This was a tough one to estimate!")
    
    # Store all the calculated values
    st.session_state.responses.update({
        "Estimation_Error_Ratio": error_ratio,
        "Estimation_Percent_Error": percent_error,
        "Estimation_Percent_Accuracy": percent_accuracy,
        "Estimation_Over_Under": over_under,
        "Estimation_Difference": difference
    })
    
    # Optional: Show the calculation breakdown
    with st.expander("🔍 See the detailed estimation calculation breakdown"):
        st.markdown(f"""
        **Mathematical Breakdown of Your Estimation:**
        
        1. **Absolute Difference**: |{estimation} - {actual_strips}| = {difference}
        2. **Estimation Error Ratio**: {difference} ÷ {actual_strips} = {difference/actual_strips:.4f} ≈ {error_ratio}
        3. **Estimation Percent Error**: ({difference} ÷ {actual_strips}) × 100 = {(difference/actual_strips)*100:.1f}%
        4. **Estimation Percent Accuracy**: 100% - {percent_error}% = {percent_accuracy}%
        5. **Estimation Direction**: {estimation} {">" if estimation > actual_strips else ("<" if estimation < actual_strips else "=")} {actual_strips}, so you estimated {"above" if estimation > actual_strips else ("below" if estimation < actual_strips else "exactly")}
        """)

else:
    st.info("Complete Step 2 above to see your automatic estimation error calculation!")

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

# Add segments around the circle
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

# Step 5: Area Calculator
st.markdown("---")
st.markdown("### 📦 Step 5: Understanding Area")
st.markdown("""
If you could unwrap all the correction tape from your pencil and lay it flat, you'd get a rectangle!
- **Length** = length of your pencil
- **Width** = width of one tape strip
- **Number of strips** = how many strips went around (from cross section)
- **Total Area** = Length × Width × Number of strips around
""")

st.markdown("#### 🧮 Area Calculator")
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

if calc_length > 0 and calc_width > 0 and calc_strips > 0:
    total_area = calc_length * calc_width * calc_strips
    
    st.markdown("#### 📊 Your Calculation:")
    st.markdown(f"""
    **{calc_length}** inches (length) × **{calc_width}** inches (width) × **{calc_strips}** strips = **{total_area:.2f} square inches**
    """)
    
    st.success(f"🎯 Total Surface Area: **{total_area:.2f} square inches**")
    
    st.session_state.responses.update({
        "Calculated_Area": total_area,
        "Calc_Length": calc_length,
        "Calc_Width": calc_width,
        "Calc_Strips": calc_strips
    })
else:
    st.info("Enter all measurements above to calculate the area!")

# Word Problems
st.markdown("---")
st.markdown("### 📝 Challenge Word Problems")

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

st.session_state.responses.update({
    "Word_Problem_1": problem1_answer,
    "Word_Problem_2": problem2_answer,
    "Word_Problem_3": problem3_answer
})

with st.expander("💡 Need help? Click for hints"):
    hint_col1, hint_col2, hint_col3 = st.columns(3)
    with hint_col1:
        st.markdown("**Problem 1:**\n8 × 0.2 × 6 = ? \nThen × 4 pencils")
    with hint_col2:
        st.markdown("**Problem 2:**\n7 × 0.5 × 5 = ?")
    with hint_col3:
        st.markdown("**Problem 3:**\nFind each area first, then subtract!")

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
st.markdown("### ✅ Submit Your Complete Work")
if st.button("✅ Submit My Work", type="primary"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success("Great work! Your responses have been saved.")
        
        st.markdown("### 📊 Your Summary")
        summary_col1, summary_col2, summary_col3 = st.columns(3)
        with summary_col1:
            st.metric("Estimate", f"{estimation} strips")
        with summary_col2:
            st.metric("Actual", f"{actual_strips} strips")
        with summary_col3:
            st.metric("Difference", f"{difference} strips")
    else:
        st.error("Please fill in your name and date before submitting!")

# Teacher's Data View
if st.checkbox("🏫 Teacher View: Show All Student Data"):
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        
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
