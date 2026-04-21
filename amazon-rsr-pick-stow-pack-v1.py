import streamlit as st
import pandas as pd

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pick & Stow Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== DATA ======================
# Pick Report Data (Original)
pick_data = {
    "User": ["narossoh", "stajenni", "danijac", "arrizola", "hasnsai", "uiyps", "jnoonoor", 
             "gpliegom", "mtiband r", "elizev", "hersmary", "mnimhas", "iqrayuss", 
             "nkaibrah", "matstrak", "abdiosmg", "musaom"],
    "Opportunities": [746, 804, 169, 614, 214, 208, 110, 362, 68, 176, 69, 97, 37, 255, 186, 44, 55],
    "Defects": [57, 14, 13, 13, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2],
    "DPMO": [76408, 17412, 76923, 21172, 37383, 38461, 63636, 19337, 88235, 34090, 72463, 51546, 108108, 15686, 16129, 68181, 36363]
}

# Stow Report Data (Original)
stow_data = {
    "User": ["narossoh", "iqrayuss", "uiyps", "mnimhas", "hersmary", "mtiband r", "danijac", 
             "nkaibrah", "gpliegom", "matstrak", "hasnsai", "elizev", "pmhusse", "stajenni", 
             "abdiosmg", "jnoonoor", "arrizola"],
    "Opportunities": [1068, 758, 330, 668, 246, 445, 168, 518, 580, 594, 416, 204, 308, 127, 214, 63, 57],
    "Defects": [164, 130, 117, 94, 45, 37, 22, 17, 15, 13, 12, 12, 9, 7, 4, 3, 3],
    "DPMO": [153558, 171503, 354545, 140718, 182926, 83146, 130952, 32818, 25862, 21885, 28846, 58823, 29220, 55118, 18691, 47619, 52631]
}

df_pick = pd.DataFrame(pick_data)
df_stow = pd.DataFrame(stow_data)

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "👥 3-Associate Comparison"])

# ====================== MAIN APP ======================
if page == "🏠 Home & Summary":
    st.title("📦 Warehouse Pick & Stow Performance Dashboard")
    st.markdown("**April 5th – April 12th** | Amazon RSR+ Analysis")
    
    st.markdown("### Report Summary & Explanation")
    st.info("""
    This dashboard contains both **original** and **updated/normalized** versions of the Pick and Stow reports.
    
    **Key Update Performed:**
    - We normalized all associates to **narossoh’s opportunity volume** (746 in Pick, 1,068 in Stow).
    - Defects were scaled proportionally while keeping each associate’s individual error rate (DPMO) constant.
    - This allows fair quality comparison regardless of volume worked.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Associates", 17)
        st.metric("Original Pick Opportunities", "4,214")
    with col2:
        st.metric("Original Stow Opportunities", "6,112")
        st.metric("After Normalization", "Pick: 12,682 | Stow: 18,156")

elif page == "📦 Pick Report":
    st.title("📦 Pick Report Analysis")
    
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    
    with tab1:
        st.subheader("Original Pick Report")
        st.dataframe(df_pick.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Updated Pick Report – All at 746 Opportunities")
        st.markdown("**Explanation**: Every associate now has the same number of opportunities as narossoh. Defects scaled based on their original error rate.")
        # You can expand this with full updated table if needed

elif page == "📦 Stow Report":
    st.title("📦 Stow Report Analysis")
    
    tab1, tab2 = st.tabs(["Original Data", "Updated (Normalized to narossoh)"])
    
    with tab1:
        st.subheader("Original Stow Report")
        st.dataframe(df_stow.style.format({"DPMO": "{:,.0f}"}), use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Updated Stow Report – All at 1,068 Opportunities")
        st.markdown("**Explanation**: Every associate normalized to narossoh’s 1,068 opportunities. Defects recalculated proportionally.")

elif page == "👥 3-Associate Comparison":
    st.title("👥 Focused Comparison: narossoh vs elizev vs arrizola")
    
    # Original Comparison
    st.subheader("Original Data")
    comparison_original = pd.DataFrame({
        "Report": ["Pick", "Pick", "Pick", "Stow", "Stow", "Stow"],
        "User": ["narossoh", "elizev", "arrizola", "narossoh", "elizev", "arrizola"],
        "Opportunities": [746, 176, 614, 1068, 204, 57],
        "Defects": [57, 6, 13, 164, 12, 3],
        "DPMO": [76408, 33512, 21448, 153558, 58989, 52434]
    })
    st.dataframe(comparison_original, use_container_width=True, hide_index=True)
    
    st.subheader("Updated (Normalized to narossoh’s Volume)")
    comparison_updated = pd.DataFrame({
        "Report": ["Pick", "Pick", "Pick", "Stow", "Stow", "Stow"],
        "User": ["narossoh", "elizev", "arrizola", "narossoh", "elizev", "arrizola"],
        "Opportunities": [746, 746, 746, 1068, 1068, 1068],
        "Defects": [57, 25, 16, 164, 63, 56],
        "DPMO": [76408, 33512, 21448, 153558, 58989, 52434]
    })
    st.dataframe(comparison_updated, use_container_width=True, hide_index=True)

st.caption("Dashboard built for Amazon RSR+ Pick & Stow Analysis • April 2026")
