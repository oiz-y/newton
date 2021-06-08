import sympy as sp
import numpy as np

def newton_method(f, variables, init_value, num):
    for i in range(num):
        hesse = get_hesse(f, variables, init_value)
        subs_vector = np.array(
            [[f[i].subs(init_value)] for i in range(len(f))],
            dtype=float
        )
        init_vector = np.array(
            [[v] for v in list(init_value.values())],
            dtype=float
        )

        next_value = init_vector - np.linalg.inv(hesse) @ subs_vector
        init_value = {key: next_value[n][0] for n, key in enumerate(init_value)}
    return init_value

def get_hesse(f, variables, init_value):
    hesse = []
    for i in range(len(variables)):
        l = []
        row = []
        l.append(variables[i])
        for j in range(len(variables)):
            if len(l) == 1:
                l.append(variables[j])
            else:
                l[1] = variables[j]
            row.append(
                sp.diff(f[i], *l).subs(
                    init_value
                )
            )
        hesse.append(row)
    return np.array(hesse, dtype=float)

if __name__ == '__main__':
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    z = sp.Symbol('z')
    variables = [x, y, z]
    # ここで関数を設定する
    f = [x ** 2 - 2, (x ** 2) * (y ** 2) - 4, x * z ** 2 - 1]
    # ここで初期値を設定する
    init_value = {x: 1, y: 2, z: 0.3}
    # ここで繰り返し回数を設定する
    solution = newton_method(f, variables, init_value, 50)
    print(solution)
