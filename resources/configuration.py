import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))

# policy_structure_parser configurations
paragraph_number_regex_path = os.path.join(current_file_dir,
                                           "policy_structure_parser_resources/paragraph_number_regex.csv")
paragraph_numbers_path = os.path.join(current_file_dir, "policy_structure_parser_resources/paragraph_numbers.txt")

# word2vec configurations
w2v_model_path = os.path.join(current_file_dir, "../common/word2vec/model/w2v.model")
w2v_vector_path = os.path.join(current_file_dir, "../common/word2vec/model/wv.vector")

# the saving path of PI.txt
PI_path = os.path.join(current_file_dir, "personal_information.txt")

# the saving path of stopwords.txt
stopwords_path = os.path.join(current_file_dir, "stopwords.txt")

# the saving path of ui_regex (for extracting pi in gui text)
ui_regex_path = os.path.join(current_file_dir, "ui_regex.txt")

# the benchmark subtitles
benchmark_subtitles = {1: ['适用范围'],
                       2: ['联系', '开发者信息', '运营者基本信息'],
                       3: ['未成年人信息保护', '处理未成年人信息', '处理儿童信息', '未成年人条款', '未成年人保护', '青少年条款'],
                       4: ['管理信息', '权利', '访问信息', '查阅和修订', '更新和通知', '访问和控制信息', '自主管理', '信息访问及管理', '政策更新', '修订'],
                       5: ['收集信息', '使用信息', '收集和使用信息', '信息存储', '存储期限', '保存及保护信息', '信息安全', '保护信息安全', '提供的信息', '信息范围',
                           '信息安全事件处置', '个人敏感信息提示', '保护信息', '信息采集和使用'],
                       6: ['使用第三方SDK', '分享信息', '共享信息', '对外提供', '信息披露', '共享、转让、公开披露信息', '数据使用过程中涉及合作方以及转移、公开信息',
                           '与第三方共享、对外提供信息', '可能从第三方间接获取信息', '合作伙伴与SDK', '第三方数据处理及信息的公开披露', '第三方服务', '合作场景'],
                       7: ['信息在全球范围转移', '信息存储地域', '保存地域', '信息存储和交换', '信息保存及跨境传输']}

# the similarity threshold for subtitle similarity calculation
subtitle_word_frequency_similarity_threshold = 0.9
subtitle_semantic_similarity_threshold = 0.95

# gui analyzer configurations
apktool_path = os.path.join(current_file_dir, "apktool_2.7.0.jar")
apk_decompile_save_dir = os.path.join(current_file_dir, "../inconsistency_analyzer/gui_analyzer/tmp")
gui_result_save_dir = os.path.join(current_file_dir, "../inconsistency_analyzer/gui_analyzer/gui_result")

# permission and api analyzer configurations
permission_path = os.path.join(current_file_dir, "permissions.txt")
api_path = os.path.join(current_file_dir, "apis.txt")
permission_api_result_save_dir = os.path.join(current_file_dir,
                                              "../inconsistency_analyzer/permission_api_analyzer/permission_api_result")

# model training
dataset_dir = os.path.join(current_file_dir, "../dataset/")
bert_trained_model_dir = os.path.join(current_file_dir, "../violation_analyzer/model_training/bert/trained_models")
rf_save_dir = os.path.join(current_file_dir, "../violation_analyzer/model_training/random_forest/trained_models")
rf_tfidf_vectorizer_path = os.path.join(rf_save_dir, 'tfidf_vectorizer.pkl')

if __name__ == '__main__':
    print(apk_decompile_save_dir)
