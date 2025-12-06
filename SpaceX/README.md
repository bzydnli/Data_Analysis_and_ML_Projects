# SpaceX Falcon 9 Landing Prediction

This project is part of the IBM Data Science Capstone.  
It explores SpaceX Falcon 9 launch data and builds machine learning models to predict whether the **first stage will successfully land**.

If a Falcon 9 first stage can be reused, the launch cost drops dramatically (SpaceX advertises ~\$62M vs. \$165M+ for traditional providers).  
Being able to predict landing success is therefore valuable for any competitor that wants to **estimate launch costs and make informed bids**.

---

## Project Goals

- Collect and consolidate SpaceX launch data from multiple sources  
- Perform data wrangling and exploratory data analysis (EDA)  
- Visualize launch patterns, success rates and geographic information  
- Build, tune and evaluate classification models that predict landing outcome  
- Deploy interactive analytics with **Folium** and **Plotly Dash**

---

## Data Sources

Data is collected and combined from:

- **SpaceX REST API** – launch records, rocket and payload information  
- **Web scraping (Wikipedia)** – additional details for launches and payloads  
- **CSV files** generated during the labs (cleaned and merged datasets)

---

## Repository Structure (SpaceX folder)

- `spacex_data_collection_api.ipynb`  
  - Calls the **SpaceX REST API**, normalizes JSON responses and saves raw launch data.

- `webscraping.ipynb`  
  - Uses **BeautifulSoup** to scrape Wikipedia tables and enrich the launch dataset.

- `Data Wrangling EDA.ipynb`  
  - Cleans the data, handles missing values, converts data types and creates derived features.
  - Produces the final analytical dataset used in later steps.

- `eda_dataviz.ipynb`  
  - Exploratory data analysis with **Matplotlib / Seaborn**  
  - Visualizes relationships between:
    - Launch site and success rate  
    - Orbit type and success rate  
    - Payload mass, orbit and landing outcome  
    - Trends in success rate over the years

- `eda_sql_coursera_sqllite.ipynb`  
  - Loads the cleaned data into **SQLite**  
  - Uses SQL queries to:
    - Find unique launch sites  
    - Aggregate payload statistics  
    - Analyze mission and landing outcomes  
    - Identify boosters with maximum payload etc.

- `launch_site_location.ipynb`  
  - Creates **Folium** maps to show:
    - Locations of all launch sites  
    - Clustered markers for launches  
    - Circles around launch sites to visualize the local area

- `dash.py`  
  - **Plotly Dash dashboard** that includes:
    - Dropdown to select launch site  
    - Pie chart of launch success counts  
    - Range slider for payload mass  
    - Scatter plot of payload vs. outcome, colored by booster version

- `SpaceX_Machine Learning Prediction_Part_5.ipynb`  
  - Builds and evaluates classification models to predict whether the first stage lands:
    - Logistic Regression  
    - Support Vector Machine (SVM)  
    - Decision Tree  
    - K-Nearest Neighbors (KNN)  
  - Uses **StandardScaler** for feature scaling  
  - Applies **GridSearchCV** for hyperparameter tuning  
  - Compares model accuracies and plots:
    - Accuracy bar chart  
    - Confusion matrix for the best model

---

## Methodology

1. **Data Collection**
   - Retrieve launch data from the SpaceX REST API.
   - Scrape complementary information from Wikipedia.
   - Save intermediate datasets for reproducibility.

2. **Data Wrangling**
   - Merge API and scraped data.
   - Clean column names and data types.
   - Handle missing values and inconsistent entries.
   - Engineer features such as:
     - Binary landing outcome (class)
     - Encoded categorical variables (launch site, orbit, landing pad, booster)

3. **Exploratory Data Analysis (EDA)**
   - Statistical summaries and correlation inspection.
   - Visual patterns between:
     - Orbit and success rate  
     - Payload mass and landing outcome  
     - Launch site and mission success  
     - Yearly trends in success rate

4. **Interactive Visual Analytics**
   - **Folium** maps to explore geographic distribution of launch sites and missions.
   - **Plotly Dash** dashboard for:
     - Dynamic filtering by launch site
     - Exploring payload ranges vs. success probability

5. **Predictive Modeling**
   - Train/test split and additional validation split.
   - Standardization of numeric features.
   - Model training with:
     - Logistic Regression  
     - SVM  
     - Decision Tree  
     - KNN  
   - Hyperparameter tuning using GridSearchCV (cv = 10).
   - Model selection based on test accuracy.
   - Evaluation using accuracy score and confusion matrix.

---

## Key Insights

- Some launch sites (e.g., **KSC LC-39A**) show higher overall success rates.  
- **Orbit type** and **payload mass** have a visible relationship with landing success.  
- Newer booster versions (e.g., **B4, B5**) tend to achieve higher success rates, especially for heavier payloads.  
- The best-performing classification model achieves **high accuracy** with very few misclassifications, as confirmed by the confusion matrix.

---

## Technologies Used

- **Python**, **Jupyter Notebook**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **SQLite / SQL**
- **Requests**, **BeautifulSoup**
- **Folium**
- **Plotly Dash**
