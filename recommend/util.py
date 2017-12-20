from douban.douban.models import Douban, db_connect
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db_connect())
session = Session()

CORPUS_TYPE_SETTINGS = {
    '剧情': 1, '喜剧': 2, '动作': 3, '爱情': 4, '科幻': 5,
    '动画': 6, '悬疑': 7, '惊悚': 8, '恐怖': 9, '纪录片': 10,
    '短片': 11, '情色': 12, '同性': 13, '音乐': 14, '歌舞': 15,
    '家庭': 16, '儿童': 17, '传记': 18, '历史': 19, '战争': 20,
    '犯罪': 21, '西部': 22, '奇幻': 23, '冒险': 24, '灾难': 25,
    '武侠': 26, '古装': 27, '运动': 28, '黑色电影': 29
}

def check_label(usr_label):
    if not isinstance(usr_label, list):
        usr_label = usr_label.split("|")
    label_ok = True
    for tmp_label in usr_label:
        if tmp_label not in CORPUS_TYPE_SETTINGS:
            label_ok = False
            break
    return label_ok

def get_message(id):
    query = session.query(Douban)
    return query.filter_by(id=id).first()

def get_accuracy_datasets():
    query = session.query(Douban)
    #获取测试数据
    query_obj_list = query.filter_by(property='1').all()
    corpus_list = []
    labels = []
    for query_obj in query_obj_list:
        types = query_obj.types
        corpus_list.append(types.split("|"))
        labels.append(query_obj.movie_type)
    return corpus_list, labels