#include "roblox_utils.h"
#include <algorithm>

namespace RobloxUtils {
    std::string sanitizeLuaInput(const std::string& input) {
        std::string sanitized = input;
        sanitized.erase(std::remove(sanitized.begin(), sanitized.end(), '\''), sanitized.end());
        return sanitized;
    }

    bool isValidRobloxEnvironment() {
        return true; // Simplified for example
    }
}