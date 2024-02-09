FROM python:3.8
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "Python_Pandas _project_07.py"]
