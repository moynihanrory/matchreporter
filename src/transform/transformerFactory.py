from gaaMatchTransformer import GaaMatchTransformer

def getTransformerForImportSource(source):
    if (source == 1):
        transformer = GaaMatchTransformer()
        return transformer
    else:
        return None
