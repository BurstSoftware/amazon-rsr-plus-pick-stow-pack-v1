import streamlit as st
import pandas as pd
import altair as alt

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="10% Pick Increase Staffing Calculator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📦 10% Pick Volume Increase — Staffing Impact")
st.markdown("**April 5th – April 12th, 2026** | Amazon RSR+ Warehouse Analysis")

# ====================== KEY DATA ======================
current_pick = 4214
current_stow = 6456
current_total = current_pick + current_stow
num_associates = 17

new_pick = round(current_pick * 1.10, 1)
additional_pick = round(new_pick - current_pick, 1)
new_total_opp = round(new_pick + current_stow, 1)

avg_opp_per_assoc = round(current_total / num_associates, 1)
additional_fte = round(additional_pick / avg_opp_per_assoc, 2)

# ====================== METRICS ======================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Current Pick Opportunities", f"{current_pick:,}")
    st.metric("Current Stow Opportunities", f"{current_stow:,}")

with col2:
    st.metric("Current Total Opportunities", f"{current_total:,}")
    st.metric("Associates", num_associates)

with col3:
    st.metric("New Pick Opportunities (+10%)", f"{new_pick:,}")
    st.metric("Additional Pick Opportunities", f"+{additional_pick:,}")

with col4:
    st.metric("New Total Opportunities", f"{new_total_opp:,}")
    st.metric("Net Workload Increase", f"{((new_total_opp - current_total)/current_total*100):.2f}%")

# ====================== STAFFING RECOMMENDATION ======================
st.markdown("---")
st.header("Staffing Recommendation")

st.success(f"""
**Approximately {additional_fte} additional full-time equivalent (FTE) associates** 
are needed to handle a **10% increase in pick orders**.
""")

st.info(f"""
**Practical Interpretation:**

- This is equivalent to adding **1 new associate** working roughly **⅔ of a full weekly schedule**  
  (or distributing the extra work across the existing team + a partial new hire).

- Average weekly opportunities per associate right now: **{avg_opp_per_assoc}** total  
  (≈ **{round(current_pick/num_associates)}** pick-only).

- **No hours data** is available in the source reports, so this calculation is based purely on opportunity volume.  
  If you provide average hours worked per associate or pick time per opportunity, we can convert this into exact **man-hours**.
""")

# ====================== DETAILED CALCULATION TABLE ======================
st.subheader("Detailed Calculation Breakdown")

calc_data = {
    "Metric": [
        "Current Pick Opportunities",
        "Current Stow Opportunities",
        "Current Total Opportunities",
        "New Pick Opportunities (+10%)",
        "Additional Pick Opportunities",
        "New Total Opportunities",
        "Average Opportunities per Associate",
        "Additional FTE Required"
    ],
    "Value": [
        f"{current_pick:,}",
        f"{current_stow:,}",
        f"{current_total:,}",
        f"{new_pick:,}",
        f"+{additional_pick:,}",
        f"{new_total_opp:,}",
        f"{avg_opp_per_assoc}",
        f"{additional_fte} FTE"
    ]
}

df_calc = pd.DataFrame(calc_data)
st.dataframe(df_calc, use_container_width=True, hide_index=True)

# ====================== VISUALIZATIONS ======================
st.subheader("Workload Comparison")

chart_data = pd.DataFrame({
    "Category": ["Current Total", "New Total (After +10% Pick)"],
    "Opportunities": [current_total, new_total_opp]
})

bar_chart = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X("Category:N", sort=None, title="Scenario"),
    y=alt.Y("Opportunities:Q", title="Total Opportunities"),
    color=alt.Color("Category:N", scale=alt.Scale(range=["#636efa", "#ff7f0e"]))
).properties(height=350)

st.altair_chart(bar_chart, use_container_width=True)

# Pie chart breakdown
st.subheader("Breakdown of the Increase")
pie_data = pd.DataFrame({
    "Type": ["Additional Pick Volume", "Existing Volume"],
    "Opportunities": [additional_pick, current_total]
})

pie_chart = alt.Chart(pie_data).mark_arc(innerRadius=60).encode(
    theta=alt.Theta(field="Opportunities", type="quantitative"),
    color=alt.Color("Type:N", scale=alt.Scale(range=["#ff7f0e", "#636efa"])),
    tooltip=["Type", "Opportunities"]
).properties(height=300)

st.altair_chart(pie_chart, use_container_width=True)

st.caption("Dashboard built with opportunity data from Pick Report and Weekly Spend Report • April 2026")
