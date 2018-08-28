"""
1.每小时执行一次
2.读取后台添加的指定账号
3.爬取每个账号的所有文章
"""
import time

import pymysql
from lxml import etree

import requests

g_connect = None
g_cursor = None


def get_all_username():
    """
    获取所有username和id
    """
    g_cursor = g_connect.cursor()
    sql = "select id,username from csdn_user"
    g_cursor.execute(sql)
    rs = g_cursor.fetchall()
    for row in rs:
        yield row
    g_cursor.close()


def insert_data(username, article):
    g_cursor = g_connect.cursor()
    # 插入数据
    sql = "insert into data(username,post_time,num_comments,num_likes,csdn_article_id,csdn_article_name) values('%s',%s,%s,%s,%s,'%s')" % (
        username, article['post_time'], article['num_comments'], article['num_likes'], article['csdn_article_id'],
        article['csdn_article_name'])

    print(sql)
    g_cursor.execute(sql)
    g_connect.commit()
    g_cursor.close()


def update_data(user_id, username):
    """
    更新数据
    """
    base_url = 'https://blog.csdn.net/%s/article/list/{page}/' % username
    # 获取这个用户一共有多少页文章
    cur_page = 1
    while True:
        # 请求html
        url = base_url.replace('{page}', str(cur_page))
        html = requests.get(url).text
        dom_tree = etree.HTML(html)
        # 有内容说明存在这一页
        try:
            if dom_tree.xpath('//h6')[0].text:
                break
        except:
            pass

        # 爬取数据
        for article in dom_tree.xpath(
                '//div[@class="article-list"]/div[@class="article-item-box csdn-tracking-statistics"]'):
            # csdn中的文章id
            csdn_article_id = article.xpath('./@data-articleid')[0]

            # csdn文章标题
            csdn_article_name = "".join(article.xpath('./h4/a/text()')).replace('\n', '').replace(' ', '')

            # 阅读数
            num_likes = \
                article.xpath('./div[@class="info-box d-flex align-content-center"]/p[2]/span/text()')[0].split('：')[1]

            # 评论数
            num_comments = \
                article.xpath('./div[@class="info-box d-flex align-content-center"]/p[3]/span/text()')[0].split('：')[1]

            # 当前时间
            post_time = int(time.time())

            # 录入数据
            dict_article = {
                'csdn_article_id': csdn_article_id,
                'csdn_article_name': csdn_article_name,
                'num_likes': num_likes,
                'num_comments': num_comments,
                'post_time': post_time
            }
            insert_data(username, dict_article)
        cur_page += 1


def main():
    global g_connect, g_cursor
    # 连接数据库
    g_connect = pymysql.Connect(host='gz-cdb-8bjsdhgv.sql.tencentcdb.com',
                                port=62263,
                                user='root',
                                passwd='Zxf_4342987',
                                db='csdn',
                                charset='utf8'
                                )

    for user in get_all_username():
        update_data(*user)
    # 关闭数据库

    g_connect.close()