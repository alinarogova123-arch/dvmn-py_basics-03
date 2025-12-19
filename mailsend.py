import smtplib
import os

from dotenv import load_dotenv

load_dotenv('login.env.py')

login = os.getenv('login')

password = os.getenv('password')

email_to = os.getenv('email_to')

site_name = 'https://dvmn.org/profession-ref-program/roma_belozerov/Mg57L/'

friend_name = 'Виконтий'

my_name = 'Роман'

letter = """\
From: {login}
To: {email_to}
Subject: Заголовок письма
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""" .format(login=login, email_to=email_to)

letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', my_name)
letter = letter.replace('%website%', site_name)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(login, password)
server.sendmail(login, email_to, letter)
server.quit()




