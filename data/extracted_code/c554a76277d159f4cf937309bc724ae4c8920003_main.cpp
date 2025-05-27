	Piece(Piece&& other) noexcept :
		_attrs_map(std::move(other._attrs_map)),
		_current_loc(std::move(other._current_loc)),
		_name(std::move(other._name)),
		_symbol(other._symbol)
	{}
	
	Piece& operator=(Piece&& other) noexcept {
		if(this != &other) {
			_attrs_map = std::move(other._attrs_map);
			_current_loc = std::move(other._current_loc);
			_name = std::move(other._name);
			_symbol = other._symbol;
		}
		return *this;
	}
	
	Piece(const Piece& other)
	: _attrs_map(other._attrs_map),
	_name(other._name),
	_symbol(other._symbol) {
		if(other._current_loc) 
			_current_loc = std::make_unique<cc::BoardCoord>(*other._current_loc);
		else _current_loc = nullptr;
	}
	
	// Copy assignment (deep copy)
    Piece& operator=(const Piece& other) {
        if (this != &other) {
            _attrs_map = other._attrs_map;
            _name = other._name;
            _symbol = other._symbol;
            if (other._current_loc) {
                _current_loc = std::make_unique<cc::BoardCoord>(*other._current_loc);
            } else {
                _current_loc.reset();
            }
        }
        return *this;
    }
