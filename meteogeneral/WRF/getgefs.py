# Downloads all variables for GEFS R2 reforecasts
import os
import numpy as N
import calendar
import time

# Dates in YYYYMMDD format - all runs are 00z
# Need to be strings
#dates = ['20111128','20111129','20111130']
dates = ['20111129']

# This switch downloads the GEFS data ran at lower resolution after t190.
lowres = 0

# This downloads all ensemble members. Change ens for desired member (or mean/sprd)
ens = ['p0' + str(p) if p<10 else 'p10' for p in range(1,11)]

# Control?
control = 1
if control:
    ens.append('c00')

# Choose gaussian or latlon.
coord = 'latlon'

# Root directory
FTP = 'ftp://ftp.cdc.noaa.gov/Projects/Reforecast2/'

# -nc does not download a renamed multiple copy of file
# --output-document=CATNAME concatenates all files together for the big grib file
# -nd makes sure hierachy isn't downloaded too

"""
for d in dates:
    for e in ens:
        url = os.path.join(FTP, d[0:4], d[0:6], d+'00', e, coord)
        fname = '/*' + e + '.grib2'
        CATNAME = d + '_' + e + '.grib2'
        cmnd = "wget -nc -nd --output-document=" + CATNAME + ' ' + url + fname
        os.system(cmnd)
        print d, e, " Downloaded."

# This section will split the data into forecast times for WRF to read
# Using WGRIB2
# fin : grib2 input file
# fout : smaller grib2 output file with just one forecast time
# timestr : search pattern to find the forecast time
"""
for d in dates:
    # Convert this date to python time for later conversion
    pytime_anl = calendar.timegm((int(d[:4]),int(d[4:6]),int(d[6:8]),0,0,0))
    for e in ens:
        fin = ''.join((d,'_',e,'.grib2'))
        fprefix = '_'.join((d,e,'f'))
        for t in N.arange(0,198,6):
            ts = "%03d" %t # Gets files into chron order with padded zeroes
            if t==0:
                timestr = '":anl:"'    
            else:
                timestr = ''.join(('":(',str(t),' hour fcst):"'))
            fout = fprefix + ts + '_OLD.grib2'
            str1 = ' '.join(('wgrib2',fin,'-match',timestr,'-grib',fout)) 
            os.system(str1)
            #print fout, "created."

            # Convert time to forecast time, because WRF demands it so
            fout2 = fprefix + ts + '.grib2'
            pytime_fcst = pytime_anl + (3600*t)
            ddate = ''.join(["%02d" %x for x in time.gmtime((pytime_fcst))])[:10] 
            str2 = ' '.join(('wgrib2 -match "^[0-9]*(:|\.1)"', fout, '-set_date', ddate, '-grib', fout2))
            os.system(str2)
