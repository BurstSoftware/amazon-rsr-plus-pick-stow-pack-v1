import streamlit as st
import pandas as pd

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pick & Stow Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CORE DATA (Pick & Stow) ======================
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
pick_norm_data = { ... }   # (keep the same normalized data as before - omitted for brevity)
stow_norm_data = { ... }   # (keep the same normalized data as before)

df_pick_norm = pd.DataFrame(pick_norm_data)
df_stow_norm = pd.DataFrame(stow_norm_data)

# ====================== WORK HOURS DATA ======================
# Only narossoh has hours data for now. Others will show "No data available"
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

# All users list for filter
all_users = sorted(df_pick_orig["User"].unique())

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "👥 3-Associate Comparison",
     "⏰ Associate Work Hours & Productivity"])

# ====================== PAGES ======================
if page == "🏠 Home & Summary":
    # ... (keep unchanged)

elif page == "📦 Pick Report":
    # ... (keep unchanged)

elif page == "📦 Stow Report":
    # ... (keep unchanged)

elif page == "👥 3-Associate Comparison":
    # ... (keep unchanged)

elif page == "⏰ Associate Work Hours & Productivity":
    st.title("⏰ Associate Work Hours & Productivity")
    st.markdown("**April 5th – April 12th, 2026**")

    # User Filter
    selected_user = st.selectbox("Select Associate", options=all_users, index=all_users.index("narossoh"))

    st.subheader(f"Work Hours & Productivity for **{selected_user}**")

    # Filter hours data for selected user
    user_hours = df_hours[df_hours["User"] == selected_user]

    if user_hours.empty:
        st.warning(f"No work hours data available for **{selected_user}** yet.")
        st.info("Currently, detailed work hours are only loaded for **narossoh**. Other associates will be added as data becomes available.")
    else:
        st.subheader("Raw Work Hours Log")
        st.dataframe(user_hours[["Date", "Day", "Start Time", "End Time", "Hours Worked"]], 
                     use_container_width=True, hide_index=True)

        # Daily summary
        daily_hours = user_hours.groupby(["Date", "Day"]).agg({
            "Hours Worked": "sum",
            "Start Time": "first",
            "End Time": "last"
        }).reset_index()

        st.subheader("Hours Worked by Day")
        st.dataframe(daily_hours.style.format({"Hours Worked": "{:.1f}"}), 
                     use_container_width=True, hide_index=True)

        # Productivity Calculations
        total_hours = user_hours["Hours Worked"].sum()

        # Get pick & stow data for the user
        user_pick = df_pick_orig[df_pick_orig["User"] == selected_user].iloc[0]
        user_stow = df_stow_orig[df_stow_orig["User"] == selected_user].iloc[0] if selected_user in df_stow_orig["User"].values else None

        if user_pick is not None:
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
                st.metric("Pick Defect Rate", f"{(pick_def / pick_opp * 100):.2f}%" if pick_opp > 0 else "N/A")

            with col2:
                if user_stow is not None:
                    stow_opp = user_stow["Opportunities"]
                    stow_def = user_stow["Defects"]
                    stow_per_hour = round(stow_opp / total_hours, 2) if total_hours > 0 else 0
                    stow_def_per_hour = round(stow_def / total_hours, 2) if total_hours > 0 else 0

                    st.metric("Total Stow Opportunities", int(stow_opp))
                    st.metric("Stow Units per Hour", f"{stow_per_hour}")
                    st.metric("Stow Defects per Hour", f"{stow_def_per_hour}")
                    st.metric("Stow Defect Rate", f"{(stow_def / stow_opp * 100):.2f}%" if stow_opp > 0 else "N/A")
                else:
                    st.info("No Stow data available for this associate.")

            # Per-day productivity (using average rates)
            st.subheader("Per-Day Productivity (Average Rates)")
            daily_prod = daily_hours.copy()
            daily_prod["Pick Units/Hour"] = pick_per_hour
            daily_prod["Pick Defects/Hour"] = pick_def_per_hour
            if user_stow is not None:
                daily_prod["Stow Units/Hour"] = stow_per_hour
                daily_prod["Stow Defects/Hour"] = stow_def_per_hour

            st.dataframe(daily_prod.style.format({
                "Hours Worked": "{:.1f}",
                "Pick Units/Hour": "{:.2f}",
                "Pick Defects/Hour": "{:.2f}",
                "Stow Units/Hour": "{:.2f}",
                "Stow Defects/Hour": "{:.2f}"
            }), use_container_width=True, hide_index=True)

st.caption("Dashboard built for Amazon RSR+ Pick & Stow Analysis")
