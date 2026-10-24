# AI-Driven Business Intelligence & Presentation Automation Pipeline

### Python | Pandas | Matplotlib | ReportLab | PowerPoint Automation | Financial Analytics

## Project Overview

This project demonstrates an automated business intelligence and financial reporting workflow for multifamily real estate operations.

The pipeline transforms synthetic property-level financial data into calculated performance metrics, visualizations, management commentary, a PDF investor report, and a PowerPoint presentation.

**Business objective:** Reduce repetitive reporting work, standardize financial analysis, and make operational performance easier to communicate to investors and management.

The current version uses Python-based rules for automated commentary rather than a generative AI API.

## Business Scenario

Parkside Apartments is a simulated 100-unit multifamily property with 12 months of operational and financial data for 2026.

The analysis evaluates:

- Rental and effective revenue
- Operating expenses
- Net Operating Income (NOI)
- Occupancy performance
- Budget variances
- Monthly financial trends
- Management recommendations

All data is synthetic and used exclusively for portfolio demonstration.

## Key Financial Results

| Performance Metric | 2026 Result |
|---|---:|
| Average Occupancy | 95.17% |
| Effective Revenue | $1,434,500 |
| Operating Expenses | $750,500 |
| Net Operating Income | $684,000 |
| Revenue vs. Budget | -$44,500 |
| Expenses vs. Budget | +$15,500 |
| Strongest NOI Month | December ($61,500) |
| Weakest NOI Month | May ($49,600) |

### Business Insights

1. Average occupancy exceeded the 95% operational target.
2. Revenue finished $44,500 below budget.
3. Operating expenses exceeded budget by $15,500.
4. December delivered the strongest monthly NOI.
5. May recorded the weakest monthly NOI.

These findings support recommendations to investigate revenue shortfalls, monitor expenses, and analyze occupancy-related performance.

## Automation Workflow

**Synthetic CSV Data → Python Financial Analysis → KPI Calculations → Data Visualization → Rule-Based Management Summary → PDF Report + PowerPoint Presentation**

The workflow is organized into reusable Python scripts.

### 1. Financial Data Processing

`src/analyze_metrics.py`

Processes operational data and calculates financial performance metrics.

### 2. Automated Data Visualization

`src/create_charts.py`

Generates a monthly NOI visualization using Matplotlib.

### 3. Management Commentary Generation

`src/generate_summary.py`

Creates standardized financial insights and recommendations using Python rules.

### 4. Automated PDF Reporting

`src/create_report.py`

Produces an investor performance report with financial KPIs, a chart, and management commentary.

### 5. Automated PowerPoint Generation

`src/create_presentation.py`

Generates a six-slide investor presentation with financial results, trends, recommendations, and methodology.

## Technology Stack

| Technology | Application |
|---|---|
| Python | Workflow automation |
| Pandas | Data analysis and KPI calculations |
| Matplotlib | Financial visualization |
| ReportLab | PDF report generation |
| python-pptx | PowerPoint presentation automation |
| Google Colab | Development and testing |
| GitHub | Version control and portfolio hosting |

## Project Deliverables

**Investor Performance Report**

[View PDF Report](outputs/investor_report.pdf)

**Automated Investor Presentation**

[Download PowerPoint Presentation](outputs/investor_presentation.pptx)

**Financial Visualization**

[View Monthly NOI Chart](outputs/monthly_noi.png)

## How to Run

Clone the repository:

```bash
git clone https://github.com/julykalyta2/AI-Driven-Business-Intelligence-Presentation-Automation-Pipeline.git
```

Navigate into the project directory:

```bash
cd AI-Driven-Business-Intelligence-Presentation-Automation-Pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline in sequence:

```bash
python src/analyze_metrics.py
python src/create_charts.py
python src/generate_summary.py
python src/create_report.py
python src/create_presentation.py
```

Generated deliverables are saved in the `outputs` directory.

## Skills Demonstrated

- Financial statement and operational KPI analysis
- Budget variance analysis
- Data processing and transformation
- Python workflow automation
- Business intelligence reporting
- Financial data visualization
- Automated document and presentation generation
- Translating analytical findings into management recommendations
- GitHub project organization and documentation

## Future Enhancements

Potential extensions include:

- Integrating an LLM API for AI-generated management commentary
- Adding automated data quality checks
- Supporting multiple properties and portfolio-level comparisons
- Connecting to real estate CRM or approved property management data sources
- Scheduling recurring investor reports
- Measuring reporting time savings against a manual workflow

## Data & AI Disclosure

This project uses **synthetic financial data** and does not represent an actual investment property.

The management commentary is generated using deterministic Python rules. No generative AI model is currently used in the reporting pipeline.

## Author

**Julie Kalyta**

Business Intelligence | Financial Analytics | Python Automation | Real Estate Operations

[GitHub Profile](https://github.com/julykalyta2)
