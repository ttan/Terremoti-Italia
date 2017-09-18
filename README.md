# Terremoti Italia
This script fetch earthquake list form INGV website in *QuakeML* format every minute. If a new earthquake is found, it buzzes via GPIO interface.

**The script uses hardware implementation with Onion Omega2+. See [this post](https://blog.ttan.org/earthquake-monitor-with-omega2-ac86583476b4) for more info about the hardware**

## Usage
```shell
earthquakes-italy.py [-h] [-m MAG] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -m MAG, --mag MAG     minimun magnitude: it will buzz for earthquakes
                        greater than this value (default: 1).
  -t TIME, --time TIME  lenght of the buzz, in seconds (default: 0.5).
```

