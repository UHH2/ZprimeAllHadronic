from sys import argv
from subprocess import check_output
selector=''
if len(argv)>3:
	selector=argv[3]
l=check_output(['ls','-1',argv[1]]).split('\n')[:-1]
f=open(argv[2],'w')
for i in l:
	if 'Ntuple' in i and selector in i:
		f.write('<In FileName="'+argv[1]+'/'+i+'" Lumi="0.0"/>\n')
f.close()