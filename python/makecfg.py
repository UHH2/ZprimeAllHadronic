from sys import argv
from subprocess import check_output
#run with python makecfg.py /nfs/dust/cms/user/usaiem/gc-output/PHYS14v0/signals4/ newzp selector
selector=''
if len(argv)>3:
	selector=argv[3]
#l=check_output(['ls','-1',argv[1]]).split('\n')[:-1]
l=check_output(['ls','-lh',argv[1]]).split('\n')[:-1]
f=open(argv[2],'w')
for i in l:
	if 'Ntuple' in i and selector in i and not '7.4K' in i:
		f.write('<In FileName="'+argv[1]+'/'+i.split(' ')[-1]+'" Lumi="0.0"/>\n')
f.close()