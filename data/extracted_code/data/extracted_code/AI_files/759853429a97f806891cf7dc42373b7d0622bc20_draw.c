SET(INSTALL_TIIGRAPHICS_DIR ${CMAKE_INSTALL_PREFIX}/include/tiigraphics)
INSTALL(DIRECTORY ${CMAKE_SOURCE_DIR}/include/tiigraphics/
        DESTINATION ${INSTALL_TIIGRAPHICS_DIR}
        FILES_MATCHING PATTERN "*.h"
)

install(TARGETS tiigraphics
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)


SET(INSTALL_PKGCONFIG_DIR ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)
CONFIGURE_FILE(${CMAKE_SOURCE_DIR}/lib/tiigraphics/libtiigraphics.pc.in
        ${CMAKE_BINARY_DIR}/libtiigraphics.pc @ONLY
)

INSTALL(FILES ${CMAKE_BINARY_DIR}/libtiigraphics.pc
        DESTINATION ${INSTALL_PKGCONFIG_DIR}
)
