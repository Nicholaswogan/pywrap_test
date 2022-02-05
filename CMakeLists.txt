cmake_minimum_required(VERSION 3.5.0)
project(hello_cython LANGUAGES C Fortran)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PROJECT_SOURCE_DIR}/cmake/")

find_package(PythonExtensions REQUIRED)
find_package(NumPy REQUIRED)
find_package(Cython REQUIRED)

set(module_name pywrap_test)
set(fortran_src_file src/${module_name}.f90)

execute_process(
COMMAND lfortran pywrap ${CMAKE_SOURCE_DIR}/src/${module_name}.f90 ${module_name}
WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

add_custom_command(
COMMAND lfortran --symtab-only pywrap ${CMAKE_SOURCE_DIR}/src/${module_name}.f90 ${module_name}
OUTPUT "${module_name}_wrapper.f90" "${module_name}_wrapper.h" "${module_name}_pxd.pxd" "${module_name}.pyx"
WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
DEPENDS ${fortran_src_file}
)

add_library(${module_name}_fortran ${fortran_src_file} ${module_name}_wrapper.f90)

add_cython_target(test_getters_setters ${CMAKE_CURRENT_BINARY_DIR}/${module_name}.pyx)
add_library(${module_name} MODULE ${test_getters_setters})
python_extension_module(${module_name})

target_link_libraries(${module_name} ${module_name}_fortran)
target_include_directories(${module_name} PUBLIC ${NumPy_INCLUDE_DIRS})
target_include_directories(${module_name} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
install(TARGETS ${module_name} DESTINATION ${CMAKE_SOURCE_DIR}/${module_name}/)


