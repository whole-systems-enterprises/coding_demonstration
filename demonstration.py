
#######################################################################################
#   Live coding demonstration for Illumina candidacy. Emily Williams, 22 April 2019   #
#######################################################################################

#
# import system libraries
#
# I don't know what I need yet, so just setting up my standard kit:
#
import pprint as pp
import numpy as np
import pandas as pd

#
# user settings
#
input_file = 'data/SQAHuman01_S1.vcf'
output_directory = 'output'
format_content_column_name = 'Human1'

#
# iterate through the lines
#
f = open(input_file)
unique_gqx_codes = {}
for index, line in enumerate(f):
    line = line.strip()
    
    if line[0:2] == '##':
        continue

    if line.find('#CHROM') == 0:
        header = line.split('\t')
        format_index = header.index('FORMAT')
        format_content_index = header.index(format_content_column_name)
    else:
        line = line.split('\t')
        formats = line[format_index]
        formats_split = formats.split(':')
        contents = line[format_content_index]
        contents_split = contents.split(':')
        if 'GQX' in formats_split:
            gqx_index = formats_split.index('GQX')
            gqx_content = int(contents_split[gqx_index])
            unique_gqx_codes[gqx_content] = None

pp.pprint(unique_gqx_codes)


    



