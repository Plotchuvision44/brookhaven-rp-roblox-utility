#pragma once
#include <string>

namespace RobloxUtils {
    std::string sanitizeLuaInput(const std::string& input);
    bool isValidRobloxEnvironment();
}