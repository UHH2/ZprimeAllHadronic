import ROOT
from ROOT import TFile,TCanvas,gROOT,kFALSE
from ROOT.TH1 import kPoisson
import math

def sum_square(lista):
	s=0.0
	for i in lista:
		s=s+i*i
	return math.sqrt(s)

gROOT.SetBatch()

systypes_ttbar=[
		'btag',
		'jec',
		'jer',
		'mu',
		'pdf',
		'pu',
		'toptag',
		'wtag'
          ]

systypes_rate=[
		[0.023,'lumi'],[0.03,'trig']#,[0.15,'norm']
		]

systypes_rate2=[
		[0.028,'norm']
		]

systypes_top=[
		'btag',
		'jec',
		'jer',
		'mu',
		'pu',
		'toptag',
		'wtag'
          ]

systypes_qcd=[
		'bkgcorr',
		'bkgfit'
          ]

procs_with_rates=['ttbar','singletop']
procs_with_rates2=['qcd']
#procs_with_binomial=['DATA']



cats=['allhad1btag','allhad2btag']
sides=['plus','minus']
uu='__'
procs={'ttbar':systypes_ttbar,'singletop':systypes_top,'qcd':systypes_qcd,'DATA':[]}

infile = TFile('theta/theta_66_1p0_0p0_0p0.root','READ')
data_tmp=infile.Get(cats[0]+uu+'DATA').Clone()
blow=data_tmp.GetXaxis().FindFixBin(0.0)
bhigh=data_tmp.GetXaxis().FindFixBin(3500.0)

results={}

for cat in cats:
	results[cat]={}
	for proc in procs:
		up=[]
		down=[]
		mean_h=infile.Get(cat+uu+proc).Clone()
		#mean_h.Sumw2(kFALSE)
  		#mean_h.SetBinErrorOption(kPoisson)
  		e_stat=ROOT.Double(0.0)
		mean=mean_h.IntegralAndError(blow,bhigh,e_stat)
		up.append([e_stat,'stat'])
		down.append([e_stat,'stat'])
		if proc in procs_with_rates:
			for rate in systypes_rate:
				e_rate=mean*rate[0]
				up.append([e_rate,rate[1]])
				down.append([e_rate,rate[1]])

		if proc in procs_with_rates2:
			for rate in systypes_rate2:
				e_rate=mean*rate[0]
				up.append([e_rate,rate[1]])
				down.append([e_rate,rate[1]])

		print cat,proc,mean
		for sys in procs[proc]:
			e_sys=[]
			for side in sides:
				#print cat+uu+proc+uu+sys+uu+side
				sys_h=infile.Get(cat+uu+proc+uu+sys+uu+side).Clone()
				int_sys=sys_h.Integral(blow,bhigh)
				e_sys.append(int_sys-mean)
			if e_sys[0]*e_sys[1]<0.0:
				if e_sys[0]>0.0:
					up.append([abs(e_sys[0]),sys])
					down.append([abs(e_sys[1]),sys])
				else:
					down.append([abs(e_sys[0]),sys])
					up.append([abs(e_sys[1]),sys])
			elif e_sys[0]*e_sys[1]>0.0:
				if e_sys[0]>0:
					up.append([max(abs(e_sys[0]),abs(e_sys[1])),sys])
				else:
					down.append([max(abs(e_sys[0]),abs(e_sys[1])),sys])
			else:
				assert(False)
		#print 'up',up
		#print 'down',down
		e_up=0.0
		e_down=0.0
		for i in up:
			e_up=e_up+i[0]*i[0]
		for i in down:
			e_down=e_down+i[0]*i[0]
		e_up=math.sqrt(e_up)
		e_down=math.sqrt(e_down)
		#print e_up,e_down
		results[cat][proc]={'up':e_up,'down':e_down,'mean':mean}
print results

print "\hline"
print "Multijet QCD & $%.0f^{+%.0f}_{-%.0f}$ & $%.0f^{+%.0f}_{-%.0f}$\\\\" % (
	results['allhad1btag']['qcd']['mean'],results['allhad1btag']['qcd']['up'],results['allhad1btag']['qcd']['down'],
	results['allhad2btag']['qcd']['mean'],results['allhad2btag']['qcd']['up'],results['allhad2btag']['qcd']['down'])
print "SM top & $%.0f^{+%.0f}_{-%.0f}$ & $%.0f^{+%.0f}_{-%.0f}$\\\\" % (
	results['allhad1btag']['ttbar']['mean']+results['allhad1btag']['singletop']['mean'],
	sum_square([results['allhad1btag']['ttbar']['up'],results['allhad1btag']['singletop']['up']]),
	sum_square([results['allhad1btag']['ttbar']['down'],results['allhad1btag']['singletop']['down']]),
	results['allhad2btag']['ttbar']['mean']+results['allhad2btag']['singletop']['mean'],
	sum_square([results['allhad2btag']['ttbar']['up'],results['allhad2btag']['singletop']['up']]),
	sum_square([results['allhad2btag']['ttbar']['down'],results['allhad2btag']['singletop']['down']]),
	)
print "\hline"
print "Total background & $%.0f^{+%.0f}_{-%.0f}$ & $%.0f^{+%.0f}_{-%.0f}$\\\\" % (
	results['allhad1btag']['ttbar']['mean']+results['allhad1btag']['singletop']['mean']+results['allhad1btag']['qcd']['mean'],
	sum_square([results['allhad1btag']['ttbar']['up'],results['allhad1btag']['singletop']['up'],results['allhad1btag']['qcd']['up']]),
	sum_square([results['allhad1btag']['ttbar']['down'],results['allhad1btag']['singletop']['down'],results['allhad1btag']['qcd']['down']]),
	results['allhad2btag']['ttbar']['mean']+results['allhad2btag']['singletop']['mean']+results['allhad2btag']['qcd']['mean'],
	sum_square([results['allhad2btag']['ttbar']['up'],results['allhad2btag']['singletop']['up'],results['allhad2btag']['qcd']['up']]),
	sum_square([results['allhad2btag']['ttbar']['down'],results['allhad2btag']['singletop']['down'],results['allhad2btag']['qcd']['down']]),
	)
print 'DATA & %.0f & %.0f' % (results['allhad1btag']['DATA']['mean'],results['allhad2btag']['DATA']['mean'])

