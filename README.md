# QA Learning

This repository is a personal learning project to build a strong foundation in **Python**, **testing fundamentals**, and eventually **test automation with Playwright**.

---

## 🚀 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/marclfleming-me/qa-learning.git
cd qa-learning
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

Activate it:
- **Windows (cmd/PowerShell):**
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers
```bash
python -m playwright install
```

### 5. Run tests

- **All tests:**
  ```bash
  pytest -v
  ```

- **API tests only:**
  ```bash
  pytest -v -m api --html=reports/api-report.html --self-contained-html
  ```

- **Playwright/browser tests only:**
  ```bash
  pytest -v -m browser --html=reports/browser-report.html --self-contained-html
  ```

Reports are saved in the `reports/` folder (ignored by Git).

---

## 📝 Notes
- Never commit `.venv/`, `reports/`, or Playwright browsers – these are ignored via `.gitignore`.
- If dependencies change, update `requirements.txt` with:
  ```bash
  pip freeze > requirements.txt
  ```

---

📖 This repo will grow as I progress from **Python basics** → **QA fundamentals** → **automation with Playwright** → **API testing**.
