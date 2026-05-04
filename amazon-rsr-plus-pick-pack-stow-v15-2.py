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

# Normalized Data (unchanged)
pick_norm_data = { ... }   # (keeping your original normalized data)
stow_norm_data = { ... }   # (keeping your original normalized data)

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

# ====================== WEEKLY SPEND DATA (UPDATED) ======================
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

# === APPLIED UPDATES ===
df_spend = df_spend.rename(columns={"Estimated Spend": "Estimated Value"})

# Add ratio column - only for narossoh based on 32 hours
df_spend["Value per 32h (Ratio)"] = ""
narossoh_mask = df_spend["User"] == "narossoh"
if narossoh_mask.any():
    nar_value = df_spend.loc[narossoh_mask, "Estimated Value"].iloc[0]
    df_spend.loc[narossoh_mask, "Value per 32h (Ratio)"] = f"${nar_value:,.2f}"

# Reorder columns for better table display
df_spend = df_spend[[
    "User", "Pick Opportunities", "Stow Opportunities", "Total Opportunities",
    "% of Total Volume", "Estimated Value", "Value per 32h (Ratio)"
]]

# ====================== NAROSSOH PACKING DATA ======================
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
     "👥 3-Associate Comparison",
     "⏰ Associate Work Hours & Productivity",
     "📊 Team Overview",
     "💰 Payroll Overview",
     "💰 Weekly Spend by Associate",
     "⏱️ Narossoh Packing Time Calculator"])

# ====================== MAIN PAGES ======================
# ... (All other pages remain unchanged) ...

elif page == "💰 Weekly Spend by Associate":
    st.title("💰 Weekly Spend by Associate")
    st.markdown("**April 5th – April 12th, 2026** | Based on Total Opportunities (Pick + Stow)")

    total_spend = df_spend["Estimated Value"].sum()
    total_opp = df_spend["Total Opportunities"].sum()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Weekly Spend", f"${total_spend:,.2f}")
    with col2:
        st.metric("Total Opportunities", f"{total_opp:,}")
    with col3:
        st.metric("Number of Associates", len(df_spend))

    st.subheader("Full Spending Allocation Table")
    st.dataframe(
        df_spend.style.format({
            "% of Total Volume": "{:.2f}%",
            "Estimated Value": "${:,.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Spending Distribution (Top 10 Associates)")
    chart_data = df_spend.nlargest(10, "Estimated Value")

    spend_chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X("User:N", sort="-y", title="Associate"),
        y=alt.Y("Estimated Value:Q", title="Estimated Value ($)"),
        tooltip=["User", "Total Opportunities", "% of Total Volume", "Estimated Value"]
    ).properties(height=400)

    st.altair_chart(spend_chart, use_container_width=True)

    st.info("""
    **Updates Applied:**
    - Column **Estimated Spend** renamed to **Estimated Value**
    - New column **Value per 32h (Ratio)** added — only **narossoh** shows his full value (based on 32 hours). All other associates are blank.
    """)

# Final caption
st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
