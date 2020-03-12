from ROOT import *
import os

import sys
from optparse import OptionParser

parser = OptionParser()



parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                     help="Specify which channel mu or ele? default is mu" )

parser.add_option("-y", "--year", dest="Year", default="",type='str',
                     help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-s", "--step", dest="step", default="",type='str',
                     help="Specify which iteration , ita1 or ita2, or ita3?" )

parser.add_option("-p", "--opt", dest="sel", default="",type='str',
                     help="Specify which selection?" )

(options, args) = parser.parse_args()

channel=options.channel
year=options.Year
step=options.step
sel=options.sel

if channel=="ele":
        Chan="Ele"
elif channel=="mu":
        Chan="Mu"


#sel2 = "Ele_2jet0b_"

file_=TFile("fitDiagnostics%s_%s_%s.root"%(sel,year,step),"read")
#print file_
fit_s=file_.Get("fit_s")

if "0b_pho" in sel:
#	print "line 43"
	par1_fitresult = fit_s.floatParsFinal().find("r")
	r=par1_fitresult.getVal()
	r_err=par1_fitresult.getError()
	#par2_fitresult = fit_s.floatParsFinal().find("WGammaSF")
	#WGammaSF=par2_fitresult.getVal()
	#WGammaSF_err=par2_fitresult.getError()
	#par3_fitresult = fit_s.floatParsFinal().find("ZGammaSF")
	#ZGammaSF=par3_fitresult.getVal()
	#ZGammaSF_err=par3_fitresult.getError()

	#print sel, step
	print "QCDTF_%s=%.3f"%(sel,r)
        print "QCDTF_err_%s=%.3f"%(sel,r_err) 
	#print "WGammaSF_%s=%s"%(sel,WGammaSF)
        #print "WGammaSF_err_%s=%s"%(sel,WGammaSF_err)
	#print "ZGammaSF_%s=%s"%(sel,ZGammaSF)
	#print "ZGammaSF_err_%s=%s"%(sel,ZGammaSF_err) 
	print "#########################################################################################"

elif "1b_pho" in sel:
	par1_fitresult = fit_s.floatParsFinal().find("r")
	r=par1_fitresult.getVal()
	r_err=par1_fitresult.getError()

	#print sel, step
	print "QCDTF_%s=%.3f"%(sel,r)
        print "QCDTF_err_%s=%.3f"%(sel,r_err) 
	#print "WGammaSF_%s=1"%(sel)
        #print "WGammaSF_err_%s=0"%(sel)
	#print "ZGammaSF_%s=1"%(sel)
	#print "ZGammaSF_err_%s=0"%(sel) 
	print "#########################################################################################"



else :
	par1_fitresult = fit_s.floatParsFinal().find("r")
        r=par1_fitresult.getVal()
        r_err=par1_fitresult.getError()
        par2_fitresult = fit_s.floatParsFinal().find("wjetSF")
        wjetSF=par2_fitresult.getVal()
        wjetSF_err=par2_fitresult.getError()

        #print sel, step
	print "QCDTF_%s=%.3f"%(sel,r)
        print "QCDTF_err_%s=%.3f"%(sel,r_err) 
	print "WJetsSF_%s=%.3f"%(sel,wjetSF)
        print "WJetsSF_err_%s=%.3f"%(sel,wjetSF_err)
	print "##################################"





