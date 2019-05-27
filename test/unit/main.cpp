#include "gtest/gtest.h"
#include <iostream>

int main(int argc, char* argv[])
{
    testing::InitGoogleTest(&argc, argv);
    RUN_ALL_TESTS();
    std::cout << "Sample Tests Finished" << std::endl;
    return 0;
}