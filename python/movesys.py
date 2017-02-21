from shutil import copyfile

systypes={
          'mur':'_MUR',
          'muf':'_MUF',
          'murmuf':'_MURMUF',
          'jec':'_JEC',
          'jer':'_JER',
          'pu':'_PU',
          'btag':'_BAK4SF',
          # 'subjetbtag':'_BAK8SF',
#          'ttbar':'_TTBAR',
          'toptag':'_TSF',
          'wtag':'_WSF',
           'pdf':'_PDF',
          'mean':''
          }

sides={'UP':'plus','DOWN':'minus'}

names=[
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_RH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_RH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_RH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1500Nar_LH',
# 'MC.MC_TpTp_M-1000',
# 'MC.MC_TpTp_M-1100',
# 'MC.MC_TpTp_M-1200',
# 'MC.MC_TpTp_M-1300',
# 'MC.MC_TpTp_M-1400',
# 'MC.MC_TpTp_M-1500',
# 'MC.MC_TpTp_M-1600',
# 'MC.MC_TpTp_M-1700',
# 'MC.MC_TpTp_M-1800',
# 'MC.MC_TpTp_M-700',
# 'MC.MC_TpTp_M-800',
# 'MC.MC_TpTp_M-900',
'MC.SingleT_sChannel',
'MC.SingleT_tChannel',
'MC.SingleT_WAntitop',
'MC.SingleT_WTop',

'MC.QCD_HT500to700','MC.QCD_HT700to1000','MC.QCD_HT1000to1500','MC.QCD_HT1500to2000','MC.QCD_HT2000toInf',
'MC.TTbar']#,'DATA.JetHT_Run2015D_05Oct2015_v1','DATA.JetHT_Run2015D_PromptReco_v4']

for sys in systypes:
  for side in sides:
    if side=='DOWN' and (sys=='mean' or sys=='pdf'):
      continue
    for name in names:
      copyfile('/nfs/dust/cms/user/usaiem/sys/Sys'+systypes[sys]+side+'/uhh2.AnalysisModuleRunner.'+name+systypes[sys]+side+'_0.root','/nfs/dust/cms/user/usaiem/sys/uhh2.AnalysisModuleRunner.'+name+systypes[sys]+side+'.root')
