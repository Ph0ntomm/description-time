import vk_api # for work with VK
from datetime import datetime # to determine time
import time # for delay and further automation

try:
    user_token = input("Please, write your VK token: ") # get token!
except:
    print("It seems to me that there is something wrong with your token.. ") # this not token...

work = vk_api.VkApi(token=user_token) # initialize to work with your page
vk = work.get_api() # dude.. I don’t know why


def set_status():
    now = datetime.now() # a variable so as not to write 'datetime.now()' 100 times
    a = "hours:{}. minute:{}. second:{}".format(now.hour, now.minute, now.second) # determine the time and format it for beautiful output
    vk.status.set(text=f"My present time: {a}.") # send a request to change the user description

while True:
    set_status() # call the function
    time.sleep(10) # if we send many requests per second, the VK API will ask you to pass a captcha. Automation!
