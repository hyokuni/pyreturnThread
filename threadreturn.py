import threading
from man import man

aplay = man()
rvalue = aplay.run()
print(rvalue)
