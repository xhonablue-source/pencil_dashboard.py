import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Cognitive Cloud | 4th Grade Area & Measurement", 
    layout="centered",
    page_icon="🧠"
)

# Header with new branding
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #2E4A6B 0%, #4A9B8E 50%, #F4A261 100%); border-radius: 15px; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <h2 style="color: white; margin: 0; font-weight: bold; font-size: 2.2rem;">🧠 Cognitive Cloud</h2>
    <p style="color: #f0f0f0; margin: 0.5rem 0; font-style: italic; font-size: 1.1rem;">Think Beyond. Learn Without Limits.</p>
    <p style="color: #e0e0e0; margin: 0; font-size: 0.85rem; opacity: 0.9;">Adaptive Learning Experience | © Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

st.title("📐 Adaptive Mathematics: Area and Measurement Discovery")

# Michigan Learning Standards
st.markdown("---")
st.markdown("### 📚 Learning Standards & Cognitive Pathways")
with st.expander("🎯 View aligned standards and adaptive learning objectives"):
    st.markdown("""
    **Michigan Learning Standards Addressed:**
    
    **4.MD.1** - Know relative sizes of measurement units within one system of units including km, m, cm; kg, g; lb, oz.; l, ml; hr, min, sec. Within a single system of measurement, express measurements in a larger unit in terms of a smaller unit.
    *Cognitive Pathway: Converting between inches and centimeters, understanding fractions of an inch (3/16), decimal conversions*
    
    **4.MD.2** - Use the four operations to solve word problems involving distances, intervals of time, liquid volumes, masses of objects, and money, including problems involving simple fractions or decimals.
    *Cognitive Pathway: Multi-step word problems using surface area calculations, working with fractions (3/16 inch), estimation error calculations*
    
    **4.MD.3** - Apply the area and perimeter formulas for rectangles in real world and mathematical problems.
    *Cognitive Pathway: Surface area formula (Length × Width × Number of strips), calculating area of tape strips, real-world application to pencil covering*
    
    **4.OA.3** - Solve multistep word problems posed with whole numbers and having whole-number answers using the four operations, including problems in which remainders must be interpreted.
    *Cognitive Pathway: Estimation vs. actual comparisons, error ratio calculations, multi-step area problems*
    
    **4.NF.6** - Use decimal notation for fractions with denominators 10 or 100.
    *Cognitive Pathway: Converting 3/16 to decimal form (0.1875), understanding decimal representations*
    
    **Cognitive Learning Practices:**
    - **Adaptive Reasoning** - Make sense of problems and develop personalized solution strategies
    - **Pattern Recognition** - Reason abstractly and quantitatively *(error ratios, percent calculations)*
    - **Critical Analysis** - Construct viable arguments and evaluate reasoning *(analytical thinking about estimates)*
    - **Mathematical Modeling** - Connect mathematics to real-world applications *(surface area formula, practical applications)*
    - **Strategic Thinking** - Use appropriate tools and methods strategically *(rulers, fraction visualization, correction tape)*
    - **Precision & Accuracy** - Attend to mathematical precision *(fraction measurements, decimal accuracy)*
    """)
st.markdown("---")

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# Student Information Section
st.markdown("### 👨‍🎓 Learner Profile")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name:", key="student_name")
with col2:
    date = st.text_input("Date:", key="student_date")

st.session_state.responses.update({"Name": name, "Date": date})

# Learning Objective with Cognitive Cloud approach
st.markdown("---")
st.markdown("""
### 🧠 Adaptive Learning Objective
Discover **area and measurement** concepts through hands-on exploration, adaptive reasoning, and personalized problem-solving using everyday materials.

**Cognitive Cloud adapts to your thinking patterns as you:**
- Develop estimation strategies that match your reasoning style
- Build spatial understanding through multiple measurement approaches
- Connect abstract mathematical concepts to tangible experiences

### 📦 Learning Materials
- 📝 **Wood pencil** (standard #2 pencil)
- ⚪ **BIC Wite-Out EZ Correct** correction tape dispenser
- 📏 **Ruler** (with both inches and centimeters)
""")

# Area Formula Introduction with Cognitive Cloud styling
st.markdown("---")
st.markdown("### 🌟 **FOUNDATIONAL CONCEPT FOR THIS DISCOVERY**")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #2E4A6B 0%, #4A9B8E 100%); border-radius: 20px; margin: 1rem 0; box-shadow: 0 6px 20px rgba(0,0,0,0.15);">
    <h3 style="color: white; margin: 0; font-size: 1.6rem;">Surface Area Discovery Formula</h3>
    <h2 style="color: #F4A261; margin: 1rem 0; font-family: monospace; font-size: 2.2rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">Area = Length × Width × Strips</h2>
    <p style="color: #f0f0f0; margin: 0; font-style: italic; font-size: 1.1rem;">Length of pencil × Width of tape × Number of strips around</p>
    <p style="color: #e0e0e0; margin: 0.5rem 0; font-size: 0.9rem;">🧠 Cognitive Cloud adapts this formula to your learning style</p>
</div>
""", unsafe_allow_html=True)

# Plan view of tape strip with enhanced visualization
st.markdown("### 📋 Understanding Your BIC Wite-Out EZ Correct Strip")
st.markdown("**Cognitive Cloud Visual Learning: Examining ONE strip from above (Plan View):**")

fig_tape, ax_tape = plt.subplots(figsize=(12, 5))

tape_length = 6.5
tape_width = 3/16
scale_factor = 20  # Enhanced for better visibility

rect = plt.Rectangle((0, 0), tape_length, tape_width * scale_factor, 
                    facecolor='white', edgecolor='#2E4A6B', linewidth=4)
ax_tape.add_patch(rect)

# Enhanced dimensions with Cognitive Cloud colors
ax_tape.annotate('', xy=(0, -0.5), xytext=(tape_length, -0.5),
                arrowprops=dict(arrowstyle='<->', color='#4A9B8E', lw=4))
ax_tape.text(tape_length/2, -0.8, f'{tape_length}" long', 
            ha='center', va='top', fontsize=16, color='#4A9B8E', fontweight='bold')

ax_tape.annotate('', xy=(-0.6, 0), xytext=(-0.6, tape_width * scale_factor),
                arrowprops=dict(arrowstyle='<->', color='#F4A261', lw=4))
ax_tape.text(-0.9, (tape_width * scale_factor)/2, f'3/16" wide', 
            ha='center', va='center', fontsize=14, color='#F4A261', fontweight='bold', rotation=90)

# Enhanced area calculation with cognitive emphasis
ax_tape.text(tape_length/2, (tape_width * scale_factor)/2, 
            f'Area = {tape_length}" × 3/16" = {tape_length * (3/16):.4f} square inches', 
            ha='center', va='center', fontsize=14, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#F4A261", alpha=0.9, edgecolor="#2E4A6B"))

ax_tape.set_xlim(-1.5, tape_length + 0.7)
ax_tape.set_ylim(-1.2, tape_width * scale_factor + 0.7)
ax_tape.set_aspect('equal')
ax_tape.set_title('🧠 Cognitive Cloud Visualization: ONE BIC Wite-Out EZ Correct Strip\n(Actual dimensions for adaptive learning)', 
                 fontsize=18, fontweight='bold', pad=25, color='#2E4A6B')
ax_tape.axis('off')

st.pyplot(fig_tape)

st.markdown("""
**Why these measurements enhance your cognitive understanding:**
- **Length: 6.5 inches** - This is how long each strip is when you pull it from the dispenser
- **Width: 3/16 inch** - This is how wide the tape is (we'll explore this fraction cognitively!)
- **Area of ONE strip: 1.2188 square inches** - This is the area each strip covers

🧠 **Cognitive Learning Note:** Plan View means looking down from directly above, showing length and width. This spatial reasoning skill transfers to many mathematical concepts!
""")

# Enhanced Interactive Fraction Tutorial
st.markdown("---")
st.markdown("### 📏 Cognitive Discovery: Understanding 3/16 Inch (Your Tape Width!)")
st.markdown("**Your BIC Wite-Out tape is 3/16 inch wide. Cognitive Cloud adapts to help you understand fractions through multiple pathways!**")

# Create enhanced ruler showing sixteenths
fig_ruler, ax_ruler = plt.subplots(figsize=(12, 5))
ruler_length = 1
ax_ruler.add_patch(plt.Rectangle((0, 0), ruler_length, 0.6, facecolor='#F8F9FA', edgecolor='#2E4A6B', linewidth=2))

# Add inch marks with Cognitive Cloud styling
for i in range(2):
    ax_ruler.plot([i, i], [0, 0.6], color='#2E4A6B', linewidth=4)
    ax_ruler.text(i, -0.15, f'{i}"', ha='center', va='top', fontweight='bold', fontsize=14, color='#2E4A6B')

# Enhanced sixteenth marks with special highlighting for 3/16
for i in range(ruler_length * 16 + 1):
    x = i / 16
    if i % 16 == 0:
        continue
    elif i % 8 == 0:
        ax_ruler.plot([x, x], [0, 0.5], color='#4A9B8E', linewidth=3)
    elif i % 4 == 0:
        ax_ruler.plot([x, x], [0, 0.4], color='#4A9B8E', linewidth=2)
    elif i % 2 == 0:
        ax_ruler.plot([x, x], [0, 0.3], 'k-', linewidth=1.5)
    else:
        ax_ruler.plot([x, x], [0, 0.2], 'k-', linewidth=1)

# Enhanced highlight for 3/16
tape_width_pos = 3/16
ax_ruler.plot([tape_width_pos, tape_width_pos], [0, 0.6], color='#F4A261', linewidth=6)
ax_ruler.text(tape_width_pos, 0.85, '3/16"\n(Your tape width!)', ha='center', va='bottom', 
             fontweight='bold', color='#F4A261', fontsize=14,
             bbox=dict(boxstyle="round,pad=0.4", facecolor="#F4A261", alpha=0.2, edgecolor="#F4A261"))

ax_ruler.set_xlim(-0.15, 1.15)
ax_ruler.set_ylim(-0.3, 1.1)
ax_ruler.set_title('🧠 Cognitive Cloud Ruler: Understanding Your Tape Width (3/16 Inch)', 
                  fontsize=16, fontweight='bold', color='#2E4A6B')
ax_ruler.axis('off')
st.pyplot(fig_ruler)

# Enhanced Interactive fraction calculator
st.markdown("#### 🧮 Adaptive Fraction Explorer: Discover Different Sixteenths")
st.markdown("**Cognitive Cloud adapts: Try different fractions to see how 3/16 compares to other measurements:**")

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

# Enhanced feedback with Cognitive Cloud approach
if numerator == 3:
    st.success(f"🧠 **Cognitive Cloud Recognition!** This is your tape width: 3/16 = {decimal_result:.4f} inches")
else:
    st.info(f"🧠 Cognitive Cloud Comparison: This measures {decimal_result:.4f} inches vs. your tape width of {3/16:.4f} inches")

# Enhanced visual representation
fig_frac, (ax_whole, ax_zoom) = plt.subplots(1, 2, figsize=(14, 4))

# Enhanced whole inch visualization
ax_whole.add_patch(plt.Rectangle((0, 0), 1, 0.6, facecolor='#F8F9FA', edgecolor='#2E4A6B', linewidth=2))
for i in range(17):
    x = i / 16
    ax_whole.plot([x, x], [0, 0.6], color='#2E4A6B', linewidth=1)

# Enhanced highlighting with Cognitive Cloud colors
for i in range(numerator):
    x1 = i / 16
    x2 = (i + 1) / 16
    ax_whole.add_patch(plt.Rectangle((x1, 0), x2 - x1, 0.6, facecolor='#4A9B8E', alpha=0.8))

# Always show where 3/16 is for cognitive comparison
if numerator != 3:
    for i in range(3):
        x1 = i / 16
        x2 = (i + 1) / 16
        ax_whole.add_patch(plt.Rectangle((x1, 0), x2 - x1, 0.6, facecolor='#F4A261', alpha=0.6))
    ax_whole.text(3/32, 0.75, 'Tape width\n(3/16)', ha='center', va='bottom', fontsize=10, 
                 color='#F4A261', fontweight='bold')

ax_whole.set_xlim(-0.05, 1.05)
ax_whole.set_ylim(-0.15, 0.9)
ax_whole.set_title(f'🧠 Cognitive View: One Inch Showing {numerator}/16', fontweight='bold', color='#2E4A6B')
ax_whole.text(0.5, -0.08, '1 inch = 16/16', ha='center', va='top', fontsize=12, color='#2E4A6B')
ax_whole.axis('off')

# Enhanced zoomed view
zoom_start = max(0, (numerator - 2) / 16)
zoom_end = min(1, (numerator + 2) / 16)
ax_zoom.add_patch(plt.Rectangle((zoom_start, 0), zoom_end - zoom_start, 0.6, 
                               facecolor='#F8F9FA', edgecolor='#2E4A6B', linewidth=2))

for i in range(int(zoom_start * 16), int(zoom_end * 16) + 1):
    x = i / 16
    if zoom_start <= x <= zoom_end:
        ax_zoom.plot([x, x], [0, 0.6], color='#2E4A6B', linewidth=2)
        if i == numerator:
            ax_zoom.plot([x, x], [0, 0.6], color='#4A9B8E', linewidth=5)
            ax_zoom.text(x, 0.75, f'{i}/16', ha='center', va='bottom', fontweight='bold', 
                        color='#4A9B8E', fontsize=12)
        elif i == 3:  # Always mark the tape width
            ax_zoom.plot([x, x], [0, 0.6], color='#F4A261', linewidth=3)
            ax_zoom.text(x, -0.1, 'Tape', ha='center', va='top', fontsize=10, 
                        color='#F4A261', fontweight='bold')

ax_zoom.set_xlim(zoom_start - 0.02, zoom_end + 0.02)
ax_zoom.set_ylim(-0.2, 0.9)
ax_zoom.set_title(f'🔍 Adaptive Focus: {numerator}/16 = {decimal_result:.4f}"', 
                 fontweight='bold', color='#2E4A6B')
ax_zoom.axis('off')

st.pyplot(fig_frac)

st.markdown("""
### 🧠 **Cognitive Cloud Connection: Fractions to Area Calculation**

Now your mind has built the cognitive pathway: your BIC Wite-Out **strip** is **3/16 inch wide**!

**Cognitive Cloud identifies TWO key measurements for each strip:**
- **Length of the strip**: 6.5 inches (spatial dimension)
- **Width of the strip**: 3/16 inch (fractional dimension)

**When Cognitive Cloud calculates your pencil's surface area, the adaptive algorithm uses:**
- **Length**: How long your pencil measures (you'll discover this)
- **Strip width**: 3/16 inch (0.1875 inches) - the width dimension of each strip
- **Number of strips**: How many strips wrap around the pencil (spatial reasoning)

**🧠 Cognitive Cloud Formula Adaptation:**
**Area = Pencil length × Strip width × Number of strips around**
**Area = Pencil length × 0.1875 × Number of strips around**
""")

# Enhanced Step 1: Estimation with Cognitive Cloud approach
st.markdown("---")
st.markdown("### 📏 Discovery Step 1: Cognitive Estimation")
st.markdown("**Cognitive Cloud Adaptive Challenge:** Look at your pencil. Use your spatial reasoning and estimation skills - how many strips of white correction tape do you think it will take to cover the entire length?")

estimation = st.slider(
    "My Cognitive Estimate (number of strips):", 
    min_value=1, 
    max_value=10, 
    value=4,
    help="Cognitive Cloud tracks your estimation patterns to adapt future challenges!"
)

# Enhanced visual representation with Cognitive Cloud styling
fig1, ax1 = plt.subplots(figsize=(8, 4))
for i in range(10):
    color = "#4A9B8E" if i < estimation else "#F8F9FA"
    edge_color = "#2E4A6B" if i < estimation else "#cccccc"
    ax1.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor=edge_color, linewidth=2))
    text_color = "white" if i < estimation else "#666666"
    ax1.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold', 
            color=text_color, fontsize=12)

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1)
ax1.set_title(f"🧠 Your Cognitive Estimate: {estimation} strips", fontsize=16, fontweight='bold', color='#2E4A6B')
ax1.axis('off')
st.pyplot(fig1)

st.session_state.responses["Estimate"] = estimation

# Enhanced Analytical Thinking with Cognitive Cloud approach
st.markdown("### 🧠 Cognitive Cloud: Advanced Estimation Analysis")
st.markdown("**Cognitive Cloud adapts to your reasoning patterns. Analyze your estimation process:**")
st.markdown("""
**Cognitive Questions for Deep Thinking:**
- Why is **zero** not cognitively valid for this challenge?
- Is **10** a reasonable maximum estimate? What's your reasoning?
- How would allowing higher numbers affect your cognitive approach?
- What would be your personal maximum estimate and why?
- What cognitive strategies did you use to arrive at your number?
""")

estimation_reasoning = st.text_area(
    "Share your cognitive process:",
    height=130,
    key="estimation_reasoning",
    placeholder="Cognitive Cloud learning: What mental strategies did you use? How did you visualize the problem? What patterns influenced your thinking?"
)

st.session_state.responses["Estimation_Reasoning"] = estimation_reasoning

# Enhanced Step 2: Actual Measurement
st.markdown("---")
st.markdown("### 📐 Discovery Step 2: Hands-On Measurement")
st.markdown("**Cognitive Cloud Real-World Application:** Now use white correction tape to actually measure your pencil. Cognitive Cloud tracks how your estimation compares to reality!")

actual_strips = st.number_input(
    "Actual number of strips used:", 
    min_value=1, 
    max_value=10, 
    value=1,
    help="Cognitive Cloud analyzes this data to improve future estimation challenges"
)

# Enhanced visual comparison with Cognitive Cloud styling
fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(12, 4))

# Enhanced estimate visualization
for i in range(10):
    color = "#4A9B8E" if i < estimation else "#F8F9FA"
    edge_color = "#2E4A6B" if i < estimation else "#cccccc"
    ax2.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor=edge_color, linewidth=2))
    text_color = "white" if i < estimation else "#666666"
    ax2.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold', 
            color=text_color, fontsize=10)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 1)
ax2.set_title(f"🧠 Cognitive Estimate: {estimation} strips", fontsize=14, fontweight='bold', color='#2E4A6B')
ax2.axis('off')

# Enhanced actual visualization
for i in range(10):
    color = "#F4A261" if i < actual_strips else "#F8F9FA"
    edge_color = "#2E4A6B" if i < actual_strips else "#cccccc"
    ax3.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=color, edgecolor=edge_color, linewidth=2))
    text_color = "white" if i < actual_strips else "#666666"
    ax3.text(i + 0.4, 0.5, str(i + 1), ha='center', va='center', fontweight='bold', 
            color=text_color, fontsize=10)
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 1)
ax3.set_title(f"📏 Measured Reality: {actual_strips} strips", fontsize=14, fontweight='bold', color='#2E4A6B')
ax3.axis('off')

st.pyplot(fig2)

st.session_state.responses["Actual_Strips"] = actual_strips

# Enhanced Comparison Analysis with Cognitive Cloud approach
difference = abs(estimation - actual_strips)
st.markdown("### 🧠 Cognitive Cloud Analysis: How Did Your Mind Perform?")
if estimation == actual_strips:
    st.success("🎯 **Cognitive Perfection!** Your estimation matched exactly! Your spatial reasoning is excellently calibrated!")
else:
    st.info(f"🧠 **Cognitive Learning Opportunity:** Your estimate differed by {difference} strip(s). This builds better estimation neural pathways!")

# Enhanced Error Ratio Tutorial with Cognitive Cloud approach
st.markdown("### 💡 Cognitive Cloud Advanced Analysis: Understanding Your Estimation Accuracy")
st.markdown("**Cognitive Cloud Algorithm: Analyzing your estimation vs. actual measurement patterns**")

st.markdown("""
**Cognitive Learning Steps:**

**Step 1:** Calculate the **difference** between your **cognitive estimate** and the measured reality.

**Step 2:** Apply the Cognitive Cloud algorithm: divide that difference by the actual number to get your **estimation accuracy ratio**.

**Step 3:** Cognitive Cloud Formula: 

`Estimation Accuracy Ratio = |Cognitive Estimate - Measured Reality| / Measured Reality`

This cognitive metric helps Cognitive Cloud understand how your spatial reasoning compares to physical reality. Lower ratios indicate stronger estimation cognitive pathways!
""")

if actual_strips > 0:
    # Enhanced auto-calculation with Cognitive Cloud styling
    error_ratio = round(difference / actual_strips, 2)
    percent_error = round((difference / actual_strips) * 100, 1)
    percent_accuracy = round(100 - percent_error, 1)
    over_under = "above" if estimation > actual_strips else ("below" if estimation < actual_strips else "exact")
    
    # Enhanced auto-output calculator display
    st.markdown("#### 🧮 **Cognitive Cloud Analysis Results**")
    
    # Enhanced step-by-step calculation display
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        **Cognitive Step 1 - Calculate the difference:**
        - Your **cognitive estimate**: **{estimation}** strips
        - Measured reality: **{actual_strips}** strips  
        - Difference: |{estimation} - {actual_strips}| = **{difference}** strips
        
        **Cognitive Step 2 - Apply Cognitive Cloud algorithm:**
        - **Estimation Accuracy Ratio** = {difference} ÷ {actual_strips} = **{error_ratio}**
        
        **Cognitive Step 3 - Convert to cognitive performance metrics:**
        - **Estimation Variance**: {difference} ÷ {actual_strips} × 100 = **{percent_error}%**
        - **Cognitive Accuracy**: 100 - {percent_error} = **{percent_accuracy}%**
        """)
    
    with col2:
        # Enhanced visual summary with Cognitive Cloud styling
        st.markdown(f"""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, #2E4A6B 0%, #4A9B8E 100%); border-radius: 15px; color: white; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <h4 style="margin: 0; color: white;">🧠 Cognitive Performance</h4>
            <p style="margin: 0.7rem 0; font-size: 1.3rem;"><strong>Accuracy Ratio: {error_ratio}</strong></p>
            <p style="margin: 0.7rem 0; font-size: 1.1rem;"><strong>Cognitive Accuracy: {percent_accuracy}%</strong></p>
            <p style="margin: 0.7rem 0;"><strong>You estimated {over_under}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced interpretation with Cognitive Cloud feedback
    st.markdown("#### 🎯 **Cognitive Cloud Learning Insights:**")
    
    if over_under != "exact":
        st.markdown(f"Your **cognitive estimation** was **{over_under}** the measured reality by **{difference}** strips.")
    else:
        st.markdown("🌟 Your **cognitive estimation** perfectly matched reality! Exceptional spatial reasoning!")
    
    # Enhanced performance feedback with Cognitive Cloud approach
    if error_ratio == 0:
        st.success("🌟 **Cognitive Mastery!** Your estimation accuracy ratio = 0 - Perfect cognitive calibration!")
    elif error_ratio <= 0.2:
        st.success(f"🎯 **Advanced Cognitive Skills!** Your estimation accuracy ratio = {error_ratio} (≤ 0.2 indicates excellent spatial reasoning!)")
    elif error_ratio <= 0.5:
        st.info(f"👍 **Developing Cognitive Skills!** Your estimation accuracy ratio = {error_ratio} (≤ 0.5 shows good cognitive progress!)")
    elif error_ratio <= 1.0:
        st.warning(f"📈 **Cognitive Growth Opportunity!** Your estimation accuracy ratio = {error_ratio} - Cognitive Cloud will adapt to strengthen your estimation pathways!")
    else:
        st.warning(f"🎯 **Cognitive Challenge Identified!** Your estimation accuracy ratio = {error_ratio} - Cognitive Cloud will provide additional adaptive support!")
    
    # Store enhanced calculated values
    st.session_state.responses.update({
        "Cognitive_Accuracy_Ratio": error_ratio,
        "Cognitive_Percent_Error": percent_error,
        "Cognitive_Percent_Accuracy": percent_accuracy,
        "Cognitive_Pattern": over_under,
        "Cognitive_Difference": difference
    })
    
    # Enhanced calculation breakdown with Cognitive Cloud approach
    with st.expander("🔍 Cognitive Cloud: Deep Analysis Breakdown"):
        st.markdown(f"""
        **Cognitive Cloud Mathematical Analysis:**
        
        1. **Absolute Difference**: |{estimation} - {actual_strips}| = {difference}
        2. **Estimation Accuracy Ratio**: {difference} ÷ {actual_strips} = {difference/actual_strips:.4f} ≈ {error_ratio}
        3. **Cognitive Variance Percentage**: ({difference} ÷ {actual_strips}) × 100 = {(difference/actual_strips)*100:.1f}%
        4. **Cognitive Accuracy Percentage**: 100% - {percent_error}% = {percent_accuracy}%
        5. **Cognitive Pattern Analysis**: {estimation} {">" if estimation > actual_strips else ("<" if estimation < actual_strips else "=")} {actual_strips}, indicating your mind estimated {"above" if estimation > actual_strips else ("below" if estimation < actual_strips else "exactly at")} reality
        
        **Cognitive Cloud Insight:** Your brain's spatial reasoning patterns show {percent_accuracy}% alignment with physical measurement, providing valuable data for adaptive learning optimization.
        """)

else:
    st.info("Complete Discovery Step 2 above to activate Cognitive Cloud analysis!")

# Enhanced Step 3: Ruler Measurements with Cognitive Cloud approach
st.markdown("---")
st.markdown("### 📏 Discovery Step 3: Multi-Unit Measurement Analysis")
st.markdown("**Cognitive Cloud Adaptive Learning:** Use a real ruler to measure your pencil in both measurement systems. This builds cognitive flexibility with different unit systems.")

col1, col2 = st.columns(2)
with col1:
    inches = st.number_input("Length in inches:", min_value=0.0, step=0.1, format="%.1f")
with col2:
    centimeters = st.number_input("Length in centimeters:", min_value=0.0, step=0.1, format="%.1f")

st.session_state.responses.update({"Inches": inches, "Centimeters": centimeters})

if inches > 0 and centimeters > 0:
    ratio = centimeters / inches
    st.info(f"🧠 **Cognitive Cloud Pattern Recognition:** 1 inch ≈ {ratio:.1f} centimeters")

# Enhanced Step 4: Cross Section Exploration with Cognitive Cloud approach
st.markdown("---")
st.markdown("### ⭕ Discovery Step 4: Spatial Reasoning - Cross Section Analysis")
st.markdown("**Cognitive Cloud 3D Thinking:** If you made a cross-sectional cut through your pencil (like slicing bread), you'd see a circle. How many tape pieces would fit around this circular edge?")

circumference_estimate = st.slider(
    "Cognitive estimate: white tape pieces around the circumference:",
    min_value=1,
    max_value=8,
    value=6
)

# Enhanced cross section visualization with Cognitive Cloud styling
fig3, ax4 = plt.subplots(figsize=(8, 8))
circle = plt.Circle((0, 0), 1, color='#DEB887', alpha=0.8, edgecolor='#2E4A6B', linewidth=3)
ax4.add_patch(circle)

# Enhanced segments with Cognitive Cloud colors
degrees_per_section = 360 / circumference_estimate
colors = ['#4A9B8E', '#F4A261', '#2E4A6B']
for i in range(circumference_estimate):
    theta1 = i * degrees_per_section
    theta2 = (i + 1) * degrees_per_section
    
    wedge = mpatches.Wedge(
        (0, 0), 1.3, theta1, theta2, 
        width=0.2, facecolor=colors[i % len(colors)], 
        edgecolor='white', alpha=0.9, linewidth=2
    )
    ax4.add_patch(wedge)

ax4.set_xlim(-1.8, 1.8)
ax4.set_ylim(-1.8, 1.8)
ax4.set_aspect('equal')
ax4.set_title(f"🧠 Cognitive Cloud Cross Section Analysis\n{circumference_estimate} tape pieces around pencil edge", 
             fontsize=16, fontweight='bold', color='#2E4A6B', pad=20)
ax4.axis('off')
st.pyplot(fig3)

st.session_state.responses["Circumference_Estimate"] = circumference_estimate

# Enhanced Step 5: Area Calculator with Cognitive Cloud approach
st.markdown("---")
st.markdown("### 📦 Discovery Step 5: Cognitive Area Synthesis")
st.markdown("""
**Cognitive Cloud Advanced Thinking:** If you could unwrap all the correction tape from your pencil and lay it flat, you'd create a rectangle!

**Cognitive Cloud Dimensional Analysis:**
- **Length** = length of your pencil (linear dimension)
- **Width** = width of one tape strip (fractional dimension)
- **Depth** = number of strips around circumference (circular dimension)
- **Total Area** = Length × Width × Number of strips around
""")

st.markdown("#### 🧮 Cognitive Cloud Area Calculator")
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
        step=0.01, 
        value=0.1875,  # 3/16 in decimal
        format="%.4f",
        key="calc_width",
        help="BIC Wite-Out correction tape is 3/16 inch = 0.1875 inches wide"
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
    
    st.markdown("#### 📊 Cognitive Cloud Calculation Analysis:")
    st.markdown(f"""
    **{calc_length}** inches (length) × **{calc_width}** inches (width) × **{calc_strips}** strips = **{total_area:.4f} square inches**
    """)
    
    # Enhanced success message with Cognitive Cloud styling
    st.markdown(f"""
    <div style="padding: 1.5rem; background: linear-gradient(135deg, #4A9B8E 0%, #F4A261 100%); border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h3 style="color: white; margin: 0;">🎯 Cognitive Cloud Surface Area Discovery</h3>
        <h2 style="color: white; margin: 1rem 0; font-size: 2rem;">{total_area:.4f} square inches</h2>
        <p style="color: #f0f0f0; margin: 0;">Your pencil's total surface area coverage</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.responses.update({
        "Calculated_Area": total_area,
        "Calc_Length": calc_length,
        "Calc_Width": calc_width,
        "Calc_Strips": calc_strips
    })
else:
    st.info("🧠 Cognitive Cloud waiting: Enter all measurements above to activate area calculation!")

# Enhanced Word Problems with Cognitive Cloud approach
st.markdown("---")
st.markdown("### 📝 Cognitive Cloud Challenge Problems")

st.markdown("#### 📚 **Challenge 1: Collaborative Learning Scenario**")
st.markdown("""
**Ms. Garcia** leads a Cognitive Cloud learning group with 4 new pencils. Each pencil measures 8 inches long. 
She uses adaptive correction tape that is 0.1875 inches wide (3/16 inch), and the Cognitive Cloud analysis shows it takes 6 strips of tape to circumnavigate each pencil.

**Cognitive Challenge:** Calculate the total correction tape area needed to cover all 4 pencils using Cognitive Cloud methodology.
""")

problem1_answer = st.text_area(
    "Show your cognitive process:",
    height=120,
    key="problem1",
    placeholder="Cognitive Step 1: Calculate area for 1 pencil using the formula\nCognitive Step 2: Apply multiplication for 4 pencils\nCognitive Step 3: State your discovery with units"
)

st.markdown("#### 🎨 **Challenge 2: Creative Application**")
st.markdown("""
**Tommy** uses Cognitive Cloud thinking for an art project. His pencil measures 7 inches long, and he selects tape that is 0.5 inches wide. 
His spatial reasoning estimates suggest 5 strips will circumnavigate his pencil.

**Cognitive Challenge:** What surface area will Tommy cover using Cognitive Cloud calculation methods?
""")

problem2_answer = st.text_area(
    "Apply the Cognitive Cloud formula:",
    height=120,
    key="problem2",
    placeholder="Use Cognitive Cloud methodology: Length × Width × Number of strips = ?"
)

st.markdown("#### 🏫 **Challenge 3: Comparative Analysis**")
st.markdown("""
**Sarah** has a shortened pencil measuring 5 inches long. **Alex** has a full-length pencil measuring 10 inches long. 
Both pencils require 6 strips of 0.1875-inch wide tape for complete coverage according to Cognitive Cloud analysis.

**Cognitive Challenge:** Using Cognitive Cloud comparative thinking, determine how much additional tape area Alex needs compared to Sarah.
""")

problem3_answer = st.text_area(
    "Cognitive Cloud comparative analysis:",
    height=120,
    key="problem3",
    placeholder="Sarah's pencil area calculation = ?\nAlex's pencil area calculation = ?\nCognitive Cloud difference = ?"
)

st.session_state.responses.update({
    "Cognitive_Challenge_1": problem1_answer,
    "Cognitive_Challenge_2": problem2_answer,
    "Cognitive_Challenge_3": problem3_answer
})

# Enhanced hints with Cognitive Cloud approach
with st.expander("💡 Cognitive Cloud Learning Support - Click for adaptive hints"):
    hint_col1, hint_col2, hint_col3 = st.columns(3)
    with hint_col1:
        st.markdown("**Challenge 1 Pathway:**\n8 × 0.1875 × 6 = ? \nThen multiply by 4 pencils")
    with hint_col2:
        st.markdown("**Challenge 2 Pathway:**\n7 × 0.5 × 5 = ?")
    with hint_col3:
        st.markdown("**Challenge 3 Pathway:**\nCalculate each area first, then find the difference!")

# Enhanced Reflection Questions with Cognitive Cloud approach
st.markdown("---")
st.markdown("### 💭 Cognitive Cloud Reflection & Metacognition")

reflection1 = st.text_area("1. What cognitive discovery surprised you most about measuring your pencil?", 
                          placeholder="Cognitive Cloud learns from your insights...")
reflection2 = st.text_area("2. How might estimation be a valuable cognitive skill in real-world applications?", 
                          placeholder="Think about daily situations where estimation helps...")
reflection3 = st.text_area("3. Which measurement system (inches or centimeters) felt more cognitively natural? Why?", 
                          placeholder="Cognitive Cloud analyzes learning preferences...")
reflection4 = st.text_area("4. How did your spatial reasoning change throughout this Cognitive Cloud experience?", 
                          placeholder="Reflect on your cognitive growth...")

st.session_state.responses.update({
    "Cognitive_Reflection_1": reflection1,
    "Cognitive_Reflection_2": reflection2,
    "Cognitive_Reflection_3": reflection3,
    "Cognitive_Reflection_4": reflection4
})

# Enhanced Submit Section with Cognitive Cloud approach
st.markdown("---")
st.markdown("### ✅ Cognitive Cloud Learning Portfolio Submission")
if st.button("✅ Submit My Cognitive Cloud Portfolio", type="primary"):
    if name and date:
        st.session_state.all_responses.append(st.session_state.responses.copy())
        st.success("🧠 Excellent cognitive work! Your learning portfolio has been saved to Cognitive Cloud.")
        
        st.markdown("### 📊 Your Cognitive Cloud Learning Summary")
        summary_col1, summary_col2, summary_col3 = st.columns(3)
        with summary_col1:
            st.metric("Cognitive Estimate", f"{estimation} strips", delta=None)
        with summary_col2:
            st.metric("Measured Reality", f"{actual_strips} strips", delta=None)
        with summary_col3:
            difference_label = "Perfect!" if difference == 0 else f"{difference} strips"
            st.metric("Cognitive Accuracy", difference_label, delta=None)
    else:
        st.error("Please complete your learner profile (name and date) before submitting to Cognitive Cloud!")

# Enhanced Teacher's Data View with Cognitive Cloud approach
if st.checkbox("🏫 Educator Dashboard: Cognitive Cloud Analytics"):
    if st.session_state.all_responses:
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        
        if len(df) > 0:
            st.markdown("### 📈 Cognitive Cloud Class Analytics")
            col1, col2, col3 = st.columns(3)
            with col1:
                avg_estimate = df['Estimate'].mean() if 'Estimate' in df.columns else 0
                st.metric("Average Cognitive Estimate", f"{avg_estimate:.1f}")
            with col2:
                avg_actual = df['Actual_Strips'].mean() if 'Actual_Strips' in df.columns else 0
                st.metric("Average Measured Reality", f"{avg_actual:.1f}")
            with col3:
                completion_rate = (df['Name'].notna().sum() / len(df)) * 100
                st.metric("Cognitive Cloud Engagement", f"{completion_rate:.0f}%")
    else:
        st.info("🧠 Cognitive Cloud awaiting learner data...")

# Enhanced Footer with Cognitive Cloud branding
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #2E4A6B 0%, #4A9B8E 100%); border-radius: 15px; margin-top: 2rem;">
    <p style="color: white; margin: 0; font-size: 1.1rem; font-weight: bold;">🧠 Cognitive Cloud: Think Beyond. Learn Without Limits.</p>
    <p style="color: #f0f0f0; margin: 0.5rem 0; font-style: italic;">Remember: Your cognitive abilities grow stronger with every adaptive challenge! 🌟</p>
    <p style="color: #e0e0e0; margin: 0; font-size: 0.9rem;">Powered by adaptive learning technology that evolves with your mind</p>
</div>
""", unsafe_allow_html=True)
