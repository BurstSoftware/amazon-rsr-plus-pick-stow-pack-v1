import streamlit as st
import pandas as pd

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pick & Stow Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== DATA ======================
# Original Pick & Stow Data
pick_data = {
    "User": ["narossoh", "stajenni", "danijac", "arrizola", "hasnsai", "uiyps", "jnoonoor", 
             "gpliegom", "mtiband r", "elizev", "hersmary", "mnimhas", "iqrayuss", 
             "nkaibrah", "matstrak", "abdiosmg", "musaom"],
    "Opportunities": [746, 804, 169, 614, 214, 208, 110, 362, 68, 176, 69, 97, 37, 255, 186, 44, 55],
    "Defects": [57, 14, 13, 13, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2],
    "DPMO": [76408, 17412, 76923, 21172, 37383, 38461, 63636, 19337, 88235, 34090, 72463, 51546, 108108, 15686, 16129, 68181, 36363]
}

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

# Normalized Data (Updated to narossoh's volume)
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

# ====================== NAROSSOH WORK HOURS DATA ======================
hours_data = {
    "Date": ["2026-04-05", "2026-04-05", "2026-04-06", "2026-04-06", "2026-04-09", "2026-04-09", 
             "2026-04-10", "2026-04-11"],
    "Day": ["Sunday", "Sunday", "Monday", "Monday", "Thursday", "Thursday", "Friday", "Saturday"],
    "Start Time": ["19:00", "19:00", "19:00", "19:00", "19:00", "19:00", "19:00", "14:30"],
    "End Time": ["23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "18:30"],
    "Hours Worked": [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
}
df_hours = pd.DataFrame(hours_data)

# Calculate totals for narossoh (from reports)
total_pick_opp = 746
total_pick_defects = 57
total_stow_opp = 1068
total_stow_defects = 164
total_hours = df_hours["Hours Worked"].sum()  # 32.0 hours

# Productivity metrics
pick_units_per_hour = round(total_pick_opp / total_hours, 2)
stow_units_per_hour = round(total_stow_opp / total_hours, 2)
pick_defects_per_hour = round(total_pick_defects / total_hours, 2)
stow_defects_per_hour = round(total_stow_defects / total_hours, 2)

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "👥 3-Associate Comparison",
     "⏰ Narossoh Work Hours & Productivity"])

# ====================== PAGES ======================
if page == "🏠 Home & Summary":
    st.title("📦 Warehouse Pick & Stow Performance Dashboard")
    st.markdown("**April 5th – April 12th** | Amazon RSR+ Analysis")
    
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

elif page == "📦 Pick Report":
    st.title("📦 Pick Report Analysis")
    
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    
    with tab1:
        st.subheader("Original Pick Report")
        st.dataframe(df_pick_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Updated Pick Report – All at narossoh’s 746 Opportunities")
        st.markdown("**Explanation**: Every associate now has the same number of opportunities as narossoh (746). Defects have been scaled proportionally based on their original error rate. This enables direct quality comparison.")
        st.dataframe(df_pick_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "📦 Stow Report":
    st.title("📦 Stow Report Analysis")
    
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    
    with tab1:
        st.subheader("Original Stow Report")
        st.dataframe(df_stow_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Updated Stow Report – All at narossoh’s 1,068 Opportunities")
        st.markdown("**Explanation**: Every associate now has the same number of opportunities as narossoh (1,068). Defects have been scaled proportionally based on their original error rate. This enables direct quality comparison.")
        st.dataframe(df_stow_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "👥 3-Associate Comparison":
    st.title("👥 Focused Comparison: narossoh vs elizev vs arrizola")
    
    st.subheader("Original Data")
    comparison_original = pd.DataFrame({
        "Report": ["Pick", "Pick", "Pick", "Stow", "Stow", "Stow"],
        "User": ["narossoh", "elizev", "arrizola", "narossoh", "elizev", "arrizola"],
        "Opportunities": [746, 176, 614, 1068, 204, 57],
        "Defects": [57, 6, 13, 164, 12, 3],
        "DPMO": [76408, 33512, 21448, 153558, 58989, 52434]
    })
    st.dataframe(comparison_original, use_container_width=True, hide_index=True)
    
    st.subheader("Updated (Normalized to narossoh’s Volume)")
    comparison_updated = pd.DataFrame({
        "Report": ["Pick", "Pick", "Pick", "Stow", "Stow", "Stow"],
        "User": ["narossoh", "elizev", "arrizola", "narossoh", "elizev", "arrizola"],
        "Opportunities": [746, 746, 746, 1068, 1068, 1068],
        "Defects": [57, 25, 16, 164, 63, 56],
        "DPMO": [76408, 33512, 21448, 153558, 58989, 52434]
    })
    st.dataframe(comparison_updated, use_container_width=True, hide_index=True)

    # All Associates - Full Normalized View
    st.subheader("Full List – All Associates (Normalized to narossoh)")
    st.markdown("**Pick Report (All at 746 opportunities)**")
    st.dataframe(df_pick_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    st.markdown("**Stow Report (All at 1,068 opportunities)**")
    st.dataframe(df_stow_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "⏰ Narossoh Work Hours & Productivity":
    st.title("⏰ Narossoh Work Hours & Productivity")
    st.markdown("**April 5th – April 11th, 2026** | Work Hours from scanned timesheet")
    
    st.subheader("Raw Work Hours Log")
    st.dataframe(df_hours, use_container_width=True, hide_index=True)
    
    # Daily summary
    daily_hours = df_hours.groupby(["Date", "Day"]).agg({
        "Hours Worked": "sum",
        "Start Time": "first",
        "End Time": "last"
    }).reset_index()
    st.subheader("Hours Worked by Day")
    st.dataframe(daily_hours.style.format({"Hours Worked": "{:.1f}"}), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.subheader("Productivity Metrics (Pick & Stow)")
    
    st.info("""
    **Explanation of Calculations**  
    • Total hours worked by narossoh during the report period = **32.0 hours**  
    • All Pick & Stow opportunities and defects are from the full April 5–12 reports.  
    • Units per hour and defects per hour are calculated as:  
      **Units/Hour = Total Opportunities ÷ Total Hours**  
      **Defects/Hour = Total Defects ÷ Total Hours**  
    Since daily unit-level data is not available, these rates are period-wide averages.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Hours Worked", f"{total_hours:.1f}")
        st.metric("Total Pick Opportunities", total_pick_opp)
        st.metric("Pick Units per Hour", f"{pick_units_per_hour}")
        st.metric("Pick Defects per Hour", f"{pick_defects_per_hour}")
        st.metric("Pick Defect Rate", f"{(total_pick_defects / total_pick_opp * 100):.2f}%")
    
    with col2:
        st.metric("Total Stow Opportunities", total_stow_opp)
        st.metric("Stow Units per Hour", f"{stow_units_per_hour}")
        st.metric("Stow Defects per Hour", f"{stow_defects_per_hour}")
        st.metric("Stow Defect Rate", f"{(total_stow_defects / total_stow_opp * 100):.2f}%")
    
    # Per-day productivity table (using period-wide rates)
    st.subheader("Per-Day Productivity (using period-wide average rates)")
    daily_prod = daily_hours.copy()
    daily_prod["Pick Units/Hour"] = pick_units_per_hour
    daily_prod["Pick Defects/Hour"] = pick_defects_per_hour
    daily_prod["Stow Units/Hour"] = stow_units_per_hour
    daily_prod["Stow Defects/Hour"] = stow_defects_per_hour
    st.dataframe(daily_prod.style.format({
        "Hours Worked": "{:.1f}",
        "Pick Units/Hour": "{:.2f}",
        "Pick Defects/Hour": "{:.2f}",
        "Stow Units/Hour": "{:.2f}",
        "Stow Defects/Hour": "{:.2f}"
    }), use_container_width=True, hide_index=True)

st.caption("Dashboard built for Amazon RSR+ Pick & Stow Analysis • Updated with Narossoh Work Hours")
