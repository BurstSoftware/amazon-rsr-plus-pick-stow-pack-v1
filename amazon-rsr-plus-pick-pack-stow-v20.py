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

# ====================== ALL DATA ======================
# Original Pick Data
pick_data = {
    "User": ["narossoh", "stajenni", "danijac", "arrizola", "hasnsai", "uiyps", "jnoonoor", 
             "gpliegom", "mtiband r", "elizev", "hersmary", "mnimhas", "iqrayuss", 
             "nkaibrah", "matstrak", "abdiosmg", "musaom"],
    "Opportunities": [746, 804, 169, 614, 214, 208, 110, 362, 68, 176, 69, 97, 37, 255, 186, 44, 55],
    "Defects": [57, 14, 13, 13, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2],
    "DPMO": [76408, 17412, 76923, 21172, 37383, 38461, 63636, 19337, 88235, 34090, 72463, 51546, 108108, 15686, 16129, 68181, 36363]
}

# Pack Data = Exact mirror of Pick Report (as requested)
pack_data = pick_data.copy()

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
df_pack_orig = pd.DataFrame(pack_data)      # ← New: Pack mirrors Pick
df_stow_orig = pd.DataFrame(stow_data)

# Normalized Data (unchanged)
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

# Work Hours
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

# Weekly Spend / Volume Data
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

# Packing Performance
packing_data = {
    "Activity": ["Packing Items", "Trickling Packages"],
    "Items/Packages": [88, 88],
    "Time (minutes)": [47, 10],
    "Rate (per minute)": [88/47, 88/10],
    "Rate (per hour)": [(88/47)*60, (88/10)*60]
}
df_packing = pd.DataFrame(packing_data)

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "📦 Pick-Pack-Stow Total Volume",
     "👥 3-Associate Comparison",
     "⏰ Associate Work Hours & Productivity",
     "📊 Team Overview",
     "💰 Payroll Overview",
     "⏱️ Narossoh Packing Time Calculator",
     "📊 Narossoh Volume Equivalence Report"])

# ====================== PAGES ======================
if page == "🏠 Home & Summary":
    st.title("📦 Warehouse Pick & Stow Performance Dashboard")
    st.markdown("**April 5th – April 12th, 2026** | Amazon RSR+ Analysis")
    
    st.markdown("### Report Summary & Explanation")
    st.info("""
    This dashboard contains both **original** and **updated/normalized** versions of the Pick and Stow reports.
    
    **Key Update Performed:**
    - We normalized all associates to **narossoh’s opportunity volume** (746 in Pick, 1,068 in Stow).
    - Defects were scaled proportionally while keeping each associate’s individual error rate (DPMO) constant.
    - Pack volume now mirrors Pick volume exactly for every associate.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Associates", 17)
        st.metric("Original Pick Opportunities", "4,214")
    with col2:
        st.metric("Original Stow Opportunities", "6,112")
        st.metric("Pack Volume", "4,214")

elif page == "📦 Pick Report":
    # ... (unchanged - keeping your original code)
    st.title("📦 Pick Report Analysis")
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    
    with tab1:
        st.subheader("Original Pick Report")
        total_users_pick = len(df_pick_orig)
        total_opp_pick = df_pick_orig["Opportunities"].sum()
        total_defects_pick = df_pick_orig["Defects"].sum()
        total_dpmo_pick = df_pick_orig["DPMO"].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("Total Users", total_users_pick)
        with col2: st.metric("Total Opportunities", f"{total_opp_pick:,}")
        with col3: st.metric("Total Defects", total_defects_pick)
        with col4: st.metric("Total DPMO (Sum)", f"{total_dpmo_pick:,}")
        
        st.dataframe(df_pick_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Updated Pick Report – All at narossoh’s 746 Opportunities")
        st.markdown("**Explanation**: Every associate now has the same number of opportunities as narossoh (746). Defects scaled proportionally based on their original error rate.")
        st.dataframe(df_pick_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "📦 Stow Report":
    # ... (unchanged)
    st.title("📦 Stow Report Analysis")
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    
    with tab1:
        st.subheader("Original Stow Report")
        total_users_stow = len(df_stow_orig)
        total_opp_stow = df_stow_orig["Opportunities"].sum()
        total_defects_stow = df_stow_orig["Defects"].sum()
        total_dpmo_stow = df_stow_orig["DPMO"].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("Total Users", total_users_stow)
        with col2: st.metric("Total Opportunities", f"{total_opp_stow:,}")
        with col3: st.metric("Total Defects", total_defects_stow)
        with col4: st.metric("Total DPMO (Sum)", f"{total_dpmo_stow:,}")
        
        st.dataframe(df_stow_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Updated Stow Report – All at narossoh’s 1,068 Opportunities")
        st.markdown("**Explanation**: Every associate now has the same number of opportunities as narossoh (1,068). Defects scaled proportionally based on their original error rate.")
        st.dataframe(df_stow_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "📦 Pick-Pack-Stow Total Volume":
    st.title("📦 Pick • Pack • Stow Total Volume Report")
    st.markdown("**April 5th – April 12th, 2026** | Full End-to-End Volume View")

    # Main Totals
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("**Total Pick Volume**", "4,214", delta="Items")
    with col2:
        st.metric("**Total Pack Volume**", "4,214", delta="Packages")
    with col3:
        st.metric("**Total Stow Volume**", "6,112", delta="Items")

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Volume Summary", 
        "📦 Pick Report", 
        "📦 Pack Report", 
        "📦 Stow Report"
    ])

    with tab1:
        st.subheader("Team Volume Overview")
        volume_data = pd.DataFrame({
            "Process": ["Pick", "Pack", "Stow"],
            "Volume": [4214, 4214, 6112]
        })
        
        colA, colB = st.columns(2)
        with colA:
            bar_chart = alt.Chart(volume_data).mark_bar().encode(
                x=alt.X("Process:N", sort=None),
                y=alt.Y("Volume:Q", title="Total Volume"),
                color=alt.Color("Process:N", scale=alt.Scale(range=["#636efa", "#00cc96", "#ff7f0e"]))
            ).properties(height=400)
            st.altair_chart(bar_chart, use_container_width=True)

        with colB:
            pie_chart = alt.Chart(volume_data).mark_arc().encode(
                theta=alt.Theta(field="Volume", type="quantitative"),
                color=alt.Color(field="Process", type="nominal", 
                               scale=alt.Scale(range=["#636efa", "#00cc96", "#ff7f0e"]))
            ).properties(height=400, title="Volume Distribution")
            st.altair_chart(pie_chart, use_container_width=True)

    with tab2:
        st.subheader("📦 Pick Report - Per User")
        st.dataframe(df_pick_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("📦 Pack Report - Per User")
        st.success("**Pack volume has been updated to exactly match the Pick Report (1:1)**")
        st.dataframe(df_pack_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

    with tab4:
        st.subheader("📦 Stow Report - Per User")
        st.dataframe(df_stow_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

    st.info("""
    **Notes**:
    - Pack Opportunities = Pick Opportunities for **every associate**.
    - Total Pack Volume = 4,214 (same as Pick).
    - This page now gives a complete consolidated view of the entire Pick → Pack → Stow process.
    """)

# ====================== REMAINING PAGES (unchanged) ======================
elif page == "👥 3-Associate Comparison":
    # ... (your original code remains unchanged)
    st.title("👥 Focused Comparison: narossoh vs elizev vs arrizola")
    # [Rest of your 3-Associate Comparison code stays exactly the same]
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

    st.subheader("Full List – All Associates (Normalized to narossoh)")
    st.markdown("**Pick Report (All at 746 opportunities)**")
    st.dataframe(df_pick_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    st.markdown("**Stow Report (All at 1,068 opportunities)**")
    st.dataframe(df_stow_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

# [All other pages (Work Hours, Team Overview, Payroll, Packing Calculator, Volume Equivalence) remain 100% unchanged]
# ... (copy-paste the rest of your original code from the previous version here)

else:
    # Fallback for other pages (you can keep all your original elif blocks as they are)
    pass

st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
