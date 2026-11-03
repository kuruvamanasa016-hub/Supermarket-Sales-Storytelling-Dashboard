
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Sales Story Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM DESIGN
# -------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #F3F6FA;
}
section[data-testid="stSidebar"] {
    background-color: #142B4F;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}
div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 8px;
    border: 1px solid #DCE4EF;
}
h1, h2, h3 {
    color: #19365F;
}
.story {
    background-color: #E4EDF9;
    padding: 15px;
    border-left: 5px solid #315F9E;
    border-radius: 5px;
    color: #19365F;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "sales_data" not in st.session_state:
    st.session_state.sales_data = []

# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------
st.sidebar.title("SALES STORY")
st.sidebar.caption("DASHBOARD")

page = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Sales Trends",
        "Product Insights",
        "Regional Analysis"
    ]
)

st.sidebar.divider()

# -------------------------------------------------
# DATA ENTRY FORM
# -------------------------------------------------
st.sidebar.subheader("Add Sales Record")

with st.sidebar.form("sales_form"):

    order_date = st.date_input("Order Date")

    region = st.selectbox(
        "Region",
        ["East", "West", "North", "South", "Central"]
    )

    category = st.selectbox(
        "Category",
        ["Technology", "Furniture", "Office Supplies"]
    )

    product = st.selectbox(
        "Product",
        [
            "Laptop",
            "Mobile Phone",
            "Printer",
            "Keyboard",
            "Monitor",
            "Desk",
            "Storage Cabinet",
            "Bookcase"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    unit_price = st.number_input(
        "Unit Price",
        min_value=0.01,
        value=1000.0,
        step=100.0
    )

    discount = st.number_input(
        "Discount (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    cost = st.number_input(
        "Total Cost",
        min_value=0.0,
        value=500.0,
        step=50.0
    )

    add_record = st.form_submit_button(
        "Add Sales Record",
        use_container_width=True
    )

    if add_record:

        gross_sales = quantity * unit_price
        sales = gross_sales * (1 - discount / 100)
        profit = sales - cost

        st.session_state.sales_data.append({
            "Order Date": pd.to_datetime(order_date),
            "Region": region,
            "Category": category,
            "Product": product,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Discount": discount,
            "Sales": round(sales, 2),
            "Cost": round(cost, 2),
            "Profit": round(profit, 2)
        })

        st.sidebar.success("Record added successfully!")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
if st.session_state.sales_data:

    df = pd.DataFrame(st.session_state.sales_data)

else:
    # Demonstration data when no records are entered
    df = pd.DataFrame([
        {
            "Order Date": pd.Timestamp("2024-01-02"),
            "Region": "East",
            "Category": "Technology",
            "Product": "Laptop",
            "Quantity": 3,
            "Unit Price": 50000,
            "Discount": 5,
            "Sales": 142500,
            "Cost": 110000,
            "Profit": 32500
        },
        {
            "Order Date": pd.Timestamp("2024-02-15"),
            "Region": "West",
            "Category": "Furniture",
            "Product": "Desk",
            "Quantity": 5,
            "Unit Price": 10000,
            "Discount": 10,
            "Sales": 45000,
            "Cost": 35000,
            "Profit": 10000
        },
        {
            "Order Date": pd.Timestamp("2024-03-10"),
            "Region": "South",
            "Category": "Office Supplies",
            "Product": "Printer",
            "Quantity": 4,
            "Unit Price": 12000,
            "Discount": 5,
            "Sales": 45600,
            "Cost": 32000,
            "Profit": 13600
        },
        {
            "Order Date": pd.Timestamp("2024-04-20"),
            "Region": "Central",
            "Category": "Technology",
            "Product": "Mobile Phone",
            "Quantity": 6,
            "Unit Price": 20000,
            "Discount": 5,
            "Sales": 114000,
            "Cost": 85000,
            "Profit": 29000
        },
        {
            "Order Date": pd.Timestamp("2024-05-12"),
            "Region": "East",
            "Category": "Furniture",
            "Product": "Bookcase",
            "Quantity": 3,
            "Unit Price": 15000,
            "Discount": 0,
            "Sales": 45000,
            "Cost": 30000,
            "Profit": 15000
        },
        {
            "Order Date": pd.Timestamp("2024-06-05"),
            "Region": "West",
            "Category": "Technology",
            "Product": "Monitor",
            "Quantity": 4,
            "Unit Price": 18000,
            "Discount": 10,
            "Sales": 64800,
            "Cost": 50000,
            "Profit": 14800
        },
        {
            "Order Date": pd.Timestamp("2024-07-15"),
            "Region": "North",
            "Category": "Office Supplies",
            "Product": "Keyboard",
            "Quantity": 10,
            "Unit Price": 2000,
            "Discount": 5,
            "Sales": 19000,
            "Cost": 12000,
            "Profit": 7000
        },
        {
            "Order Date": pd.Timestamp("2024-08-20"),
            "Region": "East",
            "Category": "Technology",
            "Product": "Laptop",
            "Quantity": 5,
            "Unit Price": 50000,
            "Discount": 5,
            "Sales": 237500,
            "Cost": 180000,
            "Profit": 57500
        }
    ])

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------
st.sidebar.subheader("Filters")

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date)
)

regions = st.sidebar.multiselect(
    "Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

categories = st.sidebar.multiselect(
    "Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

products = st.sidebar.multiselect(
    "Product",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

# -------------------------------------------------
# APPLY FILTERS
# -------------------------------------------------
if len(date_range) == 2:

    start_date, end_date = date_range

    filtered_df = df[
        (df["Order Date"].dt.date >= start_date) &
        (df["Order Date"].dt.date <= end_date) &
        (df["Region"].isin(regions)) &
        (df["Category"].isin(categories)) &
        (df["Product"].isin(products))
    ]

else:
    filtered_df = df[
        (df["Region"].isin(regions)) &
        (df["Category"].isin(categories)) &
        (df["Product"].isin(products))
    ]

# -------------------------------------------------
# DASHBOARD HEADER
# -------------------------------------------------
titles = {
    "Overview": "Sales Performance | Executive Overview",
    "Sales Trends": "Sales Trends | When Do We Win?",
    "Product Insights": "Product Insights | What Drives Value?",
    "Regional Analysis": "Regional Analysis | Where Is Growth?"
}

st.title(titles[page])
st.caption("A guided story from business performance to actionable decisions")

if filtered_df.empty:

    st.warning("No records match the selected filters.")

else:

    # -------------------------------------------------
    # KPI CALCULATIONS
    # -------------------------------------------------
    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()

    profit_margin = (
        total_profit / total_sales * 100
        if total_sales != 0 else 0
    )

    avg_order_value = filtered_df["Sales"].mean()

    # -------------------------------------------------
    # KPI CARDS
    # -------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "TOTAL SALES",
        f"₹{total_sales:,.0f}"
    )

    col2.metric(
        "TOTAL PROFIT",
        f"₹{total_profit:,.0f}"
    )

    col3.metric(
        "PROFIT MARGIN",
        f"{profit_margin:.1f}%"
    )

    col4.metric(
        "AVG. ORDER VALUE",
        f"₹{avg_order_value:,.0f}"
    )

    st.divider()

    # -------------------------------------------------
    # MONTHLY SALES DATA
    # -------------------------------------------------
    monthly_df = filtered_df.copy()

    monthly_df["Month"] = (
        monthly_df["Order Date"].dt.to_period("M").astype(str)
    )

    monthly_sales = (
        monthly_df.groupby("Month", as_index=False)["Sales"]
        .sum()
    )

    # -------------------------------------------------
    # 1. EXECUTIVE OVERVIEW
    # -------------------------------------------------
    if page == "Overview":

        col1, col2 = st.columns([2, 1])

        with col1:

            st.subheader("1. Sales momentum across months")

            fig1 = px.line(
                monthly_sales,
                x="Month",
                y="Sales",
                markers=True,
                title="Monthly Sales Performance"
            )

            fig1.update_traces(
                line=dict(color="#3478C9", width=3)
            )

            fig1.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white",
                xaxis_title="Month",
                yaxis_title="Sales (₹)"
            )

            st.plotly_chart(fig1, use_container_width=True)

        with col2:

            st.subheader("2. Sales by category")

            category_sales = (
                filtered_df.groupby("Category", as_index=False)["Sales"]
                .sum()
            )

            fig2 = px.bar(
                category_sales,
                x="Sales",
                y="Category",
                orientation="h",
                color="Sales",
                color_continuous_scale="Blues",
                title="Category Contribution"
            )

            fig2.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )

            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("""
        <div class="story">
        <b>STORY 01 | Understand overall performance.</b><br>
        Compare monthly sales momentum with category contribution
        to identify the categories driving business revenue.<br><br>
        <b>Next step:</b> Protect high-performing categories while
        investigating low-performing categories.
        </div>
        """, unsafe_allow_html=True)

        st.subheader("HOW TO READ THIS")

        st.write(
            "Start with the KPIs, check whether monthly sales are "
            "rising or falling, then compare category contribution."
        )

    # -------------------------------------------------
    # 2. SALES TRENDS
    # -------------------------------------------------
    elif page == "Sales Trends":

        st.subheader("Monthly sales trend")

        fig = px.line(
            monthly_sales,
            x="Month",
            y="Sales",
            markers=True,
            title="How are sales changing over time?"
        )

        fig.update_traces(
            line=dict(color="#3478C9", width=3)
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis_title="Month",
            yaxis_title="Sales (₹)"
        )

        st.plotly_chart(fig, use_container_width=True)

        if len(monthly_sales) > 0:

            best_month = monthly_sales.loc[
                monthly_sales["Sales"].idxmax()
            ]

            low_month = monthly_sales.loc[
                monthly_sales["Sales"].idxmin()
            ]

            st.markdown(f"""
            <div class="story">
            <b>STORY 02 | Peaks and dips reveal sales momentum.</b><br>
            Highest sales occurred in <b>{best_month['Month']}</b>,
            with ₹{best_month['Sales']:,.2f}.<br>
            Lowest sales occurred in <b>{low_month['Month']}</b>,
            with ₹{low_month['Sales']:,.2f}.<br><br>
            <b>Action:</b> Compare strong and weak months with
            promotions, stock availability and regional demand.
            </div>
            """, unsafe_allow_html=True)

        st.subheader("DECISION PROMPT")

        st.write(
            "Which months repeatedly underperform, and what "
            "operational event could explain the pattern?"
        )

    # -------------------------------------------------
    # 3. PRODUCT INSIGHTS
    # -------------------------------------------------
    elif page == "Product Insights":

        col1, col2 = st.columns([2, 1])

        with col1:

            st.subheader("Top products by sales")

            product_sales = (
                filtered_df.groupby("Product", as_index=False)["Sales"]
                .sum()
                .sort_values("Sales", ascending=True)
                .tail(10)
            )

            fig1 = px.bar(
                product_sales,
                x="Sales",
                y="Product",
                orientation="h",
                color="Sales",
                color_continuous_scale="Blues",
                title="Top 10 Products"
            )

            fig1.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )

            st.plotly_chart(fig1, use_container_width=True)

        with col2:

            st.subheader("Profit contribution")

            profit_product = (
                filtered_df.groupby("Category", as_index=False)["Profit"]
                .sum()
            )

            fig2 = px.pie(
                profit_product,
                names="Category",
                values="Profit",
                hole=0.4,
                title="Profit by Category"
            )

            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("""
        <div class="story">
        <b>STORY 03 | Revenue leaders are not always the same as profit leaders.</b><br>
        Compare product sales with profit contribution to identify
        products generating strong business value.<br><br>
        <b>Action:</b> Prioritize profitable products and review
        discounting and costs on high-sales, low-profit items.
        </div>
        """, unsafe_allow_html=True)

        st.subheader("DECISION PROMPT")

        st.write(
            "Are the top-selling products also generating healthy margins?"
        )

        # Product-level comparison
        st.subheader("Product Sales and Profit Comparison")

        product_comparison = (
            filtered_df.groupby("Product", as_index=False)
            [["Sales", "Profit"]].sum()
        )

        fig3 = px.bar(
            product_comparison,
            x="Product",
            y=["Sales", "Profit"],
            barmode="group",
            title="Sales vs Profit by Product"
        )

        st.plotly_chart(fig3, use_container_width=True)

    # -------------------------------------------------
    # 4. REGIONAL ANALYSIS
    # -------------------------------------------------
    elif page == "Regional Analysis":

        col1, col2 = st.columns([2, 1])

        with col1:

            st.subheader("Sales by region")

            region_sales = (
                filtered_df.groupby("Region", as_index=False)["Sales"]
                .sum()
                .sort_values("Sales", ascending=True)
            )

            fig1 = px.bar(
                region_sales,
                x="Sales",
                y="Region",
                orientation="h",
                color="Sales",
                color_continuous_scale="Blues",
                title="Regional Sales Performance"
            )

            fig1.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )

            st.plotly_chart(fig1, use_container_width=True)

        with col2:

            st.subheader("Profit by region")

            region_profit = (
                filtered_df.groupby("Region", as_index=False)["Profit"]
                .sum()
            )

            fig2 = px.bar(
                region_profit,
                x="Region",
                y="Profit",
                color="Profit",
                color_continuous_scale="Blues",
                title="Regional Profit"
            )

            fig2.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )

            st.plotly_chart(fig2, use_container_width=True)

        st.markdown("""
        <div class="story">
        <b>STORY 04 | Regional sales and profit together reveal where growth is efficient.</b><br>
        Compare regional revenue with profit to distinguish
        high-volume regions from highly profitable regions.<br><br>
        <b>Action:</b> Replicate successful regional practices
        and investigate regions with weaker profit margins.
        </div>
        """, unsafe_allow_html=True)

        st.subheader("DECISION PROMPT")

        st.write(
            "Where should the next sales campaign or field-support budget be allocated?"
        )

        # Regional profit margin
        regional_details = (
            filtered_df.groupby("Region", as_index=False)
            [["Sales", "Profit"]].sum()
        )

        regional_details["Profit Margin (%)"] = (
            regional_details["Profit"] /
            regional_details["Sales"].replace(0, float("nan")) * 100
        )

        st.subheader("Regional Performance Details")

        st.dataframe(
            regional_details.round(2),
            use_container_width=True
        )

    # -------------------------------------------------
    # FILTERED DATA AND DOWNLOAD
    # -------------------------------------------------
    st.divider()

    with st.expander("View Filtered Sales Records"):

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Filtered Sales Data",
        data=csv,
        file_name="sales_data.csv",
        mime="text/csv"
    )

# -------------------------------------------------
# CLEAR DATA
# -------------------------------------------------
st.sidebar.divider()

if st.sidebar.button("Clear All Entered Records"):

    st.session_state.sales_data = []
    st.rerun()

st.caption(
    "Sales Story Dashboard | Illustrative data for demonstration"
)
