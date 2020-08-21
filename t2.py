# -*- encoding: utf-8 -*-
"""
---------------------------------------
@File        :   t2.py   
@Modify Time :   2020/3/2 8:32           
@Author      :   urchin_lct
@Contact     :   lichangtai17@gmail.com
@Version     :   0.0
---------------------------------------
"""
import twint

import pandas


def get_numbers(user_id):
    res = 0
    twint.run.output.users_list = []
    b = twint.Config()
    b.Username = user_id
    b.Store_object = True
    twint.run.Lookup(b)
    user = twint.run.output.users_list[0]
    res1 = user.followers
    res2 = user.following
    return [res2, res1]


if __name__ == '__main__':
    raw = pandas.read_csv('D:\OneDrive\Documents\Python_things\\twint\\twint\86twitter.csv')
    ids = []
    for r in raw.iterrows():
        s = r[1].values[0]
        ids.append(s)
    record = {}
    for i, id in enumerate(ids[0:]):
        r = get_numbers(id)
        record[id] = r
    print(record)
    #     if r > 10000:
    #         record.append(id)
    # p = pandas.DataFrame(data=record)
    # p = pandas.DataFrame(data=p.values.T)
    # p.to_csv('more_than_10000.csv', index=False)
