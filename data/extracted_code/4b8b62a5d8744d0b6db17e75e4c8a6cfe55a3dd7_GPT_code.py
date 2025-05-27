import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import pearsonr

def extract_features(data, window_length=0.2, window_slide=0.01, sampling_rate=1200):
    features = []
    labels = []
    window_size = int(window_length * sampling_rate)
    step_size = int(window_slide * sampling_rate)


    for start in range(0, len(data) - window_size + 1, step_size):
        end = start + window_size - 1
        window = data.iloc[start:end, 1:17].values
        label = data.iloc[end, 0]

        rms = np.sqrt(np.mean(window**2, axis=0))
        zc = np.sum(np.diff(np.sign(window), axis=0) != 0, axis=0)
        wl = np.sum(np.abs(np.diff(window, axis=0)), axis=0)

        features.append(np.hstack((rms, zc, wl)))
        labels.append(label)

    return np.array(features), np.array(labels)

def calculate_nmse(x_r, x_p):
    numerator = np.linalg.norm(x_r - x_p) ** 2
    denominator = np.linalg.norm(x_r - np.mean(x_r)) ** 2
    nmse = 100 * (1 - (numerator / denominator))
    return nmse

def load_data(batches):
    data = []
    for batch in batches:
        files = sorted([file for file in os.listdir(batch) if file.endswith('.csv')])
        for file in files:
            batch_data = pd.read_csv(os.path.join(batch, file), header=0)
            data.append(batch_data)
    return data

def main():
    batches = ['Data/Batch1', 'Data/Batch2', 'Data/Batch3']
    data_files = load_data(batches)

    nmse_values = []
    corr_values = []

    for i in range(10):  # Assuming there are 10 folds (i.e., 10 data files for each motion)
        train_data = [data for idx, data in enumerate(data_files) if ((idx != i) and (idx != (i+10)) and (idx != (i+20)))]
        test_data = [data for idx, data in enumerate(data_files) if ((idx == i) or (idx == (i+10)) or (idx == (i+20)))]

        train_features = np.vstack([extract_features(data)[0] for data in train_data])
        train_labels = np.concatenate([extract_features(data)[1] for data in train_data])

        test_features = np.vstack([extract_features(data)[0] for data in test_data])
        test_labels = np.concatenate([extract_features(data)[1] for data in test_data])

        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(train_features, train_labels)

        predictions = model.predict(test_features)

        nmse = calculate_nmse(test_labels, predictions)
        corr = pearsonr(test_labels, predictions)[0] * 100  # Correlation in percentage

        nmse_values.append(nmse)
        corr_values.append(corr)

        print(f"Fold {i + 1}: Correlation = {corr:.2f}%, NMSE = {nmse:.2f}%")

    print("\nAll Folds NMSE Values: ", nmse_values)
    print("All Folds Correlation Values: ", corr_values)

    print(f"\nMean Correlation: {np.mean(corr_values):.2f}%")
    print(f"Mean NMSE: {np.mean(nmse_values):.2f}%")

if __name__ == "__main__":
    main()