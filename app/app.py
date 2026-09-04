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