from tgtg import TgtgClient
import json

client = TgtgClient()
client.signup_by_email(email="Dopi21@yopmail.com")



client = TgtgClient(email="Dopi21@yopmail.com")
credentials = client.get_credentials()
print(credentials)

creds = {
    'access_token': 'e30.eyJzdWIiOiIxMDU3NTQ4MDMiLCJleHAiOjE2ODM1NzA1MDEsInQiOiJXelZxRTNXdlJuQ1FORmZyendXaTVBOjA6MSJ9.t0mfLiyh0bpdvYdSXnne-96Eo_BbIULnLJ9Df5fGSe8',
    'refresh_token': 'e30.eyJzdWIiOiIxMDU3NTQ4MDMiLCJleHAiOjE3MTUwMjAxMDEsInQiOiJmUWg5WWk3Y1FkZXUwMFJJc3BJYk1BOjA6MCJ9.Taz3Tgeihtjb5isU9L-9WOOerbEmGHcRKiWb_2G_BpY',
    'user_id': '105754803', 
    'cookie': 'datadome=7DsLspHsFwD8ZuDnmDB9~kYBo87Z8IJvye1W7FeCsD~G3ZCVbXqTqEqdVUL0s7r7dmtE2RHfIOObxYAUl8JlaCcFgrx2aD6-cSco6pd0gktp5_goaC5XvgkQ8tWmtpT4; Max-Age=5184000; Domain=.apptoogoodtogo.com; Path=/; Secure; SameSite=Lax'
    }


