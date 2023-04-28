import random
import string
passw = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(passw)
print(f"your one time password is{passw}")
