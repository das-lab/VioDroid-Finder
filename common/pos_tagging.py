import hanlp


def get_pos_hanlp():
    """
    The hanlp model for part-of-speech tagging
    :return:
    """
    pos_hanlp = hanlp.load(hanlp.pretrained.pos.CTB9_POS_ELECTRA_SMALL)
    return pos_hanlp


if __name__ == '__main__':
    words = ['我们', '会', '收集', '您', '的', '手机号码', '、', '银行卡', '号', '等',
             '个人信息']  # We will collect your mobile phone number, bank card number, etc.
    pos_hanlp = get_pos_hanlp()
    print(pos_hanlp(words))  # ['PN', 'VV', 'VV', 'PN', 'DEG', 'NN', 'PU', 'NN', 'NN', 'ETC', 'NN']
