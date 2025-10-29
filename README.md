# Project Samarth — Demo (Samarth Insight)

This is a **small, ready-to-run demo** of Project Samarth focused on **Gujarat** and **Rice** using Python + Streamlit.
The dataset files included are small sample CSVs for demonstration only (not full government datasets).

## What's included
- app.py : Streamlit demo app
- crop_data.csv : sample crop production data (Gujarat, Maharashtra)
- rainfall_data.csv : sample rainfall data (Gujarat, Maharashtra)
- requirements.txt : Python packages needed

## How to run (locally)
1. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the URL displayed (usually http://localhost:8501)

## Demo actions to try
- Use the sidebar quick actions and click **Run selected demo**
- Or type queries like:
  - `compare rainfall Gujarat Maharashtra`
  - `show rice trend in Gujarat`
  - `top crops in Gujarat`

## Next steps to make it production-ready
- Replace sample CSVs with real data.gov.in datasets (IMD & Ministry of Agriculture)
- Add robust NLP (OpenAI or HuggingFace) to parse complex questions
- Add mapping between different state/district codes and normalize datasets
- Implement source-level citations per output row for traceability

