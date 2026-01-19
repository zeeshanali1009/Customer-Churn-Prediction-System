FROM python:3.10

WORKDIR /app

# Upgrade tooling
RUN pip install --upgrade pip setuptools wheel

# Install streamlit WITHOUT heavy deps (no pyarrow)
RUN pip install streamlit --no-deps

# Copy and install only required ML libs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
