#include "gtest/gtest.h"

using namespace std;

TEST(sample_test_case, sample_test)
{
    EXPECT_EQ(1, 1);
    ASSERT_EQ(1, 1);
}