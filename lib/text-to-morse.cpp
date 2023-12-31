#include <iostream>
#include <unordered_map>
#include <SFML/Audio.hpp>
#include <string>
#include <cctype>

int main(int argc, char *argv[]) {
    std::string morse_text;
    std::string text = argv[1];

    for (char &c : text) {
        c = std::toupper(c);
    }

    std::unordered_map<char, std::string> morseCodes = {
        {'A', ".-"}, {'B', "-..."}, {'C', "-.-."}, {'D', "-.."}, {'E', "."},
        {'F', "..-."}, {'G', "--."}, {'H', "...."}, {'I', ".."}, {'J', ".---"},
        {'K', "-.-"}, {'L', ".-.."}, {'M', "--"}, {'N', "-."}, {'O', "---"},
        {'P', ".--."}, {'Q', "--.-"}, {'R', ".-."}, {'S', "..."}, {'T', "-"},
        {'U', "..-"}, {'V', "...-"}, {'W', ".--"}, {'X', "-..-"}, {'Y', "-.--"},
        {'Z', "--.."}
    };

    for(int i = 0; i < text.size(); i++) {
        if(text[i] == ' ') {
            morse_text += "/";
        }
        
        morse_text += morseCodes[text[i]];
        morse_text += " ";
    }

    std::cout<<morse_text<<std::endl;
    return 0;
}