# Python-Exploratory-Data-Analysis
# 📈 Global Sales & Profit Margin Data Analysis

This project features a comprehensive end-to-end data analysis pipeline built with Python. By analyzing historical business performance datasets across segments, countries, products, and temporal timelines, the code evaluates operational drivers, revenue streams, and critical profitability dynamics.

---

## 📊 Key Analytical Insights

Based on the generated visualizations, here is an executive breakdown of the business dataset performance metrics:

### 💼 Segment Performance & Financial Vulnerability
* **Government Dominance:** The **Government** sector stands out as the primary business engine, driving over **41.74% of total sales** and capturing the highest absolute profit share (exceeding \$10M).
* **Enterprise Risk Factor:** Despite capturing a substantial **14.24% of raw sales value**, the **Enterprise** segment registers an **overall net financial loss**. This points to severe margin erosion, potentially due to unsustainable procurement overheads or aggressive discounting strategies.
* **Manufacturing Cost Distribution:** **Government** and **Channel Partners** account for the largest shares of manufacturing expenses at **36.8%** and **19.7%** respectively, closely matching their transactional volumes.

### 🗺️ Geographic & Product Performance
* **International Disparities:** Market sales are robust and relatively evenly distributed across **England, Canada, Germany, France, and the USA** (each fluctuating near or above the \$1M benchmark). Conversely, **India** presents a major market bottleneck, generating sub-baseline sales volumes under \$0.2M.
* **Product Volume Uniformity:** Product distribution is highly stable across the catalog. **Paseo** leads global consumption tracks at over **4,500 units sold**, closely followed by **Carretera** and **Amarilla**, while **VTT** experiences softer market demand at roughly **3,250 units**.

### 🗓️ Temporal Trends & Correlation
* **Positive Financial Correlation:** The sales-to-profit scatter distribution demonstrates a **strong, positive linear correlation**. This proves that increasing transaction sizes generally scales net profitability successfully across stable operational segments.
* **The High Volume Low Margin Reality:** A distribution histogram reveals the dataset is heavily **right-skewed**. Over 500 individual orders are concentrated in lower-tier pricing buckets (\$0 to \$100K), demonstrating that overall corporate health relies heavily on high-frequency, smaller transactions.

<img width="1245" height="408" alt="year,quarter,month sales" src="https://github.com/user-attachments/assets/729c13e9-8bc4-44b7-8a21-5d3114be69e9" />

<img width="640" height="480" alt="co-relation" src="https://github.com/user-attachments/assets/04632085-270e-4064-8c0d-528b49716e7d" />

<img width="640" height="480" alt="country wise sales" src="https://github.com/user-attachments/assets/17fd4fdb-a27d-4ad1-ae0a-1dc6a32b98d7" />

<img width="862" height="480" alt="highest selling products" src="https://github.com/user-attachments/assets/b37b6ef2-d8b4-48b3-bd50-117a15054e67" />

<img width="640" height="480" alt="histogram-sales" src="https://github.com/user-attachments/assets/6eb4f0c2-33d2-440b-aa65-7b3a0e692f1f" />

<img width="640" height="480" alt="mnf_price" src="https://github.com/user-attachments/assets/8ad52e7c-6516-4ce6-9266-5431616409b8" />

<img width="640" height="480" alt="month wise profit" src="https://github.com/user-attachments/assets/a73352dd-77e0-4aaa-b472-0b49d79cc4e2" />

<img width="640" height="480" alt="profit by segment" src="https://github.com/user-attachments/assets/78847140-4f4d-4272-8814-be5f5c28fb5c" />

<img width="640" height="480" alt="sales by segment" src="https://github.com/user-attachments/assets/f3e4c655-ccb1-4605-b693-ec8b1b3fe340" />

<img width="640" height="480" alt="segment wise sales-pie" src="https://github.com/user-attachments/assets/f28889ce-f523-458d-bf9b-88754fd243e5" />

















---

## 🛠️ Python Implementation Details

The provided data analysis script processes raw business information and generates multiple analytical charts using standard data science libraries:

### ⚙️ Analytical Components Inside the Script
1. **Aggregations & Groupings:** Uses `pandas.DataFrame.groupby()` to aggregate both `Sales` and `Profit` fields across categorical variables (`Segment`, `Country`, `Product_Name`).
2. **Data Profiling:** Runs foundational auditing checks using `df.columns` and `df.info()` to track column types and handle missing data.
3. **Statistical Distribution:** Employs `plt.hist()` to evaluate transaction density variations.
4. **Relational Analysis:** Uses `.corr()` alongside `plt.scatter()` to map statistical dependencies between top-line revenue and bottom-line earnings.

---

## 💻 Tech Stack & Requirements

The scripts are written in Python 3 and depend on the following core data science libraries:

```bash
pip install pandas numpy matplotlib openpyxl
```

| Library | Primary Use Case |
| :--- | :--- |
| **Pandas** | Data parsing, structural manipulation, aggregation, and filtering. |
| **NumPy** | Vectorized math arrays and missing value computation operations. |
| **Matplotlib** | Custom visualization layer rendering charts, histograms, and plots. |
| **Openpyxl** | Engine driving seamless ingestion of background Microsoft Excel sheets. |

---

## 🚀 Execution & Usage

To run the pipeline and view the visual dashboard components locally, configure your local storage paths and run the entry file:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Update your absolute local system path to point to your Excel dashboard data:
df = pd.read_excel(r"C:\DATA ANALYSIS\Sales Data_Dashboard.xlsx", sheet_name="Sheet18")

# 2. Execute the python script
# The system will profile columns and sequentially output all 10 analysis charts!
```

---

## 🗂️ Visualization Portfolio

The pipeline automatically compiles and presents the following diagnostic plots:

* **Segment Analysis Dashboard:** A breakdown comparing *Sales by Segment (Bar Chart)*, *Segment Wise Sales Distribution (Pie Chart)*, *Profit by Segment (Bar Chart)*, and *Segment wise Manufacturing Price Allocations (Pie Chart)*.
* **Socio-Economic & Geographical Plots:** Plots tracking absolute performance trends across *Sales by Country* and *Highest Selling Product Volume analysis*.
* **Time-Series Matrix:** A comprehensive 3-column sub-plot grid structuring *Sales by Year*, *Sales by Quarter*, and *Sales by Month* into a single visualization layer.
* **Financial Health Audits:** Statistical charts rendering the *Sales and Profit Co-Relation* scatter matrix alongside the *Sales Data-HIST* structural volume histogram.

* ## 👤 Author

**Debjyoti Paul**
Data Analyst 

