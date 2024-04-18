# Getting Started

1. Create a virtual env
```bash
python3 -m venv venv
```

2. Activate virtual environment
```bash 
source ./venv/bin/activate
```

3. Pip install
```bash
pip install -r requirements.txt
```

4. Run Web API
```bash
python3 -m uvicorn main:app --reload
```