# load model and predict
import os.path

import joblib

from common.segmentation import seg_by_jieba_for_model
from resources.configuration import rf_tfidf_vectorizer_path, rf_save_dir

tfidf_vectorizer = joblib.load(rf_tfidf_vectorizer_path)

loaded_rf_PC_model = joblib.load(os.path.join(rf_save_dir, 'rf_pc.pkl'))
texts = ['哈哈']
seg_texts = [" ".join(seg_by_jieba_for_model(text)) for text in texts]

texts_tfidf = tfidf_vectorizer.transform(seg_texts)
predictions = loaded_rf_PC_model.predict(texts_tfidf)
print(predictions)

loaded_rf_CR_model = joblib.load(os.path.join(rf_save_dir, 'rf_cr13.pkl'))
predictions = loaded_rf_CR_model.predict(texts_tfidf)
print(predictions)
