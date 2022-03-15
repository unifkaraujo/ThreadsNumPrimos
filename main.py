from time import perf_counter_ns
import simples as sp
import mtrhead as mt

with open("data.csv") as file:
    data = [line.strip() for line in file]

media1 = 0
media2 = 0
qtdproc = 50
data = list(map(int, data))

print('\n\nanalise de %d valores\n\n'%(len(data)))

for i in range(qtdproc):
    start1 = perf_counter_ns()
    primo_sp = sp.resolve_simples(data)
    finish1 = perf_counter_ns()
    media1 += (finish1-start1)/1000000
  
for i in range(qtdproc):
    start2 = perf_counter_ns()
    primo_mt = mt.resolve_trhread(data)
    finish2 = perf_counter_ns()
    media2 += (finish2-start2)/1000000

media1 = media1/qtdproc
media2 = media2/qtdproc

print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt))
print('Média de SpeedUP sem Threads: %f'%(media1))
print('Média de SpeedUP com Threads: %f'%(media2))
print('SpeedUP: %f'%((media1/media2)))
