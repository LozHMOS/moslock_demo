import streamlit as st
from PIL import Image

st.set_page_config(page_title="MOSLock Demo", page_icon="🔒", layout="wide")

# Session state
if 'step' not in st.session_state: st.session_state.step = 1
if 'role' not in st.session_state: st.session_state.role = None
if 'completed_steps' not in st.session_state: st.session_state.completed_steps = []
if 'lock_box' not in st.session_state: st.session_state.lock_box = []
if 'permit_locks' not in st.session_state: st.session_state.permit_locks = []
if 'photo_taken' not in st.session_state: st.session_state.photo_taken = False
if 'doc_mode' not in st.session_state: st.session_state.doc_mode = "Full Digital"

# Sidebar
st.sidebar.title("MOSLock Demo")
st.sidebar.markdown("**Industrial Isolation Safety Platform**  \nGeneric 12-Step Process – Aligned with AS/NZS 4871.1:2012")
role = st.sidebar.selectbox("Select Role", ["Select Role", "Certified Electrician", "Supervisor", "Permit Holder"], index=0)
if role != "Select Role" and st.session_state.role != role:
    st.session_state.role = role
    st.rerun()

if st.sidebar.button("Reset Demo"):
    for key in list(st.session_state.keys()): del st.session_state[key]
    st.rerun()

st.sidebar.info("Interactive demonstration of the 12-step isolation process with advanced safety features.")

# Header
st.title("MOSLock – Safe Isolation Management")
st.markdown("**Mapped Out Solutions** – A digital platform for electrical isolation safety in mining and high-risk industrial environments.")
if st.session_state.role:
    st.success(f"Logged in as: {st.session_state.role} | Equipment Example: Underground Switchgear / Conveyor Drive Motor | Job: ISO-2026-078")

# Documentation mode
col1, col2 = st.columns([3, 1])
with col1: st.subheader("Documentation Mode")
with col2:
    doc_mode = st.selectbox("Choose Mode", ["Full Digital", "Hybrid", "Paper Retention"], index=["Full Digital", "Hybrid", "Paper Retention"].index(st.session_state.doc_mode))
    if doc_mode != st.session_state.doc_mode: st.session_state.doc_mode = doc_mode

# Progress
completed = len(st.session_state.completed_steps)
progress_fraction = completed / 12.0
st.progress(progress_fraction)
st.caption(f"**Progress:** Step {st.session_state.step} of 12 | {completed}/12 steps completed ({progress_fraction*100:.1f}%)")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📋 12-Step Isolation Process", "🖼️ Electrical Drawing Library", "🔐 Hybrid Group Lock Box", "📸 AI Photo Verification", "📊 Audit & Observation", "🚀 Advanced Safety Features"])

with tab1:
    st.subheader("The 12-Step Isolation Process")
    st.image(Image.open("12step_flowchart.png"), 
             caption="12-Step Isolation Process Flowchart – Aligned with industry standards", 
             use_container_width=True)

    steps = ["1. Identify Energy Sources", "2. Advise Relevant Parties", "3. Isolate & Secure Energy Sources", 
             "4. Place Locks, Tags or Permits", "5. Verify Isolation – Test for Dead", "6. Commence Work", 
             "7. Complete Work", "8. Check Work", "9. Clear Area", "10. Remove Locks & Tags", 
             "11. Restore Energy", "12. Check Operation"]

    st.subheader(f"Current Step {st.session_state.step}: {steps[st.session_state.step-1]}")

    if st.session_state.step == 1:
        st.markdown("**Identify all energy sources (electrical, mechanical, hydraulic, stored, etc.).**")
        st.info("Engagement Prompt: Confirm you have identified every energy source before proceeding.")
        if st.button("✅ Acknowledge – All Energy Sources Identified"):
            if 1 not in st.session_state.completed_steps: st.session_state.completed_steps.append(1)
            st.success("Step 1 completed.")
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.markdown("**Notify all affected parties (team, supervisors, comms). Obtain acknowledgments.**")
        if st.button("✅ Send Notifications & Confirm All Acknowledged"):
            if 2 not in st.session_state.completed_steps: st.session_state.completed_steps.append(2)
            st.success("Notifications sent.")
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.markdown("**Isolate and secure all energy sources. Dissipate stored energy (e.g. bleed hydraulics, release tension).**")
        if st.button("✅ Confirm Isolation & Secure Complete"):
            if 3 not in st.session_state.completed_steps: st.session_state.completed_steps.append(3)
            st.success("Equipment isolated and secured.")
            st.session_state.step = 4
            st.rerun()

    elif st.session_state.step == 4:
        st.markdown("**Place Personal Locks, Permit Locks & Tags.**")
        lock_type = st.radio("Lock Type", ["Personal Isolation Lock", "Permit/Group Lock"])
        lock_id = st.text_input("Enter Lock Serial / Tag Number (simulate scan)")
        if st.button("Add Lock/Tag") and lock_id:
            if lock_type == "Personal Isolation Lock":
                st.session_state.lock_box.append(lock_id)
            else:
                st.session_state.permit_locks.append(lock_id)
            st.success(f"{lock_type} **{lock_id}** added.")
        st.write("Personal Locks in box:", st.session_state.lock_box)
        st.write("Permit Locks applied:", st.session_state.permit_locks)
        if st.button("✅ Complete Lock/Tag Placement"):
            if 4 not in st.session_state.completed_steps: st.session_state.completed_steps.append(4)
            st.success("Locks and tags placed.")
            st.session_state.step = 5
            st.rerun()

    elif st.session_state.step == 5:
        st.markdown("**Verify Isolation – Test for Dead.**")
        st.info("In the full application this step triggers the AI photo verification (see dedicated tab).")
        if st.button("✅ Confirm Verification Complete"):
            if 5 not in st.session_state.completed_steps: st.session_state.completed_steps.append(5)
            st.success("Isolation verified – Test for Dead complete.")
            st.session_state.step = 6
            st.rerun()

    elif st.session_state.step == 6:
        st.markdown("**Commence Work – Engagement Prompt: Confirm all hazards controlled.**")
        if st.button("✅ Safe to Commence Work"):
            if 6 not in st.session_state.completed_steps: st.session_state.completed_steps.append(6)
            st.success("Work commenced.")
            st.session_state.step = 7
            st.rerun()

    elif st.session_state.step in [7,8,9,10,11,12]:
        step_name = steps[st.session_state.step-1]
        st.markdown(f"**{step_name}**")
        notes = st.text_area("Notes / Observations", key=f"notes_{st.session_state.step}")
        if st.button(f"✅ Complete Step {st.session_state.step}"):
            if st.session_state.step not in st.session_state.completed_steps:
                st.session_state.completed_steps.append(st.session_state.step)
            st.success(f"Step {st.session_state.step} completed.")
            if st.session_state.step < 12:
                st.session_state.step += 1
            st.rerun()

    cols = st.columns(3)
    with cols[0]:
        if st.session_state.step > 1 and st.button("← Previous Step"):
            st.session_state.step -= 1
            st.rerun()
    with cols[1]:
        if st.session_state.step < 12 and st.button("Next Step →"):
            st.session_state.step += 1
            st.rerun()
    with cols[2]:
        if len(st.session_state.completed_steps) == 12:
            st.success("Full 12-Step Isolation Process Completed Successfully")
            st.balloons()

with tab2:
    st.subheader("Electrical Drawing Library")
    equip = st.radio("Select Equipment", ["Underground Switchgear Isolation Point", "Conveyor Drive Motor Isolation Point"])
    if equip == "Underground Switchgear Isolation Point":
        st.image(Image.open("underground_switchgear.png"), 
                 caption="Underground switchgear with visible isolation points.", 
                 use_container_width=True)
    else:
        st.image(Image.open("conveyor_motor_isolator.png"), 
                 caption="Conveyor drive motor isolation point with personal lock applied.", 
                 use_container_width=True)

with tab3:
    st.subheader("Hybrid Group Isolation Lock Box")
    st.image(Image.open("group_lock_box.png"), 
             caption="Group lock box with multiple personal locks and permit tag applied.", 
             use_container_width=True)
    lock_id = st.text_input("Simulate Scan – Enter Lock Serial")
    if st.button("Add to Lock Box"):
        st.session_state.lock_box.append(lock_id)
    st.write("Personal Locks in Box:", st.session_state.lock_box)
    st.write("Permit Locks Applied:", st.session_state.permit_locks)
    st.image(Image.open("danger_tags.png"), 
             caption="Danger tags used with locks.", 
             use_container_width=True)

with tab4:
    st.subheader("AI-Powered Photo Verification")
    picture = st.camera_input("Capture Verification Photo of Isolation Point", key="verification_photo")
    if picture:
        st.image(picture, use_container_width=True)
        st.success("AI Analysis: Lock placement correct | Tag visible | Zero-energy confirmed (target 98%+ accuracy)")

with tab5:
    st.subheader("Audit & Observation")
    st.markdown("**Supervisor Observation Checklist**")
    obs = st.checkbox("Supervisor credentials checked")
    locks = st.checkbox("Personal locks present and correct")
    signage = st.checkbox("Electrical signage correct and legible")
    eeha = st.checkbox("EEHA competency current")
    ppe = st.checkbox("Arc flash PPE worn correctly")
    if st.button("Submit Observation"):
        st.success("Observation logged – Green rating. No issues found.")

    st.subheader("Safety Performance Dashboard")
    st.metric("Risk Reduction", "30%", "↑ from last quarter")
    st.metric("Downtime Reduction", "20%", "↓")
    st.metric("Audit Compliance", "100%", "↑")

with tab6:
    st.subheader("Advanced Safety Features")
    st.markdown("**1. Permit-to-Work / Energisation Approval Simulation**")
    st.text_input("Energisation Title", value="Conveyor Drive Motor – Planned Maintenance")
    st.text_area("Scope", value="Isolate and verify conveyor drive motor for maintenance")
    if st.button("Approve Energisation Request"):
        st.success("Energisation request approved and linked to isolation record.")

    st.markdown("**2. Remote Isolation Simulation**")
    st.toggle("Simulate Remote Isolation (Conveyor SS94)", value=False)
    st.info("In the full application remote isolation is confirmed via SCADA with audible tone.")

    st.markdown("**3. Competency & PPE Quick-Check**")
    st.checkbox("QLD Electrical Licence current")
    st.checkbox("EEHA competency greater than 6 months valid")
    st.checkbox("LVR/CPR current")
    st.checkbox("Arc flash clothing and non-contact tester carried")

    st.markdown("**4. Immutable Audit Export**")
    if st.button("Export Full Audit Report"):
        st.success("Audit report exported with timestamps, photos, and signatures – ready for CMMS/PTW or regulator submission.")

st.caption("MOSLock Demo – Professional Version. Ready for review.")
