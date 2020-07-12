# <u>**CLANG BEAR COMPILE GENERATOR**</u>

## Goal:

Main goal is to automate the process of creating a [compile_commands.json]() file. 

The default behaviour is to treat it like you are compiling your source in tree: eg. if you project is in directory **ABC/** then your build directory will be at **ABC/build/** or any directory under **ABC/** of your own choice, it will then put the  [compile_commands.json]() file from the build directory into the main source directory, which is the main **ABC/** directory in this case.

## Reason:

Many people use LSP servers like clangd for C/C++ developer which are reliant on [compile_commands.json]() file being passed in order to know which special header files/libraries are to be used when generating auto completion for you and also displaying error messages. Tools like Cmake should be able to produce this file with flag **CMAKE_EXPORT_COMPILE_COMMANDS** set to **ON** but not all projects resulted in the creation of the file eg: some KDE based projects. So I came to find out that **bear** is a tool that can generate the  [compile_commands.json]() without any problems straight from a make file of most build tools. This script simply automates the creation of [compile_commands.json]() and placing it into source directory for easy access.