from datetime import datetime

datetime .now (). isoformat()

from datetime import datetime
from dateutil.tz import tzlocal

datetime,now (tzlocal()).isoformat()

from datetime import datetime
from dateutil.tz import tzlocal

datetime.now(tzlocal()).replace(microsecond=0).isoformat()