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
# (Your original pick/stow/normalized data remains unchanged)
pick_data = { ... }   # Keep as is
stow_data = { ... }
df_pick_orig = pd.DataFrame(pick_data)
df_stow_orig = pd.DataFrame(stow_data)

# Normalized data...
# (Keep your existing pick_norm_data and stow_norm_data)

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

# === FILL ALL RATIO COLUMNS BASED ON UNITS ===
df_spend = df_spend.rename(columns={"Estimated Spend": "Estimated Value"} if "Estimated Spend" in df_spend.columns else {})

nar_value_per_hour = 50.75
nar_cost_per_hour = 19.00
nar_hours = 32
nar_total_opp = 1814
nar_equiv = 2.97

# Calculations for all associates
df_spend["Value per 32h (Ratio)"] = (df_spend["Estimated Value"] / nar_value_per_hour * nar_hours).round(2)
df_spend["Value per Hour"] = f"${nar_value_per_hour:.2f}"
df_spend["Cost per Hour"] = f"${nar_cost_per_hour:.2f}"
df_spend["Total Weekly Hours Worked"] = (df_spend["Estimated Value"] / nar_value_per_hour).round(1)
df_spend["Equivalent Associates"] = (df_spend["Total Opportunities"] / (nar_total_opp / nar_equiv)).round(2).astype(str) + "×"

# Format narossoh's Value per 32h as currency string
df_spend.loc[df_spend["User"] == "narossoh", "Value per 32h (Ratio)"] = df_spend.loc[df_spend["User"] == "narossoh", "Value per 32h (Ratio)"].apply(lambda x: f"${x:,.2f}")

# Reorder columns
df_spend = df_spend[[
    "User", 
    "Pick Opportunities", 
    "Stow Opportunities", 
    "Total Opportunities",
    "% of Total Volume", 
    "Estimated Value", 
    "Value per 32h (Ratio)",
    "Value per Hour",
    "Cost per Hour",
    "Total Weekly Hours Worked",
    "Equivalent Associates"
]]

# ====================== SIDEBAR & PAGES ======================
# (Keep your existing sidebar and other pages unchanged)

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
            "Value per 32h (Ratio)": "${:,.2f}",
            "Total Weekly Hours Worked": "{:.1f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    # Chart remains the same
    st.subheader("Spending Distribution (Top 10 Associates)")
    chart_data = df_spend.nlargest(10, "Estimated Value")
    spend_chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X("User:N", sort="-y", title="Associate"),
        y=alt.Y("Estimated Value:Q", title="Estimated Value ($)"),
        tooltip=["User", "Total Opportunities", "% of Total Volume", "Estimated Value"]
    ).properties(height=400)
    st.altair_chart(spend_chart, use_container_width=True)

    st.info("All ratio columns are now calculated based on Total Opportunities (units) and narossoh’s benchmark rates.")

# Final caption
st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
