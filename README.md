## graphing-demo

This is a very high level overview of some of the most popular python graphing libraries. As an exercise, I attempted to produce the same chart using Matplotlib, Seaborn, Plotly, and Bokeh and report on ease of use, aesthetics, applications, etc.

This was put together for the Boston Python Data Science Study group in Jan. 2022. The accompanying slide deck can be found [here](https://docs.google.com/presentation/d/1zjz4TTVolt_jww-uJD15RS1tRXCE56KT_JCbOfrgn4w/edit?usp=sharing).

## Running the Demos

1. First, create a virtual environment using `python -m venv venv`.
2. Activate the virtual environment with `source venv/bin/activate` (on Unix) or `./venv/scripts/activate.bat` (on Windows)
3. Install the requirements with `pip install -r requirements.txt`.
   - You may have to install these dependencies manually using `pip install <package>`:
     - `attrdict3`
     - `requests`
4. Run each demo from the command line, e.g. `python matplotlib_demo.py`

## Troubleshooting Install

- On some (all?) OSX computers, `wxPython` fails to install with a message like "C compiler cannot create executables". A workaround for this is to use a different graphics backend for `matplotlib`. To do this, manually install PyQt5 (`pip install PyQt5`), and in `matplotlib_demo.py`, see the comment about switching `WxAgg` for `PyQt5`.

## Data

The data was sourced from [Kaggle](https://www.kaggle.com/shadowtime2000/dungeons-dragons?select=monsters.csv) and mostly processed with pandas.
