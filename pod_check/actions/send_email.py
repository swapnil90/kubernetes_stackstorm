import smtplib
from st2actions.runners.pythonrunner import Action

class Send_email(Action):
    def run(self, replication_count):

        if replication_count > 5:
		    # creates SMTP session
			s = smtplib.SMTP('smtp.gmail.com', 587)

			# start TLS for security
			s.starttls()

			# Authentication
			s.login("sender_email_id", "sender_email_id_password")

			# message to be sent
			message = "Replication count exceed 5, current count is $s" % replication_count

			# sending the mail
			s.sendmail("sender_email_id", "receiver_email_id", message)

			# terminating the session
			s.quit()
            return (True, replication_count)
        return (False, replication_count)
