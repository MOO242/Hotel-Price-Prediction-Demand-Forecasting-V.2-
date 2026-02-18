import os
import sys

import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]

            print(f"--- Training {model_name} (Default Params) ---")

            # Train the model directly
            model.fit(X_train, y_train)

            # Evaluate performance
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

            print(f"Model: {model_name}, R2 Score: {test_model_score:.4f}")

        return report

    except Exception as e:
        raise CustomException(e, sys)
