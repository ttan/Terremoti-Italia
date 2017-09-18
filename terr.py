import urllib2, time, xmltodict, argparse
# import onionGpio

#Args and help
parser = argparse.ArgumentParser(description='Fetch Italian earthquakes from INGV website and buzz with an Omega Onion2+')

parser.add_argument('-m', '--mag', help='minimun magnitude: it will buzz for earthquakes greater than this value (default: 1).', default=1, type=int)
parser.add_argument('-t', '--time', help='lenght of the buzz, in seconds (default: 0.5).', default=0.5, type=float)
args = parser.parse_args()

#Min magnitude, optional parameter
mag = str(args.mag)

#Lenght of the buzz
buzz = args.time

#Set GPIO
# gpioNum = 0
# gpioObj	= onionGpio.OnionGpio(gpioNum)

requestURL = "http://webservices.ingv.it/fdsnws/event/1/query?minmag="+mag+"&maxmag=10&mindepth=-10&maxdepth=1000&minlat=35&maxlat=49&minlon=5&maxlon=20&minversion=1&orderby=time"

lastId = ""

def checkLast():
	global lastId
	fsock = urllib2.urlopen(requestURL)
	data = fsock.read()
	fsock.close()
	data = xmltodict.parse(data)
	last = 0
	newId = data['q:quakeml']['eventParameters']['event'][0]['@publicID']
	if(lastId != newId):
		print "* Ultimo terremoto:",data['q:quakeml']['eventParameters']['event'][0]['description']['text'],"{",newId,"}"
		lastId = newId
		#Make it bip!
		# status 	= gpioObj.setOutputDirection(0)		# initialize the GPIO to 0 (LOW)
		time.sleep(buzz)
		# status  = gpioObj.setInputDirection()
	else:
		print "* Nessun nuovo terremoto, ultimo id", lastId
	print '---'

while True:
	checkLast()
	time.sleep(60)