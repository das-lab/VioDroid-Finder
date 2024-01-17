# 600 apps data
+ 600 target apps_metadata.zip: the metadata of 600 target apps (evaluation targets mentioned in the paper)
+ 600 target apps_policies.zip: the privacy policies of 600 target apps (evaluation targets mentioned in the paper)

# An example
+ C100003425-1.3.10.apk: the APK file
+ C100003425-1.3.10.json: the app metadata
  + app_id
  + app_name
  + app_version
  + app_download_num_description
  + app_package_name
  + app_score
  + app_package_size
  + app_package_size_precise
  + app_icon_url
  + app_developer
  + app_update_time
  + app_update_description
  + app_description
  + app_policy_url
  + app_listed_permission
  + app_listed_permission_description
  + app_category
  + app_subcategory
  + app_APK_url
  + app_APK_name
  + app_policy_name
  + policy_html_source_code: html code of privacy policy page
  + policy_text
  + policy_html_source_code_clean: _The html code of the privacy policy page (cleaned to retain only the text body, removing some navigation bars etc.)_
  + policy_text_clean: _The privacy policy text_
  + v1-ambiguous_sentences: _The detection result for v1_
  + v2-sensitive_PI_collection: _The detection result for v2_
  + v3-personalized_display: _The detection result for v3_
  + v4-sharing: _The detection result for v4_
  + v5-cross_border_transmission: _The detection result for v5_
  + v6-completeness: _The detection result for v6_
+ C100003425-1.3.10.txt: the privacy policy
+ C100003425-1.3.10.png: the privacy policy screenshot