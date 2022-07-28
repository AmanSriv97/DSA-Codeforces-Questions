from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE


n= int(input())
arr=[int(item) for item in input().split()]

a=max(arr)
b=min(arr)

maxx= arr.index(a)
arr.reverse()
minn= arr.index(b)

if maxx>(len(arr)-1-minn):
    x=(maxx+minn)-1
else:
    x=x=(maxx+minn)

print(x)