PROJECT(MyHello)
cmake_minimum_required(VERSION 2.8)

ADD_LIBRARY(hello STATIC hello.cpp)
ADD_EXECUTABLE(greet main.cpp)
TARGET_LINK_LIBRARIES(greet hello)
IF (WIN32 AND "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    TARGET_LINK_LIBRARIES(greet stdc++)
ENDIF()