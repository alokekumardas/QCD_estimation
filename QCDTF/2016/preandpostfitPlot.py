from ROOT import *
import math
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
                     help="Specify which selection? tight,tight0b,loosecRe3e0,looseCRe3g1,loosecRe2e0,looseCRe2g1" )

parser.add_option("-r", "--pre", dest="fit_op", default="",type='str',
                     help="Specify prefit or postfit" )

(options, args) = parser.parse_args()

channel=options.channel
year=options.Year
step=options.step
sel=options.sel
fit_op=options.fit_op
gROOT.SetBatch(True)
if channel=="ele":
        Chan="Ele"
elif channel=="mu":
        Chan="Mu"

#from feb6_First_Ita_2017 import *
#from feb6_Second_Ita_2017 import *
#from Feb26_2nd_Ita_2016 import *
from March12_second_Ita_2016 import *

if sel=="tight":
#	QCDTF_Ele=QCDTF_Ele_4jet1b
#        WJetsSF_Ele=WJetsSF_Ele_4jet1b  
#
#        QCDTF_Ele_pho=QCDTF_Ele_4jet1b_pho
#        WGammaSF_Ele=WGammaSF_Ele_4jet1b_pho
#        ZGammaSF_Ele=ZGammaSF_Ele_4jet1b_pho
#
#        QCDTF_Mu=QCDTF_Mu_4jet1b
#        WJetsSF_Mu=WJetsSF_Mu_4jet1b
#
#        QCDTF_Mu_pho=QCDTF_Mu_4jet1b_pho
#        WGammaSF_Mu=WGammaSF_Mu_4jet1b_pho
#        ZGammaSF_Mu=ZGammaSF_Mu_4jet1b_pho

	QCDTF_Ele=QCDTF_Ele_2jet1b
        WJetsSF_Ele=WJetsSF_Ele_2jet1b  

        #QCDTF_Ele_pho=QCDTF_Ele_2jet1b_pho
        QCDTF_Ele_pho=QCDTF_Ele_2jet1b
       # WGammaSF_Ele=WGammaSF_Ele_2jet1b_pho
       # ZGammaSF_Ele=ZGammaSF_Ele_2jet1b_pho

        QCDTF_Mu=QCDTF_Mu_2jet1b
        WJetsSF_Mu=WJetsSF_Mu_2jet1b

        QCDTF_Mu_pho=QCDTF_Mu_2jet1b
        #QCDTF_Mu_pho=QCDTF_Mu_2jet1b_pho
       # WGammaSF_Mu=WGammaSF_Mu_2jet1b_pho
       # ZGammaSF_Mu=ZGammaSF_Mu_2jet1b_pho


if sel=="tight0b":
        '''QCDTF_Ele=QCDTF_Ele_4jet0b
        WJetsSF_Ele=WJetsSF_Ele_4jet0b  

        QCDTF_Ele_pho=QCDTF_Ele_4jet0b_pho
        WGammaSF_Ele=WGammaSF_Ele_4jet0b_pho
        ZGammaSF_Ele=ZGammaSF_Ele_4jet0b_pho

        QCDTF_Mu=QCDTF_Mu_4jet0b
        WJetsSF_Mu=WJetsSF_Mu_4jet0b

        QCDTF_Mu_pho=QCDTF_Mu_4jet0b_pho
        WGammaSF_Mu=WGammaSF_Mu_4jet0b_pho
        ZGammaSF_Mu=ZGammaSF_Mu_4jet0b_pho
        '''
	QCDTF_Ele=QCDTF_Ele_2jet0b
        WJetsSF_Ele=WJetsSF_Ele_2jet0b  

        QCDTF_Ele_pho=QCDTF_Ele_2jet0b
        #QCDTF_Ele_pho=QCDTF_Ele_2jet0b_pho
       # WGammaSF_Ele=WGammaSF_Ele_2jet0b_pho
       # ZGammaSF_Ele=ZGammaSF_Ele_2jet0b_pho

        QCDTF_Mu=QCDTF_Mu_2jet0b
        WJetsSF_Mu=WJetsSF_Mu_2jet0b

        QCDTF_Mu_pho=QCDTF_Mu_2jet0b
        #QCDTF_Mu_pho=QCDTF_Mu_2jet0b_pho
       # WGammaSF_Mu=WGammaSF_Mu_2jet0b_pho
       # ZGammaSF_Mu=ZGammaSF_Mu_2jet0b_pho
if sel=="looseCRe3e0":
	QCDTF_Ele=QCDTF_Ele_2jet0b
        WJetsSF_Ele=WJetsSF_Ele_2jet0b  

        #QCDTF_Ele_pho=QCDTF_Ele_2jet0b_pho
        QCDTF_Ele_pho=QCDTF_Ele_2jet0b
       # WGammaSF_Ele=WGammaSF_Ele_3jet0b_pho
       # ZGammaSF_Ele=ZGammaSF_Ele_3jet0b_pho

        QCDTF_Mu=QCDTF_Mu_2jet0b
        WJetsSF_Mu=WJetsSF_Mu_2jet0b

        QCDTF_Mu_pho=QCDTF_Mu_2jet0b
        #QCDTF_Mu_pho=QCDTF_Mu_2jet0b_pho
       # WGammaSF_Mu=WGammaSF_Mu_3jet0b_pho
        #ZGammaSF_Mu=ZGammaSF_Mu_3jet0b_pho

if sel=="looseCRe3g1":
	QCDTF_Ele=QCDTF_Ele_2jet1b
        WJetsSF_Ele=WJetsSF_Ele_2jet1b  

        #QCDTF_Ele_pho=QCDTF_Ele_2jet1b_pho
        QCDTF_Ele_pho=QCDTF_Ele_2jet1b
       # WGammaSF_Ele=WGammaSF_Ele_3jet1b_pho
       # ZGammaSF_Ele=ZGammaSF_Ele_3jet1b_pho

        QCDTF_Mu=QCDTF_Mu_2jet1b
        WJetsSF_Mu=WJetsSF_Mu_2jet1b

        QCDTF_Mu_pho=QCDTF_Mu_2jet1b
        #QCDTF_Mu_pho=QCDTF_Mu_2jet1b_pho
       # WGammaSF_Mu=WGammaSF_Mu_3jet1b_pho
       # ZGammaSF_Mu=ZGammaSF_Mu_3jet1b_pho

if sel=="looseCRe2e0":
	QCDTF_Ele=QCDTF_Ele_2jet0b
        WJetsSF_Ele=WJetsSF_Ele_2jet0b  

        QCDTF_Ele_pho=QCDTF_Ele_2jet0b
        #QCDTF_Ele_pho=QCDTF_Ele_2jet0b_pho
       # WGammaSF_Ele=WGammaSF_Ele_2jet0b_pho
       # ZGammaSF_Ele=ZGammaSF_Ele_2jet0b_pho

        QCDTF_Mu=QCDTF_Mu_2jet0b
        WJetsSF_Mu=WJetsSF_Mu_2jet0b

        QCDTF_Mu_pho=QCDTF_Mu_2jet0b
        #QCDTF_Mu_pho=QCDTF_Mu_2jet0b_pho
       # WGammaSF_Mu=WGammaSF_Mu_2jet0b_pho
       # ZGammaSF_Mu=ZGammaSF_Mu_2jet0b_pho

if sel=="looseCRe2g1":
	QCDTF_Ele=QCDTF_Ele_2jet1b
        WJetsSF_Ele=WJetsSF_Ele_2jet1b  

        QCDTF_Ele_pho=QCDTF_Ele_2jet1b
        #QCDTF_Ele_pho=QCDTF_Ele_2jet1b_pho
       # WGammaSF_Ele=WGammaSF_Ele_2jet1b_pho
       # ZGammaSF_Ele=ZGammaSF_Ele_2jet1b_pho

        QCDTF_Mu=QCDTF_Mu_2jet1b
        WJetsSF_Mu=WJetsSF_Mu_2jet1b

        QCDTF_Mu_pho=QCDTF_Mu_2jet1b
        #QCDTF_Mu_pho=QCDTF_Mu_2jet1b_pho
       # WGammaSF_Mu=WGammaSF_Mu_2jet1b_pho
       # ZGammaSF_Mu=ZGammaSF_Mu_2jet1b_pho


W=800
H=800

canvas = TCanvas('c2','c2',W,H)

canvas.cd()
#f1= TFile("TF_%s_%s_%s_%s_rebin.root"%(channel,year,step,sel),"READ")
f1= TFile("TF_%s_%s_%s_%s_fullMET.root"%(channel,year,step,sel),"READ")
#f1= TFile("TF_mu_2018__looseCRe2e0_rebin.root","READ")
f1.Print()
Presel_data=f1.Get("presel_WtransMass_Data%s"%(Chan))
Presel_allbkg=f1.Get("presel_WtransMass_TTGamma")
Presel_QCD_DD=f1.Get("presel_WtransMass_QCD_DD")
Presel_wjets=f1.Get("presel_WtransMass_WJets")
Presel_wjets.Print()

Presel_data.SetMarkerStyle(9)
Presel_allbkg.SetLineColor(kYellow)
Presel_allbkg.SetFillColor(kYellow)
Presel_QCD_DD.SetLineColor(kGreen)
Presel_QCD_DD.SetFillColor(kGreen)
Presel_wjets.SetLineColor(kBlue)
Presel_wjets.SetFillColor(kBlue)


#Phosel_data=f1.Get("phosel_WtransMass_Data%s"%(Chan))
#Phosel_allbkg=f1.Get("phosel_WtransMass_TTGamma")
#Phosel_QCD_DD=f1.Get("phosel_WtransMass_QCD_DD")
#Phosel_wgamma=f1.Get("phosel_WtransMass_WGamma")
#Phosel_zgamma=f1.Get("phosel_WtransMass_ZGamma")


#Phosel_data.SetMarkerStyle(9)
#Phosel_allbkg.SetLineColor(kYellow)
#Phosel_allbkg.SetFillColor(kYellow)
#Phosel_QCD_DD.SetLineColor(kGreen)
#Phosel_QCD_DD.SetFillColor(kGreen)
#Phosel_wgamma.SetLineColor(kBlue)
#Phosel_wgamma.SetFillColor(kBlue)
#Phosel_zgamma.SetLineColor(kBlue+1)
#Phosel_zgamma.SetFillColor(kBlue+1)

histname="presel"
#histname={"presel","phosel"}




# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W


legendHeightPer = 0.04

legendStart = 0.69
legendEnd = 0.97-(R/W)


#prelegend = TLegend(2*legendStart - legendEnd, 1-T/H-0.01 - legendHeightPer*(5), legendEnd, 0.99-(T/H)-0.01)
#pholegend = TLegend(2*legendStart - legendEnd, 1-T/H-0.01 - legendHeightPer*(6), legendEnd, 0.99-(T/H)-0.01)
prelegend=TLegend(0.7,0.75,0.9,0.9)
pholegend=TLegend(0.7,0.75,0.9,0.9)

prelegend.AddEntry(Presel_data,"data",'pe')
prelegend.AddEntry(Presel_QCD_DD,"QCD_DD",'f')
prelegend.AddEntry(Presel_wjets,"WJets",'f')
prelegend.AddEntry(Presel_allbkg,"All_oth_bkg",'f')

#pholegend.AddEntry(Phosel_data,"data",'pe')
#pholegend.AddEntry(Phosel_QCD_DD,"QCD_DD",'f')
#pholegend.AddEntry(Phosel_wgamma,"WGamma",'f')
#pholegend.AddEntry(Phosel_zgamma,"ZGamma",'f')
#pholegend.AddEntry(Phosel_allbkg,"All_oth_bkg",'f')

prelegend.SetBorderSize(0)
prelegend.SetFillColor(0)
#pholegend.SetBorderSize(0)
#pholegend.SetFillColor(0)

_textsel = TPaveText(0.5,.865,0.6,0.9,"NDC")
_textsel.AddText("%s,%s,%s"%(year,channel,sel))
_textsel.SetTextColor(kBlack)
_textsel.SetFillColor(0)
_textsel.SetTextSize(0.03)
_textsel.SetTextFont(42)


_text = TPaveText(0.5,.815,0.6,0.85,"NDC")
_text.SetTextColor(kBlack)
_text.SetFillColor(0)
_text.SetTextSize(0.03)
_text.SetTextFont(42)

_text2 = TPaveText(0.5,.785,0.6,0.815,"NDC")
_text2.SetTextColor(kBlack)
_text2.SetFillColor(0)
_text2.SetTextSize(0.03)
_text2.SetTextFont(42)

_text4 = TPaveText(0.5,.815,0.6,0.85,"NDC")
_text4.SetTextColor(kBlack)
_text4.SetFillColor(0)
_text4.SetTextSize(0.03)
_text4.SetTextFont(42)

_text5 = TPaveText(0.5,.785,0.6,0.815,"NDC")
_text5.SetTextColor(kBlack)
_text5.SetFillColor(0)
_text5.SetTextSize(0.03)
_text5.SetTextFont(42)

_text3 = TPaveText(0.5,.755,0.6,0.785,"NDC")
_text3.SetTextColor(kBlack)
_text3.SetFillColor(0)
_text3.SetTextSize(0.03)
_text3.SetTextFont(42)

_text6 = TPaveText(0.5,.725,0.6,0.755,"NDC")
_text6.SetTextColor(kBlack)
_text6.SetFillColor(0)
_text6.SetTextSize(0.03)
_text6.SetTextFont(42)

_text7 = TPaveText(0.5,.725,0.6,0.755,"NDC")
_text7.SetTextColor(kBlack)
_text7.SetFillColor(0)
_text7.SetTextSize(0.03)
_text7.SetTextFont(42)

Rtext=""
Rtext2=""
Rtext3=""

hist="presel"

#for hist in histname:
if hist == histname:
   canvas.cd()
   gStyle.SetOptStat(0)
   if "presel" in hist:
	if fit_op=="postfit":
		if channel=="ele":
			Presel_QCD_DD.Scale(QCDTF_Ele)
			Rtext="QCDSF=%.3f"%QCDTF_Ele
			Presel_wjets.Scale(WJetsSF_Ele)
			Rtext2="WJetSF=%.3f"%WJetsSF_Ele
		if channel=="mu":
			Presel_QCD_DD.Scale(QCDTF_Mu)
			Rtext="QCDSF=%.3f"%QCDTF_Mu
			Presel_wjets.Scale(WJetsSF_Mu)
			Rtext2="WJetSF=%.3f"%WJetsSF_Mu


	stack = THStack("presel_WtransMass","presel_WtransMass")

	stack.Add(Presel_allbkg)
	stack.Add(Presel_QCD_DD)
	stack.Add(Presel_wjets)
        stack.GetStack().Last().GetXaxis().SetTitle("Wtrans Mass")

	stack.Draw("hist")
	Presel_data.Draw("e,p,same")
	prelegend.Draw()
        _textsel.Draw("same")
	_text.AddText(Rtext)
        _text.Draw("same")
	_text2.AddText(Rtext2)
        _text2.Draw("same")
	#if fit_op=="postfit" and ( ("tight" in sel) or ("CRe3" in sel) ):
	if fit_op=="postfit" :
  		rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")
 		x = Presel_data.Chi2Test(rebinnedMC,"UW CHI2/NDF") 
		chi2Text = "#Chi^{2}/NDF=%.2f"%x
                _text6.AddText(chi2Text)
		_text6.Draw("same")

	if fit_op=="postfit":
		if not os.path.exists("postfit_plot"):
			os.mkdir("postfit_plot")
		if not os.path.exists("postfit_plot/%s"%channel):
			os.mkdir("postfit_plot/%s"%channel)
		canvas.SaveAs("postfit_plot/%s/PostFit_presel_%s_%s.pdf"%(channel,sel,step))
	elif fit_op=="prefit":
		if not os.path.exists("prefit_plot"):
			os.mkdir("prefit_plot")
		if not os.path.exists("prefit_plot/%s"%channel):
			os.mkdir("prefit_plot/%s"%channel)
		canvas.SaveAs("prefit_plot/%s/PreFit_presel_%s_%s.pdf"%(channel,sel,step))

  # canvas.Update()
  # if "phosel" in hist:
#	if fit_op=="postfit":
#		if channel=="ele":
#			Phosel_QCD_DD.Scale(QCDTF_Ele_pho)
#			Rtext="QCDSF=%.3f"%QCDTF_Ele_pho
		#	Phosel_wgamma.Scale(WGammaSF_Ele)
		#	Rtext2="WgammaSF=%.3f"%WGammaSF_Ele
		#	Phosel_zgamma.Scale(ZGammaSF_Ele)
		#	Rtext3="zgammaSF=%.3f"%ZGammaSF_Ele
#		if channel=="mu":
#			Phosel_QCD_DD.Scale(QCDTF_Mu_pho)
#			Rtext="QCDSF=%.3f"%QCDTF_Mu_pho
		#	Phosel_wgamma.Scale(WGammaSF_Mu)
		#	Rtext2="WgammaSF=%.3f"%WGammaSF_Mu
		#	Phosel_zgamma.Scale(ZGammaSF_Mu)
		#	Rtext3="ZgammaSF=%.3f"%ZGammaSF_Mu
		

#	stack = THStack("phosel_WtransMass","phosel_WtransMass")
#
#	stack.Add(Phosel_QCD_DD)
#	stack.Add(Phosel_wgamma)
#	stack.Add(Phosel_zgamma)
#	stack.Add(Phosel_allbkg)
 #       stack.GetStack().Last().GetXaxis().SetTitle("Wtrans Mass")

    #    if stack.GetStack().Last().GetMaximum() > (Phosel_data.GetMaximum() + math.sqrt(Phosel_data.GetMaximum())) :
 #	     stack.Draw("hist")
  #           Phosel_data.Draw("ep same")
#	else :
#             Phosel_data.Draw("ep")
 #	     stack.Draw("hist same")
 #	stack.Draw("hist")
  #      Phosel_data.Draw("ep same")
#
#	pholegend.Draw()
 #       _textsel.Draw("same")
#	_text4.AddText(Rtext)
 #       _text4.Draw("same")
	#_text5.AddText(Rtext2)
        #_text5.Draw("same")
#	_text3.AddText(Rtext3)
 #       _text3.Draw("same")
#	if fit_op=="postfit" and ( ("tight" in sel) or ("CRe3" in sel) ):
 ## 		rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")
 #		x = Phosel_data.Chi2Test(rebinnedMC,"UW CHI2/NDF") 
#		chi2Text = "#Chi^{2}/NDF=%.2f"%x
 #               _text7.AddText(chi2Text)
#		_text7.Draw("same")

#	if fit_op=="postfit":
#		if not os.path.exists("postfit_plot"):
#			os.mkdir("postfit_plot")
#		if not os.path.exists("postfit_plot/%s"%channel):
#			os.mkdir("postfit_plot/%s"%channel)
#		canvas.SaveAs("postfit_plot/%s/PostFit_phosel_%s.pdf"%(channel,sel))
#	elif fit_op=="prefit":
#		if not os.path.exists("prefit_plot"):
#			os.mkdir("prefit_plot")
#		if not os.path.exists("prefit_plot/%s"%channel):
#			os.mkdir("prefit_plot/%s"%channel)
#		canvas.SaveAs("prefit_plot/%s/PreFit_phosel_%s.pdf"%(channel,sel))
#
