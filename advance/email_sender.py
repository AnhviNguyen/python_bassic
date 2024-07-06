from email.message import EmailMessage
# bao ve thong tin khi dang nhap giua client voi server
import ssl 
# giao thuc smtp dung de gui email qua cong mac dinh 465
import smtplib

email_sender = "nguyenngocanhvi852002@gmail.com"
email_password = "gdqq wrkc gdxg xknc"

email_receiver = "anhvinguyen85@gmail.com"

subject = "Happy email"
body = """
 Đừng lo âu về ngày mai vì ngày hôm nay của bạn chỉ vừa mới bắt đầu. Nỗ lực làm việc ngày hôm nay rồi bạn sẽ sẵn sàng chào đón một ngày mới khác. Đừng lãng phí thời gian. Chúc bạn một ngày tuyệt vời!
"""

em = EmailMessage()
em["From"] = email_sender 
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()
# with dung de quan ly tai nguyen trong python, smtplib.SMTP_SSL la 1 method dung de ket noi voi smtp va ssl sao cho bao mat va an toan
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())