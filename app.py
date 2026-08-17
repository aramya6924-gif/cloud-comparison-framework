import streamlit as st
import pandas as pd
import plotly.express as px

from data import USE_CASES, COSTS
from cloud_models import CLOUD_MODELS
from calculations import (
    calculate_all_scores,
    calculate_cost,
    get_best_model
)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="SaaS vs PaaS vs IaaS",
    page_icon="☁️",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# TITLE
# ==================================================

st.markdown(
    '<div class="main-title">☁️ SaaS vs PaaS vs IaaS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Technical & Cost Comparison Framework'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("⚙️ Configuration")

selected_use_case = st.sidebar.selectbox(
    "Select Industry Use Case",
    list(USE_CASES.keys())
)


# ==================================================
# USE CASE INFORMATION
# ==================================================

use_case = USE_CASES[selected_use_case]

st.header("📌 Selected Use Case")

st.info(use_case["description"])

st.write(
    f"**Expected Recommended Model:** "
    f"`{use_case['recommended']}`"
)


# ==================================================
# CALCULATE TECHNICAL SCORES
# ==================================================

scores = calculate_all_scores(
    use_case["weights"]
)

best_model = get_best_model(scores)


# ==================================================
# TOP METRICS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Best Technical Choice",
        best_model
    )

with col2:
    st.metric(
        "Technical Score",
        f"{scores[best_model]}/5"
    )

recommended_cost = calculate_cost(
    COSTS[selected_use_case][best_model]
)

with col3:
    st.metric(
        "Estimated Monthly Cost",
        f"${recommended_cost}"
    )


# ==================================================
# TECHNICAL COMPARISON
# ==================================================

st.header("📊 Technical Comparison")

technical_data = []

for model_name, model in CLOUD_MODELS.items():

    technical_data.append({
        "Model": model_name,
        "Customer Control": model.customer_control,
        "Scalability": model.scalability,
        "Maintenance": model.maintenance,
        "Deployment Speed": model.deployment_speed,
        "Flexibility": model.flexibility,
        "Security Control": model.security_control,
        "Management Effort": model.management_effort,
        "Weighted Score": scores[model_name]
    })


technical_df = pd.DataFrame(
    technical_data
)

st.dataframe(
    technical_df,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# TECHNICAL SCORE GRAPH
# ==================================================

st.subheader("Technical Score Comparison")

score_df = pd.DataFrame({
    "Cloud Model": list(scores.keys()),
    "Score": list(scores.values())
})

fig_score = px.bar(
    score_df,
    x="Cloud Model",
    y="Score",
    text="Score",
    range_y=[0, 5],
    title="Technical Suitability Score"
)

fig_score.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_score,
    use_container_width=True
)


# ==================================================
# COST COMPARISON
# ==================================================

st.header("💰 Cost Comparison")

cost_rows = []

for model_name in CLOUD_MODELS:

    cost_breakdown = COSTS[
        selected_use_case
    ][model_name]

    total = calculate_cost(
        cost_breakdown
    )

    cost_rows.append({
        "Cloud Model": model_name,
        "Compute": cost_breakdown["compute"],
        "Storage": cost_breakdown["storage"],
        "Network": cost_breakdown["network"],
        "Management": cost_breakdown["management"],
        "Total Monthly Cost": total
    })


cost_df = pd.DataFrame(
    cost_rows
)

st.dataframe(
    cost_df,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# COST GRAPH
# ==================================================

st.subheader("Monthly Cost Comparison")

fig_cost = px.bar(
    cost_df,
    x="Cloud Model",
    y="Total Monthly Cost",
    text="Total Monthly Cost",
    title="Estimated Monthly Cloud Cost"
)

fig_cost.update_traces(
    texttemplate="$%{text}",
    textposition="outside"
)

st.plotly_chart(
    fig_cost,
    use_container_width=True
)


# ==================================================
# CLOUD MODEL DETAILS
# ==================================================

st.header("🔍 Cloud Model Details")

tabs = st.tabs(
    ["IaaS", "PaaS", "SaaS"]
)


for tab, model_name in zip(
    tabs,
    ["IaaS", "PaaS", "SaaS"]
):

    with tab:

        model = CLOUD_MODELS[model_name]

        st.subheader(
            model.name
        )

        st.write(
            model.description
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Customer Control:** "
                f"{model.customer_control}/5"
            )

            st.write(
                f"**Scalability:** "
                f"{model.scalability}/5"
            )

            st.write(
                f"**Flexibility:** "
                f"{model.flexibility}/5"
            )

            st.write(
                f"**Security Control:** "
                f"{model.security_control}/5"
            )

        with col2:

            st.write(
                f"**Maintenance:** "
                f"{model.maintenance}/5"
            )

            st.write(
                f"**Deployment Speed:** "
                f"{model.deployment_speed}/5"
            )

            st.write(
                f"**Management Effort:** "
                f"{model.management_effort}/5"
            )

            st.write(
                f"**Suitability Score:** "
                f"{scores[model_name]}/5"
            )


# ==================================================
# FINAL RECOMMENDATION
# ==================================================

st.header("🏆 Final Recommendation")

if best_model == use_case["recommended"]:

    st.success(
        f"For **{selected_use_case}**, the framework "
        f"recommends **{best_model}**."
    )

else:

    st.warning(
        f"The calculated model is **{best_model}**, "
        f"while the predefined recommendation is "
        f"**{use_case['recommended']}**."
    )


st.write(
    "The recommendation is based on weighted technical "
    "criteria and estimated monthly operational costs."
)


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "SaaS vs PaaS vs IaaS Technical & Cost Comparison Framework | "
    "Academic Cloud Computing Project"
)