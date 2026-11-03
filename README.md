# Sales Data Visualization Dashboard with Storytelling

An interactive sales analytics dashboard built with **Python, Streamlit, Pandas, and Plotly**. The dashboard presents sales information as a business story, helping users explore overall performance, monthly trends, product performance, and regional results.

## Dashboard Sections

1. **Executive Overview** – Total sales, total profit, profit margin, average order value, monthly sales, and category contribution.
2. **Sales Trends** – Monthly sales performance, highest- and lowest-performing months, and business decision prompts.
3. **Product Insights** – Top products by sales, profit contribution by category, and sales-versus-profit comparison.
4. **Regional Analysis** – Sales and profit by region, plus regional profit-margin details.

## Features

- Add sales records through the sidebar form.
- Filter records by date range, region, category, and product.
- Interactive Plotly charts.
- KPI summary cards and storytelling insights.
- View filtered sales records.
- Download filtered records as a CSV file.

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly

## Project Structure

```text
sales-story-dashboard/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation and Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the URL and repository name with your GitHub details.

### 2. (Recommended) Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`.

## Using the Dashboard

1. Open the application.
2. Use the sidebar to select a dashboard section.
3. Add a sales record using the **Add Sales Record** form.
4. Apply the date, region, category, and product filters.
5. Explore the charts and storytelling insights.
6. Expand **View Filtered Sales Records** or download the filtered data as CSV.

## Data and Calculation Notes

- The application starts with a small set of illustrative demonstration records so that charts are visible immediately.
- Records added through the form are stored in Streamlit session state. They are temporary and may be lost when the session is reset or the application restarts.
- For each newly entered record:
  - `Gross Sales = Quantity × Unit Price`
  - `Sales = Gross Sales × (1 − Discount / 100)`
  - `Profit = Sales − Total Cost`
- The demonstration records are not the 900-row dataset described in the project documentation. Replace or extend the demonstration data with a validated dataset before drawing real business conclusions.

## Deployment

The application can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/). Push `app.py` and `requirements.txt` to a GitHub repository, then create a new app in Streamlit Community Cloud and select the repository and `app.py` entry point.

## Disclaimer

This project is intended for learning and demonstration. The included sample values are illustrative and should not be treated as actual company results.
