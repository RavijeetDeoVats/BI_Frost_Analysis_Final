1. Clone this repository in your Sytem
2. Open VS Code and to set up vitual Environment following below steps


python -m ensurepip --upgrade
python -m venv venv
        venv\Scripts\activate  -- windows
        source venv/bin/activate  -- Linux

(install the pacakages in the given sequence)
pip install streamlit==1.40.2
pip install astropy==6.0.1
pip install numpy==1.26.4
pip install matplotlib==3.9.3

pip freeze > requirements.txt

set STREAMLIT_SERVER_MAX_UPLOAD_SIZE=1000 -- Windows
export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=1000 --Linux

streamlit run <path_to_file>/<file_name>.py