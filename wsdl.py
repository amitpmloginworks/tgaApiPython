from zeep import Client
from zeep.wsse.username import UsernameToken
client = Client('https://ws.staging.training.gov.au/Deewr.Tga.WebServices/OrganisationServiceV7.svc?wsdl', wsse=UsernameToken('WebService.Read', 'Asdf098'))
print(client.service.GetServerTime())
print(client.service.Search('Mobigo'))
