"""
数据库设计：
    用户表：
        id:自增主键
        username:用户名
        
    文章表：
        id:自增主键
        csdn_article_id:csdn中的文章id，
        csdn_article_title:文章标题
        user_id:外键，用户id
        
    数据表：
        id:自增主键
        article_id:外键，文章id
        post_time:录入时间
        num_comments:评论数
        num_likes:点赞数
    
1.每小时执行一次
2.读取后台添加的指定账号
3.爬取每个账号的所有文章
    1.如果这个账号的文章已经在数据库，那么插入一条最新数据，
        如果不在，那么创建这个文章，并且插入一条数据

"""
from lxml import etree

import requests


# url = 'https://blog.csdn.net/qq_39687901/'
#
# response = requests.get(url)
#
# dom_tree = etree.HTML(response.text)
#
# print(dom_tree.xpath('//div[@class="article-list"]'))


def get_all_username():
    """
    获取所有username
    """
    pass


def update_data(username):
    """
    更新数据
    """
    url = 'https://blog.csdn.net/%s/article/list/{page}/' % username
    # 获取这个用户一共有多少页文章
    cur_page = 1
    while True:
        url = url.replace('{page}', str(cur_page))
        print(url)
        html = requests.get(url).text
        dom_tree = etree.HTML(html)
        # 如果第一个h6为None，那么说明这一页不存在
        if dom_tree.xpath('//h6')[0].text == 'None':
            break
        print(cur_page)
        cur_page += 1
    # dom_tree.xpath('//h6')[0].text
    # for li in list_li:
    #     print(li)
    #     max_page = int(li.xpath('./text()'))
    # print(max_page)


def main():
    update_data('u012702547')


if __name__ == '__main__':
    main()
