#include <vector>
#include <string>
#include <stdexcept>

using namespace std;

class Solution {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res;
        for(const string& s : strs){
            res += to_string(s.size()) + "#" + s;
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        if (s.empty()) return {};  // Handle empty input
        vector<string> res;
        res.reserve(100); // Optional: Reserve space if you have an estimate of the number of strings
        size_t i = 0;
        while (i < s.size()){
            size_t j = i;
            // Find the position of the delimiter '#'
            while (j < s.size() && s[j] != '#'){
                j++;
            }
            if (j == s.size()) {
                // Delimiter not found, malformed string
                throw invalid_argument("Malformed encoded string: '#' delimiter not found.");
            }
            // Correctly extract the length using (j - i)
            string length_str = s.substr(i, j - i);
            int length;
            try {
                length = stoi(length_str);
            } catch (const invalid_argument& e) {
                throw invalid_argument("Malformed encoded string: Length is not a valid number.");
            } catch (const out_of_range& e) {
                throw out_of_range("Malformed encoded string: Length number is out of range.");
            }
            // Move past the '#' delimiter
            i = j + 1;
            // Check if the remaining string has enough characters
            if (i + length > s.size()) {
                throw invalid_argument("Malformed encoded string: Not enough characters for the specified length.");
            }
            // Extract the string of 'length' characters
            string current_str = s.substr(i, length);
            res.push_back(current_str);
            // Move 'i' to the start of the next encoded string
            i += length;
        }
        return res;
    }
    
};
