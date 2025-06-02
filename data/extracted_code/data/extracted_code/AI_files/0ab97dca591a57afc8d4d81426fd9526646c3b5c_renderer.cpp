    try {
      ShutdownImGui();
    } catch (const std::exception& e) {
      LOG_CRITICAL("Failed to shutdown ImGui: {}", e.what());
    } catch (...) {
      LOG_CRITICAL("Failed to shutdown ImGui due to an unknown error");
    }