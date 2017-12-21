from recommend.kNN import get_datasets, get_type_datasets, classify
from recommend.util import CORPUS_TYPE_SETTINGS, get_message, check_label

def get_usr_label(usr_label):
    if not isinstance(usr_label, list):
        usr_label = usr_label.split("|")
    type_list = list(CORPUS_TYPE_SETTINGS.keys())
    array_list = [0]*len(CORPUS_TYPE_SETTINGS)
    for tmp_type in usr_label:
        type_index = type_list.index(tmp_type)
        array_list[type_index] = 1
    return array_list

def get_recommend_type(array_list, all_corpus_list, all_labels):
    all_k = 3
    recommend_type = classify(array_list, all_corpus_list, all_labels, all_k)
    return recommend_type

def get_recommend_id(array_list, recommend_type, type_datasets_dict):
    type_k = 2
    type_corpus_list = type_datasets_dict.get(recommend_type, {}).get("corpus_array")
    type_labels = type_datasets_dict.get(recommend_type, {}).get("labels")
    recommend_id = classify(array_list, type_corpus_list, type_labels, type_k)
    return recommend_id

def recommend_movie(usr_label, all_corpus_list, all_labels, type_datasets_dict):
    array_list = get_usr_label(usr_label)
    recommend_type = get_recommend_type(array_list, all_corpus_list, all_labels)
    recommend_id = get_recommend_id(array_list, recommend_type, type_datasets_dict)
    return recommend_type, recommend_id

def main():
    # usr_label支持两种数据结构：
    #       1."喜剧|动画",
    #       2.['喜剧','黑色电影']

    all_corpus_list, all_labels = get_datasets(CORPUS_TYPE_SETTINGS)
    type_datasets_dict = get_type_datasets(CORPUS_TYPE_SETTINGS)
    while True:
        print(u"请输入用户标签：")
        usr_label = input()
        if not check_label(usr_label):
            print(u"用户标签存在异常，请重新输入！")
            continue
        recommend_type, recommend_id = recommend_movie(usr_label, all_corpus_list, all_labels, type_datasets_dict)
        query_obj = get_message(recommend_id)
        print("****新用户标签****:", usr_label)
        print("****推荐电影类别****:", recommend_type)
        print("****推荐电影标签****:", query_obj.types)
        print("****推荐电影ID****:", recommend_id)
        print("****推荐电影名称****:", query_obj.title)
        print("****推荐电影链接****:", query_obj.url)
        print("****推荐电影评分****:", query_obj.score)
        print("----------------------------请输入下一条----------------------------")

if __name__ == '__main__':
    main()