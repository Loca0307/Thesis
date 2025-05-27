kth_bool_t kth_chain_utxo_has_token_data(kth_utxo_t utxo) {
    return kth_chain_utxo_const_cpp(utxo).token_data() ?
        kth::bool_to_int(true) :
        kth::bool_to_int(false);
}

kth_token_data_t kth_chain_utxo_get_token_data(kth_utxo_t utxo) {
    auto& utxo_cpp = kth_chain_utxo_cpp(utxo);
    if ( ! utxo_cpp.token_data()) {
        return nullptr;
    }
    return &utxo_cpp.token_data().value();
}

kth_hash_t kth_chain_utxo_get_token_category(kth_utxo_t utxo) {
    auto const& token_data = kth_chain_utxo_const_cpp(utxo).token_data();
    if ( ! token_data) {
        return kth::to_hash_t(kth::null_hash);
    }
    auto const& token_category_cpp = token_data->id;
    return kth::to_hash_t(token_category_cpp);
}

void kth_chain_utxo_get_token_category_out(kth_utxo_t utxo, kth_hash_t* out_token_category) {
    auto const& token_data = kth_chain_utxo_const_cpp(utxo).token_data();
    if ( ! token_data) {
        kth::copy_c_hash(kth::null_hash, out_token_category);
        return;
    }
    auto const& token_category_cpp = token_data->id;
    kth::copy_c_hash(token_category_cpp, out_token_category);
}

uint64_t kth_chain_utxo_get_token_amount(kth_utxo_t utxo) {
    auto const& token_data = kth_chain_utxo_const_cpp(utxo).token_data();
    if ( ! token_data) {
        return kth::max_uint64;
    }
    if (std::holds_alternative<kth::domain::chain::fungible>(token_data->data)) {
        return uint64_t(std::get<kth::domain::chain::fungible>(token_data->data).amount);
    }
    if (std::holds_alternative<kth::domain::chain::both_kinds>(token_data->data)) {
        return uint64_t(std::get<kth::domain::chain::both_kinds>(token_data->data).first.amount);
    }
    return kth::max_uint64;
}

kth_token_capability_t kth_chain_utxo_get_token_capability(kth_utxo_t utxo) {
    auto const& token_data_opt = kth_chain_utxo_const_cpp(utxo).token_data();
    if ( ! token_data_opt) {
        return kth_token_capability_none;
    }
    auto const& token_data = *token_data_opt;
    if (std::holds_alternative<kth::domain::chain::non_fungible>(token_data.data)) {
        auto const& non_fungible_cpp = std::get<kth::domain::chain::non_fungible>(token_data.data);
        return kth::token_capability_to_c(non_fungible_cpp.capability);
    }
    if (std::holds_alternative<kth::domain::chain::both_kinds>(token_data.data)) {
        auto const& both_kinds_cpp = std::get<kth::domain::chain::both_kinds>(token_data.data);
        auto const& non_fungible_cpp = both_kinds_cpp.second;
        return kth::token_capability_to_c(non_fungible_cpp.capability);
    }
    return kth_token_capability_none; // TODO: this is not a good way to signal an error
}

uint8_t const* kth_chain_utxo_get_token_commitment(kth_utxo_t utxo, kth_size_t* out_size) {
    auto const& token_data_opt = kth_chain_utxo_const_cpp(utxo).token_data();
    if ( ! token_data_opt) {
        *out_size = 0;
        return nullptr;
    }
    auto const& token_data = *token_data_opt;
    if (std::holds_alternative<kth::domain::chain::non_fungible>(token_data.data)) {
        auto const& non_fungible_cpp = std::get<kth::domain::chain::non_fungible>(token_data.data);
        return kth::create_c_array(non_fungible_cpp.commitment, *out_size);
    }
    if (std::holds_alternative<kth::domain::chain::both_kinds>(token_data.data)) {
        auto const& both_kinds_cpp = std::get<kth::domain::chain::both_kinds>(token_data.data);
        auto const& non_fungible_cpp = both_kinds_cpp.second;
        return kth::create_c_array(non_fungible_cpp.commitment, *out_size);
    }

    *out_size = 0;
    return nullptr;
}

// Setters

void kth_chain_utxo_set_hash(kth_utxo_t utxo, kth_hash_t const* hash) {