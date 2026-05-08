import streamlit as st
import pandas as pd
import altair as alt

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pick Pack Stow App",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧳 Pick • Pack • Stow")
st.markdown("### Warehouse Performance Tracker - April 5–12, 2026")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["📋 Overview", 
     "📊 Performance DataFrame", 
     "📈 Charts & Visuals", 
     "🔍 Nathan vs Managers", 
     "⚡ Efficiency Comparison",
     "📝 Weekly Reports",
     "👤 Associate Dashboards"]
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

# Calculations
hourly_rates = [22.50, 22.50, 22.50, 22.50, 22.50, 19.00]
df["Hourly Rate ($)"] = hourly_rates
df["Total Units"] = df["Stow Quantity"] + df["Pick Quantity"]
df["Total Cost ($)"] = df["Hourly Rate ($)"] * df["Hours Worked"]
df["Avg Cost per Unit ($)"] = df.apply(
    lambda row: round(row["Total Cost ($)"] / row["Total Units"], 4) 
    if row["Total Units"] > 0 else 0.0, axis=1
)
df["Units per Hour"] = df.apply(
    lambda row: round(row["Total Units"] / row["Hours Worked"], 2) 
    if row["Hours Worked"] > 0 else 0, axis=1
)

df["Total Cost ($)"] = df["Total Cost ($)"].round(2)
df["Hourly Rate ($)"] = df["Hourly Rate ($)"].round(2)

# ====================== PAGE 1: OVERVIEW ======================
if page == "📋 Overview":
    st.header("📋 Manager Overview")
    st.write("""
    **Pick Pack Stow App includes 5 managers that work 40 hours a week.** 
    Their names are David, Elizet, Giselle, Omar, Jennifer, and part-time Nathan (30.29 hours).
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Team Members", "6")
    with col2: st.metric("Full-time Managers", "5")
    with col3: st.metric("Part-time", "1 (Nathan)")
    with col4: st.metric("Total Hours Worked", "230.29")

# ====================== PAGE 2: PERFORMANCE DATAFRAME ======================
elif page == "📊 Performance DataFrame":
    st.header("📊 Performance DataFrame")
    st.info("""
    **Cost basis:** Managers = $22.50/hr | Nathan = $19.00/hr  
    Avg Cost per Unit = Total Cost ÷ Total Units
    """)
    
    column_order = [
        "Name", "Hours Worked", "Stow Quantity", "Pick Quantity", "Total Units",
        "Hourly Rate ($)", "Total Cost ($)", "Avg Cost per Unit ($)", "Units per Hour",
        "PC99 Errors", "SIPS Over Short", "Scan Out of Sequence", "Bin Collisions", "Wrong ASINs"
    ]
    
    st.dataframe(
        df[column_order],
        use_container_width=True,
        height=500,
        column_config={
            "Hourly Rate ($)": st.column_config.NumberColumn(format="$.2f"),
            "Total Cost ($)": st.column_config.NumberColumn(format="$.2f"),
            "Avg Cost per Unit ($)": st.column_config.NumberColumn(format="$.4f"),
            "Units per Hour": st.column_config.NumberColumn(format="%.2f")
        }
    )

# ====================== PAGE 3: CHARTS & VISUALS ======================
elif page == "📈 Charts & Visuals":
    st.header("📈 Charts & Visual Analytics")
    
    # Labor Cost
    st.subheader("Total Labor Cost by Worker")
    st.altair_chart(alt.Chart(df).mark_bar(color="#1f77b4").encode(
        x=alt.X("Name:N", sort="-y"),
        y=alt.Y("Total Cost ($):Q"),
        tooltip=["Name", alt.Tooltip("Total Cost ($)", format="$.2f")]
    ).properties(height=380), use_container_width=True)

    # Total Units
    st.subheader("Total Units Handled")
    st.altair_chart(alt.Chart(df).mark_bar(color="#2ca02c").encode(
        x=alt.X("Name:N", sort="-y"),
        y="Total Units:Q",
        tooltip=["Name", "Total Units"]
    ).properties(height=380), use_container_width=True)

    # Avg Cost per Unit
    st.subheader("Average Cost per Unit ($)")
    st.altair_chart(alt.Chart(df).mark_bar(color="#d62728").encode(
        x=alt.X("Name:N", sort="y"),
        y=alt.Y("Avg Cost per Unit ($):Q", scale=alt.Scale(domain=[0, 20])),
        tooltip=["Name", alt.Tooltip("Avg Cost per Unit ($)", format="$.4f")]
    ).properties(height=380), use_container_width=True)

# ====================== PAGE 4: NATHAN VS MANAGERS ======================
elif page == "🔍 Nathan vs Managers":
    st.header("🔍 Nathan vs Managers Detailed Comparison")
    nathan = df[df["Name"] == "Nathan"].iloc[0]
    managers = df[df["Name"] != "Nathan"]
    
    st.info("Nathan worked **30.29 hours** vs 40 hours for each manager.")
    
    for _, mgr in managers.iterrows():
        with st.container(border=True):
            st.subheader(f"{mgr['Name']} vs Nathan")
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric("Total Units", f"{int(mgr['Total Units']):,}", f"vs {int(nathan['Total Units']):,}")
            with c2:
                st.metric("Avg Cost/Unit", f"${mgr['Avg Cost per Unit ($)']:.4f}", f"vs ${nathan['Avg Cost per Unit ($)']:.4f}")
            with c3:
                st.metric("Units/Hour", f"{mgr['Units per Hour']:.2f}", f"vs {nathan['Units per Hour']:.2f}")
            with c4:
                advantage = round(nathan['Units per Hour'] / mgr['Units per Hour'], 1)
                st.metric("Nathan Advantage", f"{advantage}x", "more productive")

# ====================== PAGE 5: EFFICIENCY COMPARISON ======================
elif page == "⚡ Efficiency Comparison":
    st.header("⚡ Efficiency Comparison")
    nathan = df[df["Name"] == "Nathan"].iloc[0]
    
    st.subheader("Units per Hour (True Efficiency)")
    st.altair_chart(alt.Chart(df).mark_bar().encode(
        x=alt.X("Name:N", sort="-y"),
        y="Units per Hour:Q",
        color=alt.condition(alt.datum.Name == "Nathan", alt.value("#d62728"), alt.value("#2ca02c")),
        tooltip=["Name", "Units per Hour"]
    ).properties(height=420), use_container_width=True)

# ====================== PAGE 6: WEEKLY REPORTS ======================
elif page == "📝 Weekly Reports":
    st.header("📝 Weekly Performance Report")
    st.subheader("April 5 – April 12, 2026")
    
    st.markdown("### Executive Summary")
    st.write("""
    Nathan delivered **outstanding performance** despite working only 30.29 hours. 
    He achieved the highest total units and the lowest cost per unit in the team.
    """)

    # Key Metrics
    st.markdown("### Key Team Metrics")
    key_df = pd.DataFrame({
        "Metric": ["Hours Worked", "Total Units", "Labor Cost", "Avg Cost/Unit", "Units per Hour"],
        "Avg Manager": ["40.00", "595.8", "$900.00", "$3.15", "14.90"],
        "Nathan": ["30.29", "1,814", "$575.51", "$0.3173", "59.89"],
        "Advantage": ["−9.71 hrs", "+204%", "−36%", "−90%", "4.0×"]
    })
    st.dataframe(key_df, use_container_width=True, hide_index=True)

    # Stow Table
    st.markdown("### Stow Performance Comparison")
    stow_df = pd.DataFrame({
        "Worker": df["Name"],
        "Stow Units": df["Stow Quantity"],
        "Stow UPH": round(df["Stow Quantity"] / df["Hours Worked"], 2),
        "Stow Cost/Unit ($)": round(22.50 / (df["Stow Quantity"] / df["Hours Worked"]), 4).where(df["Stow Quantity"] > 0, "N/A")
    })
    st.dataframe(stow_df, use_container_width=True, hide_index=True)

    # Pick Table
    st.markdown("### Pick Performance Comparison")
    pick_df = pd.DataFrame({
        "Worker": df["Name"],
        "Pick Units": df["Pick Quantity"],
        "Pick UPH": round(df["Pick Quantity"] / df["Hours Worked"], 2),
        "Pick Cost/Unit ($)": round(22.50 / (df["Pick Quantity"] / df["Hours Worked"]), 4).where(df["Pick Quantity"] > 0, "N/A")
    })
    st.dataframe(pick_df, use_container_width=True, hide_index=True)

    st.success("**Conclusion:** Nathan is the clear top performer — dramatically more efficient in both picking and stowing.")

# ====================== PAGE 7: ASSOCIATE DASHBOARDS ======================
else:
    st.header("👤 Individual Associate Dashboards")
    for _, row in df.iterrows():
        with st.container(border=True):
            st.subheader(f"📌 {row['Name']}")
            c1, c2, c3 = st.columns(3, gap="large")
            with c1: st.metric("Labor Cost", f"${row['Total Cost ($)']:,.2f}")
            with c2: st.metric("Total Units", f"{int(row['Total Units']):,}")
            with c3: st.metric("Avg Cost/Unit", f"${row['Avg Cost per Unit ($)']:.4f}")
            with st.expander("More Details"):
                st.write(f"Units/Hour: **{row['Units per Hour']:.2f}**")
            st.divider()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit + Altair 5.4.0")
st.sidebar.caption("Pick • Pack • Stow Performance App")
