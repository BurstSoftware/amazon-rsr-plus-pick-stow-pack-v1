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

# ====================== WEEKLY SPEND DATA ======================
spend_data = {
    "User": ["narossoh", "gpliegom", "stajenni", "iqrayuss", "matstrak", "nkaibrah", "mnimhas", 
             "arrizola", "hasnsai", "uiyps", "mtiband r", "elizev", "danijac", "hersmary", 
             "abdiosmg", "jnoonoor", "musaom"],
    "Pick Opportunities": [746, 362, 804, 37, 186, 255, 97, 614, 214, 208, 68, 176, 169, 69, 44, 110, 55],
    "Stow Opportunities": [1068, 580, 127, 758, 594, 518, 668, 57, 416, 330, 445, 204, 168, 246, 214, 63, 0],
    "Total Opportunities": [1814, 942, 931, 795, 780, 773, 765, 671, 630, 538, 513, 380, 337, 315, 258, 173, 55],
    "% of Total Volume": [17.00, 8.83, 8.73, 7.45, 7.31, 7.24, 7.17, 6.29, 5.90, 5.04, 4.81, 3.56, 3.16, 2.95, 2.42, 1.62, 0.52],
    "Estimated Value": [1624.18, 843.62, 834.06, 711.77, 698.40, 691.71, 685.02, 600.95, 563.69, 481.52, 459.55, 340.12, 301.91, 281.84, 231.21, 154.77, 49.68]
}

df_spend = pd.DataFrame(spend_data)

# === FILL ALL RATIO COLUMNS ===
nar_value_per_hour = 50.75
nar_cost_per_hour = 19.00
nar_hours = 32
nar_total_opp = 1814
nar_equiv = 2.97

# Calculations for ALL associates
df_spend["Value per 32h (Ratio)"] = (df_spend["Estimated Value"] / nar_value_per_hour * nar_hours).round(2)
df_spend["Value per Hour"] = f"${nar_value_per_hour:.2f}"
df_spend["Cost per Hour"] = f"${nar_cost_per_hour:.2f}"
df_spend["Total Weekly Hours Worked"] = (df_spend["Estimated Value"] / nar_value_per_hour).round(1)
df_spend["Equivalent Associates"] = (df_spend["Total Opportunities"] / (nar_total_opp / nar_equiv)).round(2).astype(str) + "×"

# Fix: Format Value per 32h as string for ALL rows (this was causing the error)
df_spend["Value per 32h (Ratio)"] = df_spend["Value per 32h (Ratio)"].apply(lambda x: f"${x:,.2f}")

# Reorder columns
df_spend = df_spend[[
    "User", "Pick Opportunities", "Stow Opportunities", "Total Opportunities",
    "% of Total Volume", "Estimated Value", "Value per 32h (Ratio)",
    "Value per Hour", "Cost per Hour", "Total Weekly Hours Worked", "Equivalent Associates"
]]

# ====================== PACKING DATA ======================
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
if page == "🏠 Home & Summary":
    st.title("📦 Warehouse Pick & Stow Performance Dashboard")
    st.markdown("**April 5th – April 12th, 2026** | Amazon RSR+ Analysis")
    st.info("This dashboard contains both original and normalized Pick & Stow reports.")

elif page == "📦 Pick Report":
    st.title("📦 Pick Report Analysis")
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    with tab1:
        st.subheader("Original Pick Report")
        st.dataframe(df_pick_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    with tab2:
        st.subheader("Updated Pick Report")
        st.dataframe(df_pick_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "📦 Stow Report":
    st.title("📦 Stow Report Analysis")
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    with tab1:
        st.subheader("Original Stow Report")
        st.dataframe(df_stow_orig.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    with tab2:
        st.subheader("Updated Stow Report")
        st.dataframe(df_stow_norm.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)

elif page == "💰 Weekly Spend by Associate":
    st.title("💰 Weekly Spend by Associate")
    st.markdown("**April 5th – April 12th, 2026** | Based on Total Opportunities (Pick + Stow)")

    st.subheader("🔑 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Narrossoh Total Volume", "1,814")
    with col2: st.metric("Team Total Volume", "10,978")
    with col3: st.metric("Narrossoh % of Team", "16.52%")
    with col4: st.metric("Equivalent to Associates", "2.97×")

    total_spend = df_spend["Estimated Value"].sum()
    total_opp = df_spend["Total Opportunities"].sum()

    colA, colB, colC = st.columns(3)
    with colA: st.metric("Total Weekly Spend", f"${total_spend:,.2f}")
    with colB: st.metric("Total Opportunities", f"{total_opp:,}")
    with colC: st.metric("Number of Associates", len(df_spend))

    st.subheader("Full Spending Allocation Table")
    st.dataframe(
        df_spend.style.format({
            "% of Total Volume": "{:.2f}%",
            "Estimated Value": "${:,.2f}",
            "Total Weekly Hours Worked": "{:.1f}"
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

    st.info("All ratio columns are now calculated proportionally based on Total Opportunities.")

# Final caption
st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
