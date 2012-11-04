import argparse
import os
import rsvg
import cairo
from subprocess import call


def mkdirp(directory):
    try:
        os.makedirs(directory)
    except:
        pass
parser = argparse.ArgumentParser(description='Convert SVG file to tile PNGs (Slippy map format) using Inkscape')
parser.add_argument('svg', metavar='svg',help='original vector file')
parser.add_argument('outputdir', metavar='outputdir', help='ooutput dir')
parser.add_argument('lowestlevel', metavar='lowestlevel', type=int, help='ooutput dir')
parser.add_argument('highestlevel', metavar='lowestlevel', type=int, help='ooutput dir')
args = parser.parse_args()
svg = rsvg.Handle (file = args.svg)

svgwidth = svg.props.width
svgheight = svg.props.height
svgsize = max(svgwidth,svgheight)
for z in xrange(args.lowestlevel,args.highestlevel+1):
    blocksize = 1.0*svgsize/(2**z)
    #print blocksize
    for x in xrange(0,2**z):
        mkdirp('%s/%d/%d'%(args.outputdir,z,x))
        for y in xrange(0,2**z):
            px = blocksize*x
            py = svgheight-blocksize*(y)
            print 'inkscape -b "#ffffff" -z -e %s/%d/%d/%d.png -w 256 -h 256 -a %.6f:%.6f:%.6f:%.6f %s'%(args.outputdir,z,x,y,px,py-blocksize,px+blocksize,py,args.svg)