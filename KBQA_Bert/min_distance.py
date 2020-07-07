


def min_distance(name, word_list):
    n = len(name)
    res = []
    min_dis = float("inf")
    for word in word_list:

        m = len(word)

    # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

    # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

    # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if name[i - 1] != word[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)
        if (D[n][m] == min_dis):
            # min_dis = D[n][m]
            res.append(word)
        elif (D[n][m] < min_dis):
            min_dis = D[n][m]
            res.clear()
            res.append(word)
    return res


print(min_distance('谷歌北京',['谷歌','xx口腔','北京中软国际xxxx']))
print(min_distance('微软大楼',['微软','微软亚洲研究院','北京中软国际xxxx']))
