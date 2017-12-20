from recommend.main import recommend_movie
from recommend.util import get_accuracy_datasets

ACCURANCY_LEN = 3

def calc_accuracy():
    accuracy_corpus_list, accuracy_labels = get_accuracy_datasets()
    accuracy_total = len(accuracy_corpus_list)
    accuracy_num = 0
    for tmp_labels in accuracy_corpus_list:
        recommend_msg = recommend_movie(tmp_labels)
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