# VioDroid-Finder

This repository contains data and core code of the paper "VioDroid-Finder: Automated Evaluation of Compliance and
Consistency for Android Apps"

## Regulation wiki

We provide collected Chinese regulations related to personal privacy in `wiki`.

## Data

Data used in this study contains:

1. Our evaluation targets (discussed in this paper): 600 apps
2. Other apps that are used for creating privacy policy corpus: 40000+ apps
3. Chinese privacy policy corpus (300+ MB) and a word2vec model trained on
   corpus: [Google Drive](https://drive.google.com/drive/folders/1xMO7TEQkpsT_yQCKwX55sFsd_gYl6gQ7)

For each app, we provide its privacy policy text, APK file, privacy policy screenshot (of their privacy policy web page)
and their metadata (including app version, app developer, app update time, app download count, privacy policy url,
privacy policy page source code, etc.).

The privacy policies and metadata of 600 target apps are in `dataset/apps`.

We also present an example in `dataset/apps` [click here](https://github.com/das-lab/VioDroid-Finder/tree/main/dataset/apps):

+ Note that the app data file name `C100003425-1.3.10.txt` consists of the app id (C100003425, the corresponding home
  page is https://appgallery.huawei.com/app/C100003425) and app
  version (1.3.10).

The complete data can be downloaded from [Baidu NetDisk](https://pan.baidu.com/s/1ulm35u6AOL83VQbaye_o-g?pwd=85f3)

Labelled sentences examples (containing 5000+ sentences) are presented in `dataset/dataset.csv`.

## Policy Structure Parser

This module parses privacy policy text to XML file (by running `policy_structure_parser/run.py`).

We present two examples, the Chinese example is as follows:

+ Original privacy policies `policy_structure_parser/original_policies/original_policy_chinese.txt`
+ The parsed XML file `policy_structure_parser/parsed_policies/parsed_policy_chinese.txt`.

## Violation Analyzer

This module mainly implements classification of sentences in privacy
policies (`violation_analyzer/policy_sentence_classification.py`)

## Inconsistency Analyzer

This module analyzes the permission, api and GUI of an APK file, an example is shown
in `inconsistency_analyzer/permission_api_analyzer/permission_api_result`
and `inconsistency_analyzer/gui_analyzer/gui_result`.

+ Modify the target APK file path of `inconsistency_analyzer/permission_api_analyzer/run.py` and run, to analyze the Permission and API of the APK

+ Modify the target APK file path of `inconsistency_analyzer/gui_analyzer/run.py` and run, to analyze the GUI of the APK