import os.path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

from common.segmentation import seg_by_jieba_for_model
from resources.configuration import dataset_dir, rf_save_dir, rf_tfidf_vectorizer_path

df = pd.read_csv(os.path.join(dataset_dir, 'pc/pc.csv'), delimiter='\t')

X = df['sentence']
y = df['pc']

# segmentation
X_seg = [" ".join(seg_by_jieba_for_model(text)) for text in X]

# tf-idf
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_tfidf = tfidf_vectorizer.fit_transform(X_seg)

# dataset split
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# model creation
rf_classifier = RandomForestClassifier()

# model training
rf_classifier.fit(X_train, y_train)

# model evaluation
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("acc:", accuracy)
print("report:\n", classification_rep)

# save model
save_path = os.path.join(rf_save_dir, 'rf_pc.pkl')
joblib.dump(rf_classifier, save_path)
joblib.dump(tfidf_vectorizer, rf_tfidf_vectorizer_path)