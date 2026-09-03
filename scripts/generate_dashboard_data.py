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


def main():
	"""Generate versioned datasets used by the Streamlit dashboard."""
	OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

	df = load_data()

	travel_summary = generate_travel_type_summary(df)

	print(f"Source dataset: {len(df):,} rows")
	print("\nSatisfaction by Type of Travel:")
	print(travel_summary)
	print("\nDashboard data generated successfully.")


if __name__ == "__main__":
	main()


