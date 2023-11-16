# VioDroid-Finder

This repository contains data and core code of the paper "VioDroid-Finder: Automated Evaluation of Compliance and
Consistency for Android Apps"

## Regulation wiki

We collect all Chinese regulations related personal privacy in `wiki`.

## Data

Data used in this study contains:

1. Our evaluation targets (discussed in this paper): 600 apps
2. Other apps that are used for creating privacy policy corpus: 40000+ apps

For each app, we provide its privacy policy text, APK file, privacy policy screenshot (of their privacy policy web page)
and their metadata (including app version, app developer, app update time, app download count, privacy policy url,
privacy policy page source code, etc.). We present an example
in `dataset/apps`. Note that the name `C100003425-1.3.10.txt` consists of the app id (C100003425, the corresponding home
page is https://appgallery.huawei.com/app/C100003425) and app
version (1.3.10).

All these data can be downloaded from `https://pan.baidu.com/s/1ulm35u6AOL83VQbaye_o-g?pwd=85f3`

Labelled sentences examples (containing 5000 sentences) are presented in `dataset/dataset.csv`.

## Policy Structure Parser

This module parses privacy policy text to XML file (by running `policy_structure_parser/run.py`).

We present two examples, the Chinese example is as follows: original privacy
policies `policy_structure_parser/original_policies/original_policy_chinese.txt`, and the parsed XML
file `policy_structure_parser/parsed_policies/parsed_policy_chinese.txt`.

## Violation Analyzer

This module mainly implements classification of sentences in privacy
policies (`violation_analyzer/policy_sentence_classification.py`)

## Inconsistency Analyzer

This module analyzes the permission, api and GUI of an APK file, an example is shown
in `inconsistency_analyzer/permission_api_analyzer/permission_api_result`
and `inconsistency_analyzer/gui_analyzer/gui_result`.