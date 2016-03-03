systypes={'mur':'_MUR',
          'muf':'_MUF',
          'jec':'_JEC',
          'jer':'_JER',
          'pu':'_PU',
          'btag':'_BAK4SF',
          'subjetbtag':'_BAK8SF',
          'ttbar':'_TTBAR',
          'toptag':'_TSF',
          'wtag':'_WSF',
          'pdf':'_PDF',
          }
systype_list=['mur','muf','jec','jer','pu','btag','subjetbtag','ttbar','toptag','wtag','pdf']
model=open('../config/Model.xml','r')
for systype in systype_list:
	for side in ['UP','DOWN']:
		model=open('../config/Model.xml','r')
		sysconfig=open('../config/'+'Sys'+systypes[systype]+side+'.xml','w')
		for line in model:
			newline=line
			if '@@@' in line:
				newline=line.replace('@@@',systypes[systype]+side)
			elif systype=='jec' and '$$$JEC' in line:
				newline=line.replace('nominal',side.lower())
			elif systype=='jer' and '$$$JER' in line:
				newline=line.replace('nominal',side.lower())
			elif systype=='mur' and '$$$MUR' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='muf' and '$$$MUF' in line:
				newline=line.replace('mean',side.lower())
			sysconfig.write(newline)
		model.close()
		sysconfig.close()