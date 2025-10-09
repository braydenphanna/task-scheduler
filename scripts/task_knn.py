import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('data_set.csv')

data['DUE_DATE'] = pd.to_datetime(data['DUE_DATE'], format='%m/%d/%y %I:%M %p', errors='coerce')
data['CREATION_DATE'] = pd.to_datetime(data['CREATION_DATE'], format='%m/%d/%y %I:%M %p', errors='coerce')

# calculate how many days until each task is due
data['DAYS_UNTIL_DUE'] = (data['DUE_DATE'] - data['CREATION_DATE']).dt.days

# encode task names as numbers
le_task = LabelEncoder()
data['NAME_ENCODED'] = le_task.fit_transform(data['NAME'])

# select features and target
X = data[['NAME_ENCODED', 'PRIORITY', 'DAYS_UNTIL_DUE']]
y = data['COMPLETED'].astype(int)  # 0 = not completed, 1 = completed

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create and train the knn model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# check accuracy
accuracy = knn.score(X_test, y_test)
print(f"prediction accuracy: {accuracy:.2f}")

print("\nsummary of high-priority tasks:")
for task in data['NAME'].unique():
    subset = data[(data['NAME'] == task) & (data['PRIORITY'] >= 4)] # change to pick prio levels
    if not subset.empty:
        X_subset = subset[['NAME_ENCODED', 'PRIORITY', 'DAYS_UNTIL_DUE']]
        y_prob = knn.predict_proba(X_subset)[:, 1]  # probability completed
        avg_prob = y_prob.mean()
        print(f"{task} | max priority: {subset['PRIORITY'].max()} | avg probability completed: {avg_prob:.2f}")

        # warning if completion probability is low
        if avg_prob < 0.75:
            print(f"  -> WARNING: this task may not get done on time")

# need to fix output to be cleaner