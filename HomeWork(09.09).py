from datetime import datetime
from datetime import timedelta
now = datetime.now()
bday = datetime(2002,2,22)
averageman = 60.7
datelive = bday + timedelta(days = averageman * 365)
remain = datelive - now
print(remain.days)