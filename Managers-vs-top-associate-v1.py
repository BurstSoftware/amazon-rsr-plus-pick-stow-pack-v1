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
        st.metric("Hours Tracked", "230.29")

# ====================== PAGE 2: DATAFRAME ======================
else:
    st.header("📊 Manager Performance DataFrame")
    
    # Create the DataFrame
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
    
    # Display the dataframe
    st.dataframe(
        df,
        use_container_width=True,
        height=400,
        hide_index=False
    )
    
    # Summary statistics
    st.subheader("Summary Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Stow Units", f"{df['Stow Quantity'].sum():,}")
    with col2:
        st.metric("Total Pick Units", f"{df['Pick Quantity'].sum():,}")
    with col3:
        st.metric("Total Wrong ASINs", f"{df['Wrong ASINs'].sum()}")
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name="pick_pack_stow_performance.csv",
        mime="text/csv"
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Built with Python 3.14.4 + Streamlit")
st.sidebar.caption("Pick • Pack • Stow Performance App")
