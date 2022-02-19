# pasaport = input('Are pasaportul valid : DA/NU ')
# age = int(input(" Introduceti varsta"))
# if  pasaport == "DA":
#      if age >=18:
#            print('permite calatoria')
#      elif age<18:
#         ambii_parinti = input('Are ambii parinti? DA/NU ')
#         if ambii_parinti == 'DA':
#             print('Permite calatoria')
#         else:
#             permisiune = input('Are permisiune? DA/NU')
#             if permisiune == 'DA':
#                  print("permite calatoria")
#             else:
#                 print("Nu permite calatoria")
# else:
#     print('Nu permite calatoria');

#9.Citeste o litera de la tastatura. Verifica si afiseaza daca este vocala sau nu

litere = input('introduceti o litera: ')

if (litere=='a' or 'A' or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U'):
    print("E vocala")
else:
    print("E consoana")

