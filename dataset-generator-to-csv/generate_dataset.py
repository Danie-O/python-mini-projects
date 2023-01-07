from typing import tuple
import pandas as pd
from numpy import random

""" This script creates a dataset to test a Linear Regression model on based on pre-defined gradient and y-intercept value.
    The gradient and y-intercept use the concept of the equation of a line:
        y = mx1 + m2x2 + c
"""

def generate_data() -> dict:
    x1 = [x * 5 for x in range(100)]
    x2 = random.randint(1, 50, 100)
    
    x: zip[tuple[int, int]] = zip(x1, x2)
    y = [(5.5 * a + 3.8 * b + 15) for a, b in x]    # values for the slopes(5.5, 3.8), and y-intercept(15) can be changed
    return {'x1': x1, 'x2': x2, 'y': y}


def convert_to_dataframe(input_data):
    dataset = pd.DataFrame.from_dict(input_data, orient='columns')
    print("data converted to dataframe")
    return dataset


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = generate_data()
    sample_data = convert_to_dataframe(data)

    file_path = ""  #enter destination file path to store dataset
    sample_data.to_csv(file_path)
