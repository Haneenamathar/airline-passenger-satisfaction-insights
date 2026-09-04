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

    return (
        passenger_data,
        hypothesis_data,
        service_hypothesis_data,
    )


df, hypothesis_results, service_hypothesis_results = load_data()


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

    total_passengers = len(filtered_df)

    satisfied_passengers = (
        filtered_df["satisfaction"] == "satisfied"
    ).sum()

    satisfaction_rate = (
        satisfied_passengers / total_passengers
    ) * 100

    average_age = filtered_df["Age"].mean()
    average_distance = filtered_df["Flight Distance"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Passengers",
        f"{total_passengers:,}",
    )

    col2.metric(
        "Satisfaction Rate",
        f"{satisfaction_rate:.1f}%",
    )

    col3.metric(
        "Average Age",
        f"{average_age:.1f}",
    )

    col4.metric(
        "Average Flight Distance",
        f"{average_distance:,.0f}",
    )

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

    satisfaction_chart.update_layout(
        xaxis_title="Satisfaction",
        yaxis_title="Number of Passengers",
    )

    st.plotly_chart(
        satisfaction_chart,
        use_container_width=True,
    )

    st.subheader("Key Business Insight")

    st.info(
        "Passenger satisfaction differs considerably across travel "
        "type, travel class and service experience. The remaining "
        "dashboard pages allow these patterns to be explored in "
        "greater detail."
    )


elif page == "Passenger Insights":
    st.title("Passenger Insights")

    st.write(
        "Explore how passenger satisfaction differs across major "
        "passenger and journey characteristics."
    )

    st.info(
        "Passenger-level visualisations will be developed in the "
        "next dashboard stage."
    )


elif page == "Service Experience":
    st.title("Service Experience")

    st.write(
        "Explore which service areas have the strongest relationships "
        "with overall passenger satisfaction."
    )

    st.info(
        "Service-rating visualisations will be developed in the "
        "next dashboard stage."
    )


elif page == "Statistical & Predictive Analysis":
    st.title("Statistical & Predictive Analysis")

    st.write(
        "This section presents the statistical evidence supporting "
        "the dashboard findings."
    )

    st.subheader("Hypothesis Tests")

    st.dataframe(
        hypothesis_results,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Service Rating Associations")

    st.dataframe(
        service_hypothesis_results,
        use_container_width=True,
        hide_index=True,
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
        "non-technical users while also providing more detailed "
        "analytical information for technical users."
    )

    st.subheader("Target Audiences")

    st.markdown(
        """
        **Non-technical users**

        Airline managers, customer-experience teams, service-quality
        teams and operational decision-makers.

        **Technical users**

        Data analysts, data scientists and technically experienced
        stakeholders who require evidence supporting the dashboard
        findings.
        """
    )

    st.subheader("Responsible Interpretation")

    st.warning(
        "The relationships presented in this dashboard are associations "
        "within the available dataset. They should not be interpreted "
        "as proof that one factor directly causes passenger satisfaction."
    )