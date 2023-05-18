Algoritmo MRUA
	//AREA de descripción
	//programa que calcule ejercicios de movimiento rectilineo uniforme acelerado
	//desarrollado por: Daniel Giraldo y Laura Castaño
	//version 1.0
	//fecha: 13/03/23
	
	//area declaracion de variables
	Definir v_eje Como entero
	Definir v_velIni Como Real
	Definir v_velFin Como Real
	Definir v_velMed Como Real
	Definir v_aceleracion Como Real
	Definir  v_tiempo Como Real
	Definir v_distancia Como Real
	definir v_kilMHor Como Real
	definir v_metSeg Como Real
	

	
	//area de inicialización de variable
	v_eje = 0
	v_velIni = 0.0
	v_velFin = 0.0
	v_velMed = 0.0
	v_aceleracion  = 0.0
	v_tiempo = 0.0
	v_distancia = 0.0
	v_kilMHor = 0.0
	v_metSeg = 0.0

	
	//area de entrada de datos 
	Escribir "************************"
	Escribir "MENU DE OPCIONES DE MRUA"
	Escribir "************************"
	Escribir "1.Velocidad final"
	Escribir "2.Velocidad media"
	Escribir "3.Aceleración"
	Escribir "4.Distancia"
	Escribir "5.Conversion de Km/h a m/s"
	Escribir "6.Salir"
	Escribir "ELIJE UN OPCIÓN"
	Leer v_eje
	
	Si v_eje = 1 Entonces
		Escribir "Digite la velocidad inicial: "; leer v_velIni
		Escribir "Digite la aceleracion: "; leer v_aceleracion
		Escribir "Digite el tiempo"; leer v_tiempo
		v_velFin = v_velIni + v_aceleracion * v_tiempo
		Escribir "La velocidad final es ",v_velFin," m/s^2"
	FinSi
	
	Si v_eje = 2 Entonces
		Escribir "Digite la velocidad inicial: "; leer v_velIni
		Escribir "Digite la velocidad final: "; leer v_velFin
		v_velMed = (v_velFin + v_velIni) / 2
		Escribir "La velocidad media es ",v_velMed," m/s"
	FinSi
	
	Si v_eje = 3 Entonces
		Escribir "Digite la velocidad inicial: "; leer v_velIni
		Escribir "Digite la velocidad final: "; leer v_velFin
		Escribir "Digite el tiempo"; leer v_tiempo
		v_aceleracion = (v_velFin - v_velIni) / v_tiempo
		Escribir "La aceleración es ",v_aceleracion," m/s^2"
	FinSi
	si v_eje = 4 Entonces
		Escribir "Digite la velocidad inicial: "; leer v_velIni
		Escribir "Digite la velocidad final: "; leer v_velFin
		Escribir "Digite el tiempo"; leer v_tiempo
		v_distancia= (v_velFin + v_velIni ) / 2  * v_tiempo
		Escribir "la distancia es ",v_distancia, "m"
	FinSi
	
	Si v_eje = 5 Entonces
		Escribir "Digite los Km/h: "; leer v_kilMHor
		v_metSeg = v_kilMHor * 1000 * (1/3600)
		Escribir "La conversión de Km/h a m/s es: ", v_metSeg, " m/s"
	FinSi
FinAlgoritmo
