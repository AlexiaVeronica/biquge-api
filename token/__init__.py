import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'JKFWfjskfs3kasfjsfkj'


# 生成token的代码，token过期时长定义为默认参数，单位为秒
def create_token(uid, seconds=60):
    # 定义token过期时间，为当前utc时间加上token有效期
    expire = datetime.utcnow() + timedelta(seconds=seconds)
    to_encode = {"exp": expire, "sub": SECRET_KEY, "uid": uid}
    # 使用jwt生成token，token是根据payload和秘钥共同生成。
    jwt_token = jwt.encode(payload=to_encode, key=SECRET_KEY)
    return jwt_token
