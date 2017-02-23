#=============================================================================#
# Author: Gregory DEPUILLE                                                    #
# Date:   21/02/2017                                                          #
# Description: Build du SDK RPLidar pour Conan                                #
#=============================================================================#
# Contrôle de la version minimale de CMake
cmake_minimum_required(VERSION 3.2.2)

# Détection des fichiers par OS
if (UNIX AND NOT APPLE)
  set(ARCH_DIR "linux")
elseif (UNIX AND APPLE)
  set(ARCH_DIR "macOS")
  add_definitions(-D_MACOS)
else()
  message(FATAL_ERROR "Arch OS is not valid")
endif()

#====================================================================#
#  Setup Project                                                     #
#====================================================================#
project(rplidar_sdk)

# Récupération des sources du projets
file(GLOB SRCS "src/rplidar_driver.cpp" "src/hal/thread.cpp" "src/arch/${ARCH_DIR}/net_serial.cpp" "src/arch/${ARCH_DIR}/timer.cpp")

# Include header files
include_directories(include src)

# Création des librairie static
add_library(${PROJECT_NAME} STATIC ${SRCS})

# Install library
install(TARGETS ${PROJECT_NAME} DESTINATION lib/${PROJECT_NAME})

# Install library headers
file(GLOB HEADERS include/*.h)
install(FILES ${HEADERS} DESTINATION include/${PROJECT_NAME})
