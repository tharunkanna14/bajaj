payload={'Name': 'Tharun Kanna R','Email': 'tk5114@srmist.edu.in','College':'SRMIST','StudentId':'RA1811008020020','FileName':'bj.py','Password':'UnZ0bC4yMDAx'}
r= requests.put('https://prod-24.centralindia.logic.azure.com/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM',json=payload)
print(r.text)
