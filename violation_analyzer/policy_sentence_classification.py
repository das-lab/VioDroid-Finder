import json
import os.path

import joblib

from common.segmentation import seg_by_jieba_for_model
from resources.configuration import rf_tfidf_vectorizer_path, rf_save_dir


class policy_sentence_classification:
    def __init__(self, policy_sentences_path):
        self.tfidf_vectorizer = None
        self.loaded_rf_PC_model = None
        self.loaded_rf_CR_model = {}

        self.pc_cr_mapping = {
            1: [1, 2],
            2: [3, 4],
            3: [5],
            4: [6, 7, 8, 9, 10],
            5: [11, 12, 13, 14, 15, 16, 17],
            6: [18, 19, 20, 21, 22],
            7: [23, 24, 25, 26]
        }

        self.load_rf_models()

        self.policy_sentences = []
        self.policy_sentences_path = policy_sentences_path
        self.get_all_sentences()

        self.classified_sentences = []

    def load_rf_models(self):
        self.tfidf_vectorizer = joblib.load(rf_tfidf_vectorizer_path)
        self.loaded_rf_PC_model = joblib.load(os.path.join(rf_save_dir, 'rf_pc.pkl'))
        for i in range(1, 27):
            self.loaded_rf_CR_model[i] = joblib.load(os.path.join(rf_save_dir, 'rf_cr{}.pkl'.format(i)))

    def get_all_sentences(self):
        with open(self.policy_sentences_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.policy_sentences = data

    def sentence_classification(self):
        for data in self.policy_sentences:
            sentence = data['sentence']
            privacy_category = data['privacy_category']
            prediction = self.predict_sentence(sentence, privacy_category)

            temp = {'sentence': sentence, 'privacy_category': privacy_category, 'prediction': prediction}
            self.classified_sentences.append(temp)

    def predict_sentence(self, sentence, privacy_category):
        seg_texts = [" ".join(seg_by_jieba_for_model(sentence))]
        texts_tfidf = self.tfidf_vectorizer.transform(seg_texts)

        prediction_result_cr = []

        if privacy_category is None:
            privacy_category = self.loaded_rf_PC_model.predict(texts_tfidf)[0][2:]  # 'PC5' -> '5'

        if privacy_category == '0':
            return prediction_result_cr

        for cr in self.pc_cr_mapping[int(privacy_category)]:
            prediction = self.loaded_rf_CR_model[cr].predict(texts_tfidf)[0]
            if prediction == 1:
                prediction_result_cr.append(cr)

        return prediction_result_cr


if __name__ == '__main__':
    psc = policy_sentence_classification(
        os.path.join('../policy_structure_parser/parsed_policies/policy_sentences_chinese.txt'))
    psc.sentence_classification()
