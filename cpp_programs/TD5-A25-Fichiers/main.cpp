////////////////////////////////////////////////////////////////////////////////
/// VOTRE ENTÊTE ICI
////////////////////////////////////////////////////////////////////////////////


#pragma region "Inclusions" //{

#include <ciso646>
#include <cstddef>
#include <cstdint>

#include <iomanip>
#include <iostream>
#include <string>

#include "CodeDemande.hpp"
#include "CodeFourni.hpp"


using namespace std;

#pragma endregion //}


/**
 * Lit une dimension des morceaux et s'assure qu'elle est valide
 *
 * \param [in] message				Le texte à afficher
 * \param [in] dimensionTotale		La dimension de l'image
 *
 * \return la dimension d'un morceau
 */
int lireDimension(string message, int dimensionTotale) {
	int dimension;
	cout << message <<endl;
	cin >> dimension;
	while(dimensionTotale % dimension) {
		cout << "La taille de l'image, " << dimensionTotale << ", n'est pas divisible par " << dimension << endl;
		cout << message << endl;
		cin >> dimension;
	} 
	return dimension;
}

/**
 * Lit, modifie et écrit une image bitmap dans un fichier
 *
 */
int main ( )
{
	srand(static_cast<unsigned>(time(nullptr)));
	cout.setf(ios::boolalpha);
	cout << "Veuillez entrer le nom de l'image a lire: ";
	string fichierLire;
	cin >> fichierLire;
	bool ok = false;
	Image image = lireImage(fichierLire, ok);
	if (!ok) {
		cerr << "Impossible de lire l'image." << endl;
		return 1;
	}

	cout << "Largeur: " << image.largeur << " Hauteur: " << image.hauteur << endl;
	int dimensionX = lireDimension("Veuillez indiquer la dimension des morceaux en X", static_cast<int>(image.largeur));
	int dimensionY = lireDimension("Veuillez indiquer la dimension des morceaux en Y", static_cast<int>(image.hauteur));

	ImageDecomposee imageDecomposee = decomposerImage(image, dimensionY, dimensionX);
	imageDecomposee = melangerImage(imageDecomposee);
	desallouerImage(image);
	image = recomposerImage(imageDecomposee);

	cout << "Veuillez entrer le nom du fichier a ecrire : ";
	string fichierEcrire;
	cin >> fichierEcrire;
	ecrireImage(fichierEcrire, image, ok);

	desallouerImage(image);
	for (unsigned i = 0; i < imageDecomposee.nMorceauxY; ++i) {
		for (unsigned j = 0; j < imageDecomposee.nMorceauxX; ++j) {
			desallouerImage(imageDecomposee.morceaux[i][j]);
		}
		delete[] imageDecomposee.morceaux[i];
	}
	delete[] imageDecomposee.morceaux;
	imageDecomposee.morceaux = nullptr;

	if (ok) {
		cout << "L'image a ete ecrite dans le fichier" << endl;
	} else {
		cerr << "Erreur lors de l'ecriture du fichier." << endl;
		return 1;
	}

	return 0;
}