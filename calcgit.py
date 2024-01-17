from datetime import date, datetime

today = date.today().strftime("%d/%m/%Y")
first_day_str = "01/01/2024"
last_day_str = "31/12/2024"
meta = 4
daysOfYear = 365

today_calc = datetime.strptime(today, '%d/%m/%Y').toordinal()
first_day = datetime.strptime(first_day_str, '%d/%m/%Y').toordinal()
last_day = datetime.strptime(last_day_str, '%d/%m/%Y').toordinal()
days = (today_calc-first_day)

commit = int(input("Quantidade de commits: "))
averageCommits = commit/(days)
averageFault = (daysOfYear*meta - commit)/(last_day-today_calc)
estimativeCommitsYear = daysOfYear * averageCommits
commitYearMeta = daysOfYear*meta
# print(days)
print(f"Você realizou {commit} em {days} dias")
print(f"Sua média de commits é de {averageCommits:4.2f} por dia")
print(f"Com essa média, o número de commits no ano será de {estimativeCommitsYear:4.0f}")
print(f"Mas sua meta de commits é de {commitYearMeta:4.0f}, e faltam {commitYearMeta-averageCommits*days:4.0f}")
print(f"Sua média de commits por dia deve ser de {averageFault:4.2f} por dia")
