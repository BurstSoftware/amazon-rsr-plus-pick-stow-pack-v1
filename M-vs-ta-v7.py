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
    ["📋 Overview", "📊 Performance DataFrame", "📈 Charts & Visuals", "👤 Associate Dashboards"]
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

df["Total Cost ($)"] = df["Total Cost ($)"].round(2)
df["Hourly Rate ($)"] = df["Hourly Rate ($)"].round(2)

# ====================== CHARTS DATA ======================
viz_df = df[["Name", "Total Cost ($)", "Total Units", "Avg Cost per Unit ($)"]].copy()

# ====================== PAGE 1: OVERVIEW ======================
if page == "📋 Overview":
    st.header("Manager Overview")
    # ... (your existing overview content remains the same)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Team Members", "6")
    with col2:
        st.metric("Full-time Managers", "5")
    with col3:
        st.metric("Part-time", "1 (Nathan)")
    with col4:
        st.metric("Total Hours Worked", "230.29")

# ====================== NEW PAGE: CHARTS & VISUALS ======================
elif page == "📈 Charts & Visuals":
    st.header("📈 Charts & Visual Analytics")
    st.markdown("**Labor Cost • Total Units Handled • Average Cost per Unit** for all 6 workers")

    # 1. Combined Faceted Chart
    st.subheader("All Metrics Comparison")
    color_scale = alt.Scale(
        domain=["Total Cost ($)", "Total Units", "Avg Cost per Unit ($)"],
        range=["#1f77b4", "#2ca02c", "#d62728"]
    )

    chart1 = alt.Chart(viz_df.melt(id_vars=["Name"], var_name="Metric", value_name="Value")).mark_bar().encode(
        x=alt.X("Name:N", sort=None, title="Worker"),
        y=alt.Y("Value:Q", title="Value"),
        color=alt.Color("Metric:N", scale=color_scale),
        column=alt.Column("Metric:N", title=None, header=alt.Header(labelAngle=0, labelFontSize=14)),
        tooltip=[alt.Tooltip("Name:N"), alt.Tooltip("Metric:N"), alt.Tooltip("Value:Q", format=",.4f")]
    ).properties(width=220, height=450)

    st.altair_chart(chart1, use_container_width=True)

    # 2. Total Units Bar Chart
    st.subheader("Total Units Handled")
    chart2 = alt.Chart(df).mark_bar(color="#2ca02c").encode(
        x=alt.X("Name:N", sort="-y", title="Worker"),
        y=alt.Y("Total Units:Q", title="Total Units"),
        tooltip=["Name", "Total Units", "Stow Quantity", "Pick Quantity"]
    ).properties(height=400)
    st.altair_chart(chart2, use_container_width=True)

    # 3. Total Labor Cost Bar Chart
    st.subheader("Total Labor Cost ($)")
    chart3 = alt.Chart(df).mark_bar(color="#1f77b4").encode(
        x=alt.X("Name:N", sort="-y", title="Worker"),
        y=alt.Y("Total Cost ($):Q", title="Labor Cost ($)"),
        tooltip=["Name", alt.Tooltip("Total Cost ($)", format="$.2f")]
    ).properties(height=400)
    st.altair_chart(chart3, use_container_width=True)

    # 4. Average Cost per Unit
    st.subheader("Average Cost per Unit ($)")
    chart4 = alt.Chart(df).mark_bar(color="#d62728").encode(
        x=alt.X("Name:N", sort="y", title="Worker"),
        y=alt.Y("Avg Cost per Unit ($):Q", title="Avg Cost per Unit ($)"),
        tooltip=["Name", alt.Tooltip("Avg Cost per Unit ($)", format="$.4f")]
    ).properties(height=400)
    st.altair_chart(chart4, use_container_width=True)

# ====================== PAGE 2: PERFORMANCE DATAFRAME ======================
elif page == "📊 Performance DataFrame":
    # ... (your existing dataframe page - unchanged)
    st.header("📊 Manager Performance DataFrame")
    # (keep all your existing code for this page)

# ====================== PAGE 4: ASSOCIATE DASHBOARDS ======================
else:
    # ... (your existing individual dashboards - unchanged)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with Python + Streamlit + Altair 5.4.0")
st.sidebar.caption("Pick • Pack • Stow Performance App")
