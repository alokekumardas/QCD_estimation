from ROOT import *
import os
import numpy as numpy
from array import *
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

#from nabin's result
WJetsSF=1
ZJetsSF=1.22
WGammaSF=1
ZGammaSF=1
MisIDEleSF=1

if year=="2016":
        MisIDEleSF=2.132
        WGammaSF=1.191
        ZGammaSF=0.984
if year=="2017":
        MisIDEleSF=2.386
        WGammaSF=1.402
        ZGammaSF=1.097
if year=="2018":
        MisIDEleSF=1.453
        WGammaSF=1.574
        ZGammaSF=0.943

#DataF1 = TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/Data%s.root"%(year,channel,sel,Chan),"READ")
#TTGammaF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/TTGamma.root"%(year,channel,sel),"READ")
#DibosonF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/Diboson.root"%(year,channel,sel),"READ")
#TGJetsF1 = TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/TGJets.root"%(year,channel,sel),"READ")
#TTVF1 = TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/TTV.root"%(year,channel,sel),"READ")
#TTbarF1 = TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/TTbar.root"%(year,channel,sel),"READ")
#WGammaF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/WGamma.root"%(year,channel,sel),"READ")
#WJetsF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/WJets.root"%(year,channel,sel),"READ")
#ZGammaF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/ZGamma.root"%(year,channel,sel),"RAED")
#ZJetsF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/ZJets.root"%(year,channel,sel),"READ")
#SingleTopF1 =  TFile.Open("root://cmseos.fnal.gov//store/user/aldas/histograms_%s/%s/hists_%s/SingleTop.root"%(year,channel,sel),"READ")

DataF1 = TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/Data%s.root"%(year,channel,sel,Chan),"READ")
TTGammaF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/TTGamma.root"%(year,channel,sel),"READ")
DibosonF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/Diboson.root"%(year,channel,sel),"READ")
TGJetsF1 = TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/TGJets.root"%(year,channel,sel),"READ")
TTVF1 = TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/TTV.root"%(year,channel,sel),"READ")
TTbarF1 = TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/TTbar.root"%(year,channel,sel),"READ")
WGammaF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/WGamma.root"%(year,channel,sel),"READ")
WJetsF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/WJets.root"%(year,channel,sel),"READ")
ZGammaF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/ZGamma.root"%(year,channel,sel),"RAED")
ZJetsF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/ZJets.root"%(year,channel,sel),"READ")
SingleTopF1 =  TFile.Open("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s/SingleTop.root"%(year,channel,sel),"READ")

QCDsel=""


#QCD_DDF1 = TFile("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s_%s/QCD_DD.root"%(year,channel,step,sel),"READ")
QCD_DDF1 = TFile("/uscms_data/d3/aldas/2017Analysis_v1/CMSSW_10_2_4/src/NanoAod/TTGammaSemiLep_13TeV/Plotting/histograms_%s/%s/hists_%s_%s/QCD_DD.root"%(year,channel,step,sel),"READ")

print QCD_DDF1

#f1= TFile("%s/TF_%s_%s_%s_%s_rebin.root"%(year,channel,year,step,sel),"RECREATE")
f1= TFile("%s/TF_%s_%s_%s_%s_fullMET.root"%(year,channel,year,step,sel),"RECREATE")

###################################################################################################
data= DataF1.Get("presel_WtransMass_Data%s"%Chan)
TTGammaF1.Print()
mc1 = TTGammaF1.Get("presel_WtransMass_TTGamma")
TTbar    =TTbarF1.Get("presel_WtransMass_TTbar")
Diboson  = DibosonF1.Get("presel_WtransMass_Diboson")
TGJets   = TGJetsF1.Get("presel_WtransMass_TGJets")
TTV      = TTVF1.Get("presel_WtransMass_TTV")
WGamma   = WGammaF1.Get("presel_WtransMass_WGamma")
ZGamma   = ZGammaF1.Get("presel_WtransMass_ZGamma")
ZJets   = ZJetsF1.Get("presel_WtransMass_ZJets")
SingleTop   = SingleTopF1.Get("presel_WtransMass_SingleTop")


mc1.Add(TTbar)
mc1.Add(Diboson)
mc1.Add(TGJets)
mc1.Add(TTV)

WGamma.Scale(WGammaSF)
ZGamma.Scale(ZGammaSF)
mc1.Add(WGamma)
mc1.Add(ZGamma)

ZJets.Scale(ZJetsSF)
mc1.Add(ZJets) 

mc1.Add(SingleTop)

WJets   = WJetsF1.Get("presel_WtransMass_WJets")
WJets.Scale(WJetsSF)

QCD_DD   = QCD_DDF1.Get("presel_WtransMass_QCD_DD")

mc1.SetTitle("all_NonQCD_bkg")

binning  = numpy.arange(0.0,155.0,5)
#binning  = numpy.arange(0.0,105.0,5)
#binning = array('d',[0.0,5.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,62.5,65.0,67.5,70.0,72.5,75.0,77.5,80.0,85.0,90.0,95.0,100.0,105.0])
print binning
print len(binning)-1
data.Print()

rebinnedData = data.Rebin(len(binning)-1,"",binning)
rebinnedData.Write()

rebinnedmc1 = mc1.Rebin(len(binning)-1,"",binning)
rebinnedmc1.Write()

rebinnedQCD_DD=QCD_DD.Rebin(len(binning)-1,"",binning)
rebinnedQCD_DD.Write()

rebinnedWJets=WJets.Rebin(len(binning)-1,"",binning)
rebinnedWJets.Write()


