import json

from policy_structure_parser import policy_structure_parser

original_policy_path = 'original_policies/original_policy_chinese.txt'  # the policy file to be parsed
parsed_policy_path = 'parsed_policies/parsed_policy_chinese.txt'  # the saving path of the parsed policy
policy_sentences_path = 'parsed_policies/policy_sentences_chinese.txt'  # the saving path of the policy sentences

parser = policy_structure_parser(original_policy_path)

if parser.parse_privacy_policy():
    with open(parsed_policy_path, 'w', encoding='utf-8') as f:
        f.write(parser.formatted_xml_string)
    with open(policy_sentences_path, 'w', encoding='utf-8') as f:
        json.dump(parser.parsed_sentences_with_PC, f, ensure_ascii=False)
else:
    with open(policy_sentences_path, 'w', encoding='utf-8') as f:
        json.dump(parser.parsed_sentences_with_PC, f, ensure_ascii=False)
    print(parser.parse_error_info)
