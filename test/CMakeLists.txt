project(testapp)
cmake_minimum_required(VERSION 3.2.2)

add_definitions(-std=c++11)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} testapp.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
