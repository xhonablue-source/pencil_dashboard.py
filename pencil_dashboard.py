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
Use estimation, measurement tools, and mathematical reasoning to explore **surface area** using BIC Wite-Out EZ Correct strips and a pencil.

### 📦 Materials Needed
- 📝 **Wood pencil** (standard #2 pencil)
- 📏 **Ruler** (with both inches and centimeters)
- 📋 **BIC Wite-Out EZ Correct strip dimensions** (provided below)
""")

# Area Formula Introduction
st.markdown("---")
st.markdown("### 🌟 **KEY FORMULA FOR THIS LESSON**")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; margin: 1rem 0;">
    <h3 style="color: white; margin: 0; font-size: 1.5rem;">Surface Area Formula</h3>
    <h2 style="color: white; margin: 0.5rem 0; font-family: monospace; font-size: 2rem;">Area = Strips Along × Strips Around × Strip Area</h2>
    <p style="color: #f0f0f0; margin: 0; font-style: italic;">Number of strips along length × Number around circumference × Area of one strip</p>
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
**Key Strip Specifications:**
- **Length: 6.5 inches** - This is how long each strip is
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

When we calculate the surface area of your pencil, we'll use these strip dimensions to figure out coverage!
""")

# Step 1: Estimation
st.markdown("---")
st.markdown("### 📏 Step 1: Make Your Estimate")
st.markdown("Look at your pencil and think about the BIC Wite-Out strips (6.5 inches long, 3/16 inch wide). How many strips do you estimate it would take to completely cover your pencil?")

estimation = st.slider(
    "My Estimate (total number of strips to cover pencil):", 
    min_value=1, 
    max_value=20, 
    value=10,
    help="Think about how many 6.5\" × 3/16\" strips you'd need!"
)

st.markdown(f"**Your estimate: {estimation} strips total**")

st.session_state.responses["Estimate"] = estimation

# Analytical Thinking about Estimates
st.markdown("### 🧠 Analytical Thinking: Reasoning About Estimates")
st.markdown("Think about your estimation process:")
st.markdown("""
- Why is **zero** not a valid option?
- Is **20** a reasonable maximum estimate? Why or why not?
- How did you think about the strip dimensions in your estimate?
- What factors did you consider?
""")

estimation_reasoning = st.text_area(
    "Write your thoughts:",
    height=120,
    key="estimation_reasoning",
    placeholder="Think about: How did the strip size (6.5\" × 3/16\") influence your estimate?"
)

st.session_state.responses["Estimation_Reasoning"] = estimation_reasoning

# Step 2: Ruler Measurements
st.markdown("---")
st.markdown("### 📏 Step 2: Measure Your Pencil")
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

# Step 3: Cross Section Exploration
st.markdown("---")
st.markdown("### ⭕ Step 3: Explore the Pencil's Cross Section")
st.markdown("If you cut your pencil like a slice of bread, you'd see a circle. Estimate how many BIC strips (3/16\" wide) would fit around the circumference.")

circumference_estimate = st.slider(
    "Estimate: BIC strips around the circumference:",
    min_value=1,
    max_value=12,
    value=8,
    help="How many 3/16\" wide strips would go around the pencil's edge?"
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
ax4.set_title(f"Pencil Cross Section - {circumference_estimate} BIC strips around edge")
ax4.axis('off')
st.pyplot(fig3)

st.session_state.responses["Circumference_Estimate"] = circumference_estimate

# Step 4: Calculate Coverage
st.markdown("---")
st.markdown("### 🧮 Step 4: Calculate BIC Strip Coverage")
st.markdown("Now let's calculate how many BIC Wite-Out strips we actually need!")

if inches > 0:
    # Calculate strips needed along length
    strips_along_length = inches / 6.5
    strips_along_length_rounded = round(strips_along_length)
    
    st.markdown(f"""
    **Strips needed along the length:**
    - Pencil length: **{inches}** inches
    - BIC strip length: **6.5** inches
    - Strips needed: {inches} ÷ 6.5 = **{strips_along_length:.2f}** strips
    - Rounded to whole strips: **{strips_along_length_rounded}** strips
    """)
    
    # Calculate total strips needed
    total_calculated_strips = strips_along_length_rounded * circumference_estimate
    
    st.markdown(f"""
    **Total strips needed:**
    - Strips along length: **{strips_along_length_rounded}**
    - Strips around circumference: **{circumference_estimate}**
    - Total strips: {strips_along_length_rounded} × {circumference_estimate} = **{total_calculated_strips}** strips
    """)
    
    # Store calculated results
    st.session_state.responses.update({
        "Strips_Along_Length": strips_along_length,
        "Strips_Along_Length_Rounded": strips_along_length_rounded,
        "Total_Calculated_Strips": total_calculated_strips
    })
    
    # Compare with estimate - THE ESTIMATE VS ACTUAL SECTION
    st.markdown("### 🤔 How Did Your Estimate Compare?")
    difference = abs(estimation - total_calculated_strips)
    
    if estimation == total_calculated_strips:
        st.success("🎯 Perfect! Your estimate matched exactly!")
    else:
        st.info(f"Your estimate was **{estimation}** strips, actual calculation is **{total_calculated_strips}** strips. Difference: **{difference}** strips.")
    
    # ERROR RATIO TUTORIAL - Auto Calculator (KEEPING THIS!)
    st.markdown("### 💡 Estimation Tutorial: Understanding Your Estimation Error")
    st.markdown("Now let's analyze your **estimation** compared to the calculated number:")

    st.markdown("""
    **Step 1:** Find the **difference** between your **estimation** and the calculated value.

    **Step 2:** Divide that difference by the calculated number of strips to get your **estimation error ratio**.

    **Step 3:** Use this formula: 

    `Estimation Error Ratio = |Estimation - Calculated| / Calculated`

    This helps us understand how close your **estimation** was. Smaller ratios mean better **estimation** accuracy!
    """)
    
    # Error ratio calculation
    if total_calculated_strips > 0:
        error_ratio = round(difference / total_calculated_strips, 2)
        percent_error = round((difference / total_calculated_strips) * 100, 1)
        percent_accuracy = round(100 - percent_error, 1)
        over_under = "above" if estimation > total_calculated_strips else ("below" if estimation < total_calculated_strips else "exact")
        
        # Create auto-output calculator display
        st.markdown("#### 🧮 **Your Estimation Error Calculator Results**")
        
        # Step-by-step calculation display
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            **Step 1 - Find the difference:**
            - Your **estimation**: **{estimation}** strips
            - Calculated result: **{total_calculated_strips}** strips  
            - Difference: |{estimation} - {total_calculated_strips}| = **{difference}** strips
            
            **Step 2 - Calculate estimation error ratio:**
            - **Estimation Error Ratio** = {difference} ÷ {total_calculated_strips} = **{error_ratio}**
            
            **Step 3 - Convert to percentages:**
            - **Estimation Error**: {difference} ÷ {total_calculated_strips} × 100 = **{percent_error}%**
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
            st.markdown(f"Your **estimation** was **{over_under}** the calculated amount by **{difference}** strips.")
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
        
        # Store estimation analysis
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
            
            1. **Absolute Difference**: |{estimation} - {total_calculated_strips}| = {difference}
            2. **Estimation Error Ratio**: {difference} ÷ {total_calculated_strips} = {difference/total_calculated_strips:.4f} ≈ {error_ratio}
            3. **Estimation Percent Error**: ({difference} ÷ {total_calculated_strips}) × 100 = {(difference/total_calculated_strips)*100:.1f}%
            4. **Estimation Percent Accuracy**: 100% - {percent_error}% = {percent_accuracy}%
            5. **Estimation Direction**: {estimation} {">" if estimation > total_calculated_strips else ("<" if estimation < total_calculated_strips else "=")} {total_calculated_strips}, so you estimated {"above" if estimation > total_calculated_strips else ("below" if estimation < total_calculated_strips else "exactly")}
            """)

else:
    st.info("Enter your pencil length in Step 2 to see the calculations!")

# Step 5: Surface Area Calculator
st.markdown("---")
st.markdown("### 📦 Step 5: Calculate Total Surface Area")
st.markdown("""
Now let's calculate the total surface area that would be covered by all the BIC Wite-Out strips!

**Remember:** Each BIC strip has an area of 6.5" × 3/16" = 1.2188 square inches
""")

if inches > 0 and 'Total_Calculated_Strips' in st.session_state.responses:
    total_strips = st.session_state.responses['Total_Calculated_Strips']
    strip_area = 6.5 * (3/16)  # 1.2188 square inches
    total_surface_area = total_strips * strip_area
    
    st.markdown("#### 🧮 Surface Area Calculation")
    st.markdown(f"""
    **Calculation:**
    - Number of strips needed: **{total_strips}**
    - Area per strip: 6.5" × 3/16" = **{strip_area:.4f}** square inches
    - Total surface area: {total_strips} × {strip_area:.4f} = **{total_surface_area:.4f}** square inches
    """)
    
    st.success(f"🎯 **Total Surface Area: {total_surface_area:.4f} square inches**")
    
    st.session_state.responses.update({
        "Strip_Area": strip_area,
        "Total_Surface_Area": total_surface_area
    })
else:
    st.info("Complete Steps 2 and 4 to calculate the surface area!")

# Word Problems
st.markdown("---")
st.markdown("### 📝 Challenge Word Problems")

st.markdown("#### 📚 **Problem 1: Classroom Pencils**")
st.markdown("""
**Ms. Garcia** has 4 new pencils for her reading group. Each pencil is 7.5 inches long. 
She plans to use BIC Wite-Out strips (6.5" × 3/16") to cover them. Each pencil needs 8 strips around its circumference.

**Question:** How many total BIC strips does she need for all 4 pencils?
""")

problem1_answer = st.text_area(
    "Show your work:",
    height=100,
    key="problem1",
    placeholder="Step 1: Calculate strips along length for 1 pencil\nStep 2: Calculate total strips for 1 pencil\nStep 3: Multiply by 4 pencils"
)

st.markdown("#### 🎨 **Problem 2: Art Supply**")
st.markdown("""
**Tommy** is covering a 6-inch pencil with BIC Wite-Out strips. 
It takes 6 strips to go around the circumference of his pencil.

**Question:** What is the total surface area Tommy will cover?
""")

problem2_answer = st.text_area(
    "Show your calculation:",
    height=100,
    key="problem2",
    placeholder="Step 1: How many strips along the length?\nStep 2: Total strips needed?\nStep 3: Total surface area?"
)

st.markdown("#### 🏫 **Problem 3: Strip Efficiency**")
st.markdown("""
**Sarah** has a 4-inch pencil and **Alex** has a 9-inch pencil. 
Both pencils need 7 strips around their circumference.

**Question:** How many more BIC strips does Alex need than Sarah?
""")

problem3_answer = st.text_area(
    "Find the difference:",
    height=100,
    key="problem3",
    placeholder="Sarah's total strips = ?\nAlex's total strips = ?\nDifference = ?"
)

st.session_state.responses.update({
    "Word_Problem_1": problem1_answer,
    "Word_Problem_2": problem2_answer,
    "Word_Problem_3": problem3_answer
})

with st.expander("💡 Need help? Click for hints"):
    hint_col1, hint_col2, hint_col3 = st.columns(3)
    with hint_col1:
        st.markdown("**Problem 1:**\nStrips along length: 7.5 ÷ 6.5 ≈ 2 strips\nTotal per pencil: 2 × 8 = 16\nAll 4 pencils: 16 × 4 = 64 strips")
    with hint_col2:
        st.markdown("**Problem 2:**\nStrips along length: 6 ÷ 6.5 ≈ 1 strip\nTotal strips: 1 × 6 = 6\nArea: 6 × 1.2188 = 7.31 sq in")
    with hint_col3:
        st.markdown("**Problem 3:**\nSarah: 1 × 7 = 7 strips\nAlex: 2 × 7 = 14 strips\nDifference: 14 - 7 = 7 strips")

# Reflection Questions
st.markdown("---")
st.markdown("### 💭 Reflection Questions")

reflection1 = st.text_area("1. How did working with specific BIC strip dimensions (6.5\" × 3/16\") help you understand surface area?")
reflection2 = st.text_area("2. Why might estimation be a useful skill when planning how many supplies you need?")
reflection3 = st.text_area("3. Which was easier to visualize: the strips along the length or around the circumference? Why?")

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
            if 'Total_Calculated_Strips' in st.session_state.responses:
                st.metric("Calculated", f"{st.session_state.responses['Total_Calculated_Strips']} strips")
            else:
                st.metric("Calculated", "Not completed")
        with summary_col3:
            if 'Total_Surface_Area' in st.session_state.responses:
                st.metric("Surface Area", f"{st.session_state.responses['Total_Surface_Area']:.2f} sq in")
            else:
                st.metric("Surface Area", "Not calculated")
    else:
        st.error("Please fill in your name and date before submitting!")

# Teacher's Data View - Password Protected
st.markdown("---")
teacher_password = st.text_input("🏫 Teacher Access Code:", type="password", key="teacher_pass")

if teacher_password == "mathcraft2025":  # You can change this password
    st.markdown("### 📊 Teacher Dashboard")
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
                avg_calculated = df['Total_Calculated_Strips'].mean() if 'Total_Calculated_Strips' in df.columns else 0
                st.metric("Average Calculated", f"{avg_calculated:.1f}")
            with col3:
                completion_rate = (df['Name'].notna().sum() / len(df)) * 100
                st.metric("Completion Rate", f"{completion_rate:.0f}%")
                
        # Download option for teacher
        if len(df) > 0:
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Student Data as CSV",
                data=csv,
                file_name="student_responses.csv",
                mime="text/csv"
            )
    else:
        st.info("No student responses recorded in this session.")
elif teacher_password and teacher_password != "mathcraft2025":
    st.error("❌ Incorrect access code")

# Footer
st.markdown("---")
st.markdown("*Happy learning! Remember: estimation is a superpower that gets better with practice! 🌟*")
