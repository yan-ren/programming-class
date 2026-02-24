////////////////////////////////////////////////////////////////////////////////
/// \file   utf8.cpp
///
/// Implementation of functions for encoding and decoding UTF-8.
////////////////////////////////////////////////////////////////////////////////

#pragma region "Inclusions" //{

#include <cstddef>
#include <cstdint>

#include <cmath>
#include <string>

#include "cppitertools/range.hpp"

#include "constantes.hpp"
#include "utf16.hpp"

#include "utf8.hpp"

using namespace std;
using namespace iter;

#pragma endregion //}

#pragma region "Définitions" //{

#pragma region "Fonctions" //{

// Calculates the number of bytes needed to encode a code point in UTF-8.
// [in] pointCode: The Unicode code point to encode.
// Returns: The number of bytes (1-4) needed for encoding.
int calculerNbOctetsEncodageUtf8(uint32_t pointCode)
{
	// Count the number of significant bits in the code point.
	// We want the bits before everything else becomes 0.
	// For example, 0b01011010 has 7 significant bits.
	// Another example, 0b00000010 has 2 significant bits.
	int nSignificantBits = 0;
	if (pointCode == 0)
	{
		nSignificantBits = 1;
	}
	else
	{
		uint32_t temp = pointCode;
		while (temp != 0)
		{
			nSignificantBits++;
			temp >>= 1;
		}
	}

	// Determine the number of bytes needed for encoding based on the number
	// of bits to encode (see table in instructions or Wikipedia).
	// 1 byte: 7 bits, 2 bytes: 11 bits, 3 bytes: 16 bits, 4 bytes: 21 bits
	int nBytes = 0;
	if (nSignificantBits <= 7)
	{
		nBytes = 1;
	}
	else if (nSignificantBits <= 11)
	{
		nBytes = 2;
	}
	else if (nSignificantBits <= 16)
	{
		nBytes = 3;
	}
	else
	{
		nBytes = 4;
	}

	return nBytes;
}

// Calculates the prefix for the first byte of a UTF-8 encoding.
// [in] nbOctetsEncodage: The number of bytes in the encoding (1-4).
// Returns: The prefix byte (high bits set according to encoding length).
uint8_t
calculerPrefixePremierOctetUtf8(int nbOctetsEncodage)
{
	// Determine and return the prefix of the first byte based on encoding length.
	// See table (Byte 1 column) and Wiki page.
	// 1 byte: 0xxxxxxx -> prefix 0b00000000
	// 2 bytes: 110xxxxx -> prefix 0b11000000
	// 3 bytes: 1110xxxx -> prefix 0b11100000
	// 4 bytes: 11110xxx -> prefix 0b11110000
	uint8_t prefix = 0;
	switch (nbOctetsEncodage)
	{
	case 1:
		prefix = 0b00000000;
		break;
	case 2:
		prefix = 0b11000000;
		break;
	case 3:
		prefix = 0b11100000;
		break;
	case 4:
		prefix = 0b11110000;
		break;
	}

	return prefix;
}

// Decodes a UTF-8 sequence to get the Unicode code point.
// [in] sequenceUtf8: Pointer to the UTF-8 byte sequence.
// [out] nbOctetsTraites: Number of bytes processed.
// Returns: The decoded code point, or INVALIDE if invalid.
uint32_t
calculerPointDeCodeUtf8(const uint8_t *sequenceUtf8, int &nbOctetsTraites)
{
	uint32_t resultat = INVALIDE;
	nbOctetsTraites = 0;

	// If the first byte is ASCII (< 0x80), return it and set nbOctetsTraites to 1.
	if (sequenceUtf8[0] < 0x80)
	{
		resultat = sequenceUtf8[0];
		nbOctetsTraites = 1;
	}
	else
	{
		// Determine the number of bytes encoded for the character.
		// Count the number of 1 bits before the first 0, starting from the high order.
		// So if the first byte is 1110xxxx, then 3 bytes (including the first) are needed.
		int nBytesEncoded = 0;
		uint8_t firstByte = sequenceUtf8[0];
		uint8_t mask = 0b10000000;
		while ((firstByte & mask) != 0)
		{
			nBytesEncoded++;
			mask >>= 1;
		}

		// Extract the code bits from the first byte and assign to result.
		// For 2 bytes: 5 bits, for 3 bytes: 4 bits, for 4 bytes: 3 bits
		int nDataBitsFirstByte = 8 - nBytesEncoded - 1;
		uint8_t dataMask = (1 << nDataBitsFirstByte) - 1;
		resultat = firstByte & dataMask;

		// Initialize nbOctetsTraites to 1
		nbOctetsTraites = 1;

		// For each *FOLLOWING* byte of the character:
		for (int i = 1; i < nBytesEncoded; i++)
		{
			// Increment nbOctetsTraites.
			nbOctetsTraites++;

			// If the byte is not of the form 10xxxxxx, set INVALIDE and break.
			if ((sequenceUtf8[i] & 0b11000000) != 0b10000000)
			{
				resultat = INVALIDE;
				break;
			}

			// Shift result left by 6 bits and add the low 6 bits of current byte.
			resultat = (resultat << 6) | (sequenceUtf8[i] & 0b00111111);
		}
	}

	return resultat;
}

// Encodes a code point into UTF-8 and appends to the result string.
// [in] pointCode: The Unicode code point to encode.
// [in,out] resultat: The string to append the encoded bytes to.
void encoderCaractereUtf8(uint32_t pointCode, string &resultat)
{
	// If the code point is ASCII (< 0x80), add it to result converted to char.
	if (pointCode < 0x80)
	{
		resultat.push_back((char)pointCode);
	}
	else
	{
		// Count significant bits and determine number of bytes needed.
		int nBytes = calculerNbOctetsEncodageUtf8(pointCode);

		// Determine the prefix of the first byte.
		uint8_t prefix = calculerPrefixePremierOctetUtf8(nBytes);

		// Declare an array of 4 bytes.
		uint8_t octets[4] = {0};

		// For each byte except the first, extract the low 6 bits of the code point
		// and add them as a byte to the array with prefix 10xxxxxx,
		// then shift the code point by 6 bits.
		for (int i = nBytes - 1; i > 0; i--)
		{
			octets[i] = 0b10000000 | (pointCode & 0b00111111);
			pointCode >>= 6;
		}

		// Add to the array the byte with remaining bits and the previously determined prefix.
		octets[0] = prefix | (uint8_t)pointCode;

		// Add to the string the bytes in the order they were calculated.
		for (int i = 0; i < nBytes; i++)
		{
			resultat.push_back((char)octets[i]);
		}
	}
}

// Converts a UTF-16 string to UTF-8.
// [in] str: The UTF-16 string to convert.
// Returns: The converted UTF-8 string.
string
convertirStringVersUtf8(const u16string &str)
{
	string resultat;

	// While there are code units remaining in str:
	const char16_t *codetCourant = &str[0];
	while (codetCourant < (&str[0] + str.size()))
	{
		// Calculate the code point of the current character and skip
		// the number of code units indicated by nbCodetsTraites.
		int nbCodetsTraites = 0;
		uint32_t pointCode = calculerPointDeCodeUtf16(codetCourant, nbCodetsTraites);
		codetCourant += nbCodetsTraites;

		// If the code point is not invalid, encode it in UTF-8 in the result string.
		if (pointCode != INVALIDE)
		{
			encoderCaractereUtf8(pointCode, resultat);
		}
	}

	return resultat;
}

#pragma endregion //}

#pragma endregion //}
