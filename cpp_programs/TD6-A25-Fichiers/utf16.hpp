////////////////////////////////////////////////////////////////////////////////
/// \file   utf16.hpp
///
/// Declaration of functions for encoding and decoding UTF-16.
////////////////////////////////////////////////////////////////////////////////

#pragma once

#pragma region "Inclusions" //{

#include <cstddef>
#include <cstdint>

#include <string>

using namespace std;

#pragma endregion //}

#pragma region "Déclarations" //{

#pragma region "Fonctions" //{

uint32_t calculerPointDeCodeUtf16(const char16_t *, int &);

void encoderCaractereUtf16(uint32_t, u16string &);

u16string convertirStringVersUtf16(const string &);

#pragma endregion //}

#pragma endregion //}
