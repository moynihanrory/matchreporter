
from pymongo import MongoClient
from constants import MDB_USERNAME, MDB_PASSWORD, MDB_DATABASE_NAME, MDB_MLAB_URL, MDB_ORIGINAL_DOC_NAME, \
    MDB_CLEANED_DOC_NAME, MDB_CLEANED_DATA_CONTENTS_COLUMN_NAME, MDB_SPORTSCODE_DOC_NAME, MDB_TRANSFORMED_DATA_NAME, \
    MDB_TRANSFORM_MAPPING_NAME, MDB_TRANSFORM_TABLENAME_TEMPLATE
from jsonBuilder import createImportDoc, createCleanedDocFromImport, getImportedTextById, \
    createSportsCodeDoc, createTransformedDataDoc, createTransformMappingDoc
from stringBuilder import createTablename

def connectClient():
    client = MongoClient(MDB_MLAB_URL, username=MDB_USERNAME, password=MDB_PASSWORD, authSource=MDB_DATABASE_NAME)

    db = client.analysis

    return db


def insert(collectionName, doc):
    db = connectClient()

    return db[collectionName].insert(doc)


def storeGaaMatchImportAndCleanedData(original, cleaned):
    result = insert(MDB_ORIGINAL_DOC_NAME, createImportDoc(original))

    if result is not None:
        return insert(MDB_CLEANED_DOC_NAME, createCleanedDocFromImport(result, cleaned))


def storeGaaMatchImportData(original):
    return insert(MDB_ORIGINAL_DOC_NAME, createImportDoc(original))


def storeGaaMatchCleanedData(cleaned):
    return insert(MDB_CLEANED_DOC_NAME, createCleanedDocFromImport(cleaned))


def storeSportsCodeXml(xml):
    return insert(MDB_SPORTSCODE_DOC_NAME, createSportsCodeDoc(xml['file']['ALL_INSTANCES']['instance']))


def storeTransformedData(name, transformed):
    return insert(name, createTransformedDataDoc(transformed))


def storeKpiMapping(parent, mapping, name):
    return insert(MDB_TRANSFORM_MAPPING_NAME, createTransformMappingDoc(parent, mapping, name))


def storeMappingAndTransform(cleanedDataOid, transformedData, mapping):
    name = createTablename(MDB_TRANSFORM_TABLENAME_TEMPLATE)

    result = storeTransformedData(name, transformedData)

    if result is not None:
        storeKpiMapping(cleanedDataOid, mapping, name)

def getCleanedDataById(id):
    db = connectClient()

    query = getImportedTextById(id)

    queryResult = db.cleanedData.find_one(query)

    return queryResult[MDB_CLEANED_DATA_CONTENTS_COLUMN_NAME]


def getTransformedDataById(id):
    db = connectClient()

    query = getTransformedDataById(id)

    queryResult = db.cleanedData.find_one(query)

    return queryResult[MDB_CLEANED_DATA_CONTENTS_COLUMN_NAME]