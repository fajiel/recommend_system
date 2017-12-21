from recommend.main import recommend_movie, get_datasets, get_type_datasets
from recommend.util import get_accuracy_datasets, CORPUS_TYPE_SETTINGS

ACCURANCY_LEN = 3

def calc_accuracy():
    all_corpus_list, all_labels = get_datasets(CORPUS_TYPE_SETTINGS)
    type_datasets_dict = get_type_datasets(CORPUS_TYPE_SETTINGS)
    accuracy_corpus_list, accuracy_labels = get_accuracy_datasets()
    accuracy_total = len(accuracy_corpus_list)
    accuracy_num = 0
    for tmp_labels in accuracy_corpus_list:
        recommend_msg = recommend_movie(tmp_labels, all_corpus_list, all_labels, type_datasets_dict)
        recommend_type = recommend_msg[0]
        if recommend_type in tmp_labels[:ACCURANCY_LEN]:
            accuracy_num += 1
    accuracy = 1.00 * accuracy_num / accuracy_total
    accuracy_rate = u'%.2f%%' % (accuracy_num / accuracy_total)
    print("测试集合总数:{}".format(accuracy_total))
    print("准确推荐个数:{}".format(accuracy_num))
    print("准确率:{}  ({})".format(accuracy_rate, accuracy))
    return accuracy_rate

def main():
    calc_accuracy()

if __name__ == '__main__':
    main()