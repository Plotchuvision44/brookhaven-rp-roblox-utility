#include "roblox_script.h"
#include "roblox_utils.h"
#include <iostream>

void RobloxScript::execute(const std::string& luaCode) {
    if (!RobloxUtils::isValidRobloxEnvironment()) {
        lastOutput = "Error: Invalid Roblox environment";
        return;
    }

    std::string safeCode = RobloxUtils::sanitizeLuaInput(luaCode);
    std::cout << "[Roblox Script] Executing: " << safeCode << "\n";
    lastOutput = "Script executed successfully";
}

std::string RobloxScript::getLastOutput() const {
    return lastOutput;
}