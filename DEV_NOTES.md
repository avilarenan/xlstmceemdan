# Development Notes

This markdown is intended for tracking development issues and bugfixing, as well as new features or releases.

---

- 16/02/2021:

**BugFixing**: 

*cut_spare_imfs* during data preprocessing phase. 

This solved a bug which caused high level imfs from exogenous features to be added up along with the imfs of the target feature. 

This bug was intermitent since the number of imfs may vary for the same decompositions, according to ceemdan's nature. 

The bug fix was done in the two source Python notebooks: *xlstm_ceemdan_full_spline.ipynb* and *xlstm_ceemdan_full.ipynb*

This bug was already being tracked but thanks to **Le Li** to reaching me and telling the bug occurred with him too with many details!

Obs.: all the .ipynb notebooks in *executed_notebooks* folders were not fixed, only the source notebooks from which the experiments are run using *run_batch_exps.py* were fixed.

---

- 18/03/2021:

**Docs**

Added README.md for explicit steps to reproduce experiments.

---