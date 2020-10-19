from ROOT import TH1F, TFile, TChain, TCanvas, gROOT
import sys

from sampleInformation import sampleList
import sampleInformation
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="Mu",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )
parser.add_option("-s", "--sample", dest="sample", default="",type='str',
                     help="Specify which sample to run on" )
parser.add_option("--lev", "--level", dest="level", default="",type='str',
                     help="Specify up/down of systematic")
parser.add_option("--syst", "--systematic", dest="systematic", default="",type='str',
                     help="Specify which systematic to run on")
parser.add_option("--Tight","--tight", dest="isTightSelection", default=False,action="store_true",
                     help="Use 4j1t selection" )
parser.add_option("--VeryTight","--verytight", dest="isVeryTightSelection", default=False,action="store_true",
                     help="Use 4j2t selection" )
parser.add_option("--Tight0b","--tight0b", dest="isTightSelection0b", default=False,action="store_true",
                     help="Use 4j0t selection" )
##nabin

parser.add_option("--makeNabinPlots", dest="makeNabinPlots",action="store_true",default=False,
                     help="Make larger list of plots in histogramDict (mostly object kinematics)" )
###
parser.add_option("--LooseCRge2ge0","--looseCRge2ge0", dest="isLooseCRge2ge0Selection", default=False,action="store_true",
                     help="Use >=2 jets + >=0 bjets selection" )

parser.add_option("--LooseCRge2e0","--looseCRge2e0", dest="isLooseCRge2e0Selection", default=False,action="store_true",
                     help="Use >=2 jets + =0 bjets selection" )

## today
parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="isLooseCRe2e0Selection", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )

parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="isLooseCRe2e1Selection", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" )

parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="isLooseCRe3e0Selection", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" )

parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="isLooseCRge4e0Selection", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" )
## 3 more
parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="isLooseCRe3e1Selection", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" )

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="isLooseCRe2e2Selection", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" )

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="isLooseCRe3ge2Selection", default=False,action="store_true",
                     help="Use ==3 jets + >=2 bjets selection" )

parser.add_option("--dilepmassPlots","--dilepmassPlots", dest="Dilepmass",action="store_true",default=False,
                     help="Make only plots for ZJetsSF fits" )

parser.add_option("--makePlotsForSF","--makePlotsForSF", dest="makePlotsForSF",action="store_true",default=False,
                     help="Extra jets" )
### nabin
parser.add_option("--LooseCR2e1","--looseCR2e1", dest="isLooseCR2e1Selection",default=False,action="store_true",
                  help="Use 2j exactly 1t control region selection" )
parser.add_option("--LooseCRe2g1","--looseCRe2g1", dest="isLooseCRe2g1Selection",default=False,action="store_true",
                  help="Use exactly 2j >= 1t control region selection" )
parser.add_option("--LooseCR3g0","--looseCR3g0", dest="isLooseCR3g0Selection",default=False,action="store_true",
                  help="Use >=3j and 0btag control region selection" )
parser.add_option("--LooseCR2g1","--looseCR2g1", dest="isLooseCR2g1Selection",default=False,action="store_true",
                  help="Use 2j at least 1t control region selection")
parser.add_option("--LooseCRe3g1","--looseCRe3g1", dest="isLooseCRe3g1Selection",default=False,action="store_true",
                  help="Use exactly 3j >= 1t control region selection" )
parser.add_option("--addPlots","--addOnly", dest="onlyAddPlots", default=False,action="store_true",
                     help="Use only if you want to add a couple of plots to the file, does not remove other plots" )
parser.add_option("--output", dest="outputFileName", default="hists",
                     help="Give the name of the root file for histograms to be saved in (default is hists.root)" )
parser.add_option("--plot", dest="plotList",action="append",
                     help="Add plots" )
parser.add_option("--multiPlots", "--multiplots", dest="multiPlotList",action="append",
                     help="Add plots" )
parser.add_option("--testone", "--testoneplot", dest="testoneplot",action="store_true",default=False,
                     help="test one plot without replacing it in the original one" )
parser.add_option("--allPlots","--AllPlots", dest="makeAllPlots",action="store_true",default=False,
                     help="Make full list of plots in histogramDict" )
parser.add_option("--morePlots","--MorePlots","--makeMorePlots", dest="makeMorePlots",action="store_true",default=False,
                     help="Make larger list of plots in histogramDict (mostly object kinematics)" )
parser.add_option("--EgammaPlots","--EgammaPlots", dest="makeEGammaPlots",action="store_true",default=False,
                     help="Make only plots for e-gamma mass fits" )
parser.add_option("--dRPlots","--dRPlots", dest="makedRPlots",action="store_true",default=False,
                     help="Make only plots for dR" )
parser.add_option("--genPlots","--genPlots", dest="makegenPlots",action="store_true",default=False,
                     help="Make only plots for 2D histograms" )
parser.add_option("--preselPlots","--preselPlots", dest="preselPlots",action="store_true",default=False,
                     help="Make only plots presel" )
parser.add_option("--phoselPlots","--phoselPlots", dest="phoselPlots",action="store_true",default=False,
                     help="Make only plots phosel" )
parser.add_option("--jetsonly","--jetsonly", dest="makeJetsplots",action="store_true",default=False,
                     help="Extra jets" )

parser.add_option("--quiet", "-q", dest="quiet",default=False,action="store_true",
                     help="Quiet outputs" )
parser.add_option("--fwdjets","--fwdjets", dest="FwdJets",action="store_true",default=False,
                     help="include fwd jets" )

parser.add_option("-y", "--year", dest="Year", default="",type='str',
                     help="Specify which year 2016, 2017 or 2018?" )





(options, args) = parser.parse_args()

level =options.level
syst = options.systematic
if syst=="":
        runsystematic = False
else:
        runsystematic = True



gROOT.SetBatch(True)

selYear = options.Year
if selYear=="":
        print "Specify which year 2016, 2017 or 2018?"
        sys.exit()

samples = sampleInformation.main([selYear])

Dilepmass=options.Dilepmass
finalState = options.channel
sample = options.sample
testoneplot=options.testoneplot
isVeryTightSelection=options.isVeryTightSelection
isTightSelection = options.isTightSelection
isTightSelection0b = options.isTightSelection0b
## nabin
makeNabinPlots = options.makeNabinPlots
##
isLooseCRge2ge0Selection = options.isLooseCRge2ge0Selection
isLooseCRge2e0Selection  = options.isLooseCRge2e0Selection

##
isLooseCRe2e0Selection   = options.isLooseCRe2e0Selection
isLooseCRe2e1Selection   = options.isLooseCRe2e1Selection
isLooseCRe3e0Selection   = options.isLooseCRe3e0Selection
isLooseCRge4e0Selection  = options.isLooseCRge4e0Selection
## 3more today
isLooseCRe3e1Selection   = options.isLooseCRe3e1Selection
isLooseCRe2e2Selection   = options.isLooseCRe2e2Selection
isLooseCRe3ge2Selection  = options.isLooseCRe3ge2Selection

makePlotsForSF = options.makePlotsForSF
## nabin
isLooseCR2e1Selection = options.isLooseCR2e1Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCR3g0Selection=options.isLooseCR3g0Selection
isLooseCRe2g1Selection = options.isLooseCRe2g1Selection
isLooseCRe3g1Selection = options.isLooseCRe3g1Selection

onlyAddPlots = options.onlyAddPlots
outputFileName = options.outputFileName
FwdJets=options.FwdJets
makedRPlots=options.makedRPlots
makeAllPlots = options.makeAllPlots
makeMorePlots = options.makeMorePlots
makeEGammaPlots = options.makeEGammaPlots
makeJetsplots = options.makeJetsplots

makegenPlots=options.makegenPlots
runQuiet = options.quiet
phosel_plot=options.phoselPlots
presel_plot=options.preselPlots

#from nov14_first_Ita_2016 import *
#from nov14_first_Ita_2017 import *
#from nov14_first_Ita_2018 import *

#from nov14_Second_Ita_2016 import *
#from nov14_Second_Ita_2017 import *
#from nov14_Second_Ita_2018 import *

#from nov25_First_Ita_2016 import *
#from nov25_Second_Ita_2016 import *
#from nov26_First_Ita_2016 import *
#from nov26_Second_Ita_2016 import *
#from nov26_Third_Ita_2016 import *
#from nov27_First_Ita_2016 import *

#from nov27_Second_Ita_2016 import *
#from nov27_Third_Ita_2016 import *
#from Dec3_First_Ita_2017 import *
#from Dec3_Second_Ita_2017 import *
#from dec3_First_Ita_2018 import *
#from dec3_Second_Ita_2018 import *

#from Zero_photon_2016 import *
#from Zero_photon_2017 import *
#from Zero_photon_2018 import *
#from jan_5_First_Ita_2016 import *
#from jan_5_Second_Ita_2016 import *
#from jan13_Ita_2017_fullMET_zeropho import *
#from jan13_Ita_2018_fullMET_zeropho import *
#from feb6_First_Ita_2017 import *

#from Feb19_first_Ita_2016 import *
#from Feb19_first_Ita_2017 import *
#from Feb19_first_Ita_2018 import *
#from Feb26_First_Ita_2016 import *
#from March12_first_Ita_2016 import *
#from March12_first_Ita_2017 import *
from March12_first_Ita_2016 import *

WJetsSF=1
ZJetsSF=1.22
WGammaSF=1
ZGammaSF=1
if selYear=="2016":
	misIdEleSF=2.132
	WGammaSF=1.191
	ZGammaSF=0.984
if selYear=="2017":
	misIdEleSF=2.386
	WGammaSF=1.402
	ZGammaSF=1.097
if selYear=="2018":
	misIdEleSF=1.453
	WGammaSF=1.574
	ZGammaSF=0.943



inputdir="qcdhistsCR"
#outputdir="hists_ita1"
#outputdir="hists_ita2"
#outputdir="hists_ita2_test"
#outputdir="hists_ita3"
#outputdir="hists_ita3_test"
outputdir="hists_ita4"

noSF=""
applylow="yes"
if outputdir=="hists_ita1" :
   noSF="yes"
if outputdir=="hists_ita4" :
   applylow="yes"

if finalState=="Ele":
	dir="histograms_%s/ele/"%(selYear)
if finalState=="Mu":
	dir="histograms_%s/mu/"%(selYear)


if isTightSelection:
    if not runQuiet: print "Tight Select"
    inputdir = inputdir +"_tight"
    outputdir = outputdir +"_tight"
 #   if finalState=="Mu":
#	WJetsSF=WJetsSF_Mu_4jet1b
 #   if finalState=="Ele":
#	WJetsSF=WJetsSF_Ele_4jet1b
    if applylow=="yes":
    	if finalState=="Mu":
		WJetsSF=WJetsSF_Mu_2jet1b
    	if finalState=="Ele":
		WJetsSF=WJetsSF_Ele_2jet1b

if isVeryTightSelection:
    if not runQuiet: print "Very Tight Select"
    inputdir = inputdir + "_verytight"

if isTightSelection0b:
    if not runQuiet: print "Tight0b Select"
    inputdir = inputdir + "_tight0b"
    outputdir = outputdir +"_tight0b"
 #   if finalState=="Mu":
#	WJetsSF=WJetsSF_Mu_4jet0b
 #   if finalState=="Ele":
#	WJetsSF=WJetsSF_Ele_4jet0b
    if applylow=="yes":
    	if finalState=="Mu":
		WJetsSF=WJetsSF_Mu_2jet0b
    	if finalState=="Ele":
		WJetsSF=WJetsSF_Ele_2jet0b
## start nabin
if isLooseCRge2ge0Selection:
    if not runQuiet: print " Loose CR >=2 jet and >=0 bjet"
    inputdir = inputdir + "_looseCRge2ge0"
    outputdir = outputdir + "_looseCRge2ge0"

if isLooseCRge2e0Selection:
    if not runQuiet: print " Loose CR >=2 jet and =0 bjet"
    inputdir = inputdir + "_looseCRge2e0"
    outputdir = outputdir + "_looseCRge2e0"
    if finalState=="Mu":
	WJetsSF=WJetsSF_Mu_2jet0b
    if finalState=="Ele":
	WJetsSF=WJetsSF_Ele_2jet0b

if isLooseCRe2e0Selection:
    if not runQuiet: print " Loose CR ==2 jet and ==0 bjet"
    inputdir = inputdir + "_looseCRe2e0"
    outputdir = outputdir + "_looseCRe2e0"
    if finalState=="Mu":
	WJetsSF=WJetsSF_Mu_2jet0b
    if finalState=="Ele":
	WJetsSF=WJetsSF_Ele_2jet0b

if isLooseCRe2e1Selection:
    if not runQuiet: print " Loose CR ==2 jet and ==1 bjet"
    inputdir = inputdir + "_looseCRe2e1"
    outputdir = outputdir + "_looseCRe2e1"

if isLooseCRe3e0Selection:
    if not runQuiet: print " Loose CR ==3 jet and ==0 bjet"
    inputdir = inputdir + "_looseCRe3e0"
    outputdir = outputdir + "_looseCRe3e0"
  #  if finalState=="Mu":
#	WJetsSF=WJetsSF_Mu_3jet0b
 #   if finalState=="Ele":
#	WJetsSF=WJetsSF_Ele_3jet0b
    if applylow=="yes":
    	if finalState=="Mu":
		WJetsSF=WJetsSF_Mu_2jet0b
    	if finalState=="Ele":
		WJetsSF=WJetsSF_Ele_2jet0b


if isLooseCRge4e0Selection:
    if not runQuiet: print " Loose CR >=4 jet and ==0 bjet"
    inputdir = inputdir + "_looseCRge4e0"
    outputdir = outputdir + "_looseCRge4e0"

## 3 more
if isLooseCRe3e1Selection:
    if not runQuiet: print " Loose CR ==3 jet and ==1 bjet"
    inputdir = inputdir + "_looseCRe3e1"
    outputdir = outputdir + "_looseCRe3e1"




if isLooseCRe2e2Selection:
    if not runQuiet: print " Loose CR ==2 jet and ==2 bjet"
    inputdir = inputdir + "_looseCRe2e2"
    outputdir = outputdir + "_looseCRe2e2"




if isLooseCRe3ge2Selection:
    if not runQuiet: print " Loose CR >=3 jet and >=2 bjet"
    inputdir = inputdir + "_looseCRe3ge2"
    outputdir = outputdir + "_looseCRe3ge2"



## end nabin 

if isLooseCR2e1Selection:
    if not runQuiet: print "Loose Control Region Select"
    inputdir = inputdir + "_looseCR2e1"
    outputdir = outputdir + "_looseCR2e1"


if isLooseCRe2g1Selection:
    if not runQuiet: print "Loose Control Region1 Select"
    inputdir = inputdir + "_looseCRe2g1"
    outputdir = outputdir + "_looseCRe2g1"
    if finalState=="Mu":
	WJetsSF=WJetsSF_Mu_2jet1b
    if finalState=="Ele":
	WJetsSF=WJetsSF_Ele_2jet1b

                                                                                                                                                                                                                                                                                                                                                           
if isLooseCR3g0Selection:                                                                                                                          
    if not runQuiet: print "Loose Control Region for EGamma"
    inputdir = inputdir + "_looseCRe3g0"
    outputdir = outputdir + "_looseCRe3g0"



if isLooseCRe3g1Selection:
    if not runQuiet: print "Loose Control Region Select"
    inputdir = inputdir + "_looseCRe3g1"
    outputdir = outputdir + "_looseCRe3g1"
 #   if finalState=="Mu":
#	WJetsSF=WJetsSF_Mu_3jet1b
 #   if finalState=="Ele":
#	WJetsSF=WJetsSF_Ele_3jet1b
    if applylow=="yes":
    	if finalState=="Mu":
		WJetsSF=WJetsSF_Mu_2jet1b
    	if finalState=="Ele":
		WJetsSF=WJetsSF_Ele_2jet1b

########################################

#reset if needed

#WJetsSF=1
#WGammaSF=1
#ZGammaSF=1
if noSF=="yes":
	WJetsSF=1


from sampleInformation import *

stackList = sampleList[:-3]



gROOT.SetBatch(True)

#if presel_plot:
#
#	keylist=["presel_WtransMass","presel_WtransMass_METless30","presel_WtransMass_METgreat30","presel_WtransMass_METless30_control", "presel_WtransMass_METgreat30_control"]
#elif phosel_plot:
#	keylist=["phosel_WtransMass","phosel_WtransMass_METless30","phosel_WtransMass_METgreat30"]

#keylist=["presel_WtransMass_control","presel_WtransMass_METless30","presel_WtransMass_METgreat30","presel_WtransMass_METless30_control", "presel_WtransMass_METgreat30_control","phosel_WtransMass","phosel_WtransMass_METless30","phosel_WtransMass_METgreat30"]

#keylist=["presel_WtransMass_METgreat30_control_cut","presel_WtransMass_METgreat30_control_cut","presel_WtransMass_METgreat30_control_cut","phosel_WtransMass_METgreat30_cut"]
#keylist=["presel_WtransMass","presel_WtransMass_METless30","presel_WtransMass_METgreat30","presel_WtransMass_METless30_control","presel_WtransMass_METgreat30_control","phosel_WtransMass","phosel_WtransMass_METless30","phosel_WtransMass_METgreat30"]
#keylist=["presel_Njet","presel_WtransMass","phosel_MassEGamma","phosel_MassEGamma_GenuinePhoton","phosel_MassEGamma_MisIDEle","phosel_MassEGamma_HadronicPhoton","phosel_MassEGamma_HadronicFake","phosel_Njet","phosel_WtransMass","presel_jet1Pt","phosel_jet1Pt","phosel_WtransMass_GenuinePhoton","phosel_WtransMass_MisIDEle","phosel_WtransMass_HadronicPhoton","phosel_WtransMass_HadronicFake","phosel_jet1Pt_GenuinePhoton","phosel_jet1Pt_MisIDEle","phosel_jet1Pt_HadronicPhoton","phosel_jet1Pt_HadronicFake","presel_M3", "phosel_M3","phosel_mediumID_ChIso","presel_WtransMass_control","presel_WtransMass_METless30","presel_WtransMass_METgreat30","presel_WtransMass_METless30_control", "presel_WtransMass_METgreat30_control","phosel_WtransMass_METless30","phosel_WtransMass_METgreat30"]
#keylist=["phosel_M3_GenuinePhoton","phosel_M3_MisIDEle","phosel_M3_HadronicPhoton","phosel_M3_HadronicFake","phosel_mediumID_ChIso_GenuinePhoton","phosel_mediumID_ChIso_MisIDEle","phosel_mediumID_ChIso_HadronicPhoton","phosel_mediumID_ChIso_HadronicFake"]
#keylist=[#"presel_Njet", 
 #          "phosel_MassEGamma",
           #"presel_M3", 
     #      "phosel_M3",
  #         "phosel_mediumID_ChIso","presel_WtransMass","phosel_WtransMass"]
          # "presel_WtransMass","presel_WtransMass_METless30","presel_WtransMass_METgreat30",
	  # "phosel_WtransMass","phosel_WtransMass_METless30","phosel_WtransMass_METgreat30",
	   #"presel_WtransMass_METless20]
           #"phosel_Njet","phosel_WtransMass","presel_jet1Pt","phosel_jet1Pt",
	#	"phosel_WtransMass_METless30_GenuinePhoton","phosel_WtransMass_METless30_MisIDEle","phosel_WtransMass_METless30_HadronicPhoton","phosel_WtransMass_METless30_HadronicFake",
        #   "phosel_WtransMass_METgreat30_GenuinePhoton","phosel_WtransMass_METgreat30_MisIDEle","phosel_WtransMass_METgreat30_HadronicPhoton","phosel_WtransMass_METgreat30_HadronicFake"]
keylist=["phosel_MassEGamma","phosel_M3","phosel_ChIso","phosel_mediumID_ChIso"]
print keylist


_file_data=TFile("%s%s/Data%s.root"%(dir,inputdir,finalState),"read")


#phocatlist=["MisIDEle","GenuinePhoton","HadronicPhoton","HadronicFake"]
phocatlist=["GenuinePhoton","HadronicPhoton","HadronicFake"]

print "data file"
print _file_data
histoList = {}
print stackList
for key in keylist:
    print key
    hName = "%s_QCD_DD"%(key)
    print hName
    histoList[key]= _file_data.Get("%s_%s"%( key,"Data%s"%finalState))
    print "%s_%s"%( key,"Data%s"%finalState)
    print "working"
    print hName
    histoList[key].SetNameTitle(hName,hName)

    for sample in stackList:
        _file=TFile("%s%s/%s.root"%(dir,inputdir,sample),"read")
        print _file
	if ("phosel" in key) :
			tempHist=_file.Get("%s_MisIDEle_%s"%(key,sample))
			temphist.Scale(misIdEleSF)
			for pho in phocatlist:
		   		photemphist=_file.Get("%s_%s_%s"%(key,pho,sample))	
				print "adding pho histogram %s"%(pho)
				tempHist.Add(photemphist)
	else :
       	      tempHist = _file.Get("%s_%s"%(key,sample))
	if sample =="WJets":
		print "WJetsSF = ", WJetsSF
		tempHist.Scale(WJetsSF)
	if sample =="ZJets":
		 tempHist.Scale(ZJetsSF)
	if sample =="WGamma":
		 tempHist.Scale(WGammaSF)
        if sample =="ZGamma":
		 tempHist.Scale(ZGammaSF)
	if key=="presel_DilepMass":continue
	if "endcap" in key:continue
        histoList[key].Add(tempHist,-1)
        _file.Close()

if not os.path.exists("%s%s"%(dir,outputdir)):
    os.makedirs("%s%s"%(dir,outputdir))

#outputFile = TFile("%s%s/QCD_DD.root"%(dir,outputdir),"recreate")
outputFile = TFile("%s%s/QCD_DD.root"%(dir,outputdir),"update")
#outputFile = TFile("test/QCD_DD.root","recreate")
print "output file:"," %s%s/QCD_DD.root"%(dir,outputdir)
for h in histoList:
    print histoList[h]
    histoList[h].Write()

outputFile.Close()

