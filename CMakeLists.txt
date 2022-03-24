cmake_minimum_required(VERSION 3.18.2)
project(experiment-dirty)

option(EXPERIMENT_TARGET_CPU "CPU to optimise for, e.g. skylake, icelake or native" OFF)

set(CMAKE_CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_EXE_LINKER_FLAGS "-fuse-ld=lld")

if(EXPERIMENT_TARGET_CPU)
    message(STATUS "Optimising Faasm for CPU ${EXPERIMENT_TARGET_CPU}")
    add_compile_options(-march=${EXPERIMENT_TARGET_CPU} -mtune=${EXPERIMENT_TARGET_CPU})
else()
    message(STATUS "Experiment not optimised for specific CPU")
endif()

add_compile_options(-fno-omit-frame-pointer)
add_link_options(-Wl,--export-dynamic)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Faabric
set(FAABRIC_TARGET_CPU ${EXPERIMENT_TARGET_CPU} CACHE BOOL "" FORCE)
add_subdirectory(faabric)
list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_BINARY_DIR}/faabric)
list(PREPEND CMAKE_PREFIX_PATH ${CMAKE_CURRENT_BINARY_DIR}/faabric)
include(${CMAKE_CURRENT_BINARY_DIR}/faabric/conan_paths.cmake)

add_subdirectory(src)
