from resources.configuration import PI_path


def get_PI():
    """
    Get all the PI(personal information) from the configuration file
    :return: dict, Contains PI name, PI type, and its alias. For example: [birthday, basic PI, [date of birth, ...]]
    """
    PI = {}

    with open(PI_path, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.split('\n\n')
        for d in data:
            ds = d.split('\n')
            for description in ds[2].split(';'):
                PI[description] = {'pi_type': ds[0], 'pi': ds[1]}
    return PI


if __name__ == '__main__':
    pi = get_PI()
    print(pi)
