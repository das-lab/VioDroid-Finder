# 600 apps data
+ 600 target apps_metadata.zip: the metadata of 600 target apps (evaluation targets mentioned in the paper)
+ 600 target apps_policies.zip: the privacy policies of 600 target apps (evaluation targets mentioned in the paper)

# An example
+ {_app_id_-_app_version_}.apk: the APK file
+ {_app_id_-_app_version_}.json: the app metadata, which includes information that may be useful in future research, including:
  + app_id: _the id assigned to each app by Huawei AppGallery_
  + app_name
  + app_version
  + app_download_num_description: _the description of the number of downloads_
  + app_package_name
  + app_score: _app rating shown in Huawei AppGallery_
  + app_package_size
  + app_package_size_precise
  + app_icon_url
  + app_developer
  + app_update_time: _the last update time of the app (as of the time it is crawled)_
  + app_update_description: _the update description displayed in Huawei AppGallery_
  + app_description: _the app description shown in Huawei AppGallery_
  + app_policy_url: _the privacy policy link of the app_
  + app_listed_permission
  + app_listed_permission_description
  + app_category
  + app_subcategory
  + app_APK_url
  + app_APK_name
  + app_policy_name
  + policy_html_source_code: _html code of privacy policy page_
  + policy_html_source_code_clean: _The html code of the privacy policy page (cleaned to retain only the text body, removing some navigation bars etc.)_
  + v1-ambiguous_sentences: _The detection result for v1_
  + v2-sensitive_PI_collection: _The detection result for v2_
  + v3-personalized_display: _The detection result for v3_
  + v4-sharing: _The detection result for v4_
  + v5-cross_border_transmission: _The detection result for v5_
  + v6-completeness: _The detection result for v6_
+ {_app_id_-_app_version_}.txt: the privacy policy
+ {_app_id_-_app_version_}.png: the privacy policy screenshot