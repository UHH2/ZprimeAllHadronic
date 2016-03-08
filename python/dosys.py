systypes={'mur':'_MUR',
          'muf':'_MUF',
          'murmuf':'_MURMUF',
          'jec':'_JEC',
          'jer':'_JER',
          'pu':'_PU',
          'btag':'_BAK4SF',
          'subjetbtag':'_BAK8SF',
          'ttbar':'_TTBAR',
          'toptag':'_TSF',
          'wtag':'_WSF',
          'pdf':'_PDF',
          'mean':''
          }
# systype_list=['mean','mur','muf','jec','jer','pu','btag','subjetbtag','ttbar','toptag','wtag','pdf']
model=open('../config/Model.xml','r')
for systype in systypes:
	for side in ['UP','DOWN']:
		model=open('../config/Model.xml','r')
		sysconfig=open('../config/'+'Sys'+systypes[systype]+side+'.xml','w')
		for line in model:
			newline=line
			if '@@@' in line:
				newline=line.replace('@@@',systypes[systype]+side)
			elif systype=='jec' and 'jecsmear_direction' in line:
				newline=line.replace('nominal',side.lower())
			elif systype=='jer' and 'jersmear_direction' in line:
				newline=line.replace('nominal',side.lower())
			elif systype=='mur' and 'ScaleVariationMuR' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='muf' and 'ScaleVariationMuF' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='murmuf' and 'ScaleVariationMuF' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='murmuf' and 'ScaleVariationMuR' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='btag' and 'btagging_sys' in line:
				newline=line.replace('central',side.lower())
			elif systype=='subjetbtag' and 'subjetbtag_sys' in line:
				newline=line.replace('central',side.lower())
			elif systype=='pu' and 'pileup_sys' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='ttbar' and 'ttbar_sys' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='toptag' and 'toptag_sys' in line:
				newline=line.replace('mean',side.lower())
			elif systype=='wtag' and 'wtag_sys' in line:
				newline=line.replace('mean',side.lower())


			sysconfig.write(newline)
		model.close()
		sysconfig.close()