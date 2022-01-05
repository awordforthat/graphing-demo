## graphing-demo

This is a very high level overview of some of the most popular python graphing libraries. As an exercise, I attempted to produce the same chart using Matplotlib, Seaborn, Plotly, and Bokeh and report on ease of use, aesthetics, applications, etc.

This was put together for the Boston Python Data Science Study group in Jan. 2022. The accompanying slide deck can be found [here](https://docs.google.com/presentation/d/1zjz4TTVolt_jww-uJD15RS1tRXCE56KT_JCbOfrgn4w/edit?usp=sharing).

## Running the Demos

1. First, create a virtual environment using `python -m venv venv`.
2. Activate the virtual environment with `source venv/bin/activate` (on Unix) or `source venv/scripts/activate` (on Windows)
3. Install the requirements with `pip install -r requirements.txt`.
4. Run each demo from the command line, e.g. `python matplotlib_demo.py`

## Data

The data was sourced from [Kaggle](https://www.kaggle.com/shadowtime2000/dungeons-dragons?select=monsters.csv) and mostly processed with pandas.
