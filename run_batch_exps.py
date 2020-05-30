import papermill as pm
from datetime import datetime

def run_complete_single():
    pm.execute_notebook(
        './lstm_ceemdan.ipynb',
        f"./executed_notebooks/lstm_ceemdan_{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.ipynb"
    )
    pm.execute_notebook(
        './lstm_ceemdan_spline.ipynb',
        f"./executed_notebooks/lstm_ceemdan_spline_{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.ipynb"
    )
    pm.execute_notebook(
        './xlstm_ceemdan_full.ipynb',
        f"./executed_notebooks/xlstm_ceemdan_full_{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.ipynb"
    )
    pm.execute_notebook(
        './xlstm_ceemdan_full_spline.ipynb',
        f"./executed_notebooks/xlstm_ceemdan_full_spline_{datetime.now().strftime('%H_%M_%S_%m_%d_%Y')}.ipynb"
    )

number_of_experiments = 10

for i in range(number_of_experiments):
    run_complete_single()