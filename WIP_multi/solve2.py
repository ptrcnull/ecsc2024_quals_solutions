import functools
import sympy
import random
import matplotlib
import numpy as np

a = 16607683159820969821334053668565497023672553723120463309429594505511237879034577633612046554203127383421087262122366559782549452227442655978577041006582592182736922324295338420270626819107511550881657877
b = 25551215271781189598874426878862316864812581725043603372252140494846089508926229930474790805776343733438714292797355930074164508091657786022929506398463880301910511131220554730086719022498840162517991137
c = 20786191324953792562009866853371215040863303
s24c = 17530888003368647156289259217837386783102445
N = 1187958312838759124284554573131124126935409913863314039442751811472713832328228838809156981593920545781447477983725054814300215030741029873621268923849336891499156890391241452662673230424582615690695139488563447524637075308093800898523369871415156847585677060017697705930714628064633544771455068846410636235644969832309162176585034000877398786134508512029652562351236336633606232143741296847369935403850409548447590940562502745918919243939917885124873673746920879

s1 = 52301238548999283720018992803
s3 = 53526471528723273317793958277

s1, s3 = s3, s1

p_semi = a*s1
q_semi = b*s3

print(p_semi)

target = 758

# x = np.linspace(2**94, 2**98)
# y = ((-a * s1 * (b * s3 + x) - s24c + N) // (b * s3))
# fig, ax = plt.subplots()
# ax.plot(x, y, linewidth=2.0)
# plt.show()

highest_value_of_s4 = 64600213875334817685682271828
highest_value_of_s2 = 42972249412506356614640275876
# print(step)

for i in range(0, 10):
    # print(i)
    # if i in flips:
    #     results.append(900)
    #     continue
    # print('bit', i)

    s4_guess = i
    s2_guess = ((-a * s1 * (b * s3 + s4_guess) - s24c + N) // (b * s3))

    # diff = (s4_guess - s2_guess) / 2**96

    print({'s4': s4_guess, 's2': s2_guess}, s2_guess + s4_guess)

    if s2_guess < 0:
        break

#     if s2_guess < 0:
#         print('oof')
#         # results.append(900)
#         continue

#     p_guess = p_semi + s2_guess
#     q_guess = q_semi + s4_guess
#     N_guess = p_guess*q_guess

#     # print(N)
#     # print(N_guess)
#     # print(N - N_guess)
#     # print(len(bin(N - N_guess))-2)
#     diff = len(bin(N - N_guess))-2
#     print(i, diff)
#     # results.append(diff)
#     # if diff <= target:
#     #     exit()

# print(min(results), results.index(min(results)))

# print(N - (a*b*s1*s3))

# exit()
# p1_upper = s1 * a
# print(p1_upper)
# p3_upper = s3 * a
# print(p3_upper)
# s.add(Or(, s1 == 52301238548999283720018992803))
# s.add(Implies(s1 == 53526471528723273317793958277, s3 == 52301238548999283720018992803))
# s.add(Implies(s1 == 52301238548999283720018992803, s3 == 53526471528723273317793958277))

# @functools.cache
# def is_factor(x, f):
#     return x % f == 0

# i = (N - a*b*s1*s3 - s24c)
# print(i)

# for n in range(506206739809770):