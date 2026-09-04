from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, spearmanr


DATA_PATH = Path("data/clean_data/airline_clean.csv")
OUTPUT_PATH = Path(
    "data/dashboard_data/hypothesis_results_v1.csv"
)

H3_OUTPUT_PATH = Path(
    "data/dashboard_data/service_hypothesis_results_v1.csv"
)

SERVICE_COLUMNS = [
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

def load_data():
    """Load the cleaned airline passenger satisfaction dataset."""
    return pd.read_csv(DATA_PATH)


def calculate_cramers_v(contingency_table):
    """Calculate Cramér's V effect size for a contingency table."""
    chi2, _, _, _ = chi2_contingency(contingency_table)

    n = contingency_table.to_numpy().sum()
    rows, columns = contingency_table.shape

    return np.sqrt(
        chi2 / (n * min(rows - 1, columns - 1))
    )


def validate_travel_type_hypothesis(df):
    """Test association between type of travel and satisfaction."""
    contingency_table = pd.crosstab(
        df["Type of Travel"],
        df["satisfaction"]
    )

    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    cramers_v = calculate_cramers_v(contingency_table)

    alpha = 0.05
    decision = "Reject H0" if p_value < alpha else "Fail to reject H0"

    print("\nH1: Type of Travel vs Satisfaction")
    print(contingency_table)
    print(f"\nChi-square statistic: {chi2:.2f}")
    print(f"Degrees of freedom: {dof}")
    print(f"P-value: {p_value:.6f}")
    print(f"Cramér's V: {cramers_v:.3f}")
    print(f"Decision at α = {alpha}: {decision}")

    return {
        "Hypothesis": "H1",
        "Variables": "Type of Travel vs Satisfaction",
        "Chi-square": round(chi2, 2),
        "Degrees of Freedom": dof,
        "P-value": p_value,
        "Cramer's V": round(cramers_v, 3),
        "Alpha": alpha,
        "Decision": decision,
    }


def validate_class_hypothesis(df):
    """Test association between travel class and satisfaction."""
    contingency_table = pd.crosstab(
        df["Class"],
        df["satisfaction"]
    )

    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    cramers_v = calculate_cramers_v(contingency_table)

    alpha = 0.05
    decision = "Reject H0" if p_value < alpha else "Fail to reject H0"

    print("\nH2: Travel Class vs Satisfaction")
    print(contingency_table)
    print(f"\nChi-square statistic: {chi2:.2f}")
    print(f"Degrees of freedom: {dof}")
    print(f"P-value: {p_value:.6f}")
    print(f"Cramér's V: {cramers_v:.3f}")
    print(f"Decision at α = {alpha}: {decision}")

    return {
        "Hypothesis": "H2",
        "Variables": "Travel Class vs Satisfaction",
        "Chi-square": round(chi2, 2),
        "Degrees of Freedom": dof,
        "P-value": p_value,
        "Cramer's V": round(cramers_v, 3),
        "Alpha": alpha,
        "Decision": decision,
    }

def validate_service_rating_hypothesis(df):
    """Measure associations between service ratings and satisfaction."""
    satisfaction_binary = df["satisfaction"].map({
        "neutral or dissatisfied": 0,
        "satisfied": 1,
    })

    results = []

    for service in SERVICE_COLUMNS:
        correlation, p_value = spearmanr(
            df[service],
            satisfaction_binary
        )

        results.append({
            "Service": service,
            "Spearman Correlation": round(correlation, 3),
            "P-value": p_value,
        })

    results_df = pd.DataFrame(results).sort_values(
        "Spearman Correlation",
        ascending=False
    )

    print("\nH3: Service Ratings vs Satisfaction")
    print(results_df)

    return results_df


def main():
    """Run hypothesis validation tests and save results."""
    df = load_data()

    h1_result = validate_travel_type_hypothesis(df)
    h2_result = validate_class_hypothesis(df)
    h3_results = validate_service_rating_hypothesis(df)

    results = pd.DataFrame([
        h1_result,
        h2_result,
    ])

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT_PATH, index=False)
    h3_results.to_csv(H3_OUTPUT_PATH, index=False)

    print(f"\nHypothesis results saved to: {OUTPUT_PATH}")
    print(f"H3 service results saved to: {H3_OUTPUT_PATH}")


if __name__ == "__main__":
    main()