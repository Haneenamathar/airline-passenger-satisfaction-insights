from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/clean_data/airline_clean.csv")
OUTPUT_DIR = Path("data/dashboard_data")


def load_data():
	"""Load the cleaned airline passenger satisfaction dataset."""
	return pd.read_csv(DATA_PATH)


def generate_travel_type_summary(df):
	"""Create satisfaction counts grouped by type of travel."""
	summary = pd.crosstab(
		df["Type of Travel"],
		df["satisfaction"]
	).reset_index()

	OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
	output_path = OUTPUT_DIR / "satisfaction_by_travel_type_v1.csv"
	summary.to_csv(output_path, index=False)

	return summary

def generate_class_summary(df):
    """Create satisfaction counts grouped by travel class."""
    summary = pd.crosstab(
        df["Class"],
        df["satisfaction"]
    ).reset_index()

    output_path = OUTPUT_DIR / "satisfaction_by_class_v1.csv"
    summary.to_csv(output_path, index=False)

    return summary

def generate_service_rating_summary(df):
    """Compare average service ratings by passenger satisfaction."""
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
        "Cleanliness",
    ]

    summary = (
        df.groupby("satisfaction")[service_columns]
        .mean()
        .T
        .reset_index()
        .rename(columns={"index": "Service"})
    )

    summary["Rating Difference"] = (
        summary["satisfied"]
        - summary["neutral or dissatisfied"]
    )

    summary = summary.sort_values(
        "Rating Difference",
        ascending=False
    )

    output_path = OUTPUT_DIR / "service_rating_summary_v1.csv"
    summary.to_csv(output_path, index=False)

    return summary


def main():
    """Generate versioned datasets used by the Streamlit dashboard."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_data()

    travel_summary = generate_travel_type_summary(df)
    class_summary = generate_class_summary(df)
    service_summary = generate_service_rating_summary(df)

    print(f"Source dataset: {len(df):,} rows")
    print("\nSatisfaction by Type of Travel:")
    print(travel_summary)

    print("\nSatisfaction by Travel Class:")
    print(class_summary)

    print("\nService Rating Differences:")
    print(service_summary)

    print("\nDashboard data generated successfully.")


if __name__ == "__main__":
    main()
	


