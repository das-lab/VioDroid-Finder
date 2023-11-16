import os
import json

from androguard.misc import AnalyzeAPK
import hashlib
import codecs

from resources.configuration import api_path, permission_path, permission_api_result_save_dir


def read_api_config(path):
    """
    Read api (related to PI) from configuration file
    """
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    node = {}
    configs = []
    for line in lines:
        if len(line) < 3:
            if node:
                configs.append(node)
                node = {}
            continue
        tmp = line.split('\n')[0].split(': ')
        node[tmp[0]] = tmp[1]
    if node != {}:
        configs.append(node)
    return configs


def read_permission_config(path):
    """
    Read permission (related to PI) from configuration file
    """
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    node = {}
    configs = []
    for line in lines:
        if len(line) < 3:
            if node:
                configs.append(node)
                node = {}
            continue
        tmp = line.split('\n')[0].split(': ')
        node[tmp[0]] = tmp[1]
    if node != {}:
        configs.append(node)
    return configs


api_config = read_api_config(api_path)
permission_config = read_permission_config(permission_path)


def analyze_basic_info(apk_file, a):
    """
    @:param apk_file: apk file path
    @:param a: an APK instance
    @:return : a list of dictionaries of strings lists [ { "application_information": [ ("application_name", ["com.test"]), ("application_version", ["1.0"]) ] }, { ... }]
    """

    def get_application_package_name(apk):
        """
        @:param apk : an APK instance
        @:return : the package name
        """
        return apk.get_package()

    def get_application_name(apk):
        """
        @:param apk : an APK instance
        @:return : the application common name
        """
        return apk.get_app_name()

    def get_android_version_name(apk):
        """
        @:param apk : an APK instance
        @:return : the android version name
        """
        return apk.get_androidversion_name()

    def get_filename(apk):
        """
        @:param apk : an APK instance
        @:return : the APK's filename
        """
        return os.path.basename(apk.get_filename())

    def get_apk_file_hashes(apk_file):
        """
        @:param apk_file : apk file path (not an apk instance)
        @:return : a list of several hexified hashes
        """
        results = []

        block_size = 2 ** 20

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        with open(apk_file, 'rb') as f:
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
                sha256.update(data)

        f.close()

        results.append("MD5: %s" % md5.hexdigest())
        results.append("SHA-1: %s" % sha1.hexdigest())
        results.append("SHA-256: %s" % sha256.hexdigest())

        return results

    def get_certificate_information(apk):
        """
        @:param apk : an APK instance
        @:return : a certificate object by giving the name in the apk file
        """
        cert_info = ["APK is signed: %s\n" % apk.is_signed()]

        for index, cert in enumerate(apk.get_certificates()):
            cert_info.append("Certificate #%s" % index)
            cert_info_issuer = ["Issuer:", cert.issuer.human_friendly]
            cert_info_subject = ["Subject:", cert.subject.human_friendly]

            cert_info.extend(cert_info_issuer)
            cert_info.extend(cert_info_subject)

            cert_info.append("Serial number: %s" % cert.serial_number)
            cert_info.append("Hash algorithm: %s" % cert.hash_algo)
            cert_info.append("Signature algorithm: %s" % cert.signature_algo)
            cert_info.append("SHA-1 thumbprint: %s" % codecs.encode(cert.sha1, 'hex').decode())
            cert_info.append("SHA-256 thumbprint: %s" % codecs.encode(cert.sha256, 'hex').decode())
            cert_info.append("")

        return cert_info

    def get_main_activity(apk):
        """
        @:param apk : an APK instance
        @:return : the name of the main activity
        """
        return apk.get_main_activity()

    def get_sdk_versions(apk):
        result = ["Declared target SDK: %s" % apk.get_target_sdk_version(),
                  "Effective target SDK: %s" % apk.get_effective_target_sdk_version(),
                  "Min SDK: %s" % apk.get_min_sdk_version(),
                  "Max SDK: %s" % apk.get_max_sdk_version()]
        return result

    data = {}
    data['application_information'] = {
        'application_name': get_application_name(a),
        'application_version': get_android_version_name(a),
        'package_name': get_application_package_name(a)
    }
    data['apk_file'] = {
        'file_name': get_filename(a),
        'fingerprint': get_apk_file_hashes(apk_file),
        'certificate_information': get_certificate_information(a)
    }
    data['androidmanifest.xml'] = {
        'main_activity': get_main_activity(a),
        'sdk_versions': get_sdk_versions(a),
    }

    return data


def find_in_manifest(permission_list):
    """
    Scan all permission_list (which is obtained from the apk manifest), and check whether permission is in permission_config.
    """

    for i in range(len(permission_list)):
        if '.' in permission_list[i]:
            permission_list[i] = permission_list[i].split('.')[-1]

    res = []
    for aConfig in permission_config:
        if aConfig['permission'] in permission_list:
            res.append(aConfig)

    return res


def find_in_code(class_list, api_config):
    """
    scan all classes and methods in the apk, and map them to PI
    """
    res = []

    for classItem in class_list:
        className = classItem.name
        className = className.replace('/', '.')
        className = className.replace('$', '.')

        methods = classItem.get_methods()

        for methodItem in methods:
            for config in api_config:
                if config['class'] in className and (methodItem.name == config['method'] or config['method'] == '*'):
                    if config['method'] == '*':
                        temp = json.loads(json.dumps(config))
                        temp['method'] = methodItem.name
                    else:
                        temp = config
                    res.append(temp)

    return res


def main(apk_path, result_file_path=None):
    """
    Use androguard to analyze the permission and api for an apk file
    :param apk_path: target apk file path
    :return: result
    """
    ans = {}

    try:
        a, d, dx = AnalyzeAPK(apk_path)
    except Exception as e:
        print('{}-Fail to analyze apk-{}'.format(apk_path, e))
        return None

    # Get all classes
    class_list = dx.get_classes()

    # Get permissions names declared in the AndroidManifest.xml
    permission_list = a.get_permissions()

    # Get apk basic information
    try:
        base_info_res = analyze_basic_info(apk_path, a)
        ans['base_info_res'] = base_info_res
    except Exception as e:
        print('Failed to obtain apk basic information-{}'.format(e))

    # Parse apis called to PI
    api_res = find_in_code(class_list, api_config)
    ans['api_res'] = api_res

    # Parse permissions to PI
    permission_res = find_in_manifest(permission_list)
    ans['permission_res'] = permission_res

    file_name = os.path.basename(apk_path)

    if result_file_path is None:
        result_file_path = os.path.join(permission_api_result_save_dir, file_name.split('.apk')[0] + '.json')

    with open(result_file_path, 'w', encoding='utf-8') as f:
        json.dump(ans, f, ensure_ascii=False)


if __name__ == '__main__':
    apk_path = './example_apk/C6092-11.8.3.181.apk'
    main(apk_path)
