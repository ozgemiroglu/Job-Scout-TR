# 🎯 Job-Scout-AI: Semantic Job Matching & Analysis Tool

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![NLP](https://img.shields.io/badge/NLP-Sentence--Transformers-green)
![Scraping](https://img.shields.io/badge/Scraping-JobSpy-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Job-Scout-AI** is an intelligent job search and ranking application that moves beyond traditional keyword-based searches. By utilizing **Natural Language Processing (NLP)**, it analyzes the semantic similarity between a user's professional profile and real-time job listings from **LinkedIn** and **Indeed**.



## Why Job-Scout-AI?

Traditional job boards often return generic or irrelevant results. This tool bridges the gap between deep professional expertise and modern AI by providing:
- **Semantic Ranking:** It understands the "intent" and "context" of a job description rather than just matching words.
- **Personalized Scoring:** Every job is assigned a **Match Score (%)** based on your specific background (e.g., Portfolio Management, Risk Analysis, Basel Criteria).
- **Automated Reporting:** Analyzes hundreds of listings in seconds and exports them into an organized Excel report, allowing you to focus only on high-value opportunities.

## Tech Stack

- **Python:** Core logic and automation.
- **Sentence-Transformers (SBERT):** Used to generate deep-learning-based embeddings for semantic similarity calculation.
- **JobSpy:** Handles high-performance, real-time scraping from major job boards.
- **Pandas:** Manages data structuring, ranking, and Excel generation.



## Getting Started

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/Job-Scout-TR.git](https://github.com/YOUR_USERNAME/Job-Scout-TR.git)
cd Job-Scout-TR
pip install -r requirements.txt

```

### 2. Configuration
Edit the `me.txt` file to define your search criteria and professional summary:

```text
ARANAN POZİSYON: [e.g., Senior Portfolio Manager]
ŞEHİR: [e.g., Istanbul]
DENEYİM VE ÖZET: [e.g., 25 years of experience in banking...]
```
### 3. Execution

Run the main script to start the analysis:

```bash

python main.py
```

📊 Sample Output

The application generates an Excel file named Analysis_Report_...xlsx. The report includes:

Match Score (%): How well the job aligns with your profile.
Position & Company: Cleaned job title and employer name.
Job URL: Direct link to the listing for immediate application.
