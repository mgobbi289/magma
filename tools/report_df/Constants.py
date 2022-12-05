# Indices for fuzzing campaign DF
INDEX_F = 'Fuzzer'
INDEX_T = 'Target'
INDEX_P = 'Program'
INDEX_C = 'Campaign'
INDEX_M = 'Metric'
INDEX_B = 'BugID'

INDEX_NAMES = [ INDEX_F,
                INDEX_T,
                INDEX_P,
                INDEX_C,
                INDEX_M,
                INDEX_B,
              ]

GROUP_FTP  = [ INDEX_F, INDEX_T, INDEX_P ]
GROUP_FTB  = [ INDEX_F, INDEX_T, INDEX_B ]
GROUP_FTPB = [ INDEX_F, INDEX_T, INDEX_P, INDEX_B ]
GROUP_FTCB = [ INDEX_F, INDEX_T, INDEX_C, INDEX_B ]

# Time constants used for plotting
TIME_M = 60
TIME_H = 60 * TIME_M
TIME_D = 24 * TIME_H
TIME_W =  7 * TIME_D
TIME_T = 30 * TIME_D

# Time used to run the fuzzing campaigns (in seconds)
DEFAULT_DURATION = TIME_W
# Number of fuzzing campaigns run per program
DEFAULT_TRIALS = 10