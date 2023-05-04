import pendulum
from pendulum import now, timezone, parse, yesterday

#iana
#np = pendulum.now()

norway_tz = 'Europe/Sarajevo'
rj_tz = 'America/Sao_Paulo'
no = now(norway_tz)

print('-' * 4 + 'time noruega e brasil')
print(no)
print(no.in_tz(rj_tz))

d1 = no.subtract(days = 1)
d0 = d1.subtract(days = 1)
print('-' * 4 + 't0 e t1')
print(d0)
print(d1)

print('-' * 4 + 'teste 1 troca de timezone com troca de horário de verao')
br = no.subtract(days = 40)
br.in_tz(norway_tz)
print(br)
print('-' * 4 + 'parse')
dt = '2023-03-08 21:23:10+00:00'
k = parse(dt)
print(k)

print('-' * 4 + 'teste 2 troca de timezone com troca de horário de verao')
dt_no = parse('2023-04-15 09:30:24') #neste caso o texto tem que conter a localização com +00:00. exp = '2023-04-15 09:30:24-03:00'
print(dt_no)
dt_no = dt_no.in_tz(norway_tz)
print(dt_no)
dt_br = dt_no.in_tz(rj_tz)
print(dt_br)