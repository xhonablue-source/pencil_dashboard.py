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

# Interactive Fraction Tutorial
st.markdown("---\n\n### 📏 Interactive Fraction Tutorial")
st.markdown("#### Understanding Sixteenths of an Inch")
st.markdown("Let's learn how fractions work on a ruler!")

fig_ruler, ax_ruler = plt.subplots(figsize=(10, 2))
ruler_length = 2
ax_ruler.add_patch(plt.Rectangle((0, 0), ruler_length, 0.5, facecolor='lightgray', edgecolor='black'))
for i in range(3):
    ax_ruler.plot([i, i], [0, 0.5], 'k-', linewidth=3)
    ax_ruler.text(i, -0.1, f'{i}\"', ha='center', va='top', fontweight='bold', fontsize=12)
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
ax_ruler.set_xlim(-0.1, 2.1)
ax_ruler.set_ylim(-0.3, 0.8)
ax_ruler.axis('off')
ax_ruler.set_title("Ruler Showing Sixteenths of an Inch")
st.pyplot(fig_ruler)

numerator = st.slider("Select a numerator (top number):", 1, 16, 3)
st.markdown("Denominator (bottom number): 16")
st.markdown(f"**Your fraction:** {numerator}/16")
decimal_result = numerator / 16
st.markdown(f"**Decimal equivalent:** {numerator}/16 = {decimal_result:.4f} inches")

fig_frac, (ax_whole, ax_zoom) = plt.subplots(1, 2, figsize=(10, 2))
ax_whole.add_patch(plt.Rectangle((0, 0), 1, 0.5, facecolor='lightblue', edgecolor='black'))
for i in range(17):
    x = i / 16
    ax_whole.plot([x, x], [0, 0.5], 'k-', linewidth=0.5)
for i in range(numerator):
    x1 = i / 16
    x2 = (i + 1) / 16
    ax_whole.add_patch(plt.Rectangle((x1, 0), x2 - x1, 0.5, facecolor='red', alpha=0.7))
ax_whole.set_xlim(-0.05, 1.05)
ax_whole.set_ylim(-0.1, 0.7)
ax_whole.axis('off')
ax_whole.set_title(f"One Inch Showing {numerator}/16")
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
ax_zoom.set_xlim(zoom_start - 0.02, zoom_end + 0.02)
ax_zoom.set_ylim(-0.1, 0.8)
ax_zoom.axis('off')
ax_zoom.set_title(f"Zoomed View: {numerator}/16 = {decimal_result:.4f}\"")
st.pyplot(fig_frac)

st.markdown("""
#### 📋 Plan View: One Strip of Correction Tape
This shows what the tape strip looks like when viewed from directly above.
- Length: 6.5 inches
- Width: 3/16 inch = 0.1875 inches
""")
