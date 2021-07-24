import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
message="INDIA"
connection.sendmail("vaishnavi.p6521@gmail.com", "priya.hajela358@gmail.com", message)
print("Email sent successfully")
connection.quit()