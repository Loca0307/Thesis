        components: {
          MuiAvatar: {
            styleOverrides: {
              root: {
                '.widget-wrapper &': {
                  backgroundColor: themeCustomized.palette.common.white,
                  ...themeCustomized.applyStyles('light', {
                    backgroundColor: 'transparent',
                  }),
                },
              }
            },
          }
        }