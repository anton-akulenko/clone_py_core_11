import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

'{:<30}'.format('left aligned')

'{:>30}'.format('right aligned')

'{:^30}'.format('centered')

'{:*^30}'.format('centered')
