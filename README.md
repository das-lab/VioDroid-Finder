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

We also present an example
in `dataset/apps` [click here](https://github.com/das-lab/VioDroid-Finder/tree/main/dataset/apps):

+ Note that the app data file name `C100003425-1.3.10.txt` consists of the app id (C100003425, the corresponding home
  page is https://appgallery.huawei.com/app/C100003425) and app
  version (1.3.10).

The complete data can be downloaded from [Baidu NetDisk](https://pan.baidu.com/s/1ulm35u6AOL83VQbaye_o-g?pwd=85f3)

Labelled sentences examples (containing 5000 sentences) are presented in `dataset/dataset.csv`. Examples of annotation is shown below:

| Compliance rule                                                                      |                                          Annotation scheme |                                                                    Example                                                                     |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|
| CR1 Inform when the privacy policy is updated/effective                              |                                                          - |                                                             更新日期：【2022】年【12】月【9】日                                                              |
| CR2 Inform what products/services the privacy policy applies to                      |                                                          - |                                                               本政策适用于"智慧双安""产品及服务                                                               |
| CR3 Inform the identity of the PI controller                                         |             Specify the company name or registered address |                                                               运营者公司名称：山东喵物科技有限公司                                                               |
| CR4 Inform how to contact the PI controller                                          |                                                          - |                                                              运营者客服热线：18660909762                                                               |
| CR5 Obtain consent from the guardian when collecting PI of minors under 14 years old |                                                          - |                                               若您是18周岁以下的未成年人，在使用我们的产品与/或服务前，应事先取得您家长或法定监护人的书面同意                                                |
| CR6 Obtain consent to the privacy policy before collecting PI                        |                                                          - |                                                       请在向vivo提交个人信息前，阅读、了解和同意《vivo隐私政策》                                                        |
| CR7 Provide a notice for major changes of the privacy policy                         |                                                          - |                                我们会通过在喵物商城小程序、喵物商城移动端上发出更新版本并在生效前通过网站公告或以其他适当方式提醒您相关内容的更新，也请您访问喵物商城以便及时了解最新的隐私政策                                |
| CR8 Inform how to withdraw consent                                                   |                                                          - |                                           a)你可以在设备的设置功能中开启或关闭地理位置、通讯录、摄像头、麦克风、相册、日历等权限，改变授权范围或撤回你的授权                                           |
| CR9 (Conditional) Inform how to disable the personalized display                     |                                                          - |                                     您可以在微博设置中自主控制个性化内容推荐服务的开启和关闭（路径：微博-我-设置-隐私设置-个性化内容推荐），不会影响您正常使用微博的其他功能                                     |
| CR10 Inform other rights of PI subjects like deletion, deregistration, etc           |                                                          - |                                                  你可以在【我】-【≡】-【我的订单】-【地址】中添加、删除、更改、查看你的收货地址信息                                                   |
| CR11 Inform the purpose of the collection                                            | Specify a specific purpose, not just "providing a service" |                                                                  1、帮助您完成注册及登录                                                                  |
| CR12 (Optional) Inform the personalized display service provided by the app          |                                                          - |                       我们可能会将上述信息与来自我们其他服务的信息结合，进行综合统计并通过算法做特征与偏好分析，用以向你进行个性化推荐、展示或推送你可能感兴趣的特定音视频和图片等信息，或者推送更合适你的特定功能或服务：                       |
| CR13 Inform what PI the app collects                                                 |                                                          - |                                                       当您选择通过邮箱注册360账号时，您需要提供邮箱地址和设置账号密码                                                        |
| CR14 Inform the retention period of PI                                               |                                                          - |                                                      我们仅在本政策所属目的的所必须期间和法律法规要求的时限内存储您的个人信息                                                      |
| CR15 Inform the PI protection measures                                               |                                                          - |                                                我们使用的技术手段包括但不限于防火墙、加密（例如SSL）、去标识化或匿名化处理、访问控制措施等。                                                |
| CR16 (Conditional) Inform the collection of sensitive PI                             |                                                          - |                                                  其中有关个人敏感信息以及与您个人信息权益相关的重要内容我们已用加粗形式提示，请特别关注。                                                  |
| CR17 Notify in time when the PI security incidents happen                            |                                                          - |                                     安全事件发生后，我们会及时以推送通知、邮件等形式告知您安全事件的基本情况、我们即将或已经采取的处置措施和补救措施，以及我们对您的应对建议。                                      |
| CR18 (Optional) Inform third party sharing of PI                                     |                                                          - |                                                      我们仅会出于合法、正当、必要、特定、明确的目的向第三方提供您的个人信息                                                       |
| CR19 (Conditional) Obtain consent when sharing PI                                    |                                                          - |                                                     经过您的明示同意，我们会将上述信息与第三方共享，以便第三方能及时向您提供服务                                                     |
| CR20 (Conditional) Inform information about third parties                            |                                                          - | （5）征信机构：若您授权征信机构（如百行征信、朴道征信）向我们查询、采集您的信息，我们会在法律法规及监管政策允许范围内及您对征信机构的授权范围内向征信机构共享您的信息，我们会依据与征信机构的约定、对授权的个人信息来源的合法性进行确认，在符合法律法规及监管政策的前提下，处理您的个人信息 |
| CR21 (Conditional) Inform the purpose of sharing                                     |                                                          - |                                            例如，在您上网购买我们的产品时，我们必须与物流服务提供商共享您的个人信息才能安排送货，或者安排合作伙伴提供服务                                             |
| CR22 (Conditional) Inform what PI the app shares                                     |                                                          - |                                当您使用车主权益服务时，基于服务需要可能需要您提供手机号信息，经您授权同意，我们会根据您的授权将您的信息提供给该第三方，以便您后续使用第三方为您提供的相关权益                                 |
| CR23 (Optional) Inform the cross-border transmission                                 |                                                          - |                           《我苏》收集的有关您的信息和资料将保存在《我苏》及（或）其关联公司的服务器上，这些信息和资料可能传送至您所在国家、地区或《我苏》收集信息和资料所在地的境外并在境外被访问、存储和展示                           |
| CR24 (Conditional) Obtain consent if cross-border transmission needed                |                                                          - |                                                             如需跨境传输，我们将会单独征得您的授权同意                                                              |
| CR25 (Conditional) Inform the purpose of cross-border transmission                   |                                                          - |                                                 我们的部分功能使用了境外供应商的服务，如您使用该部分功能，您的部分个人信息可能被传输至境外。                                                 |
| CR26 (Conditional) Inform the protection measures for cross-border transmission      |                                                          - |              在这类情况下，vivo将采取措施，确保有法律基础可进行这类传输，以及依适用法律，会对您个人信息提供适当的保护，例如：完成数据出境安全评估、通过使用相关授权单位核准的标准合约 (必要时)，以及通过使用其他适当的技术与组织信息安全措施等              |

## Policy Structure Parser

This module parses privacy policy text to XML file (by running `policy_structure_parser/run.py`).

We present two examples, the Chinese example is as follows:

+ Original privacy policies `policy_structure_parser/original_policies/original_policy_chinese.txt`
+ The parsed XML file `policy_structure_parser/parsed_policies/parsed_policy_chinese.txt`.

## Violation Analyzer

This module mainly implements classification of sentences in privacy
policies (`violation_analyzer/policy_sentence_classification.py`)

The code for classification model training are in `violation_analyzer/model_training`

## Inconsistency Analyzer

This module analyzes the permission, api and GUI of an APK file, an example is shown
in `inconsistency_analyzer/permission_api_analyzer/permission_api_result`
and `inconsistency_analyzer/gui_analyzer/gui_result`.

+ Modify the target APK file path of `inconsistency_analyzer/permission_api_analyzer/run.py` and run, to analyze the
  Permission and API of the APK

+ Modify the target APK file path of `inconsistency_analyzer/gui_analyzer/run.py` and run, to analyze the GUI of the APK