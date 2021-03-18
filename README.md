# X-CEEMDAN-LSTM model

## Abstract

The most recent successful time series prediction models are a combination of three elements: traditional stochastic models, machine learning models and signal processing techniques. CEEMDAN-LSTM models have combined empirical mode decomposition and long short-term memory neural networks to achieve state-of-the-art results for financial data. In this work, we propose a generalized CEEMDAN-LSTM architecture for time series forecasting capable of dealing with exogenous features as input, and the consequences of input data growth, such as convergence difficulties. Our model was applied to time series from 10 of the most liquid Brazilian stocks, and results show that accuracy is overall improved when compared to the original single feature input CEEMDAN-LSTM architecture.

## Link to paper

The article was published in Springer's [Lecture Notes in Computer Science](https://link.springer.com/chapter/10.1007/978-3-030-61380-8_38).

## Steps to reproduce experiments in Table 2 (Comparison results)

1) Set all your desired hyperparameters for a given batch of experiments in files *xlstm_ceemdan_full_spline.ipynb, lstm_ceemdan.ipynb, lstm_ceemdan_spline.ipynb , xlstm_ceemdan_full.ipynb*.
> Warning: Also set the output folder at the last cell of each of these files (the default one is *exp_records* folder).

2) Set the number of experiments in a batch and Run *run_batch_exps.py*. Then the results of a batch will be put in your desired folder (the default one is *exp_records*) in csv format.

3) Run the notebook *avg_metrics.ipynb*, which will summarize average metrics in a csv, output goes to folder *summary_results*.

4) Repeat steps 1 to 3 with different hyperparameters, for example changing the IMF number for threshold, changing data or even changing learning rate, noise scale and so on.

> Warning: in order to create new batches it is recommended to manually change the destination folder at the end of each of the above cited files.

## Steps to reproduce Figure 6 (MAPE Vs IMF threshold)

1) Set all your desired hyperparameters in file *xlstm_ceemdan_full_spline_imfs.ipynb* and run all its cells once.

2) Change IMF threshold and reproduce step 1.

> Change threshold in the following line: 
```python
imfs_to_predict_with_neural = [] # set to ['IMF1'] , ['IMF1', 'IMF2], ['IMF1','IMF2','IMF3'] and so on
```

3) Run file *imf_threshold_metrics.ipynb*. The output will be a csv file in folder *imfs_exp_records*.

> The graph will be generated in the *imf_threshold_metrics.ipynb* when ran.

## Steps to reproduce Table 3 (Average relative improvement compared to vanilla CEEMDAN-LSTM)

1) Reproduce steps to generate Table 2.

2) In *avg_metrics.ipynb* last notebook cell a Table is generated for a given IMF threshold:

<img src="https://github.com/avilarenan/xlstmceemdan/blob/master/doc_images/table3_partial_imfthreshold.png" width="300">

1) Reproduce steps to generate Table 2 with different IMF threshold number.

2) Run avg_metrics again for the new batch and generate another table as in step 2.

3) Manually merge the two tables to compare relative improvements for each of the IMF threshold values as in the paper.

## Citation

Cite this paper as:

de Luca Avila R., De Bona G. (2020) Financial Time Series Forecasting via CEEMDAN-LSTM with Exogenous Features. In: Cerri R., Prati R.C. (eds) Intelligent Systems. BRACIS 2020. Lecture Notes in Computer Science, vol 12320. Springer, Cham. https://doi.org/10.1007/978-3-030-61380-8_38

## Contact

Please, feel free to reach me at: <renan.avila@usp.br>!

Or you can even send me a message at my linkedin <https://www.linkedin.com/in/delucarenan>.

## Acknowledgement

Thanks to Escola Politécnica da Universidade de São Paulo, and thanks to BTG Pactual for supporting the work.

<p float="left">
    <img src="https://github.com/avilarenan/xlstmceemdan/blob/master/doc_images/Logo-Escola-Polit%C3%A9cnica-Minerva_Logo-Escola-Polit%C3%A9cnica-Minerva-01-scaled.jpeg" width="110">
    <img src="https://github.com/avilarenan/xlstmceemdan/blob/master/doc_images/1200px-Btg-logo-blue.svg.png" width="230">
</p>