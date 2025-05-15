# Customer Review Sentiment Analysis Pipeline (E-Commerce Platform)

This project is a full data engineering and analytics pipeline designed to collect, store, transform, and analyze customer reviews from various e-commerce platforms (Amazon, AliExpress, etc.). The goal is to extract insights from customer feedback to support product improvement and customer experience strategies.

This repository documents the end-to-end process of collecting, transforming, and analyzing customer review data from major e-commerce platforms like **Amazon** and **AliExpress**. The analysis workflow is built using **Python**, **Azure Data Lake**, **Databricks (PySpark)**, **PostgreSQL**, and **Power BI**.

---

## Project Overview

The goal of this project is to collect customer review data from global e-commerce platforms and use cloud-based data engineering tools to clean, transform, and analyze insights for product improvement, sentiment trends, and market feedback.

Team Data Collection: Team members scraped or accessed review data via API from Amazon and AliExpress.

Version Control: All raw review data files were submitted to a shared GitHub repository: mayfair_project.

Data Storage: Raw files were downloaded locally, organized into a raw_data folder, and uploaded to Azure Data Lake Storage using Python in Visual Studio Code (VS Code).

Data Processing: Files from Data Lake were read into Databricks for cleaning, transformation, and enrichment using PySpark.

Data Persistence: Transformed data was transferred to a PostgreSQL database via spark.write.jdbc().

Data Visualization: Power BI connected directly to PostgreSQL to create interactive dashboards and reports.

--

## Data Architecture


!{Data Architecture}(https://github.com/adetonayusuf/mayfairecommers/blob/main/Mayfare%20Data%20Architecture.drawio.png)



---

## 1. Data Collection

- Scraped or retrieved customer review data via APIs from:

    - Amazon

    - AliExpress and similar platforms using **web scraping tools** (like `BeautifulSoup`, `Selenium`) or public **REST APIs**

- Format: .csv or .json

- Each team member contributed a portion of the dataset.

--

## 2 Upload to GitHub

All individual `.csv` submissions were committed to the shared GitHub repository:
🔗 [GitHub Repo – Raw Submissions](https://github.com/amdari-mayfair/mayfair_project)

---

## 3. Local Consolidation & Raw Folder Creation

After data collection:
- Downloaded all individual contributions locally.

- Consolidated files into a raw_data/ directory.

--

## 4. Upload to Azure Data Lake (via VS Code + Python)

- Created Azure Storage Account: mayfairproject

- Used SAS token authentication to upload the raw_data folder to a blob container (customer-reviews) using Python in VS Code.

--

## 5. Mount Data Lake Data &  Data Transformation in Databricks

- Mounted Data Lake into Databricks using dbutils.fs.mount()

- Loaded CSVs into a Spark DataFrame:

- Cleaned & transformed data:

      - Renamed columns

      - Casted data types (e.g., rating as integer)

      - Trimmed whitespaces

      - Converted date fields

## 6.  Load into PostgreSQL

- Used spark.write.jdbc() to push cleaned data into local PostgreSQL database.
  
- Set up a local PostgreSQL DB or tunnel via ngrok

- Wrote the transformed data to PostgreSQL using JDBC:
