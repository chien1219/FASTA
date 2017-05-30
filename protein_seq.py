with open("Seq_Multiple.txt","r") as f:
    
    seq = ""
    seq_list = []
    context = []
    counter = -1
    
    for line in f:
        
        if line[0]=='>':
            context.append(line[line.find('[')+1:line.find(']')])
            
            if seq!="":
                seq_list.append(seq)
            seq = ""
            
        else:
            seq += line
            seq = seq.strip()
           
    seq_list.append(seq)   
    
    #print(context)
    #print(seq_list)
    #ACDEFGHIKLMNPQRSTVWY
    
    output=open('Multiple.xls','w')
    output.write('\tA\tC\tD\tE\tF\tG\tH\tI\tK\tL\tM\tN\tP\tQ\tR\tS\tT\tV\tW\tY\n')
    
    
    for i in range(0,len(seq_list)):
        output.write(context[i])
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('A'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('C'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('D'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('E'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('F'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('G'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('H'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('I'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('K'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('L'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('M'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('N'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('P'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('Q'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('R'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('S'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('T'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('V'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('W'))/float(len(seq_list[i]))))
        output.write('\t')
        output.write("%.2f" % (float(seq_list[i].count('Y'))/float(len(seq_list[i]))))
        output.write('\n')
