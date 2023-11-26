# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit main file into the container
COPY Skin_Disease_Predictor.py .

COPY style.py .
COPY EfficientNetB2-Skin-87.h5 .
COPY pages/02AI_Chatbot.py .
COPY pages/03Youtube_Searcher.py .
COPY pages/04Generate_pdf_report.py .
COPY pages/05About.py .
COPY . /app/
COPY .streamlit .
# Expose the port that Streamlit runs on
EXPOSE 8501

# Set the command to run Streamlit when the container starts
CMD ["streamlit", "run", "Skin_Disease_Predictor.py"]
