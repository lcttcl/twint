# -*- encoding: utf-8 -*-
"""
---------------------------------------
@File        :   t1.py   
@Modify Time :   2020/2/28 14:55           
@Author      :   urchin_lct
@Contact     :   lichangtai17@gmail.com
@Version     :   0.0
---------------------------------------
"""
import twint
import pandas
import string


def get_numbers(user_id):
    res = 0
    twint.run.output.users_list = []
    b = twint.Config()
    b.Username = user_id
    b.Store_object = True
    twint.run.Lookup(b)
    user = twint.run.output.users_list[0]
    res = user.followers
    return res


def get_followings(user_id):
    twint.run.output.follows_list = []
    d = twint.Config()
    d.Username = user_id
    d.Store_object = True
    twint.run.Following(d)
    return twint.run.output.follows_list


def get_followers(user_id):
    twint.run.output.follows_list = []
    c = twint.Config()
    c.Username = user_id
    c.Store_object = True
    twint.run.Followers(c)
    return twint.run.output.follows_list


#  -2: jumped
#  -1: failed
#   0: successful
#   1: following_failed
#   2: follower_failed

if __name__ == '__main__':
    # raw = pandas.read_csv('twint\\86twitter.csv')
    raw = pandas.read_csv('twint\\more_than_10000.csv')
    ids = []
    for r in raw.iterrows():
        s = r[1].values[0]
        ids.append(s)

    record = {}
    for i, id in enumerate(ids[:8]):
        print('--------------------------------')
        print('This is %d th --- %s' % (i, id))
        print('--------------------------------')

        outcome = []
        try:
            record[id] = 0

            # print('judging %s' % (id))
            # num = get_numbers(id)
            # cnt = 0
            # while num == 0:
            #     cnt = cnt + 1
            #     if cnt == 10:
            #         record[id] = -1
            #         continue
            #     print('%d th times judging %s' % (cnt, id))
            #     num = get_numbers(id)
            # if num > 10000:
            #     record[id] = -2
            #     print('TOO MANY, NEXT')
            #     continue

            # get followings
            print('getting %s\' FOLLOWINGS ' % (id))
            followings = get_followings(id)
            cnt = 0
            while len(followings) == 0:
                cnt = cnt + 1
                if cnt == 10:
                    record[id] = 1
                    break
                print('%d th times retrying %s\' FOLLOWINGS ' % (cnt, id))
                followings = get_followings(id)

            # output temporarily
            outcome_temp = [followings, []]
            name = ['followings', 'followers']
            out_temp = pandas.DataFrame(data=outcome_temp)
            out_temp = pandas.DataFrame(data=out_temp.values.T, columns=name)
            # out_temp.to_csv('result\\' + id + "_temp.csv", index=False)
            out_temp.to_csv('result\\' + id + ".csv", index=False)

            # get followers
            # print('getting %s\' FOLLOWERS ' % (id))
            # followers = get_followers(id)
            # cnt = 0
            # while len(followers) == 0:
            #     cnt = cnt + 1
            #     if cnt == 10:
            #         record[id] = 2
            #         break
            #     print('%d th times retrying %s\' FOLLOWERS ' % (cnt, id))
            #     followers = get_followers(id)

            # if record[id] != -1:
            #     outcome = [followings, followers]
            #     name = ['followings', 'followers']
            #     out = pandas.DataFrame(data=outcome)
            #     out = pandas.DataFrame(data=out.values.T, columns=name)
            #     out.to_csv('result\\' + id + ".csv", index=False)
        except Exception as r:
            record[id] = -1
            print('--------------------------------')
            print('error!!!!! %s' % str(r))
            print('--------------------------------')
            continue

        print('--------------------------------')
        print('%s done, status: %d' % (id, record[id]))
        print('--------------------------------')

    print(record)
