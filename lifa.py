import smtplib
# help(smtplib)
smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
smtpObj.starttls()
smtpObj.login('asonmbxnzmcb13377331@yandex.ru', 'gjxnfgjxnf2003')
smtpObj.sendmail("asodfksdiojfoisdjfoi13377331@yandex.ru", "Остановись, брат")
smtpObj.quit()