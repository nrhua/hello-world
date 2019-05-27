project( UnitTest )

add_executable( UnitTest
    main.cpp
    unitest.cpp
)

target_link_libraries( UnitTest
    PRIVATE  CONAN_PKG::gtest
)

# support CTest and the RUN_TESTS target in IDEs
add_test(
    NAME  UnitTest
    COMMAND  "$<TARGET_FILE:UnitTest>" --gtest_output=xml:${CMAKE_BINARY_DIR}/UnitTest_Results.xml
)


