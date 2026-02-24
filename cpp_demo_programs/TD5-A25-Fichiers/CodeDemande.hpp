////////////////////////////////////////////////////////////////////////////////
///				ENTETE
////////////////////////////////////////////////////////////////////////////////

#pragma once


#pragma region "Inclusions" //{

#include <ciso646>
#include <cstddef>
#include <cstdint>

#include <fstream>
#include <string>

#include "CodeFourni.hpp"


using namespace std;

#pragma endregion //}




#pragma region "Déclarations" //{

#pragma region "Globaux" //{

/**
 * \brief Lit les entêtes d'un fichier bitmap.
 *
 * \param [in,out] fichier      Flux binaire positionné au début du fichier BMP.
 *
 * \return L'entête DIB du fichier.
 */
EnteteDib lireEnteteFichier ( fstream& fichier );

/**
 * \brief Lit les données d'une image BMP à partir d'un fichier.
 *
 * \param [in,out] fichier      Flux binaire contenant l'image.
 * \param [out]     image        Image déjà allouée qui recevra les pixels.
 */
void lireDonneesImage ( fstream& fichier, Image& image );

/**
 * \brief Écrit les pixels d'une image dans un fichier BMP.
 *
 * \param [in,out] fichier      Flux binaire dans lequel écrire les pixels.
 * \param [in]      image        Image dont le contenu sera écrit.
 */
void ecrireDonneesImage ( fstream& fichier, const Image& image );

/**
 * \brief Écrit une image complète dans un fichier BMP.
 *
 * \param [in]      nomFichier   Nom du fichier de sortie.
 * \param [in]      image        Image à écrire.
 * \param [out]     ok           Indique la réussite de l'opération.
 */
void ecrireImage ( const string& nomFichier, const Image& image, bool& ok );

/**
 * \brief Alloue une image de dimensions données.
 *
 * \param [in] largeur  Largeur souhaitée.
 * \param [in] hauteur  Hauteur souhaitée.
 *
 * \return L'image allouée.
 */
Image allouerImage ( unsigned largeur, unsigned hauteur );

/**
 * \brief Désalloue complètement une image.
 *
 * \param [in,out] image Image dont la mémoire doit être libérée.
 */
void desallouerImage ( Image& image );

/**
 * \brief Lit une image BMP depuis un fichier.
 *
 * \param [in]      nomFichier   Nom du fichier à lire.
 * \param [out]     ok           Indique la réussite de l'opération.
 *
 * \return L'image lue.
 */
Image lireImage ( const string& nomFichier, bool& ok );

/**
 * \brief Extrait un morceau rectangulaire d'une image.
 *
 * \param [in] image    Image source.
 * \param [in] x        Position horizontale du morceau.
 * \param [in] y        Position verticale du morceau.
 * \param [in] hauteur  Hauteur du morceau.
 * \param [in] largeur  Largeur du morceau.
 *
 * \return Le morceau extrait.
 */
Image extraireMorceau ( const Image& image, const int x, const int y, const int hauteur, const int largeur );

/**
 * \brief Décompose une image en morceaux de taille fixe.
 *
 * \param [in] image             Image à découper.
 * \param [in] hauteurMorceaux   Hauteur de chaque morceau.
 * \param [in] largeurMorceaux   Largeur de chaque morceau.
 *
 * \return L'image décomposée.
 */
ImageDecomposee decomposerImage ( const Image& image, const int hauteurMorceaux, const int largeurMorceaux );

/**
 * \brief Mélange aléatoirement les morceaux d'une image décomposée.
 *
 * \param [in] imageDecomposee   Image décomposée à mélanger.
 *
 * \return L'image décomposée mélangée.
 */
ImageDecomposee melangerImage ( ImageDecomposee imageDecomposee );

/**
 * \brief Recompose une image à partir de ses morceaux.
 *
 * \param [in] imageDecomposee   Image décomposée à recomposer.
 *
 * \return L'image reconstituée.
 */
Image recomposerImage ( const ImageDecomposee imageDecomposee );

#pragma endregion //}

#pragma endregion //}

