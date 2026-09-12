# 📦 International Hybrid Retail, Pharmacy & Restaurant Inventory Suite

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated multi-department inventory engine, batch tracking ledger, and interactive visual dashboard built for complex retail operations—including mini-marts, pharmacy chains, boutique stores, and supermarket-bistro hybrids.

This repository houses both the **Python-driven Streamlit web application** for real-time interactive testing and the `openpyxl` engine for generating offline **Microsoft Excel (`.xlsx`) and Google Sheets master workbooks**.

---

## 🌟 Key Features & Business Modules

- **🛍️ Unit-Based Retail Stock Ledger:** Tracks packaged merchandise, barcode SKUs, daily unit sales, damaged goods, and automated reorder alerts.
- **💊 Pharmacy & Expiry Batch Control:** Monitors prescription and OTC medications by batch number, dosage form, expiration dates, and critical safety thresholds.
- **🍳 Kitchen & Restaurant Prep Engine:** Tracks raw material batching (kg/L), meal consumption, and kitchen spoilage for takeaway restaurants and internal bistros.
- **🌐 Globally Compatible:** Native `$#,##0.00` double-currency precision designed for SMEs across international markets (US, UK, EU, Africa).

---

## 📂 Repository Layout

```text
hybrid-inventory-tracker/
├── .streamlit/
│   └── config.toml                # Streamlit UI theme setup
├── data/
│   └── Hybrid_Inventory_Restock_Master.xlsx # Excel master workbook
├── app.py                         # Multi-tab Streamlit Web Application
├── generator.ipynb                # Jupyter Notebook Excel script
├── requirements.txt               # Environment dependencies
└── README.md                      # Documentation & product overview

Interactive Live Web Application
Test the multi-department inventory model live in your browser:

👉 Launch Streamlit Interactive Web App (Replace with your deployed Streamlit URL)

🛍️ Master Template Access (Excel & Google Sheets)
For commercial deployment, offline use, or custom store setups:

👉 Buy Master Template on Gumroad

⚙️ Local Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/bamideleadedeji/hybrid-inventory-tracker.git](https://github.com/bamideleadedeji/hybrid-inventory-tracker.git)
cd hybrid-inventory-tracker
Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Run the Streamlit app:

Bash
streamlit run app.py
 Built With
Python 3.10+

Streamlit - Multi-tab interactive web interface

Pandas - Dynamic inventory aggregation & threshold logic

OpenPyXL - Excel workbook formatting & automated formula generation

Plotly - Category distribution & loss analytics

👨‍💻 Author & Contact
Bamidele Adedeji

Founder & Principal Consultant, Dejifolakemi Enterprises

GitHub: @bamideleadedeji

Gumroad Store: Dejifolakemi Enterprises
