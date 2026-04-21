import streamlit as st
import pandas as pd
import plotly.express as px   # ← This line is now safely included

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

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "👥 3-Associate Comparison",
     "⏰ Associate Work Hours & Productivity",
     "📊 Team Overview"])

# ====================== MAIN PAGES ======================
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

elif page == "📦 Pick Report":
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

    st.subheader("Full List – All Associates (Normalized to narossoh)")
    st.markdown("**Pick Report (All at 746 opportunities)**")
    st.dataframe(df_pick_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    st.markdown("**Stow Report (All at 1,068 opportunities)**")
    st.dataframe(df_stow_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "⏰ Associate Work Hours & Productivity":
    st.title("⏰ Associate Work Hours & Productivity")
    st.markdown("**April 5th – April 12th, 2026**")

    selected_user = st.selectbox("Select Associate", options=all_users, index=all_users.index("narossoh"))

    st.subheader(f"Work Hours & Productivity for **{selected_user}**")

    user_hours = df_hours[df_hours["User"] == selected_user]

    if user_hours.empty:
        st.warning(f"No work hours data available for **{selected_user}** yet.")
        st.info("Currently, detailed work hours are only available for **narossoh**. Other associates will be added later.")
    else:
        st.subheader("Raw Work Hours Log")
        st.dataframe(user_hours[["Date", "Day", "Start Time", "End Time", "Hours Worked"]], 
                     use_container_width=True, hide_index=True)

        daily_hours = user_hours.groupby(["Date", "Day"]).agg({
            "Hours Worked": "sum",
            "Start Time": "first",
            "End Time": "last"
        }).reset_index()

        st.subheader("Hours Worked by Day")
        st.dataframe(daily_hours.style.format({"Hours Worked": "{:.1f}"}), 
                     use_container_width=True, hide_index=True)

        total_hours = user_hours["Hours Worked"].sum()

        user_pick_row = df_pick_orig[df_pick_orig["User"] == selected_user]
        user_stow_row = df_stow_orig[df_stow_orig["User"] == selected_user]

        if not user_pick_row.empty:
            user_pick = user_pick_row.iloc[0]
            pick_opp = user_pick["Opportunities"]
            pick_def = user_pick["Defects"]
            pick_per_hour = round(pick_opp / total_hours, 2) if total_hours > 0 else 0
            pick_def_per_hour = round(pick_def / total_hours, 2) if total_hours > 0 else 0

            st.markdown("---")
            st.subheader("Productivity Metrics")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Total Hours Worked", f"{total_hours:.1f}")
                st.metric("Total Pick Opportunities", int(pick_opp))
                st.metric("Pick Units per Hour", f"{pick_per_hour}")
                st.metric("Pick Defects per Hour", f"{pick_def_per_hour}")
                st.metric("Pick Defect Rate (%)", f"{(pick_def / pick_opp * 100):.2f}" if pick_opp > 0 else "N/A")

            with col2:
                if not user_stow_row.empty:
                    user_stow = user_stow_row.iloc[0]
                    stow_opp = user_stow["Opportunities"]
                    stow_def = user_stow["Defects"]
                    stow_per_hour = round(stow_opp / total_hours, 2) if total_hours > 0 else 0
                    stow_def_per_hour = round(stow_def / total_hours, 2) if total_hours > 0 else 0

                    st.metric("Total Stow Opportunities", int(stow_opp))
                    st.metric("Stow Units per Hour", f"{stow_per_hour}")
                    st.metric("Stow Defects per Hour", f"{stow_def_per_hour}")
                    st.metric("Stow Defect Rate (%)", f"{(stow_def / stow_opp * 100):.2f}" if stow_opp > 0 else "N/A")

            st.subheader("Per-Day Productivity (Average Rates)")
            daily_prod = daily_hours.copy()
            daily_prod["Pick Units/Hour"] = pick_per_hour
            daily_prod["Pick Defects/Hour"] = pick_def_per_hour
            if not user_stow_row.empty:
                daily_prod["Stow Units/Hour"] = stow_per_hour
                daily_prod["Stow Defects/Hour"] = stow_def_per_hour

            st.dataframe(daily_prod.style.format({
                "Hours Worked": "{:.1f}",
                "Pick Units/Hour": "{:.2f}",
                "Pick Defects/Hour": "{:.2f}",
                "Stow Units/Hour": "{:.2f}",
                "Stow Defects/Hour": "{:.2f}"
            }), use_container_width=True, hide_index=True)

# ====================== TEAM OVERVIEW PAGE ======================
elif page == "📊 Team Overview":
    st.title("📊 Team Overview")
    st.markdown("**Pick & Stow Performance** | **April 5th – April 12th, 2026**")

    # Team Summary
    st.subheader("Team Summary")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Managers", "5")
    with c2:
        st.metric("Associates", "14")
    with c3:
        st.metric("Total Picked", "4,214")
    with c4:
        st.metric("Total Stowed", "6,112")

    st.markdown("---")

    # Narossoh Productivity Metrics
    st.subheader("Narrossoh Average Productivity")
    st.caption("Calculated from Narossoh’s total opportunities/defects over the reporting period")

    colA, colB = st.columns(2)

    with colA:
        st.metric("Total Pick Opportunities", "746")
        st.metric("Pick Units per Hour", "23.31")
        st.metric("Pick Defects per Hour", "1.78")
        st.metric("Pick Defect Rate", "7.64%")

    with colB:
        st.metric("Total Stow Opportunities", "1,068")
        st.metric("Stow Units per Hour", "33.38")
        st.metric("Stow Defects per Hour", "5.12")
        st.metric("Stow Defect Rate", "15.36%")

    # Pie Charts for Narossoh Productivity
    st.subheader("Narrossoh Productivity Breakdown (Opportunities vs Defects)")

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.markdown("**Pick Productivity**")
        pick_good = 746 - 57
        pick_fig = px.pie(
            names=["Good Units", "Defects"],
            values=[pick_good, 57],
            title="Pick: 746 Opportunities",
            color_discrete_sequence=["#00cc96", "#ef553b"]
        )
        st.plotly_chart(pick_fig, use_container_width=True)

    with col_chart2:
        st.markdown("**Stow Productivity**")
        stow_good = 1068 - 164
        stow_fig = px.pie(
            names=["Good Units", "Defects"],
            values=[stow_good, 164],
            title="Stow: 1,068 Opportunities",
            color_discrete_sequence=["#00cc96", "#ef553b"]
        )
        st.plotly_chart(stow_fig, use_container_width=True)

    st.info("""
    **Note**: 
    - Pick and Stow totals (4,214 picked / 6,112 stowed) represent the **entire team's** volume.
    - Pie charts show Narossoh’s individual performance (Good Units vs Defects).
    """)

st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
