import streamlit as st
import pandas as pd
import altair as alt

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="10% Pick Increase Staffing & Cost Calculator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📦 10% Pick Volume Increase — Staffing & Production Cost Impact")
st.markdown("**April 5th – April 12th, 2026** | Amazon RSR+ Warehouse Analysis")

# ====================== KEY DATA FROM IMAGE ======================
current_pick = 4214
current_stow = 6456
current_total = current_pick + current_stow
num_associates = 17

# Weekly spend data directly from the uploaded image
spend_data = {
    "User": ["narossoh", "gpliegom", "stajenni", "iqrayuss", "matstrak", "nkaibrah", "mnimhas", 
             "arrizola", "hasnsai", "uiyps", "mtiband r", "elizev", "danijac", "hersmary", 
             "abdiosmg", "jnoonoor", "musaom"],
    "Pick Opportunities": [746, 362, 804, 37, 186, 255, 97, 614, 214, 208, 68, 176, 169, 69, 44, 110, 55],
    "Stow Opportunities": [1068, 580, 127, 758, 594, 518, 668, 57, 416, 330, 445, 204, 168, 246, 214, 63, 0],
    "Total Opportunities": [1814, 942, 931, 795, 780, 773, 765, 671, 630, 538, 513, 380, 337, 315, 258, 173, 55],
    "% of Total Volume": [17.00, 8.83, 8.73, 7.45, 7.31, 7.24, 7.17, 6.29, 5.90, 5.04, 4.81, 3.56, 3.16, 2.95, 2.42, 1.62, 0.52],
    "Estimated Spend": [1624.18, 843.62, 834.06, 711.77, 698.40, 691.71, 685.02, 600.95, 563.69, 481.52, 459.55, 340.12, 301.91, 281.84, 231.21, 154.77, 49.68]
}

df_spend = pd.DataFrame(spend_data)
total_spend = df_spend["Estimated Spend"].sum()          # $9,554.00
cost_per_opportunity = total_spend / current_total        # ≈ $0.8957 (same for every associate)

# ====================== 10% PICK INCREASE CALCULATION ======================
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
- Equivalent to **1 new associate** working roughly **⅔ of a full weekly schedule**.
- Average weekly opportunities per associate: **{avg_opp_per_assoc}** total (≈ **{round(current_pick/num_associates)}** pick-only).
""")

# ====================== PRODUCTION COST ANALYSIS ======================
st.markdown("---")
st.header("💰 Production Cost per Opportunity (from Image)")

st.metric("**Cost per Opportunity** (Pick or Stow)", f"${cost_per_opportunity:.4f}", 
          help="Calculated as Total Estimated Spend ÷ Total Opportunities. This rate is identical for every associate.")

st.caption("The image shows **$9,554.00** total weekly spend allocated purely by opportunity volume — therefore the cost per opportunity is constant across all 17 associates.")

# ====================== 10% INTERVAL COST IMPACT TABLE ======================
st.subheader("Cost Impact at 10% Pick Increase Intervals (Team Level)")

percentages = list(range(10, 110, 10))
impact_data = []

for pct in percentages:
    new_pick_vol = current_pick * (1 + pct / 100)
    add_pick_vol = new_pick_vol - current_pick
    new_total_vol = new_pick_vol + current_stow
    add_total_vol = new_total_vol - current_total
    add_cost = round(add_total_vol * cost_per_opportunity, 2)
    new_total_cost = round(total_spend + add_cost, 2)
    
    impact_data.append({
        "% Pick Increase": f"+{pct}%",
        "New Pick Opportunities": round(new_pick_vol, 1),
        "Additional Pick Opportunities": round(add_pick_vol, 1),
        "New Total Opportunities": round(new_total_vol, 1),
        "Additional Cost": f"${add_cost:,.2f}",
        "New Total Weekly Spend": f"${new_total_cost:,.2f}"
    })

df_impact = pd.DataFrame(impact_data)
st.dataframe(
    df_impact.style.format({
        "New Pick Opportunities": "{:,.1f}",
        "Additional Pick Opportunities": "{:,.1f}",
        "New Total Opportunities": "{:,.1f}"
    }),
    use_container_width=True,
    hide_index=True
)

# ====================== COST VISUALIZATION ======================
st.subheader("Additional Weekly Spend vs Pick Volume Increase")

chart_data = pd.DataFrame({
    "% Pick Increase": [f"+{p}%" for p in percentages],
    "Additional Spend ($)": [float(row["Additional Cost"].replace("$", "").replace(",", "")) for row in impact_data]
})

cost_chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X("% Pick Increase:N", title="Pick Volume Increase"),
    y=alt.Y("Additional Spend ($):Q", title="Additional Weekly Spend ($)"),
    tooltip=["% Pick Increase", "Additional Spend ($)"]
).properties(height=400)

st.altair_chart(cost_chart, use_container_width=True)

st.info("""
**Key Insights:**
- Every 10% increase in pick opportunities adds **≈ $421** in weekly production cost (because stow volume stays constant).
- The cost is driven purely by **total opportunities** (Pick + Stow), as shown in the uploaded image.
- At +50% pick volume the team would need **≈ $2,107** more per week.
""")

st.caption("Dashboard built from the uploaded “spend per week on 17 associates” image • April 2026")
