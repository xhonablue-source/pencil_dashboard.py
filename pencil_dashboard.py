import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import pandas as pd

st.set_page_config(page_title="44th Grade Math: Dimensional Thinking with a Pencil", layout="centered")

st.image("/mnt/data/fcfe8c75-0250-4090-b003-4879d74691c8.png", width=80)
st.markdown("#### Honablue M.Ed International")
st.title("📝 4th Grade Math Packet: Dimensional Thinking with a Pencil")

# Initialize response database
if "all_responses" not in st.session_state:
    st.session_state["all_responses"] = []
if "responses" not in st.session_state:
    st.session_state["responses"] = {}

# Student Info
name = st.text_input("Name:")
date = st.text_input("Date:")
st.session_state["responses"].update({"Name": name, "Date": date})

# Objective
st.markdown("""
### 🧠 Objective:
Use estimation, drawing, and measurement to explore **dimensions, area, and circumference** with a pencil and yellow tape.
""")

st.write("In 1st grade, students described a pencil by its length and weight. Some said 'yellow' — today, we explore what that really means in mathematical terms.")

# Step 1 & 4: Estimate vs. Actual Tape Strips
st.markdown("### Step 1 & 4: Estimate vs. Actual Tape Strips")

estimation = st.slider("✏️ My Estimate: How many strips do you THINK it will take to cover the pencil?", 1, 8, 4, label_visibility="visible")
actual = st.number_input("📏 Actual Strips: Count the number it took to fully cover the pencil.", min_value=1, max_value=8, value=4, label_visibility="visible")
st.session_state["responses"].update({"Estimate": estimation, "Actual": actual})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(4, 5))
for i in range(8):
    ax1.add_patch(plt.Rectangle((0, i), 1, 0.8, color="gold" if i >= (8 - estimation) else "#fefefe", ec='black'))
    ax2.add_patch(plt.Rectangle((0, i), 1, 0.8, color="gold" if i >= (8 - actual) else "#fefefe", ec='black'))
ax1.set_xlim(0, 1); ax1.set_ylim(0, 8); ax1.set_xticks([]); ax1.set_yticks([]); ax1.set_title("Estimated Strips")
ax2.set_xlim(0, 1); ax2.set_ylim(0, 8); ax2.set_xticks([]); ax2.set_yticks([]); ax2.set_title("Actual Strips")
st.pyplot(fig)

with st.expander("💭 Analytical Thought"):
    st.markdown("""
    - The shaded bars above represent the number of strips you estimated.
    - Why does the minimum start at 1 and the maximum end at 8?
    - What does this tell you about your brain's trained ability to estimate?
    - Is it possible that people who estimate really well do really good things?
    - Can you list some situations where good estimation is beneficial?
    """)

# Math reflection questions
st.markdown("### 🧮 Reflection Questions")
same = st.text_input("Did your estimated and actual count come out the same?")
diff = st.text_input("If not, how many more or less did you estimate?")
st.session_state["responses"].update({"Same Estimate/Actual": same, "Difference": diff})

# Step 2
st.markdown("---\n\n### Step 2: Sketch Your Strip Estimate")
st.markdown("Take your marker and run it along the pencil full length. Then draw how many strips you think you marked directly on the screen.")

# Step 3
st.markdown("---\n\n### Step 3: Confirm Measurement")
st.markdown("Use yellow tape to measure the full length of the pencil. Count how many strips it actually took.")
real_strip_count = st.text_input("Actual number of strips used:")
st.session_state["responses"].update({"Real Strips": real_strip_count})

# Step 3.5
st.markdown("---\n\n### 📏 Step 3.5: Compare Inches and Centimeters")
st.markdown("Use a real ruler. Notice that inches and centimeters are on opposite sides of the ruler.")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Ruler_inches_cm.svg/1200px-Ruler_inches_cm.svg.png", caption="Sample ruler with inches and centimeters on opposite sides.", use_container_width=True)
inches = st.text_input("What is the pencil's length in inches?")
centimeters = st.text_input("What is the pencil's length in centimeters?")
st.session_state["responses"].update({"Inches": inches, "Centimeters": centimeters})

with st.expander("📘 Analytical Thinking"):
    st.markdown("""
    - What does this tell you about inches compared to centimeters?
    - What words can apply? (e.g. *greater than*, *less than*)
    - What might a **conversion** look like between inches and centimeters?
    """)

# Step 4
st.markdown("---\n\n### Step 4: Sketch Total Area from Strips")
st.markdown("Draw all the yellow strips stacked on top of each other (like rectangles) to represent the total tape area directly on the screen.")

# Step 5
st.markdown("---\n\n### Step 5: Explore the Pencil's Cross Section")
st.markdown("Click how many yellow tape arcs to shade around the outside edge.")
arc_selections = st.multiselect("Select arcs to shade yellow:", options=list(range(1, 7)), default=[])
st.session_state["responses"].update({"Arcs Shaded": arc_selections})

fig3, ax3 = plt.subplots()
ax3.add_patch(plt.Circle((0.5, 0.5), 0.41, color='black', zorder=0))
for i in range(6):
    theta1 = i * (360 / 6)
    theta2 = (i + 1) * (360 / 6)
    color = "gold" if (i + 1) in arc_selections else "#fefefe"
    wedge = mpatches.Wedge((0.5, 0.5), 0.4, theta1, theta2, width=0.1, facecolor=color, edgecolor='black')
    ax3.add_patch(wedge)
ax3.add_patch(plt.Circle((0.5, 0.5), 0.3, color='#DEB887'))
ax3.text(0.5, 0.5, "pencil\ncross section", ha='center', va='center', fontsize=8, color='white')
ax3.set_aspect('equal')
ax3.axis('off')
ax3.set_title("Yellow Tape Segments Around Circular End")
st.pyplot(fig3)

# Step 6
st.markdown("---\n\n### 📦 Step 6: Flatten the Pencil — Area Visualization")
st.markdown("""
When you wrap vertical strips of yellow tape around the pencil and then unroll it, you form a rectangle:
- **Length** = the actual length of the pencil
- **Width** = the number of strips it took to go around
- **Area** = Length × Strip Count
""")

# Submit and show data
if st.button("✅ Submit My Work"):
    st.session_state["all_responses"].append(st.session_state["responses"].copy())
    st.success("Your responses have been recorded.")

if st.checkbox("📊 Show All Responses"):
    if st.session_state["all_responses"]:
        df_all = pd.DataFrame(st.session_state["all_responses"])
        st.dataframe(df_all)
    else:
        st.warning("No responses recorded yet.")

# Vocabulary
st.markdown("### 📚 Vocabulary")
st.markdown("""
- **Estimation**: A careful guess about a number or measurement.
- **Measurement**: Finding the size, length, or amount of something.
- **Length**: The longest dimension of an object.
- **Width**: The measurement of something from side to side.
- **Area**: The amount of space a surface covers; calculated by multiplying length × width.
- **Circumference**: The distance around a circle.
- **Cross Section**: A shape made by cutting straight through an object.
- **Rectangle**: A 2D shape with four sides and four right angles.
- **Inches**: A standard unit of length in the US customary system.
- **Centimeters**: A unit of length in the metric system.
- **Conversion**: Changing from one unit of measurement to another.
""")
