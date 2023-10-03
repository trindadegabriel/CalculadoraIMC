def main():
	while True:
		p = float (input ('Informe o peso (kg):'))
		a = float (input ('Informe a altura (m):'))
		imc = p/(a*a)
		
		if imc < 18.5:
			print ('Resultado: Magreza')
		
		elif imc >= 18.5 and imc <= 24.9:
			print('Resultado: Normal')
			print ('Grau: 0')
		
		elif imc >= 25.0 and imc <= 29.9:
			print ('Resultado: Sobrepeso')
			print( 'Grau: 1')
		
		elif imc >= 30.0 and imc <= 39.9:
			print ('Resultado: Obesidade')
			print ('Grau: 2')
		
		elif imc >= 40.0:
			print ('Resultado: Obesidade grave')
			print ('Grau: 3')




main()