import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pathlib import Path
from io import StringIO

# ============================================================
# GLOBAL CONFIG & THEME
# ============================================================
st.set_page_config(
    page_title="Sai Tankala | CS & Cloud Portfolio Hub",
    layout="wide",
)

# Altair executive-style theme (works well with dark mode)
@alt.theme.register('executive_theme', enable=True)
def executive_theme():
    return alt.theme.ThemeConfig({
        "config": {
            "font": "Inter",
            "axis": {
                "labelFontSize": 13,
                "titleFontSize": 14,
                "labelColor": "#CCCCCC"
            },
            "title": {
                "fontSize": 20,
                "font": "Inter",
                "color": "white"
            },
            "view": {"stroke": "transparent"},
            "legend": {
                "labelFontSize": 12,
                "symbolSize": 120
            }
        }
    })



# ============================================================
# 0️⃣ LANDING PAGE
# ============================================================
def landing_page():
    # ---------- Custom CSS for card-style layout ----------
    st.markdown("""
        <style>
            .landing-title {
                font-size: 34px !important;
                font-weight: 750 !important;
                margin-bottom: 0.2rem;
            }
            .landing-subtitle {
                font-size: 20px !important;
                color: #CCCCCC !important;
                margin-bottom: 1.5rem;
            }
            .landing-intro {
                font-size: 17px !important;
                line-height: 1.6 !important;
                margin-bottom: 1.8rem;
            }
            /* Style all expanders on the landing page like cards */
            div[data-testid="stExpander"] {
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 14px;
                box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
                padding: 0.15rem 0.35rem 0.6rem 0.35rem;
                background: rgba(15, 17, 26, 0.95);
            }
            div[data-testid="stExpander"] > details > summary {
                font-size: 18px !important;
                font-weight: 650 !important;
            }
            .card-body-text {
                font-size: 15px !important;
                line-height: 1.55 !important;
            }
            .chip-row {
                margin: 0.4rem 0 0.8rem 0;
            }
            .chip {
                display: inline-block;
                padding: 0.12rem 0.55rem;
                margin: 0.08rem;
                border-radius: 999px;
                font-size: 12px;
                font-weight: 600;
                border: 1px solid rgba(255, 255, 255, 0.35);
                background: rgba(255, 255, 255, 0.04);
            }
            .chip-cs {
                border-color: #2ecc71aa;
                color: #b8f5cd;
            }
            .chip-cloud {
                border-color: #3498dbaa;
                color: #c8e7ff;
            }
            .chip-pm {
                border-color: #f1c40faa;
                color: #ffe9b8;
            }
            .use-instructions {
                font-size: 17px !important;
                line-height: 1.6 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # ---------- Title + Intro ----------
    st.markdown(
        '<p class="landing-title">Portfolio of Projects & Tool kits Customer Success, Cloud Transformation & Program Management</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="landing-subtitle">Built by <strong>Sai Tankala – Sr. Customer Success & Service Experience Leader</strong></p>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p class="landing-intro">
        This hub brings together three hands-on apps that demonstrate strengths in
        <strong>Customer Success analytics</strong>, <strong>Cloud readiness & migration</strong>,
        and <strong>Program / Project Management excellence</strong>.
        Use the <strong>sidebar</strong> to open each app, and skim the cards below for a quick
        view of expertise areas.
        </p>
        """,
        unsafe_allow_html=True
    )

    # ---------- 3 card columns ----------
    col1, col2, col3 = st.columns(3)

    # ===== Card 1: Customer Success Health Dashboard =====
    with col1:
        with st.expander("📊  Customer Success Health Dashboard", expanded=True):
            st.markdown(
                """
                <div class="chip-row">
                    <span class="chip chip-cs">Customer Analytics</span>
                    <span class="chip chip-cs">Health Scoring</span>
                    <span class="chip chip-cs">Renewal Risk</span>
                    <span class="chip chip-cs">ARR Protection</span>
                </div>
                <p class="card-body-text">
                A data-driven dashboard that blends <strong>NPS, CSAT, product usage,
                support volume,</strong> and <strong>renewal horizon</strong> into a unified Health Score.
                </p>
                <p class="card-body-text">
                It helps Customer Success and Account teams quickly identify:
                </p>
                <ul class="card-body-text">
                    <li>🔥 <strong>At-risk accounts</strong> (Red / Yellow)</li>
                    <li>🌱 <strong>Expansion opportunities</strong> (high adoption + promoters)</li>
                    <li>🧭 <strong>Next best actions</strong> for QBRs, EBRs, and renewals</li>
                    <li>🧮 <strong>ARR at risk & band-level rollups</strong> for exec views</li>
                </ul>
                <p class="card-body-text">
                Under the hood, it uses weighted scoring, segment filters, and automated
                recommendations—very similar to what you’d expect from a modern CS platform.
                </p>
                """,
                unsafe_allow_html=True
            )

    # ===== Card 2: Cloud Readiness Assessment Tool =====
    with col2:
        with st.expander("☁️  Cloud Readiness Assessment Tool", expanded=False):
            st.markdown(
                """
                <div class="chip-row">
                    <span class="chip chip-cloud">AWS CAF</span>
                    <span class="chip chip-cloud">Well-Architected</span>
                    <span class="chip chip-cloud">Cloud Migration</span>
                    <span class="chip chip-cloud">FinOps Readiness</span>
                </div>
                <p class="card-body-text">
                A lightweight assessment tool inspired by <strong>AWS Cloud Adoption Framework</strong>
                and the <strong>Well-Architected Framework</strong>.
                </p>
                <p class="card-body-text">
                It scores current state across:
                </p>
                <ul class="card-body-text">
                    <li>🔐 <strong>Security</strong> – IAM, baselines, monitoring & guardrails</li>
                    <li>🔧 <strong>Operations</strong> – incidents, CI/CD, resilience & DR</li>
                    <li>💰 <strong>Cost Management</strong> – tagging, visibility, optimization</li>
                    <li>👩‍💻 <strong>Team Skills</strong> – cloud skills + agile / delivery maturity</li>
                </ul>
                <p class="card-body-text">
                Based on the scores, it recommends whether an organization should focus on
                <strong>foundations first</strong>, run <strong>structured pilots</strong>, or is ready for
                <strong>Wave 1–2 migration</strong>, with concrete next steps for each dimension.
                </p>
                """,
                unsafe_allow_html=True
            )

    # ===== Card 3: PM Toolkit + Templates Generator =====
    with col3:
        with st.expander("🗂️  PM Toolkit + Templates Generator", expanded=False):
            st.markdown(
                """
                <div class="chip-row">
                    <span class="chip chip-pm">PMO Frameworks</span>
                    <span class="chip chip-pm">Delivery Excellence</span>
                    <span class="chip chip-pm">Executive Reporting</span>
                    <span class="chip chip-pm">Templates</span>
                </div>
                <p class="card-body-text">
                A practical toolkit that surfaces <strong>PMO templates and frameworks</strong> from a
                local <code>templates/</code> folder.
                </p>
                <p class="card-body-text">
                It includes templates for:
                </p>
                <ul class="card-body-text">
                    <li>📋 <strong>RAID Logs</strong> (Risks, Assumptions, Issues, Dependencies)</li>
                    <li>👥 <strong>RACI Matrices</strong></li>
                    <li>📄 <strong>Project Charters</strong></li>
                    <li>🏃 <strong>Sprint Backlog / Board CSVs</strong></li>
                    <li>📅 <strong>Weekly Status Reports</strong></li>
                    <li>🧭 <strong>Executive Summary One-Pagers</strong></li>
                </ul>
                <p class="card-body-text">
                Each template can be previewed in-app (as a table or rendered Markdown) and
                downloaded for direct use in Excel, Sheets, Confluence, or PowerPoint—matching
                real-world consulting and program delivery workflows.
                </p>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    # ---------- How to Use Section ----------
    st.markdown(
        """
        <p class="use-instructions">
        <strong>How to use this hub</strong><br><br>
        1. Use the <strong>sidebar</strong> to switch between apps.<br>
        2. Adjust per-app configurations (weights, scoring ranges, template selection).<br>
        3. Use the main panel for dashboards, tables, recommendations, and downloads.<br>
        4. This hub is ideal for portfolio demos, interviews, and leadership conversations
           around Customer Success, Cloud, and Program Delivery.
        </p>
        """,
        unsafe_allow_html=True
    )




# ============================================================
# 1️⃣ CUSTOMER SUCCESS HEALTH DASHBOARD
# ============================================================
def compute_health_scores(df, weights):
    df = df.copy()

    # Numeric coercion
    df["ARR"] = pd.to_numeric(df["ARR"], errors="coerce").fillna(0)
    df["NPS"] = pd.to_numeric(df["NPS"], errors="coerce").fillna(0)
    df["Tickets_Last_90d"] = pd.to_numeric(df["Tickets_Last_90d"], errors="coerce").fillna(0)
    df["CSAT"] = pd.to_numeric(df["CSAT"], errors="coerce").fillna(0)
    df["Logins_Last_30d"] = pd.to_numeric(df["Logins_Last_30d"], errors="coerce").fillna(0)
    df["Active_Users"] = pd.to_numeric(df["Active_Users"], errors="coerce").fillna(0)
    df["Total_Seats"] = pd.to_numeric(df["Total_Seats"], errors="coerce").fillna(1)

    # Usage ratio
    df["Usage_Ratio"] = (df["Active_Users"] / df["Total_Seats"]).clip(0, 1)

    # Feature scores (0–1)
    df["score_nps"] = (df["NPS"].clip(-100, 100) + 100) / 200.0
    df["score_csat"] = df["CSAT"].clip(1, 5) / 5.0
    df["score_usage"] = df["Usage_Ratio"]
    df["score_logins"] = (df["Logins_Last_30d"] / df["Logins_Last_30d"].max()).fillna(0)

    df["score_tickets"] = 1 - (df["Tickets_Last_90d"] / df["Tickets_Last_90d"].max()).fillna(0)
    df["score_tickets"] = df["score_tickets"].clip(0, 1)

    w = weights
    df["Health_Score"] = (
        df["score_nps"] * w["nps"]
        + df["score_csat"] * w["csat"]
        + df["score_usage"] * w["usage"]
        + df["score_logins"] * w["logins"]
        + df["score_tickets"] * w["tickets"]
    )
    df["Health_Score"] = (df["Health_Score"] / sum(w.values()) * 100).round(1)

    df["Health_Band"] = pd.cut(
        df["Health_Score"],
        bins=[-1, 49.9, 74.9, 100],
        labels=["Red", "Yellow", "Green"]
    )

    df["Renewal_Date"] = pd.to_datetime(df["Renewal_Date"], errors="coerce")
    today_ts = pd.Timestamp.today().normalize()
    df["Days_to_Renewal"] = (df["Renewal_Date"] - today_ts).dt.days

    return df


def expansion_potential(row):
    if row["Health_Band"] == "Green" and row["Usage_Ratio"] > 0.7 and row["NPS"] >= 50:
        return "High"
    if row["Health_Band"] == "Yellow" and row["Usage_Ratio"] > 0.5 and row["NPS"] >= 20:
        return "Medium"
    return "Low"


def renewal_risk(row):
    if row["Health_Band"] == "Red":
        return "High"
    if row["Health_Band"] == "Yellow":
        return "Medium"
    return "Low"


def recommended_actions(row):
    actions = []

    # Health-based
    if row["Health_Band"] == "Red":
        actions.append("Exec-sponsored recovery plan and deep-dive on blockers.")
    elif row["Health_Band"] == "Yellow":
        actions.append("Align on 90-day success plan and ownership on both sides.")
    else:
        actions.append("Reinforce value via QBR/EBR and explore expansion.")

    # Usage
    if row["Usage_Ratio"] < 0.4:
        actions.append("Low adoption: run enablement, expand use cases, activate champions.")
    elif row["Usage_Ratio"] > 0.8:
        actions.append("High adoption: discuss seat expansion or advanced modules.")

    # Tickets
    if row["Tickets_Last_90d"] >= 40:
        actions.append("High ticket volume: review top themes, fix root causes.")

    # NPS / CSAT
    if row["NPS"] < 0:
        actions.append("Negative NPS: stakeholder interviews and targeted recovery plan.")
    elif row["NPS"] >= 50:
        actions.append("Promoter: invite to reference program or case study.")
    if row["CSAT"] < 3.5:
        actions.append("Improve support quality and SLAs; review playbooks.")

    # Renewal horizon
    days = row.get("Days_to_Renewal")
    if pd.notnull(days) and days <= 120:
        actions.append("Renewal <120 days: lock in mutual success plan and early commit.")

    return " • ".join(actions)


def page_customer_success():
    st.title("1️⃣ Customer Success Health Dashboard")

    st.write(
        """
        Blend **NPS, CSAT, usage, tickets, and renewal timing** into a single view
        to prioritize accounts, protect ARR, and prep for QBRs.
        """
    )

    # --- Data source ---
    st.markdown("#### Data")
    uploaded = st.file_uploader(
        "Upload customer CSV (or leave empty to use sample data).",
        type=["csv"],
        key="cs_upload",
    )

    if uploaded is not None:
        df_raw = pd.read_csv(uploaded)
    else:
        sample_csv = StringIO(
            "Customer,Segment,ARR,Renewal_Date,NPS,Tickets_Last_90d,CSAT,Logins_Last_30d,Active_Users,Total_Seats\n"
            "Acme Corp,Enterprise,450000,2025-03-15,45,38,4.1,520,180,200\n"
            "Globex Inc,Mid-Market,180000,2025-01-20,15,52,3.6,210,70,100\n"
            "Innotech,SMB,60000,2025-06-10,72,8,4.7,95,18,20\n"
            "BlueSky Analytics,Enterprise,320000,2024-12-01,-10,75,3.2,140,65,120\n"
            "Vertex Labs,SMB,40000,2024-11-25,80,3,4.9,60,10,10\n"
        )
        df_raw = pd.read_csv(sample_csv)

    required_cols = [
        "Customer","Segment","ARR","Renewal_Date","NPS",
        "Tickets_Last_90d","CSAT","Logins_Last_30d","Active_Users","Total_Seats"
    ]
    missing = [c for c in required_cols if c not in df_raw.columns]
    if missing:
        st.error(f"Missing required columns in CSV: {missing}")
        return

    # --- Sidebar config for this app ---
    st.sidebar.markdown("### ⚙️ Health Score Weights")
    nps_w = st.sidebar.slider("NPS", 0.0, 5.0, 3.0, 0.5)
    csat_w = st.sidebar.slider("CSAT", 0.0, 5.0, 2.0, 0.5)
    usage_w = st.sidebar.slider("Usage", 0.0, 5.0, 3.0, 0.5)
    logins_w = st.sidebar.slider("Logins", 0.0, 5.0, 1.0, 0.5)
    tickets_w = st.sidebar.slider("Tickets (lower is better)", 0.0, 5.0, 2.0, 0.5)

    weights = {
        "nps": nps_w,
        "csat": csat_w,
        "usage": usage_w,
        "logins": logins_w,
        "tickets": tickets_w,
    }

    df = compute_health_scores(df_raw, weights)
    df["Expansion_Potential"] = df.apply(expansion_potential, axis=1)
    df["Renewal_Risk"] = df.apply(renewal_risk, axis=1)
    df["Recommended_Actions"] = df.apply(recommended_actions, axis=1)

    # --- KPI row ---
    col1, col2, col3, col4 = st.columns(4)
    total_arr = df["ARR"].sum()
    at_risk_arr = df.loc[df["Health_Band"].isin(["Red", "Yellow"]), "ARR"].sum()
    near_term_mask = df["Days_to_Renewal"].between(0, 180, inclusive="both")
    near_term_arr = df.loc[near_term_mask, "ARR"].sum()
    red_accounts = (df["Health_Band"] == "Red").sum()

    with col1:
        st.metric("Total ARR", f"${total_arr:,.0f}")
    with col2:
        st.metric("ARR (Yellow + Red)", f"${at_risk_arr:,.0f}")
    with col3:
        st.metric("ARR Renewing in 180 Days", f"${near_term_arr:,.0f}")
    with col4:
        st.metric("# Red Accounts", int(red_accounts))

    st.markdown("---")

    # --- Charts ---
    bands = ["Green", "Yellow", "Red"]
    colors = ["#2ecc71", "#f1c40f", "#e74c3c"]
    left, right = st.columns(2)

    with left:
        st.subheader("Health Band Distribution")
        band_counts = (
            df["Health_Band"]
            .value_counts()
            .reindex(bands)
            .fillna(0)
            .reset_index()
        )
        band_counts.columns = ["Health_Band", "Count"]
        chart1 = (
            alt.Chart(band_counts, title="Accounts by Health Band")
            .mark_bar(size=45, cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
            .encode(
                x=alt.X("Health_Band:N", sort=bands, title=""),
                y=alt.Y("Count:Q", title="Accounts", axis=alt.Axis(grid=False)),
                color=alt.Color(
                    "Health_Band:N",
                    scale=alt.Scale(domain=bands, range=colors),
                    legend=None,
                ),
                tooltip=["Health_Band", "Count"],
            )
        )
        st.altair_chart(chart1, use_container_width=True)

    with right:
        st.subheader("ARR by Health Band")
        arr_by_band = (
            df.groupby("Health_Band")["ARR"]
            .sum()
            .reindex(bands)
            .fillna(0)
            .reset_index()
        )
        arr_by_band.columns = ["Health_Band", "ARR"]
        chart2 = (
            alt.Chart(arr_by_band, title="ARR by Health Band")
            .mark_bar(size=45, cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
            .encode(
                x=alt.X("Health_Band:N", sort=bands, title=""),
                y=alt.Y("ARR:Q", title="ARR ($)", axis=alt.Axis(grid=False, format="$,.0f")),
                color=alt.Color(
                    "Health_Band:N",
                    scale=alt.Scale(domain=bands, range=colors),
                    legend=None,
                ),
                tooltip=[alt.Tooltip("Health_Band"), alt.Tooltip("ARR", format="$,.0f")],
            )
        )
        st.altair_chart(chart2, use_container_width=True)

    st.markdown("---")

    # --- Table ---
    st.subheader("Account-Level View")
    seg_filter = st.multiselect(
        "Segment",
        sorted(df["Segment"].unique()),
        default=sorted(df["Segment"].unique()),
    )
    band_filter = st.multiselect(
        "Health Band",
        ["Green", "Yellow", "Red"],
        default=["Green", "Yellow", "Red"],
    )
    risk_filter = st.multiselect(
        "Renewal Risk",
        ["Low", "Medium", "High"],
        default=["Low", "Medium", "High"],
    )

    filtered = df[
        df["Segment"].isin(seg_filter)
        & df["Health_Band"].isin(band_filter)
        & df["Renewal_Risk"].isin(risk_filter)
    ]

    display_cols = [
        "Customer","Segment","ARR","Renewal_Date","Health_Score","Health_Band",
        "Renewal_Risk","Expansion_Potential","NPS","CSAT","Usage_Ratio",
        "Tickets_Last_90d","Days_to_Renewal","Recommended_Actions",
    ]
    st.dataframe(filtered[display_cols].sort_values("Health_Score"))


# ============================================================
# 2️⃣ CLOUD READINESS ASSESSMENT TOOL
# ============================================================
def page_cloud_readiness():
    st.title("2️⃣ Cloud Readiness Assessment Tool")
    st.write(
        """
        A lightweight **AWS CAF / Well-Architected** inspired assessment to understand
        how ready your organization is to move workloads to the cloud.
        """
    )

    # Sidebar config for this app
    st.sidebar.markdown("### ⚙️ Scoring Options")
    label_min = st.sidebar.number_input("Minimum score", 1, 3, 1)
    label_max = st.sidebar.number_input("Maximum score", 3, 5, 5)

    st.markdown("#### Rate your organization (1 = very weak, 5 = excellent)")

    cols1 = st.columns(2)
    with cols1[0]:
        sec_policy = st.slider("Security policies & compliance mapped to cloud", label_min, label_max, 3)
        sec_iam = st.slider("IAM / access model well-defined", label_min, label_max, 3)
        sec_monitor = st.slider("Security monitoring / logging in place", label_min, label_max, 3)
    with cols1[1]:
        ops_incident = st.slider("Incident & on-call process maturity", label_min, label_max, 3)
        ops_ci_cd = st.slider("Automation & CI/CD usage", label_min, label_max, 3)
        ops_backup = st.slider("Backup / DR / resilience posture", label_min, label_max, 3)

    cols2 = st.columns(2)
    with cols2[0]:
        cost_visibility = st.slider("Cost visibility & tagging standards", label_min, label_max, 3)
        cost_optimization = st.slider("Experience with rightsizing / reservations", label_min, label_max, 3)
    with cols2[1]:
        skills_cloud = st.slider("Team cloud skills (AWS / infra)", label_min, label_max, 3)
        skills_agile = st.slider("Agile / program delivery maturity", label_min, label_max, 3)

    if st.button("Run Readiness Assessment"):
        security_score = np.mean([sec_policy, sec_iam, sec_monitor])
        ops_score = np.mean([ops_incident, ops_ci_cd, ops_backup])
        cost_score = np.mean([cost_visibility, cost_optimization])
        skills_score = np.mean([skills_cloud, skills_agile])
        overall = np.mean([security_score, ops_score, cost_score, skills_score])

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Security", f"{security_score:.1f}/5")
        with col2:
            st.metric("Operations", f"{ops_score:.1f}/5")
        with col3:
            st.metric("Cost", f"{cost_score:.1f}/5")
        with col4:
            st.metric("Team Skills", f"{skills_score:.1f}/5")
        with col5:
            st.metric("Overall Readiness", f"{overall:.1f}/5")

        st.markdown("---")

        if overall >= 4:
            phase = "Wave 1–2 ready"
            summary = (
                "You can move business-critical workloads early. Focus on landing zones, "
                "standard architectures, and scaling a migration factory."
            )
        elif overall >= 3:
            phase = "Pilot first, then scale"
            summary = (
                "Start with a structured pilot of 2–3 representative apps. Use lessons learned "
                "to harden security, operations, and cost management before broad rollout."
            )
        else:
            phase = "Foundation first"
            summary = (
                "Invest in cloud foundations: identity, networking, logging, security baselines, "
                "and team enablement before large migrations."
            )

        st.subheader(f"Recommended Migration Posture: **{phase}**")
        st.write(summary)

        st.markdown("##### Suggested Next Steps")
        bullets = []
        if security_score < 3:
            bullets.append("• Define cloud security baseline, guardrails, and IAM patterns.")
        if ops_score < 3:
            bullets.append("• Build SRE-style incident process and observability stack.")
        if cost_score < 3:
            bullets.append("• Stand up FinOps: tagging, budgets, and cost dashboards.")
        if skills_score < 3:
            bullets.append("• Run targeted cloud training and pair with experienced teams.")
        if not bullets:
            bullets.append("• Scale migration factory and tackle more complex workloads.")

        st.write("\n".join(bullets))


# ============================================================
# 3️⃣ PM TOOLKIT + TEMPLATES GENERATOR
# ============================================================

# Directory where PM templates are stored
TEMPLATE_DIR = Path("templates")

# Map display name -> (filename, file_type)
TEMPLATE_FILES = {
    "RAID Log (Risks, Assumptions, Issues, Dependencies)": ("raid_log.csv", "csv"),
    "RACI Matrix": ("raci_matrix.csv", "csv"),
    "Project Charter": ("project_charter.md", "md"),
    "Sprint Board (Backlog CSV)": ("sprint_board.csv", "csv"),
    "Weekly Status Report": ("weekly_status.md", "md"),
    "Executive Summary One-Pager": ("executive_summary.md", "md"),
}

def get_template(name: str):
    if name == "RAID Log (Risks, Assumptions, Issues, Dependencies)":
        return (
            "ID,Type,Risk/Issue,Owner,Impact,Probability,Mitigation/Action,Target Date,Status\n"
            "R1,Risk,Example risk goes here,Owner Name,High,Medium,Mitigation action,2025-01-15,Open\n"
        )
    if name == "RACI Matrix":
        return (
            "Task/Deliverable,R (Responsible),A (Accountable),C (Consulted),I (Informed)\n"
            "Define Scope,Name1,Name2,Name3,Stakeholders\n"
        )
    if name == "Project Charter":
        return (
            "Section,Details\n"
            "Project Name,\n"
            "Sponsor,\n"
            "Problem Statement,\n"
            "Objectives & Success Metrics,\n"
            "Scope (In/Out),\n"
            "Timeline & Milestones,\n"
            "Risks & Assumptions,\n"
        )
    if name == "Sprint Board (Backlog CSV)":
        return (
            "ID,Title,Status,Priority,Story Points,Assignee,Due Date\n"
            "US-1,Example user story,To Do,High,5,Name,2025-01-10\n"
        )
    if name == "Weekly Status Report":
        return (
            "Section,Details\n"
            "Week Ending,\n"
            "Overall RAG (Red/Amber/Green),\n"
            "Accomplishments This Week,\n"
            "Plan for Next Week,\n"
            "Risks & Issues,\n"
            "Decisions Needed,\n"
        )
    if name == "Executive Summary One-Pager":
        return (
            "Section,Details\n"
            "Overview,\n"
            "Business Outcomes,\n"
            "Key Metrics,\n"
            "Timeline & Milestones,\n"
            "Risks & Mitigations,\n"
            "Ask from Leadership,\n"
        )
    return ""


def page_pm_toolkit():
    st.title("3️⃣ Project / Program Management Toolkit")
    st.write(
        """
        Generate and preview **battle-tested PMO templates** stored in the local
        `templates/` folder. These can be used across customer implementations,
        migrations, and internal initiatives.
        """
    )

    # Sidebar config for this app
    st.sidebar.markdown("### ⚙️ Template Options")

    template_names = list(TEMPLATE_FILES.keys())
    selected = st.sidebar.selectbox("Template", template_names)

    st.markdown("#### Template Preview")

    # Ensure templates folder exists
    if not TEMPLATE_DIR.exists():
        st.warning(
            "`templates/` folder not found. "
            "Create it and add the template files, or run your generator script.",
            icon="⚠️",
        )
        return

    # Resolve file mapping
    filename, ftype = TEMPLATE_FILES[selected]
    path = TEMPLATE_DIR / filename

    if not path.exists():
        st.error(f"`{filename}` not found in `templates/`. Please generate templates first.")
        return

    st.subheader(selected)

    # CSV preview
    if ftype == "csv":
        df = pd.read_csv(path)
        st.markdown("**Preview as table**")
        st.dataframe(df, use_container_width=True)

        with st.expander("Show raw CSV"):
            st.code(path.read_text(encoding="utf-8"), language="csv")

        st.download_button(
            label="⬇️ Download CSV",
            data=path.read_text(encoding="utf-8"),
            file_name=filename,
            mime="text/csv",
        )

    # Markdown preview
    elif ftype == "md":
        content = path.read_text(encoding="utf-8")

        tab1, tab2 = st.tabs(["Rendered", "Raw Markdown"])

        with tab1:
            st.markdown(content, unsafe_allow_html=False)

        with tab2:
            st.code(content, language="markdown")

        st.download_button(
            label="⬇️ Download Markdown",
            data=content,
            file_name=filename,
            mime="text/markdown",
        )

    else:
        st.info(f"Unsupported file type `{ftype}` for now.")



# ============================================================
# MAIN NAVIGATION (SIDEBAR)
# ============================================================
st.sidebar.title("📚 Portfolio Hub")
page = st.sidebar.radio(
    "Go to:",
    ["🏠 Landing", "Customer Success Health Dashboard",
     "Cloud Readiness Assessment Tool", "PM Toolkit + Templates Generator"],
)

if page == "🏠 Landing":
    landing_page()
elif page == "Customer Success Health Dashboard":
    page_customer_success()
elif page == "Cloud Readiness Assessment Tool":
    page_cloud_readiness()
else:
    page_pm_toolkit()
