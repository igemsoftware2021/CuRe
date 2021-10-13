for t in True, False :
    for i in range(1000):
        print(f'sudo chmod {i} fiveNine/metadata')
        if t :
            print(f'sudo chmod o+t fiveNine/metadata')
        print('python3 Ecorp.py share')
quit()


samples = """Sample
, blanc, -0.0001
, blanc, 0.0004
, t0 2mg 1, 0.0519
, t0 2mg 1, 0.0521
, t0 2mg 1, 0.0521
, cu 2mg 1, 0.0707
, cu 2mg 1, 0.0708
, cu 2mg 1, 0.0706
, t0 2mg 2, 0.0497
, t0 2mg 2, 0.0498
, t0 2mg 2, 0.0501
, cu 2mg 2, 0.0731
, cu 2mg 2, 0.0739
, cu 2mg 2, 0.0735
, t0 10mg 1, 0.1839
, t0 10mg 1, 0.1842
, t0 10mg 1, 0.1840
, cu 10mg 1, 0.3629
, cu 10mg 1, 0.3625
, cu 10mg 1, 0.3627
, t0 10mg 2, 0.1905
, t0 10mg 2, 0.1913
, t0 10mg 2, 0.1916
, cu 10mg 2, 0.3416
, cu 10mg 2, 0.3416
, cu 10mg 2, 0.3416
, t1 2mg 1, 0.0518
, t1 2mg 1, 0.0517
, t1 2mg 1, 0.0520
, t1 2mg 2, 0.0532
, t1 2mg 2, 0.0532
, t1 2mg 2, 0.0528
, t1 10mg 1, 0.1877
, t1 10mg 1, 0.1877
, t1 10mg 1, 0.1878
, t1 10mg 2, 0.1830
, t1 10mg 2, 0.1828
, t1 10mg 2, 0.1829
, blanc, 0.0007
, t2 2mg 1, 0.0491
, t2 2mg 1, 0.0491
, t2 2mg 1, 0.0494
, t2 2mg 2, 0.0502
, t2 2mg 2, 0.0500
, t2 2mg 2, 0.0500
, t2 10mg 1 , 0.1821
, t2 10mg 1, 0.1819
, t2 10mg 1, 0.1820
, t2 10mg 2, 0.1847
, t2 10mg 2, 0.1843
, t2 10mg 2, 0.1841
, t3 2mg 1, 0.0497
, t3 2mg 1, 0.0494
, t3 2mg 1, 0.0495
, t3 2mg 2, 0.0498
, t3 2mg 2, 0.0498
, t3 2mg 2, 0.0498
, blanc, -0.0005
, t3 10mg 1, 0.1939
, t3 10mg 1, 0.1937
, t3 10mg 1, 0.1937
, t3 10mg 2, 0.1863
, t3 10mg 2, 0.1863
, t3 10mg 2, 0.1863
, t4 2mg 1, 0.0500
, t4 2mg 1, 0.0500
, t4 2mg 1, 0.0501
, t4 2mg 2, 0.0544
, t4 2mg 2, 0.0549
, t4 2mg 2, 0.0548
, t4 10mg 1, 0.1903
, t4 10mg 1, 0.1909
, t4 10mg 1, 0.1900
, t4 10mg 2, 0.1861
, t4 10mg 2, 0.1862
, t4 10mg 2, 0.1868
, t5 2mg 1, 0.0753
, t5 2mg 1, 0.0750
, t5 2mg 1, 0.0750
, t5 2mg 2, 0.0508
, t5 2mg 2, 0.0505
, t5 2mg 2, 0.0507
, t5 10mg 1, 0.1836
, t5 10mg 1, 0.1838
, t5 10mg 1, 0.1843
, t5 10mg 2, 0.2031
, t5 10mg 2, 0.2029
, t5 10mg 2, 0.2059"""
samples = [sample for sample in samples.split('\n') if 'mg' in sample]
print(samples)

samples = [[e.strip() for e in sample.split(',')[1:]] for sample in samples]
times = {sample[0].split(' ')[0] for sample in samples}
times = list(times)
times.sort()

groups = {tuple(sample[0].split(' ')[1:]): {t: [] for t in times} for sample in samples}
for sample in samples:
    g = sample[0]
    t = g.split(' ')[0]
    groups[tuple(g.split(' ')[1:])][t].append(float(sample[1].strip()))
print(groups)


def mean(ls): return sum(ls) / len(ls)


groups = {group: {i: mean(groups[group][i]) for i in groups[group]} for group in groups}
print(groups)

import matplotlib.pyplot as plt

for group in groups:
    g = groups[group]
    v = []
    print(f'{group[0]} {group[1]}')
    for t in times:
        v.append(g[t])
        print(f'\t{g[t]:.5f}')
    plt.title(group)
    plt.plot(times, [v * 88.4 / 3.25 for v in v])
    plt.savefig(f'plots/{group}.png')
    plt.show()
