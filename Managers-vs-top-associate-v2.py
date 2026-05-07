import streamlit as st
import pandas as pd

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
    ["📋 Overview", "📊 Performance DataFrame"]
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
    Nathan works 30.29 hours, stows 1068 units, with 1 pc99, 19 sips over short, 
    79 scan out out of sequence, and 65 bin colisions.
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

# ====================== PAGE 2: DATAFRAME ======================
else:
    st.header("📊 Manager Performance DataFrame")
    
    # Base data
    data = {
        "Name": ["David", "Elizet", "Giselle", "Omar", "Jennifer", "Nathan"],
        "Hours Worked": [40.00, 40.00, 40.00, 40.00, 40.00, 30.29],
        "Stow Quantity": [57, 204, 580, 0, 127, 1068],
        "Pick Quantity": [614, 176, 362, 55, 0, 0],
        "PC99 Errors": [1, 1, 0, 0, 0, 1],
        "SIPS Over Short": [0, 1, 1, 0, 4, 19],
        "Scan Out of Sequence": [0, 3, 9, 0, 0, 79],
        "Bin Collisions": [2, 7, 5, 0, 3, 65],
        "Wrong ASINs": [13, 6, 7, 2, 0, 0]
    }
    
    df = pd.DataFrame(data)
    
    # ====================== COST CALCULATIONS ======================
    # Hourly rates as specified
    hourly_rates = [22.50, 22.50, 22.50, 22.50, 22.50, 19.00]
    df["Hourly Rate ($)"] = hourly_rates
    
    # Total units handled (stow + pick)
    df["Total Units"] = df["Stow Quantity"] + df["Pick Quantity"]
    
    # Total labor cost = hourly rate × hours worked
    df["Total Cost ($)"] = df["Hourly Rate ($)"] * df["Hours Worked"]
    
    # Cost per total unit = total cost ÷ total units (0 units = 0)
    df["Cost per Unit ($)"] = df.apply(
        lambda row: round(row["Total Cost ($)"] / row["Total Units"], 4) 
        if row["Total Units"] > 0 else 0.0, 
        axis=1
    )
    
    # Round money columns for clean display
    df["Total Cost ($)"] = df["Total Cost ($)"].round(2)
    df["Hourly Rate ($)"] = df["Hourly Rate ($)"].round(2)
    
    # ====================== DISPLAY ======================
    # Verbiage requested by user to accompany the data table
    st.info("""
    **Cost basis used for all calculations:**  
    Managers (David, Elizet, Giselle, Omar, Jennifer) = $22.50 per hour  
    Nathan (Nate) = $19.00 per hour  
    Cost per Unit = (Hourly Rate × Hours Worked) ÷ Total Units
    """)
    
    # Reorder columns so cost metrics appear at the end
    column_order = [
        "Name", "Hours Worked", "Stow Quantity", "Pick Quantity", "Total Units",
        "Hourly Rate ($)", "Total Cost ($)", "Cost per Unit ($)",
        "PC99 Errors", "SIPS Over Short", "Scan Out of Sequence", 
        "Bin Collisions", "Wrong ASINs"
    ]
    df_display = df[column_order]
    
    # Show the enhanced dataframe with nice formatting
    st.dataframe(
        df_display,
        use_container_width=True,
        height=420,
        hide_index=False,
        column_config={
            "Hourly Rate ($)": st.column_config.NumberColumn(format="$.2f"),
            "Total Cost ($)": st.column_config.NumberColumn(format="$.2f"),
            "Cost per Unit ($)": st.column_config.NumberColumn(format="$.4f"),
            "Total Units": st.column_config.NumberColumn(format="%,.0f")
        }
    )
    
    # Summary metrics
    st.subheader("Cost Summary")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Labor Cost", f"${df['Total Cost ($)'].sum():,.2f}")
    with col2:
        st.metric("Average Cost per Unit", f"${df['Cost per Unit ($)'].mean():.4f}")
    with col3:
        st.metric("Total Units Handled", f"{df['Total Units'].sum():,}")
    with col4:
        st.metric("Weighted Avg Cost/Unit", 
                  f"${(df['Total Cost ($)'].sum() / df['Total Units'].sum()):.4f}")
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Data (with costs) as CSV",
        data=csv,
        file_name="pick_pack_stow_performance_with_costs.csv",
        mime="text/csv"
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with Python 3.14.4 + Streamlit")
st.sidebar.caption("Pick • Pack • Stow Performance App")
st.sidebar.caption("Cost per Unit calculation added per request")
