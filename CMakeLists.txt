# set the CMake to support a modern C++ version
cmake_minimum_required( VERSION  3.3 )

#set the main project name
project(jenny-canary)

# enable using CTest
enable_testing()

option(WITH_TESTS "" ON)
option(WITH_DOCS "" OFF)
option(WITH_EXAMPLES "" OFF)
option(WITH_BENCHMARKS "" ON)

# default initialize the output paths
if( NOT  DEFINED  CMAKE_RUNTIME_OUTPUT_DIRECTORY )
    set( CMAKE_RUNTIME_OUTPUT_DIRECTORY  "${CMAKE_BINARY_DIR}/bin" )
endif()
if( NOT  DEFINED  CMAKE_LIBRARY_OUTPUT_DIRECTORY )
    set( CMAKE_LIBRARY_OUTPUT_DIRECTORY  "${CMAKE_BINARY_DIR}/lib" )
endif()
if( NOT  DEFINED  CMAKE_ARCHIVE_OUTPUT_DIRECTORY )
    set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY  "${CMAKE_BINARY_DIR}/lib" )
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory(src)
add_subdirectory(test/unit)

