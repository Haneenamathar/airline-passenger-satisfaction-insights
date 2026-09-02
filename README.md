# Project Title

*Airline Passenger Satisfaction Analysis 2026*

---
## Project Overview

This project analyses airline passenger satisfaction data to identify the passenger, travel and service factors associated with a positive or negative passenger experience.

The dataset contains information about passenger characteristics, type of travel, travel class, flight distance, flight delays and ratings for different airline services.

The project applies data cleaning, exploratory data analysis, statistical analysis and supervised machine learning to investigate passenger satisfaction. A Random Forest classification model was developed to predict whether a passenger is satisfied or neutral/dissatisfied.

The final Random Forest model achieved **96.42% test accuracy**, outperforming both the baseline classifier and Logistic Regression model.

An interactive Streamlit dashboard was also developed to communicate the main analytical findings, machine-learning performance and business recommendations to stakeholders.

---

## Project Links

* **GitHub Repository:** [Airline Passenger Satisfaction](https://github.com/Haneenamathar/airline-passenger-satisfaction)
* **Live Dashboard:** https://airline-satisfaction-2026-815befa26a7c.herokuapp.com/

---

##  Business Problem

This project investigates the available passenger data to identify patterns associated with satisfaction and provides insights that could help an airline understand which areas of the passenger experience may need more attention.

---

##  Project Aim


The main aim of this project is to analyse airline passenger data to identify factors associated with passenger satisfaction and develop a machine-learning model capable of predicting whether a passenger is satisfied or neutral/dissatisfied.

The project also aims to translate the analytical findings into practical business insights through an interactive dashboard that can support customer-experience and service-improvement decisions.

---

##  Target Audience / Stakeholders

The main stakeholders for this project could include:

* Airline management
* Customer experience teams
* Operations teams
* Marketing teams

The results can help these stakeholders better understand passenger behaviour and identify areas where improvements to services may have the greatest impact.

---

#  Business Requirements

## BR1 — Understand Passenger Satisfaction

The first business requirement was to understand the overall level of passenger satisfaction in the dataset.

The analysis examined:

* The number of satisfied passengers.
* The number of neutral or dissatisfied passengers.
* The percentage of passengers belonging to each satisfaction category.

### Outcome

The analysis found that approximately **43.3% of passengers were satisfied**, while approximately **56.7% were neutral or dissatisfied**.

This established the overall satisfaction profile of the dataset and showed that fewer than half of the passengers were classified as satisfied.


---



## BR2 — Investigate Passenger and Travel Characteristics

The second business requirement was to investigate whether passenger and travel characteristics were associated with satisfaction.

The analysis considered:

* Gender
* Age
* Customer Type
* Type of Travel
* Travel Class
* Flight Distance

### Outcome

Gender showed relatively little difference in satisfaction, suggesting that gender alone is unlikely to be a major factor associated with passenger satisfaction.

Satisfied passengers tended to be older than neutral or dissatisfied passengers, although the age distributions overlapped considerably.

Loyal customers showed a higher proportion of satisfied passengers than disloyal customers.

Clear differences were also identified according to travel characteristics. Business travellers showed substantially higher satisfaction than personal travellers.

Travel class showed a particularly strong pattern. Approximately **69.43% of Business Class passengers were satisfied**, compared with **24.58% of Eco Plus passengers** and **18.61% of Eco passengers**.

Flight distance showed some differences between satisfaction groups, although the distributions overlapped considerably.

Overall, the results indicate that **customer type, type of travel and travel class** are particularly relevant characteristics when investigating passenger satisfaction.

---
## BR3 — Investigate Airline Service Ratings

The third business requirement was to investigate which airline services showed the strongest relationship with passenger satisfaction.

The analysis considered service areas including:

* Inflight Wi-Fi
* Online booking
* Online boarding
* Seat comfort
* Food and drink
* Inflight entertainment
* Leg room
* Baggage handling
* Check-in service
* Inflight service
* Cleanliness
* On-board service

### Outcome

Satisfied passengers generally gave higher service ratings than neutral or dissatisfied passengers.

The largest difference in average rating was identified for **Online boarding**, where satisfied passengers gave an average rating of **4.03**, compared with **2.66** among neutral or dissatisfied passengers, a difference of **1.37 points**.

Other notable differences included:

* **Inflight entertainment:** 1.07 points
* **Seat comfort:** 0.93 points
* **On-board service:** 0.84 points
* **Leg room service:** 0.83 points

The machine-learning feature importance analysis supported these findings. **Online boarding** was the most important feature in the final Random Forest model, followed closely by **Inflight Wi-Fi service**.

Overall, the results suggest that the digital passenger journey and onboard service experience are important areas for understanding passenger satisfaction.

---

## BR4 — Investigate Flight Delays

The fourth business requirement was to investigate the relationship between flight delays and passenger satisfaction.

The analysis considered:

* Departure delays
* Arrival delays
* Delay distributions
* Delay patterns across satisfaction groups

### Outcome

Both departure and arrival delay variables showed strongly right-skewed distributions.

The mean departure delay was approximately **14.75 minutes**, while the mean arrival delay was approximately **15.18 minutes**. However, the median for both variables was **0 minutes**.

This difference between the mean and median indicates that most passengers experienced little or no delay, while a relatively small number of flights experienced very large delays.

Passengers with longer delays generally showed lower satisfaction, although delay was only one of several factors associated with the overall passenger experience.

The results suggest that reducing severe delays may contribute to improved passenger experience, but service quality and travel characteristics also play important roles in satisfaction.


---

## BR5 — Predict Passenger Satisfaction

The final analytical business requirement was to develop a machine-learning model capable of predicting passenger satisfaction using passenger characteristics, travel information and airline service ratings.

The target variable was:

* `satisfaction`

The target contains two classes:

* `satisfied`
* `neutral or dissatisfied`

Therefore, the machine-learning task was treated as a **supervised binary classification problem**.

### Model Development

An 80/20 stratified train/test split was used to preserve the satisfaction-class distribution.

Categorical variables were one-hot encoded, while numerical variables were standardised as part of a Scikit-learn preprocessing pipeline.

Three levels of predictive performance were evaluated:

| Model | Accuracy |
| --- | ---: |
| Baseline Classifier | 56.7% |
| Logistic Regression | 87.18% |
| Random Forest | 96.42% |

### Outcome

The **Random Forest classifier** achieved the strongest performance with **96.42% test accuracy**.

The model also performed strongly across both target classes:

* Neutral or dissatisfied — **Precision: 0.96, Recall: 0.98, F1-score: 0.97**
* Satisfied — **Precision: 0.97, Recall: 0.94, F1-score: 0.96**

Random Forest was therefore selected as the final model.

Feature importance analysis identified **Online boarding** and **Inflight Wi-Fi service** as the two most influential predictors, with travel class, type of travel, seat comfort and inflight entertainment also contributing strongly to predictions.

These results demonstrate that the available passenger, travel and service information can be used effectively to predict passenger satisfaction.

#  Research Questions

The analysis will attempt to answer the following questions:

1. What proportion of passengers are satisfied?

2. Do passenger characteristics such as age, customer type or gender show different satisfaction patterns?

3. Does passenger satisfaction vary according to travel type and class?

4. Which airline service ratings have the strongest relationship with overall passenger satisfaction?

5. Are departure and arrival delays associated with passenger satisfaction?

6. Can passenger satisfaction be predicted using the available passenger and flight information?

---

# Hypothesis Testing

A formal hypothesis test was conducted to determine whether the relationship observed between type of travel and passenger satisfaction was statistically significant.

## Hypothesis — Type of Travel and Passenger Satisfaction

**H0 (Null Hypothesis):** Type of travel and passenger satisfaction are independent; there is no statistically significant association between them.

**H1 (Alternative Hypothesis):** Type of travel and passenger satisfaction are associated; there is a statistically significant relationship between them.

**Significance Level:** α = 0.05

### Statistical Method

A **Chi-square test of independence** was selected because both `Type of Travel` and `satisfaction` are categorical variables.

The test produced:

* **Chi-square statistic:** 20,882.22
* **Degrees of freedom:** 1
* **p-value:** < 0.001
* **Minimum expected frequency:** 13,924.51

The expected frequencies were well above 5, satisfying the expected-frequency assumption for the Chi-square test.

### Result

Because the p-value was below the significance level of 0.05, the **null hypothesis was rejected**.

There is statistically significant evidence of an association between type of travel and passenger satisfaction.

Business travellers showed substantially higher satisfaction than personal travellers.

### Effect Size

Cramér's V was calculated as:

**Cramér's V = 0.449**

This indicates a meaningful association between type of travel and passenger satisfaction.

The result supports the exploratory analysis and demonstrates that type of travel is an important characteristic when analysing passenger satisfaction.

---

# Project Methodology

The project followed an end-to-end data analysis and machine-learning workflow.

### 1. Business Understanding

The business problem, project aim, target audience, business requirements and research questions were defined before beginning the analysis.

### 2. Data Collection and Understanding

The airline passenger satisfaction dataset was loaded and inspected to understand its structure, variables, data types, missing values and general data quality.

### 3. Data Cleaning / ETL

The dataset was cleaned by investigating missing values, duplicates and unnecessary identifier columns. The cleaned dataset was then saved for use throughout the remaining stages of the project.

### 4. Exploratory Data Analysis

Exploratory analysis was performed to investigate:

* Passenger satisfaction distribution
* Passenger characteristics
* Travel characteristics
* Airline service ratings
* Flight delays
* Relationships between numerical variables
* Correlations between service ratings and satisfaction

Multiple visualisation techniques were used to communicate the findings.

### 5. Statistical Analysis

Descriptive statistics were used to examine measures including mean, median and standard deviation.

Basic probability was demonstrated by calculating the probability of selecting a satisfied passenger.

A Chi-square test of independence was used to test the relationship between type of travel and passenger satisfaction, followed by Cramér's V to measure the strength of the association.

### 6. Machine Learning

The project treated passenger satisfaction prediction as a supervised binary classification problem.

The data was divided into stratified training and testing sets. Categorical features were one-hot encoded and numerical features were standardised using a Scikit-learn preprocessing pipeline.

A baseline classifier, Logistic Regression and Random Forest classifier were evaluated.

Random Forest achieved the strongest performance and was selected as the final model.

### 7. Interactive Dashboard

A Streamlit dashboard was developed to communicate the main project findings to stakeholders.

The dashboard presents:

* Key passenger satisfaction metrics
* Satisfaction distribution
* Satisfaction by type of travel
* Important service-rating differences
* Machine-learning model performance
* Important predictive features
* Business recommendations

### 8. Conclusions and Business Recommendations

Findings from the exploratory analysis, statistical testing and machine-learning analysis were combined to identify practical areas that airlines could prioritise when seeking to improve passenger satisfaction.


---

# Dataset

The project uses the **Airline Passenger Satisfaction** dataset available from Kaggle.

**Dataset source:**  
 
[Teejmahal — Airline Passenger Satisfaction (Kaggle)](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

The dataset contains passenger demographic information, travel characteristics, airline service ratings, flight delays and an overall passenger satisfaction classification.

The original dataset provides separate training and testing CSV files. For this project, the data was combined during the data collection stage before cleaning and analysis.

## Main Variables

The dataset includes:

* Passenger characteristics such as gender and age
* Customer type
* Type of travel
* Travel class
* Flight distance
* Airline service ratings on a 0–5 scale
* Departure and arrival delays
* Passenger satisfaction

The target variable used for machine learning is `satisfaction`, containing:

* `satisfied`
* `neutral or dissatisfied`

## Data Quality and Cleaning

During the ETL process, the dataset was inspected for:

* Missing values
* Duplicate records
* Data types
* Unnecessary identifier columns
* Numerical distributions and potential outliers

The unnecessary `id` and `Unnamed: 0` columns were removed.

Missing values in `Arrival Delay in Minutes` were handled during the cleaning process, and the cleaned dataset was saved as:

`data/clean_data/airline_clean.csv`

The cleaned dataset contains **103,594 passenger records and 23 columns** and was used consistently for exploratory analysis, statistical analysis and machine learning.

# Project Structure

The project is organised into separate notebooks and application files so that each stage of the analysis can be followed clearly.

```text
airline-passenger-satisfaction/
│
├── app/
│   └── app.py
│
├── data/
│   └── clean_data/
│       └── airline_clean.csv
│
├── images/
│
├── jupyter_notebooks/
│   ├── 01DataCollection.ipynb
│   ├── 02DataCleaning.ipynb
│   ├── 03EDA.ipynb
│   ├── 04statisticalanalysis.ipynb
│   └── 05machinelearning.ipynb
│
├── .gitignore
├── Procfile
├── README.md
├── requirements.txt
└── setup.sh



# Project Success Criteria

The project was considered successful based on the following criteria:

* Clearly describe passenger satisfaction within the dataset.
* Identify meaningful relationships between passenger/travel characteristics and satisfaction.
* Identify airline services that appear strongly associated with satisfaction.
* Evaluate the relationship between flight delays and satisfaction.
* Statistically test a relevant relationship identified during the analysis.
* Develop and evaluate machine-learning classification models.
* Present the main findings clearly through an interactive dashboard.
* Provide conclusions and business recommendations supported by the analysis.

All of these criteria were addressed through the exploratory analysis, statistical analysis, machine-learning modelling and interactive dashboard.

----




# Main Findings and Conclusions

The analysis identified several important patterns associated with airline passenger satisfaction.

## Passenger Satisfaction

Approximately **43.3% of passengers were satisfied**, while **56.7% were neutral or dissatisfied**. This means neutral or dissatisfied passengers formed the majority class in the dataset.

## Passenger and Travel Characteristics

Travel characteristics showed clear differences in satisfaction.

Business travellers were substantially more likely to be satisfied than personal travellers. A Chi-square test confirmed a statistically significant association between type of travel and satisfaction (**p < 0.001**), with **Cramér's V = 0.449** indicating a meaningful association.

Travel class was also important. Business Class passengers showed considerably higher satisfaction than Eco and Eco Plus passengers.

## Airline Service Experience

Satisfied passengers generally provided higher service ratings.

**Online boarding** showed the largest difference in average service rating between satisfied and neutral/dissatisfied passengers.

Other important service areas included:

* Inflight Wi-Fi service
* Seat comfort
* Inflight entertainment
* On-board service
* Leg room service
* Ease of online booking

These findings suggest that both the digital passenger journey and onboard experience are important when investigating satisfaction.

## Flight Delays

Departure and arrival delays were strongly right-skewed. Most passengers experienced little or no delay, while a smaller number experienced very large delays.

Longer delays were generally associated with lower satisfaction, although the analysis indicates that passenger satisfaction depends on several factors rather than delay alone.

## Machine Learning

The machine-learning analysis demonstrated that passenger satisfaction could be predicted effectively using the available features.

The models achieved:

* **Baseline Classifier:** 56.7%
* **Logistic Regression:** 87.18%
* **Random Forest:** 96.42%

Random Forest was selected as the final model because it achieved the strongest overall test performance.

Feature importance identified **Online boarding** and **Inflight Wi-Fi service** as the two strongest predictors, with travel class, type of travel and several onboard service ratings also contributing to predictions.

The predictive relationships identified by the model should not be interpreted as evidence of causation.


---

# Business Recommendations

Based on the findings from the exploratory analysis, statistical testing and machine-learning model, the following recommendations could be considered by airline stakeholders.

## 1. Prioritise the Online Boarding Experience

Online boarding showed the largest service-rating difference between satisfaction groups and was the most important feature in the Random Forest model.

Airlines should therefore review the online boarding journey and identify opportunities to make the process simpler, more reliable and easier for passengers to use.

## 2. Improve Inflight Wi-Fi Service

Inflight Wi-Fi was one of the strongest predictors of passenger satisfaction.

Improving connection reliability and the overall inflight connectivity experience may therefore be an important area for customer-experience improvement.

## 3. Focus on Key Onboard Services

Seat comfort, inflight entertainment, on-board service and leg room were all associated with differences in passenger satisfaction.

These areas could be prioritised when reviewing the onboard passenger experience.

## 4. Consider Different Passenger Segments

Satisfaction varied considerably according to type of travel and travel class.

Airlines could therefore analyse Business, Personal, Business Class, Eco Plus and Eco passengers separately when developing customer-experience strategies rather than assuming that all passengers have the same expectations.

## 5. Continue Monitoring Flight Delays

Although service-related variables were particularly important, longer delays were generally associated with lower passenger satisfaction.

Operational teams should continue monitoring severe departure and arrival delays and investigate opportunities to reduce disruption and improve communication when delays occur.

## 6. Use Predictive Modelling as Decision Support

The Random Forest model achieved **96.42% test accuracy**, demonstrating strong predictive performance within this dataset.

A predictive model could potentially support the identification of passengers at greater risk of dissatisfaction. However, the model should be validated on new and operational data before being used for real-world decision-making.

These recommendations are based on associations and predictive relationships identified within the available dataset and should not be interpreted as proof of direct causal relationships.


-----

# Technologies Used

## Languages

* **Python** — data cleaning, analysis, statistical testing, machine learning and dashboard development.
* **Markdown** — project documentation and notebook explanations.

## Python Libraries

* **Pandas** — data manipulation, cleaning and analysis.
* **NumPy** — numerical operations.
* **Matplotlib** — data visualisation.
* **Seaborn** — statistical data visualisation.
* **SciPy** — statistical hypothesis testing.
* **Scikit-learn** — preprocessing, machine-learning pipelines, classification models and model evaluation.
* **Streamlit** — development of the interactive dashboard.

## Development Tools

* **Jupyter Notebook** — development and documentation of the analytical workflow.
* **Visual Studio Code** — project development environment.
* **Git** — version control.
* **GitHub** — source-code repository and project version management.

----


# Installation and Local Setup

To run this project locally:

1. Clone the GitHub repository. (https://github.com/Haneenamathar/airline-passenger-satisfaction.git)

2. Open the project folder in Visual Studio Code.

3. Create a virtual environment:

**
python -m venv .venv


 Activate the virtual environment:

**
source .venv/Scripts/activate


Install the required Python packages:

**
pip install -r requirements.txt


 The analysis notebooks are available in the `jupyter_notebooks/` folder and should be viewed in numerical order.

 To run the interactive dashboard, use:

**
streamlit run app/app.py

The dashboard will then open in a web browser.



----

# Deployment

The interactive dashboard was developed using Streamlit and tested locally before deployment.

The project includes the following files required to support deployment:

* `Procfile` — defines the command used to start the Streamlit application.
* `setup.sh` — configures Streamlit for the deployment environment.
* `requirements.txt` — contains the Python packages required to run the project.

The application is started using:

```text
web: sh setup.sh && streamlit run app/app.py
```

The `setup.sh` file configures Streamlit to run in headless mode and use the port provided by the deployment environment.

Before deployment, the application was tested locally using:

```bash
streamlit run app/app.py
```

A Python syntax check was also performed using:

```bash
python -m py_compile app/app.py
```

The dashboard was manually tested to confirm that the passenger filters, reset button, KPI metrics, charts and machine-learning results displayed correctly.

The final dashboard includes interactive filters for:

* Type of Travel
* Travel Class
* Customer Type
* Gender

The KPI metrics and relevant analytical charts update according to the selected filters, while the machine-learning performance results remain fixed because they represent the model evaluation performed on the original test dataset.

----

# Testing and Debugging

Testing and debugging were carried out throughout the project to ensure that the notebooks, machine-learning pipeline and interactive dashboard worked correctly.

## Jupyter Notebook Testing

Each completed notebook was tested using a fresh kernel and **Restart Kernel → Run All**.

This ensured that:

* Cells executed successfully in the correct order.
* Variables did not depend on previous notebook sessions.
* Data files loaded correctly.
* Analytical outputs and visualisations were reproducible.
* No execution errors remained before committing the notebook to GitHub.

## Machine Learning Debugging

During Logistic Regression development, the model initially reached the maximum number of iterations before convergence.

To address this, numerical features were standardised using `StandardScaler` within the preprocessing pipeline. The model was then retrained and completed successfully without the convergence warning.

The final Logistic Regression and Random Forest models were evaluated using accuracy, precision, recall, F1-score and confusion matrices.

## Streamlit Dashboard Testing

The Streamlit application was tested locally using:

```bash
streamlit run app/app.py
```

The application was checked to confirm that:

* The cleaned dataset loaded successfully.
* KPI metrics displayed correctly.
* Dashboard charts rendered without errors.
* Type of Travel, Travel Class, Customer Type and Gender filters worked correctly.
* KPI metrics and relevant charts updated when filters were changed.
* The Reset Filters button returned all filters to their default values.
* Machine-learning results remained unchanged by dashboard filters because they represent evaluation results from the original test dataset.

The application was also checked for Python syntax errors using:

```bash
python -m py_compile app/app.py
```

The syntax validation completed without errors.

## Debugging Examples

During development, several issues were identified and corrected, including:

* An initially empty `app.py` file causing a blank Streamlit page.
* Incorrect indentation while adding interactive dashboard filters.
* Streamlit session-state handling for the Reset Filters button.
* Logistic Regression convergence during model training.
* The `Procfile` initially pointing to `app.py` instead of the correct `app/app.py` location.

These issues were resolved and the affected components were retested before finalising the project.

---

# Credits and Acknowledgements

## Dataset

The dataset used in this project is the **Airline Passenger Satisfaction** dataset published on Kaggle by **Teejmahal**.

The original dataset contains airline passenger characteristics, travel information, service ratings, flight delays and passenger satisfaction classifications.

## Learning and Documentation Resources

The following resources supported the development of this project:

* Code Institute Data Analytics and AI Bootcamp learning materials and assessment guidance.
* Kaggle for providing access to the airline passenger satisfaction dataset.
* Pandas documentation for data manipulation and analysis.
* Matplotlib and Seaborn documentation for data visualisation.
* SciPy documentation for statistical analysis.
* Scikit-learn documentation for preprocessing, machine-learning models and model evaluation.
* Streamlit documentation for development of the interactive dashboard.

## Acknowledgements

I would like to sincerely thank Code Institute for providing the learning environment, resources and guidance that supported me throughout this Data Analytics and AI Bootcamp project.

A special thanks to Mr. Vasi for his guidance, support and encouragement throughout the course. His explanations and feedback helped me develop my understanding of data analytics, statistics, machine learning and the practical application of these skills.

I would also like to thank my fellow students for their collaboration, discussions, encouragement and willingness to share ideas and learning experiences throughout the bootcamp.

I am grateful to the wider technology and open-source community whose tools, libraries, documentation and learning resources made this project possible. In particular, I would like to acknowledge Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Scikit-learn, XGBoost, Streamlit, Plotly, Git, GitHub and Heroku for providing the technologies used to develop, analyse, visualise and deploy this project.

I would also like to acknowledge OpenAI and its AI tools for providing assistance during the development process. AI support was used as a learning and development aid for areas such as troubleshooting, understanding technical concepts, refining approaches, debugging and improving the project workflow. All analysis, interpretation, model evaluation, business recommendations and final project decisions were reviewed and validated as part of my own project work.

Finally, I would like to thank everyone involved in creating and maintaining the learning materials, documentation and resources that helped me complete this project and develop my confidence in applying data analytics and AI techniques to a real-world business problem.


---

# Reflection

This project provided an opportunity to apply the complete data analytics workflow to a real-world dataset, from data collection and cleaning through exploratory analysis, statistical testing, machine learning and interactive visualisation.

One of the main learning experiences was understanding how different analytical techniques support different stages of a project. Exploratory analysis helped identify patterns in passenger satisfaction, while statistical testing was used to determine whether an observed relationship was statistically significant. Machine learning then demonstrated how the available features could be used for prediction.

Several technical challenges were encountered during development. Logistic Regression initially failed to converge within the specified number of iterations. Standardising the numerical features within the preprocessing pipeline resolved this issue and reinforced the importance of appropriate preprocessing when applying machine-learning algorithms.

Developing the Streamlit dashboard also required adapting the analysis for an interactive audience. Issues involving file paths, widget state, filtering logic and indentation were identified through testing and corrected. Adding interactive filters demonstrated how analytical results can be transformed from static notebook outputs into a tool that stakeholders can explore themselves.

The project also reinforced the importance of reproducibility. Notebooks were validated using a fresh kernel and Run All before being committed, while the Streamlit application was tested locally and checked for Python syntax errors.

Overall, the project strengthened my understanding of how data cleaning, statistics, visualisation, machine learning, business requirements and interactive reporting work together within an end-to-end analytics project. These skills provide a foundation for adapting to new datasets, analytical methods and tools in future data analytics work.


---

# Dashboard Design and User Experience

The Streamlit dashboard was designed to present the main analytical findings in a clear and accessible format for non-technical stakeholders.

The dashboard uses a structured information hierarchy, beginning with high-level KPI metrics before progressing to satisfaction patterns, service insights, machine-learning performance and business recommendations.

Interactive sidebar filters allow users to explore the data by:

* Type of Travel
* Travel Class
* Customer Type
* Gender

A **Reset Filters** button allows users to quickly return the dashboard to its default view.

Relevant KPI metrics and analytical charts update dynamically when filters are selected, giving users control over the information displayed.

Machine-learning performance and feature-importance results remain fixed because these values represent the evaluation of the final models on the original test dataset and were not recalculated for individual dashboard filter selections.

Clear headings, descriptive chart titles and consistent dashboard sections were used to make the application easier to navigate and interpret.