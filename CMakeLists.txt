cmake_minimum_required(VERSION 3.10)
project(brookhaven-rp-roblox-utility)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(roblox_utility
    src/main.cpp
    src/roblox/roblox_utils.cpp
    src/roblox/roblox_script.cpp
)

target_include_directories(roblox_utility PRIVATE src)
target_link_libraries(roblox_utility PRIVATE fmt)