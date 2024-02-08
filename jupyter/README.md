# Jupyter Project

Very simple project to demonstrate the use of Jupyter notebooks for data analysis.
This project contains a Jupyter notebook `calc.ipynb` that performs data analysis on the 'Day Ahead Auction' for the month.
The data is sourced from the 'Electricity production and spot prices'.

## Project Structure

The project consists of a single Jupyter notebook `calc.ipynb`.


## Installation

This project uses the following dependencies:

- pandas
- matplotlib
- sklearn

You can install these dependencies using the `requirements.txt` file. Run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the Jupyter notebook, navigate to the project directory and start Jupyter notebook by running the following command:

```bash
jupyter notebook
```

Then, open the `calc.ipynb` file in the Jupyter notebook interface.

## Notebook Overview

The `calc.ipynb` notebook performs the following steps:

1. Imports the necessary libraries.
2. Reads the 'Electricity production and spot prices in the European Union in 2023' dataset from a CSV file.
3. Converts the 'Date (UTC)' column to datetime format.
4. Filters the data for the month of March.
5. Plots the 'Day Ahead Auction' for March.
6. Groups the data by day and calculates the minimum and maximum 'Day Ahead Auction' values for each day.
7. Plots the minimum and maximum 'Day Ahead Auction' values for each day in March.
8. Scales the 'Day Ahead Auction (AT)' values using the `MinMaxScaler` from the `sklearn.preprocessing` module.
9. Adds a new column 'Scaled Day Ahead Auction (AT)' to the DataFrame with the scaled values.
10. Plots the minimum and maximum 'Scaled Day Ahead Auction (AT)' values for each day in March.

## Contributing

Contributions are welcome. Please open an issue to discuss your ideas before making changes.
