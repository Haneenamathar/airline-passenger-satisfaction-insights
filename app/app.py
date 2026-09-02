
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Airline Passenger Satisfaction",
    page_icon="✈️",
    layout="wide"
)


@st.cache_data
def load_data():
    return pd.read_csv("data/clean_data/airline_clean.csv")


df = load_data()


def reset_filters():
    st.session_state["travel_filter"] = "All"
    st.session_state["class_filter"] = "All"
    st.session_state["customer_filter"] = "All"
    st.session_state["gender_filter"] = "All"


st.sidebar.header("Dashboard Filters")

travel_filter = st.sidebar.selectbox(
    "Type of Travel",
    ["All"] + sorted(df["Type of Travel"].unique().tolist()),
    key="travel_filter"
)

class_filter = st.sidebar.selectbox(
    "Travel Class",
    ["All"] + sorted(df["Class"].unique().tolist()),
    key="class_filter"
)

customer_filter = st.sidebar.selectbox(
    "Customer Type",
    ["All"] + sorted(df["Customer Type"].unique().tolist()),
    key="customer_filter"
)

gender_filter = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df["Gender"].unique().tolist()),
    key="gender_filter"
)



st.sidebar.button(
    "Reset Filters",
    on_click=reset_filters
)

filtered_df = df.copy()

if travel_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Type of Travel"] == travel_filter
    ]

if class_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Class"] == class_filter
    ]

if customer_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Customer Type"] == customer_filter
    ]

if gender_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender_filter
    ]



st.title("Airline Passenger Satisfaction Analysis 2026")

st.write(
    "This dashboard presents key findings from the airline passenger "
    "satisfaction analysis, including passenger satisfaction patterns, "
    "service experience and machine learning results."
)

st.subheader("Key Metrics")

total_passengers = len(filtered_df)

satisfied_percentage = (
    (filtered_df["satisfaction"] == "satisfied").mean() * 100
)

average_age = filtered_df["Age"].mean()

average_flight_distance = filtered_df[
    "Flight Distance"
].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Passengers",
    f"{total_passengers:,}"
)

col2.metric(
    "Satisfied Passengers",
    f"{satisfied_percentage:.1f}%"
)

col3.metric(
    "Average Age",
    f"{average_age:.1f} years"
)

col4.metric(
    "Average Flight Distance",
    f"{average_flight_distance:,.0f}"
)

st.subheader("Passenger Satisfaction")

satisfaction_counts = (
    filtered_df["satisfaction"]
    .value_counts()
    .rename_axis("Satisfaction")
    .reset_index(name="Count")
)

st.bar_chart(
    satisfaction_counts,
    x="Satisfaction",
    y="Count"
)

st.subheader("Satisfaction by Type of Travel")

travel_satisfaction = pd.crosstab(
    filtered_df["Type of Travel"],
    filtered_df["satisfaction"],
    normalize="index"
) * 100

st.bar_chart(travel_satisfaction)

st.subheader("Top Service Rating Differences")

service_columns = [
    "Inflight wifi service",
    "Departure/Arrival time convenient",
    "Ease of Online booking",
    "Gate location",
    "Food and drink",
    "Online boarding",
    "Seat comfort",
    "Inflight entertainment",
    "On-board service",
    "Leg room service",
    "Baggage handling",
    "Checkin service",
    "Inflight service",
    "Cleanliness"
]

service_means = (
    filtered_df.groupby("satisfaction")[service_columns]
    .mean()
    .T
)

service_means["Rating Difference"] = (
    service_means["satisfied"]
    - service_means["neutral or dissatisfied"]
)

top_service_differences = (
    service_means["Rating Difference"]
    .sort_values(ascending=False)
    .head(5)
)

st.bar_chart(top_service_differences)


st.subheader("Machine Learning Performance")

model_results = pd.DataFrame({
    "Model": [
        "Baseline",
        "Logistic Regression",
        "Random Forest"
    ],
    "Accuracy (%)": [
        56.7,
        87.18,
        96.42
    ]
})

import plotly.express as px

fig = px.bar(
    model_results,
    x="Model",
    y="Accuracy (%)",
    text="Accuracy (%)",
    range_y=[0, 100]
)

fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")

fig.update_layout(
    yaxis_title="Accuracy (%)",
    xaxis_title="Model"
)

st.plotly_chart(fig, use_container_width=True)

st.success(
    "Random Forest was selected as the final model, achieving "
    "96.42% accuracy on the test dataset."
)

st.subheader("Top Predictors of Passenger Satisfaction")

feature_importance = pd.DataFrame({
    "Feature": [
        "Online boarding",
        "Inflight wifi service",
        "Business Class",
        "Personal Travel",
        "Business Travel",
        "Seat comfort",
        "Inflight entertainment",
        "Economy Class",
        "Ease of Online booking",
        "On-board service"
    ],
    "Importance": [
        0.156948,
        0.142722,
        0.085123,
        0.061305,
        0.054054,
        0.051264,
        0.044756,
        0.035946,
        0.034350,
        0.032381
    ]
})

feature_importance = feature_importance.set_index("Feature")

st.bar_chart(feature_importance)

st.info(
    "Online boarding and inflight WiFi service were the two most "
    "important predictors in the Random Forest model. Feature importance "
    "shows predictive contribution and should not be interpreted as causation."
)


st.subheader("Business Recommendations")

st.markdown(
    """
    Based on the analysis, the airline should prioritise improvements in:

    - **Online boarding**, which showed the strongest relationship with passenger satisfaction.
    - **Inflight WiFi service**, which was one of the most important predictive features.
    - **Seat comfort, inflight entertainment and onboard service**, which showed clear differences between satisfied and dissatisfied passengers.
    - **Passenger segmentation by travel type and class**, because satisfaction patterns differed substantially across these groups.

    These findings can support targeted service improvements and help the airline focus resources on areas most closely associated with passenger satisfaction.
    """
)