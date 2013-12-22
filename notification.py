import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
 
#Next, log in to the server
server.login("johnestar.wag@gmail.com", "woshijyx16856188")
 
#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("you@gmail.com", "ethanjyx@umich.edu", msg)