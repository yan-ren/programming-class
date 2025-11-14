////////////////////////////////////////////////////////////////////////////////
////		ENTETE
////////////////////////////////////////////////////////////////////////////////


#pragma region "Inclusions" //{

#include <ciso646>
#include <cstddef>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <string>

#include "CodeFourni.hpp"


using namespace std;

#pragma endregion //}




#pragma region "Globaux" //{

#pragma region "Fonctions" //{

EnteteDib lireEnteteFichier ( fstream& fichier )
{
	// TODO: Read both the BMP and DIB headers from the file starting at the beginning.
	//       The DIB header will be returned to the caller.
	fichier.seekg(0, ios::beg);

	EnteteBmp enteteBmp{};
	fichier.read(reinterpret_cast<char*>(&enteteBmp), sizeof(enteteBmp));

	EnteteDib enteteDib{};
	fichier.read(reinterpret_cast<char*>(&enteteDib), sizeof(enteteDib));

	return enteteDib;
}

void lireDonneesImage ( fstream& fichier, Image& image )
{
	// TODO: Move to the start of the pixel array in the file (right after the headers).
	// TODO: For each image row, read the row data then skip over the padding bytes.
	fichier.seekg(static_cast<streamoff>(sizeof(EnteteBmp) + sizeof(EnteteDib)), ios::beg);

	const unsigned padding = calculerTaillePadding(image);
	const auto largeurLigne = static_cast<streamsize>(image.largeur * sizeof(Pixel));
	const int hauteurImage = static_cast<int>(image.hauteur);

	for (int ligne : range(hauteurImage)) {
		const int indexDestination = hauteurImage - 1 - ligne;
		fichier.read(reinterpret_cast<char*>(image.pixels[indexDestination]), largeurLigne);
		if (padding != 0U) {
			fichier.ignore(static_cast<streamsize>(padding));
		}
	}
}

void ecrireDonneesImage ( fstream& fichier, const Image& image )
{
	// TODO: Position the write pointer just after the headers before writing pixels.
	// TODO: Write each row of pixels followed by the necessary zero padding bytes.
	fichier.seekp(static_cast<streamoff>(sizeof(EnteteBmp) + sizeof(EnteteDib)), ios::beg);

	const unsigned padding = calculerTaillePadding(image);
	const auto largeurLigne = static_cast<streamsize>(image.largeur * sizeof(Pixel));
	const int hauteurImage = static_cast<int>(image.hauteur);
	char remplissage[ALIGNEMENT_PIXELS] = {0};

	for (int ligne : range(hauteurImage)) {
		const int indexSource = hauteurImage - 1 - ligne;
		fichier.write(reinterpret_cast<const char*>(image.pixels[indexSource]), largeurLigne);
		if (padding != 0U) {
			fichier.write(remplissage, static_cast<streamsize>(padding));
		}
	}
}

void ecrireImage ( const string& nomFichier, const Image& image, bool& ok )
{
	// TODO: Open the output file in binary mode and check for success before proceeding.
	// TODO: Build the BMP and DIB headers from the provided image dimensions.
	// TODO: Write the headers and pixel data to produce a valid BMP file.
	ok = false;
	fstream fichier(nomFichier, ios::binary | ios::out | ios::trunc);
	if (!fichier) {
		return;
	}

	const EnteteBmp enteteBmp = construireEnteteBmp(image);
	const EnteteDib enteteDib = construireEnteteDib(image);

	fichier.write(reinterpret_cast<const char*>(&enteteBmp), sizeof(enteteBmp));
	fichier.write(reinterpret_cast<const char*>(&enteteDib), sizeof(enteteDib));

	ecrireDonneesImage(fichier, image);

	ok = fichier.good();
}

Image allouerImage ( unsigned largeur, unsigned hauteur )
{
	// TODO: Initialize the Image structure and allocate a 2D array of pixels when dimensions are non-zero.
	// TODO: Default to an empty image when either dimension is zero.
	Image image{};
	image.largeur = largeur;
	image.hauteur = hauteur;
	image.pixels = nullptr;

	if (largeur == 0 || hauteur == 0) {
		image.largeur = 0;
		image.hauteur = 0;
		return image;
	}

	image.pixels = new Pixel*[hauteur];
	for (unsigned i : range(hauteur)) {
		image.pixels[i] = new Pixel[largeur]{};
	}

	return image;
}


void desallouerImage ( Image& image )
{
	// TODO: If the pixel array exists, free each row then the array of row pointers.
	// TODO: Reset the image dimensions and pointer to indicate that the memory is released.
	if (image.pixels != nullptr) {
		for (unsigned i : range(image.hauteur)) {
			delete[] image.pixels[i];
		}
		delete[] image.pixels;
		image.pixels = nullptr;
	}

	image.largeur = 0;
	image.hauteur = 0;
}

Image lireImage ( const string& nomFichier, bool& ok )
{
	// TODO: Open the BMP file in binary read mode and abort if it fails.
	// TODO: Read the DIB header, allocate an Image with the proper dimensions, then read the pixel data.
	// TODO: If a read error occurs, release any allocated memory and return an empty Image.
	ok = false;
	fstream fichier(nomFichier, ios::binary | ios::in);
	if (!fichier) {
		return {};
	}

	const EnteteDib enteteDib = lireEnteteFichier(fichier);
	const unsigned largeurImage = static_cast<unsigned>(enteteDib.largeurImage >= 0 ? enteteDib.largeurImage : -enteteDib.largeurImage);
	const unsigned hauteurImage = static_cast<unsigned>(enteteDib.hauteurImage >= 0 ? enteteDib.hauteurImage : -enteteDib.hauteurImage);

	Image image = allouerImage(largeurImage, hauteurImage);
	if ((largeurImage != 0U && hauteurImage != 0U) && image.pixels == nullptr) {
		return image;
	}

	lireDonneesImage(fichier, image);

	ok = fichier.good();
	if (!ok) {
		desallouerImage(image);
		return {};
	}

	return image;
}

Image extraireMorceau ( const Image& image, const int x, const int y, const int hauteur, const int largeur)
{
	// TODO: Allocate a new Image matching the requested piece size.
	// TODO: Copy the corresponding pixels from the source image into the new piece.
	Image morceau = allouerImage(static_cast<unsigned>(largeur), static_cast<unsigned>(hauteur));

	for (int i : range(hauteur)) {
		for (int j : range(largeur)) {
			morceau.pixels[i][j] = image.pixels[y + i][x + j];
		}
	}

	return morceau;
}

ImageDecomposee decomposerImage(const Image& image, const int hauteurMorceaux, const int largeurMorceaux)
{
	ImageDecomposee imageDecomposee;

	// TODO: Determine how many pieces fit horizontally and vertically given the target piece size.
	// TODO: Allocate an array of Image pointers representing rows of pieces.
	// TODO: Use extraireMorceau to populate each piece in the grid.
	imageDecomposee.nMorceauxX = largeurMorceaux == 0 ? 0U : image.largeur / static_cast<unsigned>(largeurMorceaux);
	imageDecomposee.nMorceauxY = hauteurMorceaux == 0 ? 0U : image.hauteur / static_cast<unsigned>(hauteurMorceaux);
	imageDecomposee.morceaux = nullptr;

	if (imageDecomposee.nMorceauxX == 0U || imageDecomposee.nMorceauxY == 0U) {
		return imageDecomposee;
	}

	imageDecomposee.morceaux = new Image*[imageDecomposee.nMorceauxY];
	for (unsigned i = 0; i < imageDecomposee.nMorceauxY; ++i) {
		imageDecomposee.morceaux[i] = new Image[imageDecomposee.nMorceauxX];
		for (unsigned j = 0; j < imageDecomposee.nMorceauxX; ++j) {
			const int origineY = static_cast<int>(i) * hauteurMorceaux;
			const int origineX = static_cast<int>(j) * largeurMorceaux;
			imageDecomposee.morceaux[i][j] = extraireMorceau(image, origineX, origineY, hauteurMorceaux, largeurMorceaux);
		}
	}

	return imageDecomposee;
}

ImageDecomposee melangerImage(ImageDecomposee imageDecomposee) 
{

	// TODO: Randomly swap each piece with another piece selected uniformly from the grid.
	if (imageDecomposee.morceaux == nullptr) {
		return imageDecomposee;
	}

	for (unsigned i = 0; i < imageDecomposee.nMorceauxY; ++i) {
		for (unsigned j = 0; j < imageDecomposee.nMorceauxX; ++j) {
			const unsigned hasardY = static_cast<unsigned>(std::rand() % static_cast<int>(imageDecomposee.nMorceauxY));
			const unsigned hasardX = static_cast<unsigned>(std::rand() % static_cast<int>(imageDecomposee.nMorceauxX));
			std::swap(imageDecomposee.morceaux[i][j], imageDecomposee.morceaux[hasardY][hasardX]);
		}
	}

	return imageDecomposee;
}

/**
 * Crée une image à partir d'une image décomposée
 *
 * \param [in] imageDecomposee		L'image de départ
 *
 * \return l'image recomposée
 */
Image recomposerImage(const ImageDecomposee imageDecomposee) 
{
	Image image;
	int largeurMorceau = imageDecomposee.morceaux[0][0].largeur;
	int hauteurMorceau = imageDecomposee.morceaux[0][0].hauteur;

	// TODO: Allocate a destination Image whose dimensions match the full puzzle.
	// TODO: Copy pixels from each piece back into their corresponding position in the full image.
	if (imageDecomposee.nMorceauxX == 0U || imageDecomposee.nMorceauxY == 0U || imageDecomposee.morceaux == nullptr) {
		return allouerImage(0, 0);
	}

	image = allouerImage(imageDecomposee.nMorceauxX * static_cast<unsigned>(largeurMorceau),
	                     imageDecomposee.nMorceauxY * static_cast<unsigned>(hauteurMorceau));

	for (unsigned morceauY = 0; morceauY < imageDecomposee.nMorceauxY; ++morceauY) {
		for (unsigned morceauX = 0; morceauX < imageDecomposee.nMorceauxX; ++morceauX) {
			const Image& morceau = imageDecomposee.morceaux[morceauY][morceauX];
			const unsigned departY = morceauY * static_cast<unsigned>(hauteurMorceau);
			const unsigned departX = morceauX * static_cast<unsigned>(largeurMorceau);
			for (int y : range(hauteurMorceau)) {
				for (int x : range(largeurMorceau)) {
					image.pixels[departY + static_cast<unsigned>(y)][departX + static_cast<unsigned>(x)] = morceau.pixels[y][x];
				}
			}
		}
	}

	return image;
}

#pragma endregion //}

#pragma endregion //}

