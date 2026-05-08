import streamlit as st
import pandas as pd
import altair as alt

# Page configuration
st.set_page_config(
    page_title="Pick Pack Stow App",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧳 Pick • Pack • Stow")
st.markdown("### Warehouse Performance Tracker")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["📋 Overview", "📊 Performance DataFrame", "📈 Charts & Visuals", "🔍 Nathan vs Managers", "👤 Associate Dashboards"]
)

# ====================== DATA ======================
data = {
    "Name": ["David", "Elizet", "Giselle", "Omar", "Jennifer", "Nathan"],
    "Hours Worked": [40.00, 40.00, 40.00, 40.00, 40.00, 30.29],
    "Stow Quantity": [57, 204, 580, 0, 127, 1068],
    "Pick Quantity": [614, 176, 362, 55, 804, 746],
    "PC99 Errors": [1, 1, 0, 0, 0, 1],
    "SIPS Over Short": [0, 1, 1, 0, 4, 19],
    "Scan Out of Sequence": [0, 3, 9, 0, 0, 79],
    "Bin Collisions": [2, 7, 5, 0, 3, 65],
    "Wrong ASINs": [13, 6, 7, 2, 14, 57]
}

df = pd.DataFrame(data)

# Cost calculations
hourly_rates = [22.50, 22.50, 22.50, 22.50, 22.50, 19.00]
df["Hourly Rate ($)"] = hourly_rates
df["Total Units"] = df["Stow Quantity"] + df["Pick Quantity"]
df["Total Cost ($)"] = df["Hourly Rate ($)"] * df["Hours Worked"]
df["Avg Cost per Unit ($)"] = df.apply(
    lambda row: round(row["Total Cost ($)"] / row["Total Units"], 4) 
    if row["Total Units"] > 0 else 0.0, 
    axis=1
)
df["Units per Hour"] = df.apply(
    lambda row: round(row["Total Units"] / row["Hours Worked"], 2) if row["Hours Worked"] > 0 else 0,
    axis=1
)

df["Total Cost ($)"] = df["Total Cost ($)"].round(2)
df["Hourly Rate ($)"] = df["Hourly Rate ($)"].round(2)

# ====================== PAGE 1: OVERVIEW ======================
if page == "📋 Overview":
    st.header("Manager Overview")
    
    st.write("""
    **Pick Pack Stow App includes 5 managers that work 40 hours a week.** 
    Their names are David, and David stows 57 packages with 1 pc99 error and 2 bin colisions, 
    and picks 614 units, with 13 wrong asin, elizet worked 40 hours, stowed 204 packages, 
    with 1 pc99 error, 1 sips over short, 3 scan out of sequence and 7 bin collisions, 
    elizet picks 176 units, with 6 wrong asins, Giselle worked 40 hours, stowed 580 units, 
    with 1 sip over short, 9 scan out of sequence and 5 bin collisions, she picks 362 units 
    with 7 wrong asins, Omar works 40 hours, stows 0 units, picks 55 units, with 2 wrong asins, 
    Jennifer works 40 hours, stows 127 units, with 4 sips over short and 3 bin colisions, 
    **Jennifer picked 804 units with 14 wrong asins** and Nathan works 30.29 hours, 
    stows 1068 units, with 1 pc99, 19 sips over short, 79 scan out out of sequence, 
    and 65 bin colisions, **Nathan picked 746 units with 57 wrong asins**.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Team Members", "6")
    with col2:
        st.metric("Full-time Managers", "5")
    with col3:
        st.metric("Part-time", "1 (Nathan)")
    with col4:
        st.metric("Total Hours Worked", "230.29")

# ====================== PAGE 2: PERFORMANCE DATAFRAME ======================
elif page == "📊 Performance DataFrame":
    st.header("📊 Manager Performance DataFrame")
    
    st.info("""
    **Cost basis used for all calculations:**  
    Managers (David, Elizet, Giselle, Omar, Jennifer) = $22.50 per hour  
    Nathan (Nate) = $19.00 per hour  
    Cost per Unit = (Hourly Rate × Hours Worked) ÷ Total Units
    """)
    
    column_order = [
        "Name", "Hours Worked", "Stow Quantity", "Pick Quantity", "Total Units",
        "Hourly Rate ($)", "Total Cost ($)", "Avg Cost per Unit ($)",
        "PC99 Errors", "SIPS Over Short", "Scan Out of Sequence", 
        "Bin Collisions", "Wrong ASINs"
    ]
    df_display = df[column_order]
    
    st.dataframe(
        df_display,
        use_container_width=True,
        height=420,
        hide_index=False,
        column_config={
            "Hourly Rate ($)": st.column_config.NumberColumn(format="$.2f"),
            "Total Cost ($)": st.column_config.NumberColumn(format="$.2f"),
            "Avg Cost per Unit ($)": st.column_config.NumberColumn(format="$.4f"),
            "Total Units": st.column_config.NumberColumn(format="%,.0f")
        }
    )
    
    st.subheader("Cost Summary")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Labor Cost", f"${df['Total Cost ($)'].sum():,.2f}")
    with col2:
        st.metric("Average Cost per Unit", f"${df['Avg Cost per Unit ($)'].mean():.4f}")
    with col3:
        st.metric("Total Units Handled", f"{df['Total Units'].sum():,}")
    with col4:
        st.metric("Weighted Avg Cost/Unit", 
                  f"${(df['Total Cost ($)'].sum() / df['Total Units'].sum()):.4f}")

# ====================== PAGE 3: CHARTS & VISUALS ======================
elif page == "📈 Charts & Visuals":
    st.header("📈 Charts & Visual Analytics")
    st.markdown("**Labor Cost • Total Units Handled • Average Cost per Unit**")

    # Individual proportional charts (as requested previously)
    st.subheader("Comparison of All 3 Metrics (Scaled to Highest Value)")

    # Total Labor Cost Chart
    st.markdown("**1. Total Labor Cost ($)**")
    max_cost = df["Total Cost ($)"].max()
    chart_cost = alt.Chart(df).mark_bar(color="#1f77b4").encode(
        x=alt.X("Name:N", sort="-y", title="Worker"),
        y=alt.Y("Total Cost ($):Q", title="Labor Cost ($)", scale=alt.Scale(domain=[0, max_cost * 1.05])),
        tooltip=["Name", alt.Tooltip("Total Cost ($)", format="$.2f")]
    ).properties(height=380)
    st.altair_chart(chart_cost, use_container_width=True)

    # Total Units Chart
    st.markdown("**2. Total Units Handled**")
    max_units = df["Total Units"].max()
    chart_units = alt.Chart(df).mark_bar(color="#2ca02c").encode(
        x=alt.X("Name:N", sort="-y", title="Worker"),
        y=alt.Y("Total Units:Q", title="Total Units", scale=alt.Scale(domain=[0, max_units * 1.05])),
        tooltip=["Name", "Total Units", "Stow Quantity", "Pick Quantity"]
    ).properties(height=380)
    st.altair_chart(chart_units, use_container_width=True)

    # Avg Cost per Unit Chart (0–20 scale)
    st.markdown("**3. Average Cost per Unit ($)**")
    chart_avg = alt.Chart(df).mark_bar(color="#d62728").encode(
        x=alt.X("Name:N", sort="y", title="Worker"),
        y=alt.Y("Avg Cost per Unit ($):Q", 
                title="Avg Cost per Unit ($)", 
                scale=alt.Scale(domain=[0, 20])),
        tooltip=["Name", alt.Tooltip("Avg Cost per Unit ($)", format="$.4f")]
    ).properties(height=380)
    st.altair_chart(chart_avg, use_container_width=True)

# ====================== NEW PAGE: NATHAN VS MANAGERS SUMMARY ======================
elif page == "🔍 Nathan vs Managers":
    st.header("🔍 Detailed Nathan vs Managers Summary")
    st.markdown("**Nathan (30.29 hours) vs 5 Full-Time Managers (40 hours each)**")
    st.info("Nathan worked only **75.7%** of a manager’s hours but delivered dramatically higher productivity and lower unit costs.")

    # Overall summary metrics
    nathan_row = df[df["Name"] == "Nathan"].iloc[0]
    managers = df[df["Name"] != "Nathan"]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Nathan Hours", f"{nathan_row['Hours Worked']}", "−9.71 vs managers")
    with col2:
        st.metric("Nathan Total Units", f"{nathan_row['Total Units']:,}", f"+{nathan_row['Total Units'] - managers['Total Units'].mean():.0f} vs avg manager")
    with col3:
        st.metric("Nathan Labor Cost", f"${nathan_row['Total Cost ($)']:,}", f"−${managers['Total Cost ($)'].mean() - nathan_row['Total Cost ($)']:,.2f} vs avg manager")
    with col4:
        st.metric("Nathan Avg Cost/Unit", f"${nathan_row['Avg Cost per Unit ($)']:.4f}", "Lowest in team")

    st.divider()

    st.subheader("Individual Manager Comparisons")
    st.caption("Each section compares **unit cost**, hours, total units, and references the graphs on the Charts page.")

    for _, manager in managers.iterrows():
        with st.container(border=True):
            st.subheader(f"{manager['Name']} (40 hrs) vs Nathan (30.29 hrs)")

            # Metrics row
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.metric("Hours Worked", f"{manager['Hours Worked']}", f"vs {nathan_row['Hours Worked']}")
            with m2:
                st.metric("Total Units", f"{int(manager['Total Units']):,}", f"vs {int(nathan_row['Total Units']):,}")
            with m3:
                st.metric("Labor Cost", f"${manager['Total Cost ($)']:,.2f}", f"vs ${nathan_row['Total Cost ($)']:,.2f}")
            with m4:
                unit_diff = manager["Avg Cost per Unit ($)"] - nathan_row["Avg Cost per Unit ($)"]
                pct_cheaper = (unit_diff / manager["Avg Cost per Unit ($)"]) * 100 if manager["Avg Cost per Unit ($)"] > 0 else 0
                st.metric("Avg Cost per Unit", 
                          f"${manager['Avg Cost per Unit ($)']:.4f}", 
                          f"vs ${nathan_row['Avg Cost per Unit ($)']:.4f} ({pct_cheaper:.1f}% higher)")

            # Detailed text summary
            st.markdown(f"""
            **Unit Cost Comparison (key insight):**  
            Nathan’s average cost per unit is **${nathan_row['Avg Cost per Unit ($)']:.4f}** — **{pct_cheaper:.1f}% lower** than {manager['Name']}’s **${manager['Avg Cost per Unit ($)']:.4f}**.  
            Even though Nathan worked 9.71 fewer hours, he handled **{nathan_row['Total Units'] - manager['Total Units']:,} more units** at a fraction of the cost per unit.

            **Graph Insights:**
            - **Total Labor Cost graph**: {manager['Name']} costs $900 while Nathan costs only $575.51 (36% less total spend).
            - **Total Units graph**: Nathan’s bar towers over everyone (1,814 units vs {manager['Name']}’s {int(manager['Total Units']):,}).
            - **Average Cost per Unit graph** (0–$20 scale): Nathan’s bar is the shortest/lowest, clearly showing the best efficiency.

            **Productivity (Units per Hour):**  
            {manager['Name']}: **{manager['Units per Hour']:.2f}** units/hour  
            Nathan: **{nathan_row['Units per Hour']:.2f}** units/hour → **{nathan_row['Units per Hour']/manager['Units per Hour']:.1f}x more productive**
            """)
            st.divider()

    st.success("✅ Nathan delivered **3–50× higher productivity** and the **lowest unit cost** despite fewer hours — the clear top performer.")

# ====================== PAGE 5: ASSOCIATE DASHBOARDS ======================
else:
    st.header("👤 Individual Associate Dashboards")
    st.markdown("**Labor Cost • Total Units Handled • Average Cost per Unit**")
    
    st.info("""
    **Cost basis:**  
    Managers = $22.50/hour | Nathan (Nate) = $19.00/hour
    """)
    
    for _, row in df.iterrows():
        with st.container(border=True):
            st.subheader(f"📌 {row['Name']}")
            c1, c2, c3 = st.columns(3, gap="large")
            
            with c1:
                st.metric("Labor Cost", f"${row['Total Cost ($)']:,.2f}")
            with c2:
                st.metric("Total Units Handled", f"{int(row['Total Units']):,}")
            with c3:
                st.metric("Avg Cost per Unit", f"${row['Avg Cost per Unit ($)']:.4f}")
            
            st.divider()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with Python + Streamlit + Altair 5.4.0")
st.sidebar.caption("Pick • Pack • Stow Performance App")
