from authy.api import AuthyApiClient
authy_api = AuthyApiClient('')

user = authy_api.users.create(
    email='aditya********20bcs8@iiitkottayam.ac.in',
    phone='7406548*',
    country_code=91)


sms = authy_api.users.request_sms(user.id)
print(sms.content)
