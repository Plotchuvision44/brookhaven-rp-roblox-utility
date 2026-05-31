#pragma once
#include <string>

class RobloxScript {
public:
    void execute(const std::string& luaCode);
    std::string getLastOutput() const;
private:
    std::string lastOutput;
};