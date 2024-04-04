#Input vom Nutzer

hourly_pay = float(input("Wie hoch ist dein Stundenlohn? "))
hours_per_day = float(input("Wie viele Stunden arbeitest du pro Arbeitstag? "))
days_per_week = int(input("Wie viele Tage arbeitest du pro Woche?"))

#Berechnungen

pay_per_day = hourly_pay * hours_per_day
pay_per_week = pay_per_day * days_per_week
pay_per_month = pay_per_week * 4.33
pay_per_year = pay_per_month * 12

#Ergebnisse

print("Bei einem Stundenlohn von", format(hourly_pay, '.2f'), "€ verdienst du pro Tag",format(pay_per_day, '.2f'), "€,",format(pay_per_month, '.2f'),"€ pro Monat und", format(pay_per_year, '.2f'),"€ pro Jahr.")
input("Beliebige Taste zum Beenden")
