FROM continuumio/miniconda3

WORKDIR /home/app

RUN apt-get update && apt-get install -y nano unzip && apt-get -f install

RUN apt install -y curl

# RUN pip install boto3 
RUN pip install numpy pandas 
RUN pip install pillow streamlit_extras 
RUN pip install gunicorn streamlit 
RUN pip install scikit-learn==1.3.0
RUN pip install plotly
RUN pip install seaborn matplotlib
COPY . /home/app
#COPY logo.jpg /opt/conda/lib/python3.10/site-packages/st_clickable_images/frontend/build/logo.jpg
#Run pip install joblib
#Run pip install cloudpickle==1.2.2 dill==0.3.0

#RUN conda install -c conda-forge scikit-surprise 
#RUN pip install Cython requests st_clickable_images streamlit_option_menu pillow

CMD streamlit run --server.port $PORT Mammals.py