from recommend.kNN import get_datasets, get_type_datasets, classify
from recommend.util import CORPUS_TYPE_SETTINGS
from recommend.util import get_message

def get_usr_label(usr_label):
    if not  isinstance(usr_label, list):
        usr_label = usr_label.split("|")
    type_list = list(CORPUS_TYPE_SETTINGS.keys())
    array_list = [0]*len(CORPUS_TYPE_SETTINGS)
    for tmp_type in usr_label:
        type_index = type_list.index(tmp_type)
        # array_list[type_index] = 1
        array_list[type_index] = CORPUS_TYPE_SETTINGS.get(tmp_type)
    return array_list

def get_recommend_type(array_list):
    all_k = 3
    all_corpus_list, all_labels = get_datasets(CORPUS_TYPE_SETTINGS)
    recommend_type = classify(array_list, all_corpus_list, all_labels, all_k)
    return recommend_type


def get_recommend_id(array_list, recommend_type):
    type_k = 2
    type_corpus_list, type_labels = get_type_datasets(CORPUS_TYPE_SETTINGS, recommend_type)
    recommend_id = classify(array_list, type_corpus_list, type_labels, type_k)
    return recommend_id

def recommend_movie(usr_label):
    array_list = get_usr_label(usr_label)
    recommend_type = get_recommend_type(array_list)
    recommend_id = get_recommend_id(array_list, recommend_type)
    query_obj = get_message(recommend_id)
    print("****新用户标签****:", usr_label)
    print("****推荐电影类别****:", recommend_type)
    print("****推荐电影ID****:", recommend_id)
    print("****推荐电影名称****:", query_obj.title)
    print("****推荐电影链接****:", query_obj.url)
    print("****推荐电影评分****:", query_obj.score)

def main():
    # usr_label支持两种数据结构：
    #       1."喜剧|动画",
    #       2.['喜剧','黑色电影']

    while True:
        print(u"请输入用户标签：")
        usr_label = input()
        recommend_movie(usr_label)
        print("------------------------请输入下一条------------------------")

if __name__ == '__main__':
    main()