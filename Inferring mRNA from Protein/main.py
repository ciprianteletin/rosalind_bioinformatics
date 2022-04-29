protein_to_possible_rna_dict = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3,
                                'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}
number_of_stop_codons = 3

aa_sequence = 'MKHATWLEKHNNFAPHDDDHINAQCNCEWPIKPYMSFFTSKACKQRVDYVRCYHLGHQECAPFRMEDKTTWAKGGFNMKDELFWWHMFIEQMSCFGANSIDIGAIMNYVLCWEHRITSWLFHDYFRSRHCKPVHQRDWDNCKPSAPDAQFLWVRSEQMGIANIYWATGFANGHEMPMIVRLFCLYCKPFIHDKTGTNEMQMTIRVMIWTHQKLGCQEFMFDSGSQACAEMARKMIRGCDVEWFYTFVFQIDRTGFYTDHNVETWMIIASAKNEFPEPVPLYTKSRQNMDWGASPTFDCAAGFEHTGIVDLIAMDVLQYFFMCDFHCKCEDARDIWRGFKNHWSCQTCQCPFCEQRCWNTHWVSSMCQQSVPTPKMWYACCMAKVWNPVLWYMDVSGPCFYLLWHSHNTGNEVMYMNGYSSEIINMGQRSSKNCWDYMHVFRDGGDELFNVLHVNEDMDELFKGTASWETEMHPRIHLTTMIIVAFIFSFKPSLRTDKLQAICDEYMSVYLVPMNPIQHFGKVAFWVRETCKKDILDAGLRSGVSMGHWDCAGTYWCVNDKLYHGYADMKDRKEVTPFHCSGFPGVVKCTKMVRRVEVNGEDCMPGQSPQLTMWLYHNSEIECHGHKEPCTSSYVPLNIIWSKQDSGRSVDRCRKHWMRDSRKSPHGRLARQRAECCQMTDTIIRWEGSQWMKLDKIMDIFLSSCEQINARAMIECCAMTPAHKMIPKRKPDKFPNEPCMPYMYSFEWLAFVHTDVPFFDGQPMGSPEDCSWPNTYCFNQYWVQQPHIFTAEIWIIMPPEIYMQHMGYMDWCWGSHMPMERWQCVNNTGKRTSVCYWRYLYYWQPTKVWKHHIFLNQQGFEACGWLDYWTKCTHAKEHWIDAKFEMCCHSGPFSWEYNMRERQWMTQAQRCINKWKPCQKGYERMGFNGAHQWYWCPFWSRWETHKERNSFRQYYDYIVDCCSFIISMNDEEHMVVKKEITFRGNCNDFVDDHHDTPWFED'

# Assuming input is provided properly
possibility_amount = 1
for aa in aa_sequence:
    possibility_amount = (possibility_amount * protein_to_possible_rna_dict[aa]) % 1E6

# Number of stop codons is taken into account.
possibility_amount = possibility_amount * number_of_stop_codons

print(possibility_amount)
