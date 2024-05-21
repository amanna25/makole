print('HOW MANY KILOMETER DID YOU CYCLR TODAY ?')

kms = input() #Get User Input

miles = float(kms)/1.660934 #Convertinf from string tp float and divide

miles = round(miles, 2) #Round Result 

print(f'Your {kms}km Ride Was {miles}M1')