import phonenumbers

from phonenumbers import geocoder, carrierdata

phone = input('Digite o telefone nop formato +001234567890: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.country_name_for_number(phone_number, 'pt'))
print(geocoder.description_for_number(phone_number, 'pt'))