#include "../src/roblox/roblox_script.h"
#include "../src/roblox/roblox_utils.h"
#include <cassert>

void testSanitizeInput() {
    std::string input = "print('Hello')";
    std::string expected = "print(Hello)";
    assert(RobloxUtils::sanitizeLuaInput(input) == expected);
}

void testScriptExecution() {
    RobloxScript script;
    script.execute("print('Test')");
    assert(script.getLastOutput() == "Script executed successfully");
}

int main() {
    testSanitizeInput();
    testScriptExecution();
    return 0;
}