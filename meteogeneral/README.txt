###### How to link these function files to your python script:

>> Add this to the script before your custom imports:

import sys
sys.path.append('/home/jrlawson/pythoncode/general/')

>> Then import the scripts with the functions you want

###### How to reload a module within python's interpreter

reload(modulename)

>> That's without quotes, or .py extension

###### Template for every plot:
# Imports
import numpy as N
import matplotlib as M
M.use('Agg')
import matplotlib.pyplot as plt
import pdb
import sys
sys.path.append('/home/jrlawson/pythoncode/general/')
sys.path.append('/uufs/chpc.utah.edu/common/home/u0737349/lawsonpython/')

# plotting
height, width = (10,10)
outdir = '/uufs/chpc.utah.edu/common/home/u0737349/public_html/'
plt.rc('text',usetex=True)
fonts = {'family':'serif','size':16}
plt.rc('font',**fonts)

plt.savefig(outdir+fname, bbox_inches = 'tight', pad_inches = 0.5)

# How to animate
convert -delay 50 files*.png > -loop file.gif
