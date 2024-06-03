import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "25163484"))
    API_HASH = os.environ.get("API_HASH", "145bcbc424d1c1ffe04f3e607ea55c9a")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7034951863:AAEM1IPG7KxGd0atadlY1zZ6MWot-2tJGok")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6302921275")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://File2Link:File2Link@cluster0.ygj9iuu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQF_9twAn3IkKSfdf-abvpPj0KRCkc8Ly5XmhmZeD8eE6QxUbUFM5Ze5Fbc4i2-2cswkgkKiKe7rsuiTs2czaN62d_Asqs1DDMkyoih5nL01INOmSPMrH5tU_4r20LNX5xpx24d4nbLHUQAN8mlP7wOBdX7y-SGmYB597oZq4-m6yBf7clCAmAw2fv6-adh_smwkUcGbJsNg1idcmU1i5HUtjSSha2R17aPC2YRmCLVQKt8-xkC1zIlM0TV7brMmgpOUI-QcXsUhlguAAPA5J2UYYrdr03gha2ZH4SjzZLH2tWYl5vBf0rdR5RHgC8aPme-mcYkmJaC8IQ7Kmg95qOgYj4ZSHgAAAAF3rvI7AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002087386412"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Dbcixv_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
