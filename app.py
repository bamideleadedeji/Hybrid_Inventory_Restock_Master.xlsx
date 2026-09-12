import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Hybrid Retail, Pharmacy & Kitchen Inventory Suite",
    page_icon="📦",
    layout="wide",
)

st.title("📦 International Hybrid Retail, Pharmacy & Restaurant Inventory Suite")
st.caption(
    "Automated Inventory, Expiration & Spoilage Engine | Designed for"
    " Multi-Department Enterprises, Mini-Marts, Pharmacies & Supermarket-Bistros"
)

# Sidebar Monetization Link
st.sidebar.header(" Download Master Template")
st.sidebar.info(
    "Need the full offline Excel & Google Sheets automated workbook?"
)
st.sidebar.markdown(
    "[👉 Buy Master Template on"
    " Gumroad](https://bamidele38.gumroad.com/l/sme-daily-tracker)"
)

# Navigation Tabs
tab_retail, tab_pharma, tab_kitchen = st.tabs(
    ["🛍️ Retail & Packaged Goods", "💊 Pharmacy & OTC Drugs", "🍳 Kitchen & Restaurant Prep"]
)

# -------------------------------------------------------------------
# TAB 1: RETAIL & PACKAGED GOODS
# -------------------------------------------------------------------
with tab_retail:
  st.subheader("1. General Retail Inventory Ledger")
  if "df_retail" not in st.session_state:
    st.session_state.df_retail = pd.DataFrame({
        "SKU": ["SKU-1001", "SKU-1002", "SKU-1004"],
        "Item Description": [
            "Organic Whole Milk 1L",
            "Coffee Beans 500g",
            "Sparkling Water 500ml",
        ],
        "Category": ["Beverages", "Pantry", "Beverages"],
        "Starting Stock": [50, 30, 120],
        "Restock": [20, 0, 0],
        "Units Sold": [45, 22, 40],
        "Damaged Loss": [2, 0, 0],
        "Min Threshold": [15, 10, 25],
        "Unit Cost ($)": [2.50, 8.00, 1.10],
    })

  edited_retail = st.data_editor(
      st.session_state.df_retail,
      num_rows="dynamic",
      use_container_width=True,
      key="ed_retail",
  )
  edited_retail["Ending Stock"] = (
      edited_retail["Starting Stock"]
      + edited_retail["Restock"]
      - (edited_retail["Units Sold"] + edited_retail["Damaged Loss"])
  )
  edited_retail["Status"] = edited_retail.apply(
      lambda r: "⚠️ REORDER NOW"
      if r["Ending Stock"] <= r["Min Threshold"]
      else "✅ OK",
      axis=1,
  )

  r_reorder = edited_retail[edited_retail["Status"] == "⚠️ REORDER NOW"]
  c1, c2, c3 = st.columns(3)
  c1.metric("Retail SKUs", len(edited_retail))
  c2.metric("Retail Reorder Items", len(r_reorder))
  c3.metric(
      "Retail Damaged Loss",
      f"${(edited_retail['Damaged Loss'] * edited_retail['Unit Cost ($)']).sum():,.2f}",
  )

  if not r_reorder.empty:
    st.error("Retail Stock Alerts:")
    st.dataframe(
        r_reorder[[
            "SKU",
            "Item Description",
            "Ending Stock",
            "Min Threshold",
            "Status",
        ]],
        use_container_width=True,
    )

# -------------------------------------------------------------------
# TAB 2: PHARMACY & OTC DRUGS
# -------------------------------------------------------------------
with tab_pharma:
  st.subheader("2. Pharmacy Batch Control & Expiration Ledger")
  if "df_pharma" not in st.session_state:
    st.session_state.df_pharma = pd.DataFrame({
        "Drug Code": ["MED-201", "MED-202", "MED-203"],
        "Medication Name": [
            "Amoxicillin 500mg",
            "Paracetamol 500mg Extra",
            "Vitamin C 1000mg",
        ],
        "Form": ["Capsules", "Tablets", "Chewable"],
        "Batch No": ["BTH-8821", "BTH-4412", "BTH-9901"],
        "Expiry Date": ["2027-12-31", "2026-11-30", "2028-06-15"],
        "Start Stock": [150, 500, 200],
        "Dispensed": [40, 420, 185],
        "Expired / Damaged": [0, 5, 0],
        "Safety Threshold": [50, 100, 40],
        "Unit Price ($)": [12.50, 3.20, 5.00],
    })

  edited_pharma = st.data_editor(
      st.session_state.df_pharma,
      num_rows="dynamic",
      use_container_width=True,
      key="ed_pharma",
  )
  edited_pharma["Current Stock"] = (
      edited_pharma["Start Stock"]
      - edited_pharma["Dispensed"]
      - edited_pharma["Expired / Damaged"]
  )
  edited_pharma["Status"] = edited_pharma.apply(
      lambda r: "⚠️ LOW DRUG STOCK"
      if r["Current Stock"] <= r["Safety Threshold"]
      else "✅ OK",
      axis=1,
  )

  p_reorder = edited_pharma[edited_pharma["Status"] == "⚠️ LOW DRUG STOCK"]
  p1, p2, p3 = st.columns(3)
  p1.metric("Active Medications", len(edited_pharma))
  p2.metric("Critical Drug Stockouts", len(p_reorder))
  p3.metric(
      "Expired/Damaged Loss Value",
      f"${(edited_pharma['Expired / Damaged'] * edited_pharma['Unit Price ($)']).sum():,.2f}",
  )

  if not p_reorder.empty:
    st.error("Critical Drug Restock Alerts:")
    st.dataframe(
        p_reorder[[
            "Drug Code",
            "Medication Name",
            "Batch No",
            "Current Stock",
            "Safety Threshold",
            "Status",
        ]],
        use_container_width=True,
    )

# -------------------------------------------------------------------
# TAB 3: KITCHEN & RESTAURANT PREP
# -------------------------------------------------------------------
with tab_kitchen:
  st.subheader("3. Restaurant & Kitchen Prepared Food Ingredient Log")
  if "df_kitchen" not in st.session_state:
    st.session_state.df_kitchen = pd.DataFrame({
        "Ingredient ID": ["ING-01", "ING-02"],
        "Ingredient Name": ["Long Grain Rice", "Fresh Poultry Cuts"],
        "Unit": ["kg", "kg"],
        "Prep Stock": [100.0, 60.0],
        "Added Stock": [50.0, 40.0],
        "Used in Meals": [120.0, 85.0],
        "Kitchen Spoilage": [2.0, 3.0],
        "Min Level": [40.0, 25.0],
        "Cost / Unit ($)": [1.80, 4.50],
    })

  edited_kitchen = st.data_editor(
      st.session_state.df_kitchen,
      num_rows="dynamic",
      use_container_width=True,
      key="ed_kitchen",
  )
  edited_kitchen["Balance"] = (
      edited_kitchen["Prep Stock"]
      + edited_kitchen["Added Stock"]
      - (edited_kitchen["Used in Meals"] + edited_kitchen["Kitchen Spoilage"])
  )
  edited_kitchen["Status"] = edited_kitchen.apply(
      lambda r: "⚠️ REORDER INGREDIENT"
      if r["Balance"] <= r["Min Level"]
      else "✅ ADEQUATE",
      axis=1,
  )

  k1, k2 = st.columns(2)
  k1.metric("Pantry Ingredients Tracked", len(edited_kitchen))
  k2.metric(
      "Kitchen Spoilage Loss",
      f"${(edited_kitchen['Kitchen Spoilage'] * edited_kitchen['Cost / Unit ($)']).sum():,.2f}",
  )
