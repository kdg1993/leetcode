select round( sum( tiv_2016 ), 2 ) as tiv_2016
from Insurance InsA
where InsA.tiv_2015 in (select tiv_2015 from Insurance InsB where InsA.pid != InsB.pid)
  and (InsA.lat, InsA.lon) not in (select InsB.lat, InsB.lon from Insurance InsB where InsA.pid != InsB.pid)