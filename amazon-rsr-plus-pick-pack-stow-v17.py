import streamlit as st
import pandas as pd
import altair as alt

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pick & Stow Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== PICK & STOW DATA ======================
# Original Pick Data
pick_data = {
    "User": ["narossoh", "stajenni", "danijac", "arrizola", "hasnsai", "uiyps", "jnoonoor", 
             "gpliegom", "mtiband r", "elizev", "hersmary", "mnimhas", "iqrayuss", 
             "nkaibrah", "matstrak", "abdiosmg", "musaom"],
    "Opportunities": [746, 804, 169, 614, 214, 208, 110, 362, 68, 176, 69, 97, 37, 255, 186, 44, 55],
    "Defects": [57, 14, 13, 13, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2],
    "DPMO": [76408, 17412, 76923, 21172, 37383, 38461, 63636, 19337, 88235, 34090, 72463, 51546, 108108, 15686, 16129, 68181, 36363]
}

# Original Stow Data
stow_data = {
    "User": ["narossoh", "iqrayuss", "uiyps", "mnimhas", "hersmary", "mtiband r", "danijac", 
             "nkaibrah", "gpliegom", "matstrak", "hasnsai", "elizev", "pmhusse", "stajenni", 
             "abdiosmg", "jnoonoor", "arrizola"],
    "Opportunities": [1068, 758, 330, 668, 246, 445, 168, 518, 580, 594, 416, 204, 308, 127, 214, 63, 57],
    "Defects": [164, 130, 117, 94, 45, 37, 22, 17, 15, 13, 12, 12, 9, 7, 4, 3, 3],
    "DPMO": [153558, 171503, 354545, 140718, 182926, 83146, 130952, 32818, 25862, 21885, 28846, 58823, 29220, 55118, 18691, 47619, 52631]
}

df_pick_orig = pd.DataFrame(pick_data)
df_stow_orig = pd.DataFrame(stow_data)

# Normalized Data
pick_norm_data = {
    "User": ["narossoh", "stajenni", "danijac", "arrizola", "hasnsai", "uiyps", "jnoonoor", 
             "gpliegom", "mtiband r", "elizev", "hersmary", "mnimhas", "iqrayuss", 
             "nkaibrah", "matstrak", "abdiosmg", "musaom"],
    "Original_Defects": [57, 14, 13, 13, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2],
    "Original_Opp": [746, 804, 169, 614, 214, 208, 110, 362, 68, 176, 69, 97, 37, 255, 186, 44, 55],
    "New_Defects": [57, 13, 57, 16, 28, 29, 47, 14, 66, 25, 54, 38, 81, 12, 12, 51, 27],
    "DPMO": [76408, 17426, 76408, 21448, 37534, 38874, 63003, 18767, 88472, 33512, 72386, 50938, 108579, 16086, 16086, 68365, 36193]
}

stow_norm_data = {
    "User": ["narossoh", "iqrayuss", "uiyps", "mnimhas", "hersmary", "mtiband r", "danijac", 
             "nkaibrah", "gpliegom", "matstrak", "hasnsai", "elizev", "pmhusse", "stajenni", 
             "abdiosmg", "jnoonoor", "arrizola"],
    "Original_Defects": [164, 130, 117, 94, 45, 37, 22, 17, 15, 13, 12, 12, 9, 7, 4, 3, 3],
    "Original_Opp": [1068, 758, 330, 668, 246, 445, 168, 518, 580, 594, 416, 204, 308, 127, 214, 63, 57],
    "New_Defects": [164, 183, 379, 150, 195, 89, 140, 35, 28, 23, 31, 63, 31, 59, 20, 51, 56],
    "DPMO": [153558, 171348, 354869, 140449, 182584, 83333, 131086, 32772, 26217, 21536, 29026, 58989, 29026, 55243, 18727, 47753, 52434]
}

df_pick_norm = pd.DataFrame(pick_norm_data)
df_stow_norm = pd.DataFrame(stow_norm_data)

# ====================== WORK HOURS DATA ======================
hours_data = {
    "User": ["narossoh"] * 8,
    "Date": ["2026-04-05", "2026-04-05", "2026-04-06", "2026-04-06", "2026-04-09", "2026-04-09", 
             "2026-04-10", "2026-04-11"],
    "Day": ["Sunday", "Sunday", "Monday", "Monday", "Thursday", "Thursday", "Friday", "Saturday"],
    "Start Time": ["19:00", "19:00", "19:00", "19:00", "19:00", "19:00", "19:00", "14:30"],
    "End Time": ["23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "18:30"],
    "Hours Worked": [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
}
df_hours = pd.DataFrame(hours_data)

all_users = sorted(df_pick_orig["User"].unique())

# ====================== WEEKLY SPEND DATA ======================
spend_data = {
    "User": ["narossoh", "gpliegom", "stajenni", "iqrayuss", "matstrak", "nkaibrah", "mnimhas", 
             "arrizola", "hasnsai", "uiyps", "mtiband r", "elizev", "danijac", "hersmary", 
             "abdiosmg", "jnoonoor", "musaom"],
    "Pick Opportunities": [0, 362, 804, 37, 186, 255, 97, 614, 214, 208, 68, 176, 169, 69, 44, 110, 55],
    "Stow Opportunities": [1068, 580, 127, 758, 594, 518, 668, 57, 416, 330, 445, 204, 168, 246, 214, 63, 0],
    "Total Opportunities": [1814, 942, 931, 795, 780, 773, 765, 671, 630, 538, 513, 380, 337, 315, 258, 173, 55],
    "% of Total Volume": [17.00, 8.83, 8.73, 7.45, 7.31, 7.24, 7.17, 6.29, 5.90, 5.04, 4.81, 3.56, 3.16, 2.95, 2.42, 1.62, 0.52],
    "Estimated Spend": [1624.18, 843.62, 834.06, 711.77, 698.40, 691.71, 685.02, 600.95, 563.69, 481.52, 459.55, 340.12, 301.91, 281.84, 231.21, 154.77, 49.68]
}

df_spend = pd.DataFrame(spend_data)

# ====================== PACKING PERFORMANCE DATA ======================
packing_data = {
    "Activity": ["Packing Items", "Trickling Packages"],
    "Items/Packages": [88, 88],
    "Time (minutes)": [47, 10],
    "Rate (per minute)": [88/47, 88/10],
    "Rate (per hour)": [(88/47)*60, (88/10)*60]
}

df_packing = pd.DataFrame(packing_data)

# ====================== TOTAL VOLUME BASED VALUE DATA ======================
volume_data = {
    "User": ["narossoh", "gpliegom", "stajenni", "iqrayuss", "matstrak", "nkaibrah", "mnimhas", 
             "arrizola", "hasnsai", "uiyps", "mtiband r", "elizev", "danijac", "hersmary", 
             "pmhusse", "abdiosmg", "jnoonoor", "musaom"],
    "Pick Opportunities": [746, 362, 804, 37, 186, 255, 97, 614, 214, 208, 68, 176, 169, 69, 0, 44, 110, 55],
    "Stow Opportunities": [1068, 580, 127, 758, 594, 518, 668, 57, 416, 330, 445, 204, 168, 246, 308, 214, 63, 0],
    "Total Opportunities": [1814, 942, 931, 795, 780, 773, 765, 671, 630, 538, 513, 380, 337, 315, 308, 258, 173, 55],
    "% of Total Volume": [16.52, 8.58, 8.48, 7.24, 7.11, 7.04, 6.97, 6.11, 5.74, 4.9, 4.67, 3.46, 3.07, 2.87, 2.81, 2.35, 1.58, 0.5],
    "Estimated Spend": [1578.32, 819.73, 810.18, 691.71, 679.29, 672.6, 665.91, 583.75, 548.4, 468.15, 446.17, 330.57, 293.31, 274.2, 268.47, 224.52, 150.95, 47.77]
}

df_volume = pd.DataFrame(volume_data)

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "👥 3-Associate Comparison",
     "⏰ Associate Work Hours & Productivity",
     "📊 Team Overview",
     "💰 Payroll Overview",
     "💰 Weekly Spend by Associate",
     "⏱️ Narossoh Packing Time Calculator",
     "📊 Narossoh Volume Equivalence Report"])

# ====================== MAIN PAGES ======================
# (All previous pages are kept exactly as in your current code base)

if page == "🏠 Home & Summary":
    st.title("📦 Warehouse Pick & Stow Performance Dashboard")
    st.markdown("**April 5th – April 12th, 2026** | Amazon RSR+ Analysis")
    
    st.markdown("### Report Summary & Explanation")
    st.info("""
    This dashboard contains both **original** and **updated/normalized** versions of the Pick and Stow reports.
    
    **Key Update Performed:**
    - We normalized all associates to **narossoh’s opportunity volume** (746 in Pick, 1,068 in Stow).
    - Defects were scaled proportionally while keeping each associate’s individual error rate (DPMO) constant.
    - This allows fair quality comparison regardless of volume worked.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Associates", 17)
        st.metric("Original Pick Opportunities", "4,214")
    with col2:
        st.metric("Original Stow Opportunities", "6,112")

# ... [Keep all your existing pages: Pick Report, Stow Report, 3-Associate Comparison, 
#      Work Hours, Team Overview, Payroll Overview, Weekly Spend, Packing Calculator] ...

# (For brevity, I'm not repeating all 8+ pages here — they stay exactly as you provided them)

elif page == "📊 Narossoh Volume Equivalence Report":
    st.title("📊 Narossoh Volume Equivalence Report")
    st.markdown("**Total Volume Based Value** | April 5th – April 12th, 2026")

    narossoh_row = df_volume[df_volume["User"] == "narossoh"].iloc[0]
    nar_total = narossoh_row["Total Opportunities"]
    team_total = df_volume["Total Opportunities"].sum()
    nar_percent = narossoh_row["% of Total Volume"]

    avg_per_assoc = team_total / len(df_volume)
    equiv_associates = round(nar_total / avg_per_assoc, 2)

    st.subheader("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Narrossoh Total Volume", f"{nar_total:,}")
    with col2: st.metric("Team Total Volume", f"{team_total:,}")
    with col3: st.metric("Narrossoh % of Team", f"{nar_percent}%")
    with col4: st.metric("Equivalent to Associates", f"{equiv_associates}×")

    st.success(f"""
    **Narrossoh performs the work of approximately {equiv_associates} average associates.**
    """)

    st.markdown("---")
    st.subheader("🔻 How Many Bottom Associates Fit Into Narossoh’s Volume?")

    # Bottom-up analysis (ascending from lowest volume)
    df_bottom = df_volume.sort_values("Total Opportunities", ascending=True).reset_index(drop=True)
    df_bottom["Cumulative Volume"] = df_bottom["Total Opportunities"].cumsum()

    # Find the smallest number of bottom associates that meet or exceed narossoh
    bottom_count = (df_bottom["Cumulative Volume"] >= nar_total).idxmax() + 1
    bottom_sum = df_bottom.loc[bottom_count-1, "Cumulative Volume"]

    st.metric(
        label=f"**Bottom {bottom_count} associates** match Narossoh",
        value=f"{bottom_sum:,} opportunities",
        delta=f"{'+' if bottom_sum > nar_total else ''}{bottom_sum - nar_total}"
    )

    # Show the bottom associates used
    st.dataframe(
        df_bottom[["User", "Total Opportunities", "Cumulative Volume"]].head(bottom_count).style.format({
            "Total Opportunities": "{:,}",
            "Cumulative Volume": "{:,}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.info(f"""
    **Result**: Starting from the **bottom** of the report (lowest volume) and moving upward,  
    it takes **{bottom_count} associates** to reach or exceed narossoh’s **{nar_total}** opportunities.  

    The bottom **{bottom_count}** associates (musaom through elizev) have a combined **{bottom_sum}** opportunities.
    """)

    # Visualization
    st.subheader("Bottom-Up Cumulative Volume vs Narossoh")
    chart_data = pd.DataFrame({
        "Category": ["Narrossoh"] + list(df_bottom["User"].head(bottom_count)),
        "Opportunities": [nar_total] + list(df_bottom["Cumulative Volume"].head(bottom_count))
    })

    bar_chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X("Category:N", sort=None, title=""),
        y=alt.Y("Opportunities:Q", title="Total Opportunities"),
        color=alt.Color("Category:N", scale=alt.Scale(range=["#ff7f0e"] + ["#636efa"] * bottom_count))
    ).properties(height=400)

    st.altair_chart(bar_chart, use_container_width=True)

    st.caption("Data Source: Total Volume Based Value Report • Bottom-up cumulative analysis")

# Final caption
st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
