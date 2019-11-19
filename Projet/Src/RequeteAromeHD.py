import os
import os.path
import sys
import datetime
import time
import requests

class ProblemeMeteoFrance(Exception):
	pass

def DateDuPlusRecentRun():
	InstantPresent=datetime.datetime.utcnow()
	InstantChoisi=datetime.datetime( InstantPresent.year, InstantPresent.month, InstantPresent.day, InstantPresent.hour, 0, 0, 0)
	# ON CONSIDERE QUE LE PLUS RECENT RUN DISPONIBLE EST CELUI LANCE AU MOINS 6H AVANT LA DATE ACTUELLE
	InstantPrecedent = InstantChoisi - datetime.timedelta(hours=6)

	if (InstantPrecedent.hour>18):
		InstantRequete=datetime.datetime( InstantPrecedent.year, InstantPrecedent.month, InstantPrecedent.day, 18, 0, 0, 0)
	elif (InstantPrecedent.hour>12):
		InstantRequete=datetime.datetime( InstantPrecedent.year, InstantPrecedent.month, InstantPrecedent.day, 12, 0, 0, 0)
	elif (InstantPrecedent.hour>6):
		InstantRequete=datetime.datetime( InstantPrecedent.year, InstantPrecedent.month, InstantPrecedent.day, 6, 0, 0, 0)
	elif (InstantPrecedent.hour>3):
		InstantRequete=datetime.datetime( InstantPrecedent.year, InstantPrecedent.month, InstantPrecedent.day, 3, 0, 0, 0)
	else:
		InstantRequete=datetime.datetime( InstantPrecedent.year, InstantPrecedent.month, InstantPrecedent.day, 0, 0, 0, 0)

	return InstantRequete

# FIN DE DateDuPlusRecentRun

def RequetePrevisionPourUnDeltaEnHeure( NomPackage, DeltaEnHeure):

	DateDuRun = DateDuPlusRecentRun();

	# INSTANT PRESENT
	InstantPresent=datetime.datetime.utcnow() 
	# HEURE CORRESPONDANTE (ON MET LES MINUTES ET SECONDES A ZERO)
	InstantChoisi=datetime.datetime( InstantPresent.year, InstantPresent.month, InstantPresent.day, InstantPresent.hour, 0, 0, 0)

	# INTERVALLE ENTRE L HEURE ACTUELLE ET LE PLUS RECENT RUN DISPONIBLE
	IntervalleEntreLeRunEtLePresent = InstantChoisi - DateDuRun

	# ON RAJOUTE LE DeltaEnHeure SPECIFIE EN ARGUMENT
	IntervalleEntreLeRunEtLaPrevisionVoulue = IntervalleEntreLeRunEtLePresent + datetime.timedelta( hours=DeltaEnHeure)

	# ON VERIFIE QUE LA PREVISION EST DISPONIBLE
	if (IntervalleEntreLeRunEtLaPrevisionVoulue > datetime.timedelta(hours=42)):
		sys.stderr.write("prevision trop lointaine, on reduit a 42h\n")
		IntervalleEntreLeRunEtLaPrevisionVoulue = datetime.timedelta(hours=42)

	# CONVERSION DE CETTE INTERVALLE A UNE CHAINE DE 3 CARACTERES DONT 2 POUR LE NOMBRE D HEURES ET "H"
	IntervalleEnHeure = str(int(IntervalleEntreLeRunEtLaPrevisionVoulue.total_seconds()/3600)).zfill(2) + "H"

	Package = NomPackage

#	Package = "SP1" # 40 Mo
# SP1 : U(10m), V(10m), U_RAF(10m), V_RAF (10m), T(2m), HU (2m)
#	Package = "SP2" # 62 Mo
# SP2 : EAU, NEIGE, GRAUPEL, P(sol), NEBBAS, NEBHAU, NEBMOY, CAPE_INS, RFLCTVT_MAX (sol)
#	Package = "SP3" # 14 Mo
# SP3 : ALTITUDE(champ constant), TERRE_MER (champ constant), BT (niveaux canaux 108)
#	Package = "HP1" # 62 Mo
# HP1 : HU, U, V ur 4 niveaux (20, 50 et 100 m)


#	BaseRequete = "http://dcpc-nwp.meteo.fr/services/PS_GetCache_DCPCPreviNum?token=__5yLVTdr-sGeHoPitnFc7TZ6MhBcJxuSsoZp6y0leVHU__&model=AROME&grid=0.01&format=grib2"
	BaseRequete = "http://dcpc-nwp.meteo.fr/services/PS_GetCache_DCPCPreviNum?token=__5yLVTdr-sGeHoPitnFc7TZ6MhBcJxuSsoZp6y0leVHU__&model=AROME&grid=0.01&grid2=0.01&format=grib2"
	Requete = BaseRequete + "&package=" + Package + "&time=" + IntervalleEnHeure + "&referencetime=" + DateDuRun.isoformat() + "Z"

	return [DateDuRun, IntervalleEntreLeRunEtLaPrevisionVoulue, DateDuRun+IntervalleEntreLeRunEtLaPrevisionVoulue, Requete]
# FIN DE RequetePrevisionPourUnDeltaEnHeure

# CODE POUR SAUVER LES DONNEES RETOURNEES PAR LA REQUETE VERS UN FICHIER BINAIRE
def SauveLeFichierDUneRequeteMeteoFrance( Requete, NomDuFichier):
	
	try:
		RawData = requests.get( Requete, stream=True)
		RawData.raise_for_status()

		Taille = 0
		with open(NomDuFichier, 'wb') as fd:
#			for chunk in RawData:
			for chunk in RawData.iter_content(128):
				Taille = Taille + 128
				TailleLisible = (int) (Taille/1024)
				sys.stderr.write(str(TailleLisible) + "kb\r")
				sys.stderr.flush()
				fd.write(chunk)

		sys.stderr.write(str(TailleLisible) + "kb\n")
		sys.stderr.flush()

	except requests.exceptions.Timeout:
		sys.stderr.write("Le serveur de meteo france ne repond plus\n");
		raise ProblemeMeteoFrance
	except requests.ConnectionError as err:
		sys.stderr.write("Le serveur de meteo france a retourne une erreur de connection\n");
		raise ProblemeMeteoFrance
	except requests.exceptions.HTTPError as err:
		sys.stderr.write("La requete vers le serveur meteo france a ete mal formee\n");
		raise ProblemeMeteoFrance

# FIN DE SauveLeFichierDUneRequeteMeteoFrance
#==============================================================================================
if __name__ == "__main__":

# ARGUMENT 1 = NBRE D'HEURE A PARTIR DU MOMENT OU LA COMMANDE EST EXECUTEE
# ARGUMENT 2 = NOM DU PACKAGE METEOFRANCE A TELECHARGER (SP1, SP2, SP3, HP1)
	if (len(sys.argv) != 3):
		print("MAUVAIX NOMBRE D'ARGUMENTS. IL FAUT DONNER UN INTERVALLE EN HEURE ET UN TYPE DE PACKAGE (SP1, SP2, SP3, HP1)")
		sys.exit(1)

	if not (sys.argv[2] in ["SP1", "SP2", "SP3", "HP1"]):
		print("LE TYPE DE PACKAGE (SECOND ARGUMENT) DOIT ETRE SP1, SP2, SP3 OU HP1")
		sys.exit(1)

	[DateDuRun, IntervalleEnHeure, DateDeLaPrevision, Requete] = RequetePrevisionPourUnDeltaEnHeure( sys.argv[2], int(sys.argv[1]))
	
	NomDuFichier="AromeHD_" + sys.argv[2] + "_DateRun_"+ DateDuRun.isoformat() + "_DatePrev_"+ DateDeLaPrevision.isoformat() + ".grib2"

	print(NomDuFichier)

	if os.path.isfile("./DATA/" + NomDuFichier):
		sys.stderr.write("LE FICHIER EXISTE DEJA - JE NE RETELECHARGE PAS LES DONNEES\n")
		sys.stderr.flush()
		sys.exit(0);
	else:
		try:
			SauveLeFichierDUneRequeteMeteoFrance( Requete, NomDuFichier);
		except ProblemeMeteoFrance:
			sys.stderr.write("il y a eu un probleme lors du telechargement du fichier");
			sys.stderr.write("\n");
			sys.exit(1);

#========================== fin de main ============================


