from enum import Enum


class Is_Active(Enum):
    false = False
    true = True


class IsEmailSend(Enum):
    false = False
    true = True


class IsReplacedEmail(Enum):
    null = None
    false = False
    true = True


class ErorsMessege:
    INCORECT_PASSWORD = "Некорректный email или пароль"
    SHORT_PASSWORD = 'password - Пароль не меньше 8 и не больше 255 символов'
    INCORECT_EMAIL = "email - Некорректный email"
    INVALID_TOKEN = "передан невалидный токен"
    NO_TOKEN = "не передан токен"
    USER_NON_ACTIVATE = 'учетная запись не активирована, письмо с активацией отправлено повторно'
    EMAIL_EXISTS = 'Пользователь с таким email уже существует'
    EMAIL_ALREADY_CONNECT = 'такой email уже привязан к данному пользователю'
    ALREADY_ACTIVE = 'учётная запись уже активирована'
    CANT_SEND_MASSEGE = 'не удалось отправить письмо'
    USED_TOKEN = 'email уже был изменён с переданным токеном'
    NOT_FAUND = 'пользователь с таким email не найден'
    PASSWORD_BEEN_CHANGED = 'пароль уже был изменён с переданным токеном'
    WRONG_PASS = 'Пароль не меньше 8 и не больше 255 символов'
    EMAIL_ALREADY_EXISTS = 'email already exists'

class AuthErrorsMSG(Enum):
    WRONG_PASS = ErorsMessege.WRONG_PASS

class EmailErrorsMSG(Enum):
    WRONG_MAIL = 'Некорректный email'




class UserErrorsMSG(Enum):
    INCORECT_PASSWORD = ErorsMessege.INCORECT_PASSWORD
    INVALID_TOKEN = ErorsMessege.INVALID_TOKEN
    USER_NON_ACTIVATE = 'учетная запись не активирована, письмо с активацией отправлено повторно'
    NO_TOKEN = ErorsMessege.NO_TOKEN
    EMAIL_EXISTS = ErorsMessege.EMAIL_EXISTS
    EMAIL_ALREADY_CONNECT = ErorsMessege.EMAIL_ALREADY_CONNECT
    ALREADY_ACTIVE = ErorsMessege.ALREADY_ACTIVE
    CANT_SEND_MASSEGE = ErorsMessege.CANT_SEND_MASSEGE
    USED_TOKEN = ErorsMessege.USED_TOKEN
    NOT_FAUND = ErorsMessege.NOT_FAUND
    PASSWORD_BEEN_CHANGED = ErorsMessege.PASSWORD_BEEN_CHANGED
    SHORT_PASSWORD = ErorsMessege.SHORT_PASSWORD
    EMAIL_ALREADY_EXISTS = 'email already exists'