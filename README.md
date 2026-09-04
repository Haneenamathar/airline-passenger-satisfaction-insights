# Airline Passenger Satisfaction Insights

## Project Overview

Airline Passenger Satisfaction Insights is an interactive data analytics application developed to explore the factors associated with airline passenger satisfaction.

This project builds on the original Airline Passenger Satisfaction analysis by transforming exploratory analysis, statistical testing and machine-learning findings into an interactive Streamlit dashboard designed for both non-technical and technical audiences.

The dataset contains passenger characteristics, travel information, airline service ratings, flight delays and an overall passenger satisfaction classification.

The application enables stakeholders to explore satisfaction patterns, investigate important passenger segments, compare airline service experiences and review the statistical evidence supporting the main findings.

The project also considers responsible data practice, privacy, GDPR principles, accessibility, data governance and the limitations of using analytical and predictive results for business decision-making.

---

# Project Purpose

The purpose of this project is to transform the findings from the Airline Passenger Satisfaction analysis into an interactive data application that enables users to explore the factors influencing passenger satisfaction.

The application presents clear business-focused insights for non-technical users while also providing more detailed analytical information for technical users.

The goal is to support data-driven decision-making by identifying service areas, passenger characteristics and travel experiences that are strongly associated with customer satisfaction.

---

# Business Problem

Passenger satisfaction is influenced by many aspects of the travel experience, including passenger characteristics, type of travel, travel class, airline services and operational factors.

For airline stakeholders, analysing these factors through static tables or notebooks alone can make it difficult to quickly identify important patterns.

This project therefore develops an interactive dashboard that allows users to explore the available passenger data and understand which factors show the strongest relationships with satisfaction.

The application is intended as a decision-support and analytical communication tool rather than a system for making automated operational decisions.

---

# Target Audiences

The application has been designed for two main audiences.

## Non-Technical Audience

The primary non-technical users could include:

- Airline managers
- Customer-experience teams
- Service-quality teams
- Operational decision-makers

These users require:

- Clear KPI metrics
- Interactive filters
- Accessible visualisations
- Plain-language explanations
- Practical business insights
- Clearly communicated recommendations

The business-facing sections of the dashboard focus on answering:

> What is happening and what should we pay attention to?

## Technical Audience

Technical users could include:

- Data analysts
- Data scientists
- Technically experienced stakeholders

These users require access to:

- Statistical methodology
- Hypothesis-testing results
- Effect sizes
- Variable relationships
- Machine-learning performance
- Assumptions and limitations
- Information about data preparation and governance

The technical sections of the dashboard focus on answering:

> What evidence supports these conclusions and how was it analysed?

---

# Business Requirements

## BR1 — Understand Passenger Satisfaction Patterns

Provide an interactive overview of passenger satisfaction and allow users to investigate differences across passenger characteristics, customer type, travel type and class.

## BR2 — Identify Key Drivers of Passenger Satisfaction

Allow users to investigate which airline service ratings and travel-related factors have the strongest relationships with overall passenger satisfaction.

## BR3 — Support Data-Driven Service Improvement

Enable non-technical airline stakeholders to identify weaker service areas, important passenger segments and potential opportunities for improving passenger experience.

## BR4 — Validate Insights with Analytical Evidence

Provide technical users with statistical evidence, hypothesis-testing results and relevant model findings so dashboard conclusions can be traced to the underlying analysis.

---

# Research Questions

The project investigates the following questions:

1. What proportion of passengers are satisfied?
2. Do passenger characteristics such as age, customer type or gender show different satisfaction patterns?
3. Does passenger satisfaction vary according to travel type and class?
4. Which airline service ratings have the strongest relationship with overall passenger satisfaction?
5. Are departure and arrival delays associated with passenger satisfaction?
6. Can passenger satisfaction be predicted using the available passenger and flight information?

---

# Dataset

The project uses the Airline Passenger Satisfaction dataset published on Kaggle by Teejmahal.

Dataset source:

**Teejmahal — Airline Passenger Satisfaction (Kaggle)**

The original dataset contains separate training and testing CSV files. These were combined during the original data-collection stage before cleaning and analysis.

The cleaned dataset contains:

- **103,594 passenger records**
- **23 variables**

The dataset includes:

- Gender
- Customer Type
- Age
- Type of Travel
- Class
- Flight Distance
- Airline service ratings
- Departure delay
- Arrival delay
- Passenger satisfaction

The target variable is:

**satisfaction**

with two categories:

- `satisfied`
- `neutral or dissatisfied`

---

# Data Quality and Cleaning

During the original ETL process, the dataset was inspected for:

- Missing values
- Duplicate records
- Data types
- Unnecessary identifier columns
- Numerical distributions
- Potential outliers

The unnecessary `id` and `Unnamed: 0` columns were removed.

Missing values in `Arrival Delay in Minutes` were handled during the cleaning process.

The validated cleaned dataset was stored as:

```text
data/clean_data/airline_clean.csv
```

This dataset contains 103,594 passenger records and 23 columns and provides the analytical foundation for the Unit 3 dashboard.

---

# Data Management and Versioning

The project uses a structured data pipeline to separate the validated cleaned dataset from dashboard-specific analytical outputs.

```text
Original Kaggle Data
        ↓
Unit 2 Data Cleaning
        ↓
data/clean_data/airline_clean.csv
        ↓
Unit 3 Reproducible Analysis Scripts
        ↓
data/dashboard_data/
        ↓
Streamlit Dashboard
```

The original cleaned dataset is retained rather than duplicated.

Dashboard-specific analytical outputs are stored separately under:

```text
data/dashboard_data/
```

Current versioned outputs include:

```text
satisfaction_by_travel_type_v1.csv
satisfaction_by_class_v1.csv
service_rating_summary_v1.csv
hypothesis_results_v1.csv
service_hypothesis_results_v1.csv
```

The `v1` naming convention provides a simple version identifier and allows future analytical outputs to be updated without silently replacing previous versions.

Reproducible Python scripts are stored in:

```text
scripts/
```

including:

```text
generate_dashboard_data.py
validate_hypotheses.py
```

This structure improves reproducibility, traceability and separation between cleaned source data and dashboard-ready analytical outputs.

---

# Project Methodology

The project follows an end-to-end analytical workflow.

## 1. Business Understanding

The project purpose, business requirements, research questions and target audiences were defined to ensure that the analysis and dashboard address a clear business problem.

## 2. Data Collection and Understanding

The airline passenger dataset was inspected to understand:

- Dataset dimensions
- Variable types
- Missing values
- Data quality
- Passenger characteristics
- Travel information
- Service-rating variables
- Satisfaction categories

## 3. Data Cleaning / ETL

The original dataset was cleaned and transformed into a validated analytical dataset.

The cleaned dataset is used consistently across exploratory analysis, statistical testing, machine learning and the interactive application.

## 4. Exploratory Data Analysis

Exploratory analysis investigated:

- Overall passenger satisfaction
- Passenger characteristics
- Customer type
- Type of travel
- Travel class
- Flight distance
- Airline service ratings
- Departure and arrival delays
- Relationships between variables

## 5. Statistical Analysis

Statistical analysis was used to determine whether important patterns observed during exploratory analysis were supported by statistical evidence.

Methods include:

- Descriptive statistics
- Chi-square tests of independence
- Cramér's V effect size
- Spearman rank correlation

## 6. Machine Learning

Passenger satisfaction prediction was treated as a supervised binary classification problem.

Models evaluated included:

- Baseline classifier
- Logistic Regression
- Random Forest

Random Forest achieved the strongest test accuracy and was selected as the final predictive model.

## 7. Dashboard Data Preparation

Reproducible Python scripts generate versioned analytical outputs for use within the Streamlit application.

## 8. Interactive Data Application

The final Streamlit application combines:

- Interactive passenger exploration
- Business-focused visualisations
- Service-experience analysis
- Statistical hypothesis results
- Predictive-model findings
- Project methodology
- Ethics and governance information

---

# Project Hypotheses

Three hypotheses were selected to validate important relationships identified during the analysis.

---

## H1 — Type of Travel and Passenger Satisfaction

### Null Hypothesis — H0

Type of travel and passenger satisfaction are independent; there is no statistically significant association between them.

### Alternative Hypothesis — H1

Type of travel and passenger satisfaction are associated; there is a statistically significant relationship between them.

### Method

A **Chi-square test of independence** was selected because both variables are categorical.

Cramér's V was used to measure the strength of the association.

### Results

- Chi-square statistic: **20,882.22**
- Degrees of freedom: **1**
- p-value: **p < 0.001**
- Cramér's V: **0.449**
- Significance level: **α = 0.05**

### Decision

The null hypothesis was rejected.

There is statistically significant evidence of an association between type of travel and passenger satisfaction.

Business travellers showed substantially higher satisfaction than personal travellers.

Cramér's V of 0.449 indicates a meaningful association within this dataset.

This relationship should not be interpreted as evidence that travel type directly causes satisfaction.

---

## H2 — Travel Class and Passenger Satisfaction

### Null Hypothesis — H0

Travel class and passenger satisfaction are independent; there is no statistically significant association between them.

### Alternative Hypothesis — H1

Travel class and passenger satisfaction are associated; there is a statistically significant relationship between them.

### Method

A **Chi-square test of independence** was used because both variables are categorical.

Cramér's V was calculated to measure association strength.

### Results

- Chi-square statistic: **26,402.22**
- Degrees of freedom: **2**
- p-value: **p < 0.001**
- Cramér's V: **0.505**
- Significance level: **α = 0.05**

### Decision

The null hypothesis was rejected.

There is statistically significant evidence of an association between travel class and passenger satisfaction.

Business Class passengers showed considerably higher satisfaction than Eco and Eco Plus passengers.

Cramér's V of 0.505 indicates a substantial association within this dataset.

The result demonstrates association rather than causation.

---

## H3 — Airline Service Ratings and Passenger Satisfaction

### Hypothesis

Airline service ratings are associated with passenger satisfaction, with some service areas showing stronger relationships than others.

### Method

Service ratings use ordered rating scales, while satisfaction was represented as a binary outcome.

**Spearman rank correlation** was therefore used to measure the strength and direction of the relationship between individual service ratings and passenger satisfaction.

### Strongest Positive Associations

| Service | Spearman Correlation |
|---|---:|
| Online boarding | 0.551 |
| Inflight entertainment | 0.400 |
| Seat comfort | 0.362 |
| On-board service | 0.328 |
| Leg room service | 0.318 |
| Cleanliness | 0.303 |
| Inflight Wi-Fi service | 0.287 |

Online boarding showed the strongest positive relationship with passenger satisfaction.

Gate location showed essentially no relationship with satisfaction:

- Spearman correlation approximately **0.000**
- p-value approximately **0.901**

Departure/Arrival time convenient produced a very small negative relationship:

- Spearman correlation: **-0.050**

Although this result was statistically significant, the effect size is very small. The large sample size means even weak relationships can produce small p-values.

For this reason, both **statistical significance and relationship strength** are considered when interpreting the results.

These correlations describe associations and do not demonstrate causal relationships.

---

# Main Analytical Findings

## Overall Passenger Satisfaction

Approximately:

- **43.3%** of passengers were satisfied.
- **56.7%** were neutral or dissatisfied.

Neutral or dissatisfied passengers therefore form the majority category in the dataset.

---

## Type of Travel

Business travel:

- Neutral or dissatisfied: **29,831**
- Satisfied: **41,634**

Personal travel:

- Neutral or dissatisfied: **28,866**
- Satisfied: **3,263**

The statistical analysis confirmed that type of travel has a meaningful association with passenger satisfaction.

---

## Travel Class

Business Class:

- Neutral or dissatisfied: **15,143**
- Satisfied: **34,390**

Eco:

- Neutral or dissatisfied: **37,922**
- Satisfied: **8,671**

Eco Plus:

- Neutral or dissatisfied: **5,632**
- Satisfied: **1,836**

Travel class demonstrated a substantial association with passenger satisfaction.

---

# Service Experience Findings

Satisfied passengers generally provided higher service ratings than neutral or dissatisfied passengers.

The largest differences in average ratings were:

| Service | Neutral/Dissatisfied | Satisfied | Difference |
|---|---:|---:|---:|
| Online boarding | 2.66 | 4.03 | 1.37 |
| Inflight entertainment | 2.89 | 3.97 | 1.07 |
| Seat comfort | 3.04 | 3.97 | 0.93 |
| On-board service | 3.02 | 3.86 | 0.84 |
| Leg room service | 2.99 | 3.82 | 0.83 |
| Cleanliness | 2.94 | 3.74 | 0.81 |

Online boarding therefore stands out in both the average-rating comparison and the statistical association analysis.

However, differences in group averages, correlations and machine-learning feature importance measure different analytical concepts and should not be interpreted as interchangeable measures.

---

# Flight Delay Findings

Departure and arrival delay variables showed strongly right-skewed distributions.

The mean departure delay was approximately **14.75 minutes**, while the mean arrival delay was approximately **15.18 minutes**.

The median for both variables was **0 minutes**.

This indicates that many passengers experienced little or no delay while a smaller number experienced considerably larger delays.

Longer delays were generally associated with lower satisfaction, although delay is only one of several factors associated with the passenger experience.

---

# Machine Learning

The project investigated whether passenger satisfaction could be predicted using the available passenger, travel and service information.

The target was:

```text
satisfaction
```

with two classes:

```text
satisfied
neutral or dissatisfied
```

An 80/20 stratified train/test split was used to preserve the target-class distribution.

Categorical variables were one-hot encoded and numerical variables were standardised as part of the Scikit-learn preprocessing workflow.

## Model Performance

| Model | Accuracy |
|---|---:|
| Baseline Classifier | 56.70% |
| Logistic Regression | 87.18% |
| Random Forest | 96.42% |

Random Forest achieved the strongest test accuracy and was selected as the final model.

The final model achieved:

**Neutral or dissatisfied**

- Precision: 0.96
- Recall: 0.98
- F1-score: 0.97

**Satisfied**

- Precision: 0.97
- Recall: 0.94
- F1-score: 0.96

Feature-importance analysis identified important predictive variables including:

- Online boarding
- Inflight Wi-Fi service
- Travel class
- Type of travel
- Seat comfort
- Inflight entertainment
- Ease of online booking
- On-board service

Feature importance represents predictive contribution within the model and does not demonstrate that a variable causes passenger satisfaction.

---

# Interactive Streamlit Dashboard

The Unit 3 application was designed as a multi-page Streamlit dashboard.

The application contains five main sections.

## 1. Executive Overview

Designed primarily for non-technical stakeholders.

Provides:

- Passenger-count KPI
- Satisfaction-rate KPI
- Neutral/dissatisfied KPI
- Overall satisfaction visualisation
- Interactive passenger filters
- Key business interpretation

This page supports **BR1 and BR3**.

---

## 2. Passenger Insights

Allows users to explore satisfaction patterns according to:

- Type of Travel
- Travel Class
- Customer Type
- Gender
- Age

Grouped percentage charts are used so that satisfaction can be compared within passenger groups rather than relying only on raw passenger counts.

An age distribution provides an additional visualisation type and allows users to examine differences in passenger age.

This page supports **BR1 and BR3**.

---

## 3. Service Experience

Provides analysis of airline service ratings.

The page includes:

- Average service-rating differences between satisfaction groups
- Spearman correlation rankings
- Key service-association metrics
- Plain-language interpretation
- Statistical interpretation warnings

Online boarding, inflight entertainment and seat comfort show some of the strongest positive associations with satisfaction.

This page supports **BR2 and BR3**.

---

## 4. Statistical & Predictive Analysis

Designed primarily for technical users.

The page presents:

- H1 — Type of Travel vs Satisfaction
- H2 — Travel Class vs Satisfaction
- H3 — Service Ratings vs Satisfaction
- Chi-square statistics
- Cramér's V
- p-value interpretation
- Spearman correlations
- Complete service-correlation results
- Machine-learning model comparison
- Technical interpretation
- Causality warnings

This page supports **BR2 and BR4**.

---

## 5. Project Information

Provides supporting project documentation directly within the application.

Topics include:

- Project purpose
- Business requirements
- Target audiences
- Data and methodology
- Ethics
- Privacy
- GDPR
- Data governance
- Accessibility
- User experience
- Project limitations
- Responsible interpretation

This page primarily supports **BR4** and the project's responsible-data objectives.

---

# Dashboard User Experience and Accessibility

The dashboard was designed to communicate analytical information to both technical and non-technical users.

UX and accessibility considerations include:

- Clear page navigation
- Descriptive page headings
- KPI metrics
- Plain-language explanations
- Chart titles and axis labels
- Legends
- Interactive filters
- Percentage-based comparisons where appropriate
- Technical results separated from business-facing analysis
- Warnings where statistical results could be misinterpreted
- Multiple forms of communication rather than relying on charts alone

The dashboard provides both visual and written interpretations so users are not required to interpret charts without supporting context.

The application also avoids presenting statistical association or machine-learning feature importance as proof of causation.

---

# Ethics, Privacy and Responsible Data Use

Responsible data practice was considered throughout the project.

The analytical dataset does not contain direct passenger identifiers such as:

- Passenger names
- Email addresses
- Telephone numbers
- Home addresses

Unnecessary identifier columns from the original dataset were removed during data cleaning.

Only variables relevant to the analytical purpose were retained.

This supports the principle of **data minimisation**.

The analysis is intended to understand aggregate passenger satisfaction patterns rather than identify individual passengers.

---

# GDPR and Data Governance Considerations

Although the project uses a public analytical dataset rather than a live airline customer database, the principles of responsible data governance remain relevant.

Important considerations include:

## Purpose Limitation

Passenger information should only be used for clearly defined and legitimate analytical purposes.

## Data Minimisation

Only information necessary for the analysis should be collected and retained.

## Access Control

In a real operational environment, passenger-level information should only be available to authorised users.

## Data Quality

Analytical conclusions depend on accurate, complete and appropriately maintained data.

## Retention

Passenger-level data should not be retained indefinitely without a legitimate business or legal requirement.

## Transparency

Organisations should clearly explain how customer information is used for analytics and predictive modelling.

## Accountability

Analytical models and dashboards should have documented ownership, validation processes and appropriate human oversight.

A real airline deployment involving identifiable passenger data would require additional organisational and legal controls based on the applicable jurisdiction, lawful basis for processing, security requirements and organisational policies.

---

# Responsible Interpretation

The dashboard identifies:

- Statistical associations
- Group differences
- Correlations
- Predictive relationships

These results should not automatically be interpreted as causal relationships.

For example, Business Class passengers show higher satisfaction in this dataset, but this does not prove that changing a passenger's travel class alone would cause satisfaction to increase.

Similarly, Random Forest feature importance describes how useful a feature was for prediction within the trained model. It does not establish a causal mechanism.

Dashboard findings should therefore be used as evidence to support further investigation and business decision-making rather than as automatic instructions for operational action.

---

# Project Limitations

Several limitations should be considered when interpreting the project.

- The analysis is based on a historical public dataset rather than live airline operational data.
- The dataset does not provide detailed information about the airline's operational environment.
- Passenger service ratings are subjective.
- Statistical associations do not prove causation.
- Machine-learning performance reflects the available dataset and may not generalise to future passengers or another airline.
- Predictive models may experience performance degradation when applied to data that differs from the training data.
- Some statistically significant results may have very small practical effects because of the large sample size.
- The dashboard is intended for analytical exploration and decision support rather than automated decision-making.

---

# Business Recommendations

Based on the combined exploratory, statistical and predictive evidence, several areas could be investigated by airline stakeholders.

## 1. Review the Online Boarding Experience

Online boarding produced:

- The largest average service-rating difference between satisfaction groups.
- The strongest Spearman association among the service ratings examined.
- Strong predictive importance in the Random Forest analysis.

Airlines could investigate the usability, reliability and convenience of the online boarding process.

## 2. Investigate the Onboard Passenger Experience

Inflight entertainment, seat comfort, on-board service, leg room and cleanliness all showed meaningful differences between satisfaction groups.

These areas could be prioritised for further customer-experience investigation.

## 3. Analyse Passenger Segments Separately

Type of travel and travel class demonstrated strong statistical associations with satisfaction.

Airlines could therefore examine passenger segments separately rather than assuming that all travellers have identical expectations.

## 4. Continue Monitoring Digital Services

Online boarding and inflight Wi-Fi appeared prominently in the analytical and predictive findings.

Digital passenger services should therefore remain an important area for customer-experience monitoring.

## 5. Continue Monitoring Severe Flight Delays

Most passengers experienced little or no delay, but a smaller group experienced considerably larger delays.

Operational teams could continue monitoring severe disruptions and passenger communication during these events.

## 6. Use Predictive Models as Decision Support

Random Forest achieved **96.42% test accuracy** within the available dataset.

However, any real-world deployment should include:

- Validation on new data
- Performance monitoring
- Bias and fairness assessment
- Data-governance controls
- Human oversight

---

# Project Planning

The project was managed using a GitHub Kanban project board.

Tasks were organised using the following workflow:

```text
Backlog
   ↓
Ready
   ↓
In Progress
   ↓
In Review
   ↓
Done
```

The project plan included:

- Assessment requirement review
- Project purpose and business requirements
- Target audience definition
- Hypothesis development
- Data management and versioning
- Dashboard development
- Interactive visualisation
- Statistical validation
- Ethics and governance
- UX and accessibility
- Testing
- Documentation
- Deployment
- Final assessment review

The Kanban workflow was updated throughout development so that project progress and remaining work could be tracked.

---

# Implementation, Maintenance and Evaluation Plan

The application was implemented using a staged development process.

## Implementation

Development progressed through:

1. Assessment requirement review
2. Business requirement definition
3. Dataset and existing-analysis review
4. Hypothesis definition
5. Reproducible dashboard-data generation
6. Statistical validation
7. Streamlit page development
8. Interactive visualisation
9. Ethics and governance documentation
10. Functional testing
11. Documentation
12. Deployment and final assessment review

## Maintenance

If the project were maintained after deployment, future updates should include:

- Dependency updates
- Streamlit compatibility testing
- Data-quality checks
- Validation of new dataset versions
- Dashboard regression testing
- Documentation updates
- Model-performance monitoring where new data becomes available

## Evaluation

Future versions of the project could be evaluated using:

- Dashboard usability feedback
- Stakeholder feedback
- Data-quality metrics
- Application reliability
- Model performance on new data
- Changes in passenger behaviour
- Accessibility testing
- Relevance of business recommendations

Versioned analytical outputs should be retained so changes can be traced between project releases.

---

# Testing and Validation

Testing was performed throughout development.

## Notebook Testing

The analytical notebooks were tested using a fresh kernel and **Restart Kernel → Run All**.

This helped confirm that:

- Cells execute in the correct order.
- Variables do not depend on previous sessions.
- Data files load correctly.
- Analytical outputs are reproducible.
- No execution errors remain.

## Statistical Validation

Hypothesis calculations were implemented through a reproducible Python script.

The resulting outputs were saved in versioned dashboard-data files.

The dashboard displays very small p-values as:

```text
p < 0.001
```

rather than reporting them as `p = 0`.

This avoids incorrectly implying that the probability is mathematically zero.

## Streamlit Functional Testing

The Streamlit application was tested locally using:

```bash
streamlit run app/app.py
```

The five dashboard pages were manually tested.

### Executive Overview

Validated:

- KPI metrics load correctly.
- Satisfaction visualisation loads.
- Type of Travel filter updates the relevant results.

### Passenger Insights

Validated:

- Type of Travel chart
- Travel Class chart
- Customer Type chart
- Gender chart
- Age distribution
- Passenger filters update relevant visualisations

### Service Experience

Validated:

- Service-rating comparison chart
- Spearman correlation chart
- Key service metrics
- Written interpretation

### Statistical & Predictive Analysis

Validated:

- H1 results
- H2 results
- H3 results
- p-value formatting
- Complete service-correlation results
- Model-performance comparison

### Project Information

Validated that all documentation sections load without application errors.

An empty-filter case was also tested to confirm that the application handles selections that return no passenger records without failing unexpectedly.

All functional tests completed successfully during the final local validation stage.

---

# Technical Challenges and Solutions

Several practical challenges were encountered during the project.

## Logistic Regression Convergence

During the original machine-learning development, Logistic Regression initially reached the maximum number of iterations before convergence.

Numerical features were standardised using `StandardScaler` within the preprocessing pipeline.

The model was then retrained successfully.

## Streamlit Application Development

Dashboard development required careful management of:

- File paths
- Application structure
- Widget filtering
- Data transformations
- Plotly visualisations
- Streamlit layout
- Statistical output formatting

Issues discovered during development were corrected and retested before commits were made.

## Statistical Result Communication

The hypothesis-validation output produced extremely small p-values that may appear as `0.0` when saved numerically.

The dashboard therefore presents these results as:

```text
p < 0.001
```

which is a more appropriate interpretation.

## Communicating Statistical Significance

The large dataset means that even very small relationships can become statistically significant.

For this reason, the project considers both:

- p-values
- effect or relationship size

rather than interpreting statistical significance alone.

## Technical and Non-Technical Communication

Another challenge was presenting the same analytical project to audiences with different levels of technical knowledge.

This was addressed by separating business-focused dashboard pages from the detailed Statistical & Predictive Analysis page.

---

# Project Reflection

This capstone project extended the original airline passenger satisfaction analysis into a more complete interactive data application.

One of the most important learning outcomes was understanding that producing an accurate analysis is only part of a data project. Analytical results must also be communicated in a way that is appropriate for the intended audience.

The project therefore required translating statistical and machine-learning findings into clear visualisations, KPI metrics and plain-language explanations while retaining enough technical information for users who want to understand the evidence behind the conclusions.

Developing additional hypothesis tests also reinforced the distinction between statistical significance and practical importance. The large dataset demonstrated that a very small relationship can still produce a very small p-value, making effect-size interpretation essential.

The project also strengthened my understanding of reproducibility. Dashboard outputs were generated through dedicated scripts and stored as versioned analytical files rather than relying entirely on manually copied results.

Ethics and governance became a more explicit part of the project during the capstone stage. Considering data minimisation, privacy, transparency, access control, retention, model limitations and responsible interpretation demonstrated that analytical quality involves more than technical model performance.

The Streamlit development process also provided practical experience in designing an application for different audiences. Business users require concise insights and intuitive visualisations, while technical users require statistical evidence, methodology and limitations.

Overall, the project strengthened my understanding of how business requirements, data preparation, exploratory analysis, statistics, machine learning, governance, visual communication and application development work together within an end-to-end data analytics project.

---

# Project Structure

```text
airline-passenger-satisfaction-insights/
│
├── app/
│   └── app.py
│
├── data/
│   ├── clean_data/
│   │   └── airline_clean.csv
│   │
│   └── dashboard_data/
│       ├── satisfaction_by_travel_type_v1.csv
│       ├── satisfaction_by_class_v1.csv
│       ├── service_rating_summary_v1.csv
│       ├── hypothesis_results_v1.csv
│       └── service_hypothesis_results_v1.csv
│
├── jupyter_notebooks/
│   ├── 01datacollection.ipynb
│   ├── 02datacleaning.ipynb
│   ├── 03EDA.ipynb
│   ├── 04statisticalanalysis.ipynb
│   └── 05machinelearning.ipynb
│
├── scripts/
│   ├── generate_dashboard_data.py
│   └── validate_hypotheses.py
│
├── .gitignore
├── .python-version
├── .slugignore
├── Procfile
├── README.md
├── requirements.txt
└── setup.sh
```

---

# Technologies Used

## Languages

- **Python** — data preparation, analysis, statistics, machine learning and dashboard development.
- **Markdown** — project documentation and notebook explanations.

## Python Libraries

- **Pandas** — data manipulation and analysis.
- **NumPy** — numerical operations.
- **Matplotlib** — data visualisation.
- **Seaborn** — statistical visualisation in the analytical notebooks.
- **SciPy** — hypothesis testing and statistical analysis.
- **Scikit-learn** — preprocessing, machine learning and model evaluation.
- **Plotly** — interactive dashboard visualisations.
- **Streamlit** — interactive data-application development.

## Development and Project Tools

- **Jupyter Notebook**
- **Visual Studio Code**
- **Git**
- **GitHub**
- **GitHub Projects / Kanban**

---

# Installation and Local Setup

To run the project locally:

## 1. Clone the repository

```bash
git clone https://github.com/Haneenamathar/airline-passenger-satisfaction-insights.git
```

## 2. Enter the project directory

```bash
cd airline-passenger-satisfaction-insights
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

For Git Bash on Windows:

```bash
source .venv/Scripts/activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Generate dashboard analytical outputs if required

```bash
python scripts/generate_dashboard_data.py
python scripts/validate_hypotheses.py
```

## 7. Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will then open in the browser.

---

# Deployment

The interactive application is developed using Streamlit.

The repository contains the supporting deployment files:

- `Procfile`
- `setup.sh`
- `requirements.txt`

The application entry point is:

```text
app/app.py
```

Before final deployment, the application is tested locally and the deployed version will be checked to confirm that:

- The application starts successfully.
- Required datasets load.
- All five pages are accessible.
- Charts render correctly.
- Interactive functionality works.
- Statistical results display correctly.
- Documentation is accessible.
- No local-only file paths are required.

The final live deployment URL will be added here after deployment.

---

# Success Criteria

The project is considered successful when it:

- Clearly communicates overall passenger satisfaction.
- Allows users to explore passenger and travel characteristics.
- Identifies airline service areas strongly associated with satisfaction.
- Validates important findings using appropriate statistical techniques.
- Communicates both statistical significance and association strength.
- Presents relevant machine-learning findings.
- Provides an interactive dashboard suitable for non-technical stakeholders.
- Provides sufficient analytical evidence for technical users.
- Addresses ethics, privacy, GDPR and data governance.
- Communicates project limitations and avoids unsupported causal claims.
- Uses reproducible and versioned analytical outputs.
- Provides clear project documentation.
- Successfully deploys as a functioning web data application.

---

# Credits and Acknowledgements

## Dataset

The dataset used in this project is the **Airline Passenger Satisfaction** dataset published on Kaggle by **Teejmahal**.

The original dataset contains passenger characteristics, travel information, service ratings, flight delays and passenger satisfaction classifications.

## Learning and Documentation Resources

Resources supporting the project include:

- Code Institute Data Analytics and AI Bootcamp learning materials and assessment guidance
- Kaggle
- Python documentation
- Pandas documentation
- NumPy documentation
- Matplotlib documentation
- Seaborn documentation
- SciPy documentation
- Scikit-learn documentation
- Plotly documentation
- Streamlit documentation
- Git documentation
- GitHub documentation

# Credits and Acknowledgements

## Dataset

The dataset used in this project is the Airline Passenger Satisfaction dataset published on Kaggle by Teejmahal.

The original dataset contains airline passenger characteristics, travel information, service ratings, flight delays and passenger satisfaction classifications.

## Learning and Documentation Resources

The following resources supported the development of this project:

- Code Institute Data Analytics and AI Bootcamp learning materials and assessment guidance.
- Kaggle for providing access to the Airline Passenger Satisfaction dataset.
- Pandas documentation for data manipulation and analysis.
- NumPy documentation for numerical operations.
- Matplotlib and Seaborn documentation for data visualisation.
- SciPy documentation for statistical analysis.
- Scikit-learn documentation for preprocessing, machine-learning models and model evaluation.
- Plotly documentation for interactive data visualisation.
- Streamlit documentation for development of the interactive dashboard.
- Git and GitHub documentation for version control and project management.

## Acknowledgements

I would like to sincerely thank Code Institute for providing the learning environment, resources and guidance that supported me throughout this Data Analytics and AI Bootcamp project.

A special thanks to Mr. Vasi for his guidance, support and encouragement throughout the course. His explanations and feedback helped me develop my understanding of data analytics, statistics, machine learning and the practical application of these skills.

I would also like to thank my fellow students for their collaboration, discussions, encouragement and willingness to share ideas and learning experiences throughout the bootcamp.

I am grateful to the wider technology and open-source community whose tools, libraries, documentation and learning resources made this project possible. In particular, I would like to acknowledge Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Scikit-learn, Streamlit, Plotly, Git, GitHub and the deployment technologies used to develop, analyse, visualise and deploy this project.

I would also like to acknowledge OpenAI and its AI tools for providing assistance during the development process. AI support was used as a learning and development aid for areas such as troubleshooting, understanding technical concepts, refining approaches, debugging and improving the project workflow. All analysis, interpretation, model evaluation, business recommendations and final project decisions were reviewed and validated as part of my own project work.

Finally, I would like to thank everyone involved in creating and maintaining the learning materials, documentation and resources that helped me complete this project and develop my confidence in applying data analytics and AI techniques to a real-world business problem.


## AI Assistance

OpenAI AI tools were used as a learning and development aid during the project.

AI assistance supported activities including:

- Troubleshooting
- Understanding technical concepts
- Debugging
- Reviewing project structure
- Refining documentation
- Improving development workflow

Analytical outputs, statistical interpretations, model results, business conclusions and final project decisions were reviewed and validated as part of the project development process.

---

# Current Project Status

The analytical application, statistical validation, dashboard development, data versioning, responsible-data documentation and local functional testing have been completed.

The remaining final stages are:

- Deployment and live application verification
- Final assessment criteria review
- Submission preparation