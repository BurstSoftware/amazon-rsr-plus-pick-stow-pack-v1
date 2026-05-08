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
    ["📋 Overview", "📊 Performance DataFrame", "👤 Associate Dashboards"]
)

# ====================== UPDATED DATA ======================
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

# ====================== COMPILED VISUAL (ALTAIR) ======================
# Prepare data for visualization
viz_df = df[["Name", "Total Cost ($)", "Total Units", "Avg Cost per Unit ($)"]].copy()
viz_df = viz_df.melt(id_vars=["Name"], 
                     var_name="Metric", 
                     value_name="Value")

# Color mapping
color_scale = alt.Scale(
    domain=["Total Cost ($)", "Total Units", "Avg Cost per Unit ($)"],
    range=["#1f77b4", "#2ca02c", "#d62728"]
)

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

    # ==================== NEW: COMPILED ALTAIR VISUAL ====================
    st.subheader("📊 All 6 Workers — Labor Cost, Total Units & Avg Cost per Unit")
    st.markdown("**Interactive Chart** — Hover for exact values • Click legend to filter")

    # Create the Altair chart
    chart = alt.Chart(viz_df).mark_bar().encode(
        x=alt.X("Name:N", sort=None, title="Worker"),
        y=alt.Y("Value:Q", title="Value"),
        color=alt.Color("Metric:N", scale=color_scale, title="Metric"),
        column=alt.Column("Metric:N", 
                         title="Metric",
                         header=alt.Header(labelAngle=0)),
        tooltip=[
            alt.Tooltip("Name:N", title="Worker"),
            alt.Tooltip("Metric:N", title="Metric"),
            alt.Tooltip("Value:Q", title="Value", format=",.4f")
        ]
    ).properties(
        width=180,
        height=400
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_legend(
        titleFontSize=13,
        labelFontSize=12
    )

    st.altair_chart(chart, use_container_width=True)

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

# ====================== PAGE 3: ASSOCIATE DASHBOARDS ======================
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
st.sidebar.caption("Built with Python 3 + Streamlit + Altair 5.4.0")
st.sidebar.caption("Pick • Pack • Stow Performance App")
