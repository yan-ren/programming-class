////////////////////////////////////////////////////////////////////////////////
/// \file   main.cpp
///
/// Main function of the program.
////////////////////////////////////////////////////////////////////////////////

#pragma region "Inclusions" //{

#include <cstddef>
#include <cstdint>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>

#include "cppitertools/range.hpp"

#include "debogageMemoire.hpp"
#include "unicode.hpp"

#include "constantes.hpp"
#include "utf8.hpp"
#include "utf16.hpp"

using namespace std;
using namespace iter;

#pragma endregion //}

void exempleAffichageUnicode();

int main()
{
	initDebogageMemoire(); // Will display memory leaks in Visual Studio's "Output" window.
	initUnicode();

	// exempleAffichageUnicode(); // Removed after verifying display is correct.

	const string inputFileNames[3] = {"TroisMousquetaires.txt",
									  "CaracteresAnciens.txt",
									  "Kalyna.txt"};
	const string outputFileNamesUtf16[3] = {"TroisMousquetaires_UTF-16.txt",
											"CaracteresAnciens_UTF-16.txt",
											"Kalyna_UTF-16.txt"};
	const string outputFileNamesUtf8[3] = {"TroisMousquetaires_UTF-8.txt",
										   "CaracteresAnciens_UTF-8.txt",
										   "Kalyna_UTF-8.txt"};

	// Read each file (in UTF-8), convert to UTF-16, then write to a file
	// with the corresponding name in outputFileNamesUtf16.
	// Don't forget the Byte Order Mark which is two bytes.
	for (int i : range(3))
	{
		// Read the UTF-8 file
		ifstream inputFile(inputFileNames[i], ios::binary);
		if (!inputFile.is_open())
		{
			wcout << "Error opening input file: " << inputFileNames[i] << endl;
			continue;
		}

		// Read the entire file content
		string utf8Content((istreambuf_iterator<char>(inputFile)),
						   istreambuf_iterator<char>());
		inputFile.close();

		// Convert UTF-8 to UTF-16
		u16string utf16Content = convertirStringVersUtf16(utf8Content);

		// Write to UTF-16 output file
		ofstream outputFile(outputFileNamesUtf16[i], ios::binary);
		if (!outputFile.is_open())
		{
			wcout << "Error opening output file: " << outputFileNamesUtf16[i] << endl;
			continue;
		}

		// Write the BOM (Byte Order Mark) first - little-endian (0xFF, 0xFE)
		uint8_t bomBytes[2] = {0xFF, 0xFE};
		outputFile.write((char *)bomBytes, 2);

		// Write the UTF-16 content (each char16_t as 2 bytes, little-endian)
		for (char16_t codeUnit : utf16Content)
		{
			uint8_t lowByte = codeUnit & 0xFF;
			uint8_t highByte = (codeUnit >> 8) & 0xFF;
			outputFile.put(lowByte);
			outputFile.put(highByte);
		}
		outputFile.close();

		wcout << "Converted " << inputFileNames[i] << " to " << outputFileNamesUtf16[i] << endl;
	}

	// Read each previously created UTF-16 file, then translate back to UTF-8
	// in a file with the corresponding name in outputFileNamesUtf8.
	// Be careful to skip the BOM (two bytes) when reading characters.
	for (int i : range(3))
	{
		// Read the UTF-16 file
		ifstream inputFile(outputFileNamesUtf16[i], ios::binary);
		if (!inputFile.is_open())
		{
			wcout << "Error opening UTF-16 file: " << outputFileNamesUtf16[i] << endl;
			continue;
		}

		// Skip the BOM (2 bytes)
		inputFile.seekg(2, ios::beg);

		// Read remaining bytes
		string rawBytes((istreambuf_iterator<char>(inputFile)),
						istreambuf_iterator<char>());
		inputFile.close();

		// Convert raw bytes to u16string (little-endian)
		u16string utf16Content;
		for (size_t j = 0; j + 1 < rawBytes.size(); j += 2)
		{
			uint8_t lowByte = (uint8_t)rawBytes[j];
			uint8_t highByte = (uint8_t)rawBytes[j + 1];
			char16_t codeUnit = lowByte | (highByte << 8);
			utf16Content.push_back(codeUnit);
		}

		// Convert UTF-16 to UTF-8
		string utf8Content = convertirStringVersUtf8(utf16Content);

		// Write to UTF-8 output file
		ofstream outputFile(outputFileNamesUtf8[i], ios::binary);
		if (!outputFile.is_open())
		{
			wcout << "Error opening output file: " << outputFileNamesUtf8[i] << endl;
			continue;
		}

		outputFile.write(utf8Content.c_str(), utf8Content.size());
		outputFile.close();

		wcout << "Converted " << outputFileNamesUtf16[i] << " to " << outputFileNamesUtf8[i] << endl;
	}

	return 0;
}

void exempleAffichageUnicode()
{
	// After initializing Unicode, you must use wcout instead of cout. Using cout will give an "ambiguous symbol" error.
	// You can still use non-Unicode character strings and display them on wcout.

	// Examples of non-Unicode C strings:
	static const char texteNonUnicode[] = "A non-Unicode text allows displaying Latin-1 characters, àâéèêïùç...\n";
	wcout << "A 'char' string is considered Latin-1 (not Unicode):" << endl
		  << texteNonUnicode << endl;

	// Examples of Unicode C strings, note the use of wchar_t (a 16-bit Unicode character) instead of char (an 8-bit character), and the use of L before the quotes:
	// (if you forget the L and use special characters, you'll get the warning "character ... cannot be represented in current code page")
	static const wchar_t texteUnicode[] = L"Ukrainian: Добрий день\nGreek: Γεια σας\nGray shades: ░▒▓█\n";
	wcout << L"A 'wchar_t' string is Unicode and allows more special characters ♪♫:" << endl
		  << texteUnicode << endl;

	// Example of string (not Unicode) and wstring (Unicode):
	static const string stringNonUnicode = "A string with Latin-1 characters.";
	static const wstring stringUnicode = L"A Unicode string ░▒▓█♪♫.";
	wcout << stringNonUnicode << endl // We provided a function to display 'string' on wcout.
		  << stringUnicode << endl;

	// UTF-16 display works for code points that fit in one code unit, code points > 0xFFFF don't currently display correctly in the console.
	static const u16string stringUtf16 = u"A Unicode string ░▒▓█♪♫."; // a small "u" in front for UTF-16.
	wcout << stringUtf16 << endl;

	// You can use cin as usual; this program doesn't configure it for unicode.
}
