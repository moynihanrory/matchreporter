CMDLINE_IMPORT_UNKNOWN_OPTION = 0
CMDLINE_IMPORT_GAAMATCHTEXT_OPTION = 1
CMDLINE_IMPORT_SPORTSCODE_OPTION = 2

def getSourceFromArgs(args):
    if args.importFile and args.xml:
        # error 1 args
        return CMDLINE_IMPORT_UNKNOWN_OPTION
    elif args.importFile and not args.xml: # if file then read it and clean it
        return CMDLINE_IMPORT_GAAMATCHTEXT_OPTION
    elif args.xml and not args.importFile:  # if sportscode xml
        return CMDLINE_IMPORT_SPORTSCODE_OPTION