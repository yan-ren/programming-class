////////////////////////////////////////////////////////////////////////////////
/// \file   constantes.hpp
///
/// Constants for special code points.
////////////////////////////////////////////////////////////////////////////////

#pragma once

#pragma region "Inclusions" //{

#include <cstddef>
#include <cstdint>

#include <istream>
#include <ostream>
#include <string>

using namespace std;

#pragma endregion //}

#pragma region "Déclarations" //{

#pragma region "Constantes" //{

enum PointsDeCodeSpeciaux : uint32_t
{
	INVALIDE = 0xFFFF,				 // Invalid code point marker
	BOM = 0xFEFF,					 // Byte Order Mark
	MULTI_CODET_UTF16_HAUT = 0xD800, // UTF-16 high surrogate base
	MULTI_CODET_UTF16_BAS = 0xDC00,	 // UTF-16 low surrogate base
};

#pragma endregion //}

#pragma endregion //}
