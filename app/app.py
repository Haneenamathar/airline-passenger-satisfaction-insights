from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path("data/clean_data/airline_clean.csv")
HYPOTHESIS_PATH = Path(
    "data/dashboard_data/hypothesis_results_v1.csv"
)
SERVICE_HYPOTHESIS_PATH = Path(
    "data/dashboard_data/service_hypothesis_results_v1.csv"
)
SERVICE_SUMMARY_PATH = Path(
    "data/dashboard_data/service_rating_summary_v1.csv"
)

st.set_page_config(
    page_title="Airline Passenger Satisfaction Insights",
    page_icon="✈️",
    layout="wide",
)


@st.cache_data
def load_data():
    """Load cleaned passenger data and analytical outputs."""
    passenger_data = pd.read_csv(DATA_PATH)
    hypothesis_data = pd.read_csv(HYPOTHESIS_PATH)
    service_hypothesis_data = pd.read_csv(
        SERVICE_HYPOTHESIS_PATH
    )
    service_summary_data = pd.read_csv(
    SERVICE_SUMMARY_PATH
)

    return (
    passenger_data,
    hypothesis_data,
    service_hypothesis_data,
    service_summary_data,
)    


(
    df,
    hypothesis_results,
    service_hypothesis_results,
    service_summary,
) = load_data()


st.sidebar.title("Dashboard Navigation")

page = st.sidebar.radio(
    "Select a page",
    [
        "Executive Overview",
        "Passenger Insights",
        "Service Experience",
        "Statistical & Predictive Analysis",
        "Project Information",
    ],
)


st.sidebar.divider()
st.sidebar.subheader("Passenger Filters")

travel_type_options = sorted(df["Type of Travel"].dropna().unique())
class_options = sorted(df["Class"].dropna().unique())
customer_type_options = sorted(df["Customer Type"].dropna().unique())
gender_options = sorted(df["Gender"].dropna().unique())

selected_travel_types = st.sidebar.multiselect(
    "Type of Travel",
    travel_type_options,
    default=travel_type_options,
)

selected_classes = st.sidebar.multiselect(
    "Travel Class",
    class_options,
    default=class_options,
)

selected_customer_types = st.sidebar.multiselect(
    "Customer Type",
    customer_type_options,
    default=customer_type_options,
)

selected_genders = st.sidebar.multiselect(
    "Gender",
    gender_options,
    default=gender_options,
)


filtered_df = df[
    df["Type of Travel"].isin(selected_travel_types)
    & df["Class"].isin(selected_classes)
    & df["Customer Type"].isin(selected_customer_types)
    & df["Gender"].isin(selected_genders)
].copy()


if filtered_df.empty:
    st.warning(
        "No passengers match the selected filters. "
        "Please adjust the sidebar selections."
    )
    st.stop()


if page == "Executive Overview":
    st.title("Airline Passenger Satisfaction Insights")

    st.caption(
        "Interactive business and analytical insights into the factors "
        "associated with passenger satisfaction."
    )

    # ---------------------------------------------------------
    # Executive KPIs
    # ---------------------------------------------------------
    total_passengers = len(filtered_df)

    satisfied_passengers = (
        filtered_df["satisfaction"]
        .eq("satisfied")
        .sum()
    )

    satisfaction_rate = (
        satisfied_passengers / total_passengers * 100
        if total_passengers > 0
        else 0
    )

    average_age = filtered_df["Age"].mean()
    average_flight_distance = filtered_df["Flight Distance"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Passengers",
        f"{total_passengers:,}"
    )

    col2.metric(
        "Satisfaction Rate",
        f"{satisfaction_rate:.1f}%"
    )

    col3.metric(
        "Average Age",
        f"{average_age:.1f}"
    )

    col4.metric(
        "Average Flight Distance",
        f"{average_flight_distance:,.0f}"
    )

    # ---------------------------------------------------------
    # Overall Satisfaction
    # ---------------------------------------------------------
    st.subheader("Overall Passenger Satisfaction")

    satisfaction_counts = (
        filtered_df["satisfaction"]
        .value_counts()
        .rename_axis("Satisfaction")
        .reset_index(name="Passengers")
    )

    satisfaction_chart = px.bar(
        satisfaction_counts,
        x="Satisfaction",
        y="Passengers",
        text="Passengers",
        title="Passenger Satisfaction Distribution",
    )

    satisfaction_chart.update_traces(
        texttemplate="%{text:,}",
        textposition="inside"
    )

    satisfaction_chart.update_layout(
        xaxis_title="Satisfaction",
        yaxis_title="Number of Passengers",
        showlegend=False,
    )

    st.plotly_chart(
        satisfaction_chart,
        use_container_width=True
    )

    st.info(
        "Use the passenger filters in the sidebar to explore how the "
        "headline metrics and satisfaction distribution change across "
        "different passenger groups."
    )

    # ---------------------------------------------------------
    # Key Project Findings
    # ---------------------------------------------------------
    st.subheader("Key Project Findings")

    st.caption(
        "The findings below are based on the complete cleaned dataset "
        "and validated statistical analysis. They are not recalculated "
        "when the sidebar filters are changed."
    )

    finding_col1, finding_col2, finding_col3 = st.columns(3)

    with finding_col1:
        st.metric(
            "Travel Type Association",
            "Cramér's V = 0.449"
        )
        st.write(
            "**Business travellers show substantially higher satisfaction "
            "than personal travellers.**"
        )
        st.caption(
            "Chi-square testing confirmed a statistically significant "
            "association between Type of Travel and Satisfaction "
            "(p < 0.001)."
        )

    with finding_col2:
        st.metric(
            "Travel Class Association",
            "Cramér's V = 0.505"
        )
        st.write(
            "**Business Class shows considerably higher satisfaction "
            "than Eco and Eco Plus.**"
        )
        st.caption(
            "Travel Class demonstrated a substantial statistically "
            "significant association with Satisfaction (p < 0.001)."
        )

    with finding_col3:
        st.metric(
            "Strongest Service Association",
            "ρ = 0.551"
        )
        st.write(
            "**Online boarding has the strongest positive service-rating "
            "association with passenger satisfaction.**"
        )
        st.caption(
            "Inflight entertainment and seat comfort were also among "
            "the stronger service relationships."
        )

    # ---------------------------------------------------------
    # Management Priorities
    # ---------------------------------------------------------
    st.subheader("Management Priorities")

    priority_col1, priority_col2 = st.columns(2)

    with priority_col1:
        st.markdown(
            """
            **1. Review the digital passenger journey**

            Online boarding shows the strongest service-rating association
            with satisfaction and also appeared prominently in the
            predictive analysis.

            **2. Investigate the onboard experience**

            Inflight entertainment, seat comfort, on-board service,
            leg room and cleanliness all show meaningful differences
            between satisfaction groups.
            """
        )

    with priority_col2:
        st.markdown(
            """
            **3. Examine lower-satisfaction passenger segments**

            Personal travellers and Economy passengers show substantially
            lower satisfaction than the corresponding comparison groups.

            **4. Use predictive results as decision support**

            The Random Forest model achieved strong test performance,
            but model findings should be validated on new operational
            data before real-world use.
            """
        )

    st.warning(
        "These findings identify associations and predictive relationships. "
        "They should guide further investigation and should not be "
        "interpreted as proof that any individual factor directly causes "
        "passenger satisfaction."
    )

    # ---------------------------------------------------------
    # Dashboard Guide
    # ---------------------------------------------------------
    st.subheader("Explore the Dashboard")

    guide_col1, guide_col2, guide_col3 = st.columns(3)

    with guide_col1:
        st.markdown(
            """
            ### 👥 Passenger Insights

            Explore satisfaction across:

            - Type of Travel
            - Travel Class
            - Customer Type
            - Gender
            - Age
            """
        )

    with guide_col2:
        st.markdown(
            """
            ### ✈️ Service Experience

            Investigate:

            - Service-rating differences
            - Strongest service relationships
            - Spearman correlations
            - Customer-experience priorities
            """
        )

    with guide_col3:
        st.markdown(
            """
            ### 📊 Statistical & Predictive Analysis

            Review:

            - H1, H2 and H3
            - Chi-square tests
            - Cramér's V
            - Spearman results
            - Machine-learning performance
            """
        )

    st.success(
        "For project methodology, ethics, privacy, GDPR, governance, "
        "limitations and responsible interpretation, visit the "
        "'Project Information' page."
    )


elif page == "Passenger Insights":
    st.title("Passenger Insights")

    st.write(
        "Explore how passenger satisfaction differs across major "
        "passenger and journey characteristics."
    )

    # ---------------------------------------------------------
    # Satisfaction by Type of Travel
    # ---------------------------------------------------------
    st.subheader("Satisfaction by Type of Travel")

    travel_summary = (
        filtered_df.groupby(
            ["Type of Travel", "satisfaction"]
        )
        .size()
        .reset_index(name="Passengers")
    )

    travel_totals = (
        travel_summary.groupby("Type of Travel")["Passengers"]
        .transform("sum")
    )

    travel_summary["Percentage"] = (
        travel_summary["Passengers"] / travel_totals * 100
    )

    travel_chart = px.bar(
        travel_summary,
        x="Type of Travel",
        y="Percentage",
        color="satisfaction",
        barmode="group",
        text="Percentage",
        title="Passenger Satisfaction by Type of Travel",
    )

    travel_chart.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )

    travel_chart.update_layout(
        xaxis_title="Type of Travel",
        yaxis_title="Passengers (%)",
        legend_title="Satisfaction",
    )

    st.plotly_chart(
        travel_chart,
        use_container_width=True,
    )

    st.caption(
        "Business and personal travellers show noticeably different "
        "satisfaction patterns in the dataset."
    )

    # ---------------------------------------------------------
    # Satisfaction by Travel Class
    # ---------------------------------------------------------
    st.subheader("Satisfaction by Travel Class")

    class_summary = (
        filtered_df.groupby(
            ["Class", "satisfaction"]
        )
        .size()
        .reset_index(name="Passengers")
    )

    class_totals = (
        class_summary.groupby("Class")["Passengers"]
        .transform("sum")
    )

    class_summary["Percentage"] = (
        class_summary["Passengers"] / class_totals * 100
    )

    class_chart = px.bar(
        class_summary,
        x="Class",
        y="Percentage",
        color="satisfaction",
        barmode="group",
        text="Percentage",
        title="Passenger Satisfaction by Travel Class",
    )

    class_chart.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )

    class_chart.update_layout(
        xaxis_title="Travel Class",
        yaxis_title="Passengers (%)",
        legend_title="Satisfaction",
    )

    st.plotly_chart(
        class_chart,
        use_container_width=True,
    )

    st.caption(
        "Satisfaction levels vary substantially across travel classes."
    )

    # ---------------------------------------------------------
    # Satisfaction by Customer Type
    # ---------------------------------------------------------
    st.subheader("Satisfaction by Customer Type")

    customer_summary = (
        filtered_df.groupby(
            ["Customer Type", "satisfaction"]
        )
        .size()
        .reset_index(name="Passengers")
    )

    customer_totals = (
        customer_summary.groupby("Customer Type")["Passengers"]
        .transform("sum")
    )

    customer_summary["Percentage"] = (
        customer_summary["Passengers"] / customer_totals * 100
    )

    customer_chart = px.bar(
        customer_summary,
        x="Customer Type",
        y="Percentage",
        color="satisfaction",
        barmode="group",
        text="Percentage",
        title="Passenger Satisfaction by Customer Type",
    )

    customer_chart.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )

    customer_chart.update_layout(
        xaxis_title="Customer Type",
        yaxis_title="Passengers (%)",
        legend_title="Satisfaction",
    )

    st.plotly_chart(
        customer_chart,
        use_container_width=True,
    )

    # ---------------------------------------------------------
    # Satisfaction by Gender
    # ---------------------------------------------------------
    st.subheader("Satisfaction by Gender")

    gender_summary = (
        filtered_df.groupby(
            ["Gender", "satisfaction"]
        )
        .size()
        .reset_index(name="Passengers")
    )

    gender_totals = (
        gender_summary.groupby("Gender")["Passengers"]
        .transform("sum")
    )

    gender_summary["Percentage"] = (
        gender_summary["Passengers"] / gender_totals * 100
    )

    gender_chart = px.bar(
        gender_summary,
        x="Gender",
        y="Percentage",
        color="satisfaction",
        barmode="group",
        text="Percentage",
        title="Passenger Satisfaction by Gender",
    )

    gender_chart.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )

    gender_chart.update_layout(
        xaxis_title="Gender",
        yaxis_title="Passengers (%)",
        legend_title="Satisfaction",
    )

    st.plotly_chart(
        gender_chart,
        use_container_width=True,
    )

    # ---------------------------------------------------------
    # Age Distribution
    # ---------------------------------------------------------
    st.subheader("Passenger Age Distribution")

    age_chart = px.histogram(
        filtered_df,
        x="Age",
        color="satisfaction",
        nbins=20,
        barmode="overlay",
        title="Age Distribution by Satisfaction",
    )

    age_chart.update_layout(
        xaxis_title="Age",
        yaxis_title="Number of Passengers",
        legend_title="Satisfaction",
    )

    st.plotly_chart(
        age_chart,
        use_container_width=True,
    )

    st.info(
        "Use the sidebar filters to compare specific travel classes, "
        "travel types, customer groups and genders. Percentages in the "
        "categorical charts are calculated within each group so that "
        "groups of different sizes can be compared fairly."
    )

elif page == "Service Experience":
    st.title("Service Experience")

    st.write(
        "Explore which airline service areas show the strongest "
        "relationships with overall passenger satisfaction."
    )

    # ---------------------------------------------------------
    # Service Rating Differences
    # ---------------------------------------------------------
    st.subheader("Service Rating Differences")

    service_difference_data = service_summary.sort_values(
        "Rating Difference",
        ascending=True,
    )

    difference_chart = px.bar(
        service_difference_data,
        x="Rating Difference",
        y="Service",
        orientation="h",
        title=(
            "Difference in Average Service Ratings: "
            "Satisfied vs Dissatisfied Passengers"
        ),
    )

    difference_chart.update_layout(
        xaxis_title="Average Rating Difference",
        yaxis_title="Service Area",
    )

    st.plotly_chart(
        difference_chart,
        use_container_width=True,
    )

    st.caption(
        "Positive values indicate that satisfied passengers gave "
        "higher average ratings to that service area."
    )

    # ---------------------------------------------------------
    # Strongest Service Associations
    # ---------------------------------------------------------
    st.subheader("Strongest Associations with Satisfaction")

    correlation_data = service_hypothesis_results.sort_values(
        "Spearman Correlation",
        ascending=True,
    )

    correlation_chart = px.bar(
        correlation_data,
        x="Spearman Correlation",
        y="Service",
        orientation="h",
        title="Service Rating Association with Passenger Satisfaction",
    )

    correlation_chart.update_layout(
        xaxis_title="Spearman Correlation",
        yaxis_title="Service Area",
    )

    st.plotly_chart(
        correlation_chart,
        use_container_width=True,
    )

    # ---------------------------------------------------------
    # Key Findings
    # ---------------------------------------------------------
    st.subheader("Key Findings")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Strongest Association",
        "Online boarding",
        "ρ = 0.551",
    )

    col2.metric(
        "Second Strongest",
        "Inflight entertainment",
        "ρ = 0.400",
    )

    col3.metric(
        "Third Strongest",
        "Seat comfort",
        "ρ = 0.362",
    )

    st.success(
        "Online boarding shows the strongest positive association "
        "with passenger satisfaction among the service ratings "
        "analysed. Inflight entertainment and seat comfort also "
        "show notable positive relationships."
    )

    st.info(
        "Gate location shows almost no association with satisfaction "
        "in this dataset. Departure/arrival time convenience shows "
        "only a very small negative association."
    )

    st.warning(
        "These results describe statistical associations, not causal "
        "effects. A stronger correlation does not prove that improving "
        "a service will directly cause an equivalent increase in "
        "passenger satisfaction."
    )


elif page == "Statistical & Predictive Analysis":
    st.title("Statistical & Predictive Analysis")

    st.write(
        "This page provides the technical evidence supporting the "
        "business insights presented elsewhere in the dashboard."
    )

    # ---------------------------------------------------------
    # H1 - Type of Travel
    # ---------------------------------------------------------
    st.subheader("H1 — Type of Travel and Passenger Satisfaction")

    st.markdown(
        """
        **Null hypothesis (H0):** Type of Travel and passenger
        satisfaction are independent.

        **Alternative hypothesis (H1):** Type of Travel and passenger
        satisfaction are associated.
        """
    )

    h1_row = hypothesis_results[
        hypothesis_results["Hypothesis"] == "H1"
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Chi-square",
        f"{h1_row['Chi-square']:,.2f}",
    )


    h1_cramers_v = h1_row["Cramer's V"]

    col2.metric(
    "Cramér's V",
    f"{h1_cramers_v:.3f}",
)

    col3.metric(
        "P-value",
        "p < 0.001",
    )

    st.success(
        "H0 is rejected. Type of Travel has a statistically significant "
        "association with passenger satisfaction. Cramér's V of 0.449 "
        "indicates a meaningful relationship in this dataset."
    )

    # ---------------------------------------------------------
    # H2 - Travel Class
    # ---------------------------------------------------------
    st.subheader("H2 — Travel Class and Passenger Satisfaction")

    st.markdown(
        """
        **Null hypothesis (H0):** Travel Class and passenger
        satisfaction are independent.

        **Alternative hypothesis (H1):** Travel Class and passenger
        satisfaction are associated.
        """
    )

    h2_row = hypothesis_results[
        hypothesis_results["Hypothesis"] == "H2"
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Chi-square",
        f"{h2_row['Chi-square']:,.2f}",
    )

    h2_cramers_v = h2_row["Cramer's V"]

    col2.metric(
    "Cramér's V",
    f"{h2_cramers_v:.3f}",
)

    col3.metric(
        "P-value",
        "p < 0.001",
    )

    st.success(
        "H0 is rejected. Travel Class has a statistically significant "
        "association with passenger satisfaction. Cramér's V of 0.505 "
        "shows a substantial relationship within this dataset."
    )

    # ---------------------------------------------------------
    # H3 - Service Ratings
    # ---------------------------------------------------------
    st.subheader("H3 — Service Ratings and Passenger Satisfaction")

    st.markdown(
        """
        **Hypothesis:** Airline service ratings are associated with
        passenger satisfaction, with some service areas showing
        stronger relationships than others.

        Spearman rank correlation is used because the service ratings
        are ordered scores. Satisfaction is represented as a binary
        outcome for this analysis.
        """
    )

    h3_chart_data = service_hypothesis_results.sort_values(
        "Spearman Correlation",
        ascending=True,
    )

    h3_chart = px.bar(
        h3_chart_data,
        x="Spearman Correlation",
        y="Service",
        orientation="h",
        title="Spearman Association Between Service Ratings and Satisfaction",
        text="Spearman Correlation",
    )

    h3_chart.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside",
    )

    h3_chart.update_layout(
        xaxis_title="Spearman Correlation (ρ)",
        yaxis_title="Service Area",
    )

    st.plotly_chart(
        h3_chart,
        use_container_width=True,
    )

    st.success(
        "Online boarding has the strongest positive association with "
        "passenger satisfaction (ρ = 0.551), followed by inflight "
        "entertainment (ρ = 0.400) and seat comfort (ρ = 0.362)."
    )

    st.info(
        "Gate location shows essentially no association "
        "(ρ ≈ 0, p = 0.901). Departure/arrival time convenience has "
        "a statistically significant but extremely small negative "
        "association (ρ = -0.050). This illustrates why effect size "
        "should be considered alongside statistical significance."
    )

    # ---------------------------------------------------------
    # Statistical Results Table
    # ---------------------------------------------------------
    st.subheader("Hypothesis Test Results")

    hypothesis_display = hypothesis_results.copy()

    hypothesis_display["P-value"] = hypothesis_display[
        "P-value"
    ].apply(
        lambda value: (
            "p < 0.001"
            if value < 0.001
            else f"p = {value:.3f}"
        )
    )

    st.dataframe(
        hypothesis_display,
        use_container_width=True,
        hide_index=True,
    )

    # ---------------------------------------------------------
    # Service Correlation Results
    # ---------------------------------------------------------
    with st.expander("View complete service correlation results"):
        service_display = service_hypothesis_results.copy()

        service_display["P-value"] = service_display[
            "P-value"
        ].apply(
            lambda value: (
                "p < 0.001"
                if value < 0.001
                else f"p = {value:.3f}"
            )
        )

        st.dataframe(
            service_display,
            use_container_width=True,
            hide_index=True,
        )

    # ---------------------------------------------------------
    # Predictive Modelling
    # ---------------------------------------------------------
    st.subheader("Predictive Model Performance")

    model_results = pd.DataFrame(
        {
            "Model": [
                "Baseline",
                "Logistic Regression",
                "Random Forest",
            ],
            "Accuracy (%)": [
                56.70,
                87.18,
                96.42,
            ],
        }
    )

    model_chart = px.bar(
        model_results,
        x="Model",
        y="Accuracy (%)",
        text="Accuracy (%)",
        title="Predictive Model Accuracy Comparison",
    )

    model_chart.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside",
    )

    model_chart.update_layout(
        yaxis_title="Accuracy (%)",
        xaxis_title="Model",
    )

    st.plotly_chart(
        model_chart,
        use_container_width=True,
    )

    st.success(
        "The Random Forest model achieved the highest accuracy at "
        "96.42%, compared with 87.18% for Logistic Regression and "
        "56.70% for the baseline model."
    )

    st.warning(
        "Predictive performance and feature importance should not be "
        "interpreted as evidence of causation. Model results indicate "
        "which variables are useful for prediction within this dataset."
    )

    # ---------------------------------------------------------
    # Technical Interpretation
    # ---------------------------------------------------------
    st.subheader("Technical Interpretation")

    st.markdown(
        """
        - **H1:** Type of Travel is associated with passenger satisfaction.
        - **H2:** Travel Class is associated with passenger satisfaction.
        - **H3:** Service ratings show different strengths of association
          with satisfaction, with Online boarding showing the strongest
          relationship among the analysed service ratings.
        - Statistical significance is considered together with effect
          size because a large dataset can produce very small p-values
          even for weak relationships.
        - The analyses identify associations and predictive patterns;
          they do not establish causal relationships.
        """
    )
elif page == "Project Information":
    st.title("Project Information")

    st.subheader("Project Purpose")

    st.write(
        "The purpose of this project is to transform the findings from "
        "the Airline Passenger Satisfaction analysis into an interactive "
        "data application that enables users to explore the factors "
        "influencing passenger satisfaction."
    )

    st.write(
        "The application presents clear business-focused insights for "
        "non-technical users while also providing more detailed analytical "
        "information for technical users. The goal is to support "
        "data-driven decision-making by identifying service areas, "
        "passenger characteristics and travel experiences that are "
        "strongly associated with customer satisfaction."
    )

    st.subheader("Business Requirements")

    st.markdown(
        """
        **BR1 — Understand passenger satisfaction patterns**

        Provide an interactive overview of passenger satisfaction and allow
        users to investigate differences across passenger characteristics,
        customer type, travel type and class.

        **BR2 — Identify key drivers of passenger satisfaction**

        Allow users to investigate which airline service ratings and
        travel-related factors have the strongest relationships with
        overall passenger satisfaction.

        **BR3 — Support data-driven service improvement**

        Enable non-technical airline stakeholders to identify weaker service
        areas, important passenger segments and potential opportunities for
        improving passenger experience.

        **BR4 — Validate insights with analytical evidence**

        Provide technical users with statistical evidence, hypothesis-testing
        results and relevant model findings so dashboard conclusions can be
        traced to the underlying analysis.
        """
    )

    st.subheader("Target Audiences")

    audience_col1, audience_col2 = st.columns(2)

    with audience_col1:
        st.markdown(
            """
            ### Non-Technical Users

            Intended users include:

            - Airline managers
            - Customer-experience teams
            - Service-quality teams
            - Operational decision-makers

            These users are supported through KPI metrics, interactive
            visualisations, plain-language interpretation and practical
            business recommendations.
            """
        )

    with audience_col2:
        st.markdown(
            """
            ### Technical Users

            Intended users include:

            - Data analysts
            - Data scientists
            - Technically experienced stakeholders

            These users are supported through methodology, statistical
            testing, effect sizes, correlation results, predictive-model
            findings, assumptions and limitations.
            """
        )

    st.subheader("Data and Methodology")

    st.write(
        "The analysis uses a cleaned dataset containing 103,594 passenger "
        "records and 23 variables covering passenger characteristics, "
        "travel information, airline service ratings, flight delays and "
        "overall passenger satisfaction."
    )

    st.markdown(
        """
        The analytical workflow includes:

        - Data collection and inspection
        - Data cleaning and validation
        - Exploratory data analysis
        - Chi-square tests of independence
        - Cramér's V effect-size analysis
        - Spearman rank correlation
        - Logistic Regression
        - Random Forest classification
        - Versioned dashboard-data outputs
        - Interactive Streamlit visualisation
        """
    )

    st.info(
        "Versioned analytical outputs used by the dashboard are stored in "
        "'data/dashboard_data/' and can be regenerated using the project "
        "scripts."
    )

    st.subheader("Ethics, Privacy and Responsible Data Use")

    st.markdown(
        """
        The project uses an analytical dataset that does not contain direct
        passenger identifiers such as names, email addresses, telephone
        numbers or home addresses.

        Unnecessary identifier columns were removed during data cleaning.
        Only variables relevant to the analytical purpose were retained,
        supporting the principle of **data minimisation**.

        The project analyses aggregate passenger-satisfaction patterns and
        is not intended to identify individual passengers or make automated
        decisions about individuals.
        """
    )

    st.subheader("GDPR and Data Governance Considerations")

    st.markdown(
        """
        Important responsible-data principles include:

        - **Purpose limitation:** passenger data should only be used for
          clearly defined and legitimate analytical purposes.
        - **Data minimisation:** only information required for the analysis
          should be collected and retained.
        - **Access control:** passenger-level information should only be
          accessible to authorised users.
        - **Data quality:** conclusions depend on accurate, complete and
          appropriately maintained data.
        - **Retention:** passenger-level information should not be retained
          indefinitely without a legitimate reason.
        - **Transparency:** organisations should explain how customer data
          is used for analytics and predictive modelling.
        - **Accountability:** analytical models and dashboards should have
          documented ownership, validation processes and human oversight.
        """
    )

    st.warning(
        "A real airline deployment involving identifiable passenger data "
        "would require additional legal, security and organisational "
        "controls based on the applicable jurisdiction, lawful basis for "
        "processing and company data-governance policies."
    )

    st.subheader("Dashboard Accessibility and User Experience")

    st.markdown(
        """
        The application was designed for both technical and non-technical
        audiences using:

        - Clear page navigation
        - Descriptive headings and chart titles
        - KPI metrics
        - Plain-language explanations
        - Interactive filters
        - Percentage-based group comparisons
        - Written interpretation alongside visualisations
        - Separate technical and business-focused sections
        - Statistical interpretation warnings where appropriate

        The dashboard does not rely on visualisations alone; key findings are
        also communicated through written explanations and metrics.
        """
    )

    st.subheader("Project Limitations")

    st.markdown(
        """
        - The analysis is based on a historical public dataset rather than
          live airline operational data.
        - Passenger service ratings are subjective.
        - Statistical association does not demonstrate causation.
        - Model performance may not generalise to future passengers, another
          airline or a different operational environment.
        - Large sample sizes can make very small relationships statistically
          significant.
        - Predictive models should be validated on new data before real-world
          operational use.
        - The dashboard is intended for analytical exploration and decision
          support rather than automated decision-making.
        """
    )

    st.subheader("Responsible Interpretation")

    st.warning(
        "Dashboard findings should be used as evidence to support further "
        "investigation and business decision-making. Correlations, group "
        "differences and machine-learning feature importance should not be "
        "interpreted as proof that an individual factor directly causes "
        "passenger satisfaction."
    )
