INSURANCE COST PREDICTOR - Run Instructions
=============================================

Folder structure:
  insurance_app/
    app.py              -> Flask backend
    model.pkl           -> Trained LinearRegression model (age, bmi, children, smoker)
    requirements.txt    -> Python dependencies
    templates/
      index.html         -> Dark terminal-style frontend

How to run (local computer / laptop):

1. Terminal/CMD kholo aur is folder me jao:
     cd insurance_app

2. (Optional but recommended) Virtual environment banao:
     python -m venv venv
     venv\Scripts\activate      (Windows)
     source venv/bin/activate   (Mac/Linux)

3. Requirements install karo:
     pip install -r requirements.txt

4. App run karo:
     python app.py

5. Browser me kholo:
     http://127.0.0.1:5000

Model details:
  - Features (exact same order as your notebook): age, bmi, children, smoker_code
  - smoker_code: yes -> 1, no -> 0
  - Trained on your medical.csv (1338 records), plain LinearRegression, no scaling
  - Training RMSE: ~6056

Notes:
  - Agar "python" command na chale to "python3" try karo.
  - Port 5000 already use ho raha ho to app.py ke last line me port=5000 ko
    kisi aur number (e.g. 5001) se badal dena.
