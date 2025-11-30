#pragma once
/// Basic functions for using Unicode on wcin/wcout.
/// \author Francois-R.Boyer@PolyMtl.ca
/// \file
#include <iostream>
#include <string>
#ifdef _MSC_VER
#include <io.h>      // For _setmode and _fileno
#include <fcntl.h>   // For _O_U8TEXT and _O_U16TEXT
#endif
// After Unicode initialization, cin and cout crash if used. These variables will cause a "ambiguous symbol" compilation error if the program tries to use cin or cout, to detect the problem at compile time rather than runtime.
struct Ne_pas_utiliser {};
static Ne_pas_utiliser cout;
#ifndef SANS_WCIN
static Ne_pas_utiliser cin;
#endif

/*************************************************************************//**
*  Initializes the library to enable Unicode display.
*  \return  \c true if successful.
*/
inline bool initUnicode()
{
	bool success;
	// Select default regional settings.
	success = setlocale(LC_ALL, "") != 0;

	// Select output and input mode;
	// necessary on VisualC but not GCC and Clang.
	#ifdef _MSC_VER
	success = _setmode(_fileno(stdout), _O_U8TEXT) != -1 && success;
	#ifndef SANS_WCIN
	success = _setmode(_fileno(stdin), _O_U16TEXT) != -1 && success;
	#endif
	#endif
	return success;
}

/*************************************************************************//**
*  Conversion from 'wstring' to Latin-1 'string'.
*/
inline std::string versString(const std::wstring& chaine) {
	static const char UNKNOWN_CHARACTER = '?';
	std::string resultat;
	resultat.resize(chaine.length());
	for (size_t i = 0; i < chaine.length(); ++i) {
		if (chaine[i] < 256)
			resultat[i] = char(chaine[i]);
		else // The character doesn't exist in 'char'.
			resultat[i] = UNKNOWN_CHARACTER; 
	}
	return resultat;
}

/*************************************************************************//**
*  Conversion from Latin-1/ASCII 'string' to 'wstring'.
*/
inline std::wstring versWstring(const std::string& chaine) {
	std::wstring resultat;
	resultat.resize(chaine.length());
	for (size_t i = 0; i < chaine.length(); ++i)
		resultat[i] = chaine[i] & 0xFF;
	return resultat;
}

/*************************************************************************//**
*  Allows displaying a 'string' on 'wcout' with the standard << operator.
*/
inline std::wostream& operator <<(std::wostream& flot, const std::string& chaine)
{
	return flot << versWstring(chaine);
}

/*************************************************************************//**
*  Allows displaying a 'u16string' on 'wcout' with the standard << operator.
* \note Assumes wstring is UTF-16 (since wstring_convert is "deprecated" since C++17) and display supports it; if it's UTF-32, code points above 0xFFFF will be displayed incorrectly.
*/
inline std::wostream& operator <<(std::wostream& flot, const std::u16string& chaine)
{
	return flot << std::wstring(chaine.begin(), chaine.end());
}
