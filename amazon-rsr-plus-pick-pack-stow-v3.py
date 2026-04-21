import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Amazon Hours Tracker",
    page_icon="📦",
    layout="centered"
)

# Dark theme + UI improvements
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .main-header { font-size: 32px; font-weight: 700; margin-bottom: 8px; }
    .sub-header { color: #aaaaaa; margin-bottom: 30px; }
    .section-title { font-size: 22px; font-weight: 600; margin: 25px 0 15px 0; }
    .stButton>button { height: 48px; font-weight: 600; }
    .red-button > button {
        background-color: #ff4d4d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "stow_pick_shifts" not in st.session_state:
    st.session_state.stow_pick_shifts = []

if "narossoh_shifts" not in st.session_state:
    # Pre-loaded Narossoh Work Time data from your message
    st.session_state.narossoh_shifts = [
        {"date": "2026-04-05", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-05", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-06", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-06", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-09", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-09", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-10", "start": "19:00", "end": "23:00"},
        {"date": "2026-04-11", "start": "14:30", "end": "18:30"},
    ]

def calculate_hours(start: str, end: str) -> float:
    if not start or not end:
        return 0.0
    try:
        s = datetime.strptime(start, "%H:%M")
        e = datetime.strptime(end, "%H:%M")
        if e < s:  # overnight
            e += timedelta(days=1)
        return round((e - s).total_seconds() / 3600, 2)
    except:
        return 0.0

# ====================== SIDEBAR NAVIGATION ======================
page = st.sidebar.selectbox(
    "Select Process",
    ["🛠️ Stow & Pick", "📍 Narossoh Work Time"]
)

# ====================== COMMON FUNCTIONS ======================
def display_shifts(shifts_list, process_name, key_prefix):
    if not shifts_list:
        st.info(f"No {process_name} shifts added yet.")
        return
    
    sorted_shifts = sorted(shifts_list, key=lambda x: x["date"], reverse=True)
    
    for i, shift in enumerate(sorted_shifts):
        date_obj = datetime.strptime(shift["date"], "%Y-%m-%d")
        hours = calculate_hours(shift["start"], shift["end"])
        
        with st.container(border=True):
            cols = st.columns([2.8, 1.7, 1.7, 1.3, 0.8])
            with cols[0]:
                st.write(f"**{date_obj.strftime('%A, %B %d, %Y')}**")
            with cols[1]:
                new_start = st.time_input(
                    "Start", 
                    value=datetime.strptime(shift["start"], "%H:%M").time(),
                    key=f"{key_prefix}_start_{i}"
                )
                shift["start"] = new_start.strftime("%H:%M")
            with cols[2]:
                new_end = st.time_input(
                    "End", 
                    value=datetime.strptime(shift["end"], "%H:%M").time(),
                    key=f"{key_prefix}_end_{i}"
                )
                shift["end"] = new_end.strftime("%H:%M")
            with cols[3]:
                st.metric("Hours", f"{hours:.2f}")
            with cols[4]:
                if st.button("🗑️", key=f"{key_prefix}_del_{i}"):
                    shifts_list.pop(i)
                    st.rerun()

def export_to_csv(shifts_list, filename_prefix):
    if not shifts_list:
        st.warning("No shifts to export.")
        return
    
    data = []
    for shift in shifts_list:
        date_obj = datetime.strptime(shift["date"], "%Y-%m-%d")
        data.append({
            "Date": shift["date"],
            "Day": date_obj.strftime("%A"),
            "Start Time": shift["start"],
            "End Time": shift["end"],
            "Hours Worked": calculate_hours(shift["start"], shift["end"])
        })
    
    df = pd.DataFrame(data)
    csv = df.to_csv(index=False)
    
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name=f"{filename_prefix}_{datetime.now().strftime('%Y-%m-%d')}.csv",
        mime="text/csv",
        use_container_width=True
    )

# ====================== MAIN PAGES ======================
if page == "🛠️ Stow & Pick":
    st.markdown('<p class="main-header">🛠️ Stow & Pick Hours</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Enter shifts with custom dates • Multiple shifts supported</p>', unsafe_allow_html=True)

    # Add New Shift - Perfectly aligned
    st.markdown('<p class="section-title">➕ Add a New Shift</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2.2, 1.6, 1.6, 1.3])

    with col1:
        shift_date = st.date_input("Shift Date", value=datetime.now().date(), key="sp_date")
    with col2:
        start_time = st.time_input("Start Time", value=datetime.strptime("14:30", "%H:%M").time(), key="sp_start")
    with col3:
        end_time = st.time_input("End Time", value=datetime.strptime("18:30", "%H:%M").time(), key="sp_end")
    with col4:
        st.write("")
        st.write("")
        if st.button("Add Shift", type="primary", use_container_width=True, key="add_sp"):
            new_shift = {
                "date": shift_date.strftime("%Y-%m-%d"),
                "start": start_time.strftime("%H:%M"),
                "end": end_time.strftime("%H:%M")
            }
            st.session_state.stow_pick_shifts.append(new_shift)
            st.success("✅ Stow/Pick shift added")
            st.rerun()

    st.divider()

    # Display Shifts
    st.markdown(f'<p class="section-title">📋 Stow & Pick Shifts ({len(st.session_state.stow_pick_shifts)})</p>', unsafe_allow_html=True)
    display_shifts(st.session_state.stow_pick_shifts, "Stow & Pick", "sp")

    # Summary & Export
    total_hours = sum(calculate_hours(s["start"], s["end"]) for s in st.session_state.stow_pick_shifts)
    col1, col2, col3 = st.columns([2, 2, 3])
    with col1:
        st.metric("**Total Hours**", f"{total_hours:.2f}")
    with col2:
        st.metric("**Total Shifts**", len(st.session_state.stow_pick_shifts))
    with col3:
        if st.button("📤 Export Stow & Pick to CSV", type="primary", use_container_width=True):
            export_to_csv(st.session_state.stow_pick_shifts, "stow_pick")

elif page == "📍 Narossoh Work Time":
    st.markdown('<p class="main-header">📍 Narossoh Work Time</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Pre-loaded data • You can edit or delete shifts</p>', unsafe_allow_html=True)

    st.divider()

    # Display Narossoh Shifts
    st.markdown(f'<p class="section-title">📋 Narossoh Shifts ({len(st.session_state.narossoh_shifts)})</p>', unsafe_allow_html=True)
    display_shifts(st.session_state.narossoh_shifts, "Narossoh", "nar")

    # Summary & Export
    total_hours = sum(calculate_hours(s["start"], s["end"]) for s in st.session_state.narossoh_shifts)
    col1, col2, col3 = st.columns([2, 2, 3])
    with col1:
        st.metric("**Total Hours**", f"{total_hours:.2f}")
    with col2:
        st.metric("**Total Shifts**", len(st.session_state.narossoh_shifts))
    with col3:
        if st.button("📤 Export Narossoh to CSV", type="primary", use_container_width=True):
            export_to_csv(st.session_state.narossoh_shifts, "narossoh")

# Footer
st.divider()
st.caption("✅ Custom date per shift • Stow & Pick + Narossoh supported • Ready for Streamlit Cloud • Python 3.14")
