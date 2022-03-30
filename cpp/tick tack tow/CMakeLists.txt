# CMakeList.txt : CMake project for tick tack tow, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("tick tack tow")

# Add source to this project's executable.
add_executable (CMakeTarget "tick tack tow.cpp" "tick tack tow.h")

message(STATUS "build type: ${CMAKE_BUILD_TYPE}")

set(CMAKE_CXX_FLAGS_RELEASE "-O2 ")
set(CMAKE_CXX_FLAGS_DEBUG "-g ")

# TODO: Add tests and install targets if needed.
