from time import time, strftime, localtime
# get the current time in format

# print(time.mktime(time.localtime()))

mytime = time()
print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation".format(mytime, mytime))
print(strftime("%b %d %Y", localtime()))
