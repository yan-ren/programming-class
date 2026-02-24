#pragma once
//! This file provides a memory leak report in Visual Studio's "Output" window when the program ends execution in debug mode. There is currently no report if used with another compiler (i.e. gcc or clang), but this file will still compile and do nothing.
//! Call "initDebogageMemoire()" at the beginning of program execution (start of "main").
//! \note   This file must be included in each source file that uses "new", to get line numbers where "new" allocations without corresponding "delete" are located. It doesn't work if you use "placement new".
//! \author Francois-R.Boyer@PolyMtl.ca
//! \since  2015-04
//! \file
#ifdef _MSC_VER
// To have a leak report including line numbers where the allocation was made.
// (source http://msdn.microsoft.com/en-us/library/x98tx3cf%28v=vs.100%29.aspx)
#define _CRTDBG_MAP_ALLOC ///< Use allocations with debugging.
#include <stdlib.h>
#include <crtdbg.h>
#define new new( _NORMAL_BLOCK , __FILE__ , __LINE__ ) ///< Adds line number to leak report.

inline void initDebogageMemoire()
{
	_CrtSetDbgFlag(0
		| _CRTDBG_ALLOC_MEM_DF    // Memory allocation debugging.
		| _CRTDBG_LEAK_CHECK_DF   // Leak report at program exit. Note that the leak report will be displayed in Visual Studio's "Output" window.
		| _CRTDBG_CHECK_ALWAYS_DF // Check for corruption at each new/delete (slow).
		);
}
#else
inline void initDebogageMemoire()
{
	// Memory debugging is currently only available on MSVC.
}
#endif
