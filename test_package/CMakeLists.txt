cmake_minimum_required(VERSION 2.8)

project(CMakeMultipleFlagsBugTest C CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
if(CMAKE_VERSION VERSION_LESS 3.1.2)
conan_basic_setup()
else()
conan_basic_setup(TARGETS)
endif()

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(CMAKE_SKIP_RPATH OFF)
set(CMAKE_MACOSX_RPATH ON)
set(CMAKE_SKIP_BUILD_RPATH ON)
set(CMAKE_SKIP_INSTALL_RPATH OFF)
set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH OFF)

add_executable(main_c main.c)
add_executable(main_cpp main.cpp)

if(CMAKE_VERSION VERSION_LESS 3.1.2)
target_link_libraries(main_c ${CONAN_LIBS})
target_link_libraries(main_cpp ${CONAN_LIBS})
else()
target_link_libraries(main_c CONAN_PKG::cmake-multiple-flags-bug)
target_link_libraries(main_cpp CONAN_PKG::cmake-multiple-flags-bug)
endif()
