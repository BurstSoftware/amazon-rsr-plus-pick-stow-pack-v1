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

# ====================== DATA ======================
# Original Pick Data
pick_data = {
    "User": ["narossoh", "stajenni", "danijac", "arrizola", "hasnsai", "uiyps", "jnoonoor", 
             "gpliegom", "mtiband r", "elizev", "hersmary", "mnimhas", "iqrayuss", 
             "nkaibrah", "matstrak", "abdiosmg", "musaom"],
    "Opportunities": [746, 804, 169, 614, 214, 208, 110, 362, 68, 176, 69, 97, 37, 255, 186, 44, 55],
    "Defects": [57, 14, 13, 13, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2],
    "DPMO": [76408, 17412, 76923, 21172, 37383, 38461, 63636, 19337, 88235, 34090, 72463, 51546, 108108, 15686, 16129, 68181, 36363]
}

# Original Stow Data
stow_data = {
    "User": ["narossoh", "iqrayuss", "uiyps", "mnimhas", "hersmary", "mtiband r", "danijac", 
             "nkaibrah", "gpliegom", "matstrak", "hasnsai", "elizev", "pmhusse", "stajenni", 
             "abdiosmg", "jnoonoor", "arrizola"],
    "Opportunities": [1068, 758, 330, 668, 246, 445, 168, 518, 580, 594, 416, 204, 308, 127, 214, 63, 57],
    "Defects": [164, 130, 117, 94, 45, 37, 22, 17, 15, 13, 12, 12, 9, 7, 4, 3, 3],
    "DPMO": [153558, 171503, 354545, 140718, 182926, 83146, 130952, 32818, 25862, 21885, 28846, 58823, 29220, 55118, 18691, 47619, 52631]
}

df_pick_orig = pd.DataFrame(pick_data)
df_stow_orig = pd.DataFrame(stow_data)

# Normalized Data (kept for other pages)
pick_norm_data = { ... }  # your existing normalized data - unchanged
stow_norm_data = { ... }  # your existing normalized data - unchanged

df_pick_norm = pd.DataFrame(pick_norm_data)
df_stow_norm = pd.DataFrame(stow_norm_data)

# Work Hours Data
hours_data = {
    "User": ["narossoh"] * 8,
    "Date": ["2026-04-05", "2026-04-05", "2026-04-06", "2026-04-06", "2026-04-09", "2026-04-09", 
             "2026-04-10", "2026-04-11"],
    "Day": ["Sunday", "Sunday", "Monday", "Monday", "Thursday", "Thursday", "Friday", "Saturday"],
    "Start Time": ["19:00", "19:00", "19:00", "19:00", "19:00", "19:00", "19:00", "14:30"],
    "End Time": ["23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "23:00", "18:30"],
    "Hours Worked": [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
}
df_hours = pd.DataFrame(hours_data)

all_users = sorted(df_pick_orig["User"].unique())

# ====================== SIDEBAR ======================
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home & Summary", 
     "📦 Pick Report", 
     "📦 Stow Report", 
     "👥 3-Associate Comparison",
     "⏰ Associate Work Hours & Productivity",
     "📊 Team Overview",
     "💰 Payroll Overview"])

# ====================== PAGES ======================
# (All previous pages remain the same - Home, Pick, Stow, Comparison, Work Hours, Team Overview)

if page == "🏠 Home & Summary":
    # ... (keep your existing Home page code) ...
    pass

# ... (keep all other elif pages exactly as they were: Pick Report, Stow Report, 3-Associate Comparison, Work Hours, Team Overview) ...

elif page == "💰 Payroll Overview":
    st.title("💰 Payroll Overview")
    st.markdown("**April 5th – April 12th, 2026**")

    # === Simple Labor Cost Estimate (your preferred UI) ===
    st.subheader("Manager & Associate Labor Cost Estimate")
    
    manager_total = 5 * 40 * 22.50
    associate_total_hours = 14 * 19
    associate_hourly_rate = 19.00
    associate_total = associate_total_hours * associate_hourly_rate
    grand_total = manager_total + associate_total

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Managers (5 × 40 hrs)", f"${manager_total:,.2f}")
        st.metric("Hourly Rate", "$22.50")
    with col2:
        st.metric("Associates (14 × 19 hrs)", f"${associate_total:,.2f}")
        st.metric("Hourly Rate", "$19.00")

    st.metric("**Grand Total Payroll**", f"${grand_total:,.2f}", delta=None)

    # Small breakdown chart
    payroll_data = pd.DataFrame({
        "Category": ["Managers", "Associates"],
        "Cost": [manager_total, associate_total]
    })
    chart = alt.Chart(payroll_data).mark_bar().encode(
        x=alt.X("Category:N", sort=None),
        y=alt.Y("Cost:Q", title="Cost ($)"),
        color=alt.Color("Category:N", scale=alt.Scale(range=["#1f77b4", "#ff7f0e"]))
    ).properties(height=300)
    st.altair_chart(chart, use_container_width=True)

    st.markdown("---")

    # === New Spending Allocation by Associate (based on opportunities) ===
    st.subheader("Spending Allocation by Associate ($9,554 Total)")
    st.caption("Allocated based on each associate's share of total Pick + Stow opportunities")

    # Combine Pick and Stow opportunities
    pick_opp = df_pick_orig.set_index("User")["Opportunities"]
    stow_opp = df_stow_orig.set_index("User")["Opportunities"].reindex(pick_opp.index, fill_value=0)

    combined = pd.DataFrame({
        "Pick Opportunities": pick_opp,
        "Stow Opportunities": stow_opp
    })
    combined["Total Opportunities"] = combined["Pick Opportunities"] + combined["Stow Opportunities"]
    combined["% of Total Volume"] = (combined["Total Opportunities"] / combined["Total Opportunities"].sum() * 100).round(2)
    combined["Estimated Spend"] = (combined["% of Total Volume"] / 100 * 9554).round(2)

    combined = combined.sort_values("Total Opportunities", ascending=False)

    display_df = combined.reset_index().rename(columns={"index": "Associate"})

    st.dataframe(
        display_df.style.format({
            "% of Total Volume": "{:.2f}%",
            "Estimated Spend": "${:,.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.info("""
    **Notes**: 
    - Manager rate: $22.50/hr for 40 hours.
    - Associate rate: $19.00/hr for ~19 hours.
    - The $9,554 total spend is distributed proportionally based on each associate's volume (Pick + Stow opportunities).
    """)

st.caption("Amazon RSR+ Pick & Stow Dashboard • April 2026")
