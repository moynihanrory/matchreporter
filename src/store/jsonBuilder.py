from bson import ObjectId
from stringBuilder import createImportTxtFilename, createSource
import json

def createImportDoc(data):
    return {"filename": createImportTxtFilename(), "source": createSource(), "contents": data}

def createCleanedDocFromImport(original, data):
    return {"originalDataOid": original, "type": createSource(), "contents": data}

def createSportsCodeDoc(data):
    return {"id": 123, "type": "SportsCode XML", "contents": data}

def getImportedTextById(originalOid):
    return {'originalDataOid':ObjectId(originalOid)}

def createTransformedDataDoc(df):
    data = json.dumps(df.to_dict('records'))
    return {"df": data}

def createTransformMappingDoc(parent, data, name):
    return {'originalDataOid': ObjectId(parent), "contents": data, "transformStorageLocation": name}

def getTransformedDataById(id):
    return {'_id': ObjectId(id)}
