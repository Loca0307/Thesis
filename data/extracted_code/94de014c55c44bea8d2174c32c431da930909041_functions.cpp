    SkipSpaces(json, position);
    char ch = json[position];

    if (ch == '{') {
        return parseObject(json, position);
    }
    else if (ch == '[') {
        return parseArray(json, position);
    }
    else if (ch == '"') {
        return parseString(json, position   );
    }
    else if (isdigit(ch) || ch == '-') {
        size_t start = position;
        while (position < json.size() && (isdigit(json[position]) || json[position] == '.' || json[position] == '-')) {
            position++;
        }
        std::string numStr = json.substr(start, position - start);
        try {
            if (numStr.find('.') != std::string::npos) {
                return std::stod(numStr);  // Parse as double
            }
            else {
                return std::stoll(numStr);  // Parse as long long
            }
        }
        catch (const std::invalid_argument&) {
            throw std::runtime_error("Invalid number format");
        }
    }
    else if (json.substr(position, 4) == "true") {
        position += 4;
        return true;
    }
    else if (json.substr(position, 5) == "false") {
        position += 5;
        return false;
    }
    else if (json.substr(position, 4) == "null") {
        position += 4;
        return nullptr;
    }
    else {
        throw std::runtime_error("Invalid JSON value");
    }