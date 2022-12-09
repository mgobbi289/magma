# Features for fuzzing campaign DF
FUZZER   = 'Fuzzer'
TARGET   = 'Target'
PROGRAM  = 'Program'
CAMPAIGN = 'Campaign'
METRIC   = 'Metric'
BUG_ID   = 'BugID'
TIME     = 'Time'

# Common lists of features
ALL_FEATs = [ FUZZER,
              TARGET,
              PROGRAM,
              CAMPAIGN,
              METRIC,
              BUG_ID,
            ]

FEATs_FT   = [ FUZZER, TARGET ]
FEATs_FTP  = [ FUZZER, TARGET, PROGRAM ]
FEATs_FTB  = [ FUZZER, TARGET, BUG_ID ]
FEATs_FTPB = [ FUZZER, TARGET, PROGRAM, BUG_ID ]
FEATs_FTCB = [ FUZZER, TARGET, CAMPAIGN, BUG_ID ]
