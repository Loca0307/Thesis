          EventDispatcher eventDispatcher;
          try {
            if (BuildConfig.IS_NEW_ARCHITECTURE_ENABLED) {
              eventDispatcher = UIManagerHelper.getUIManager(reactContext, UIManagerType.FABRIC).getEventDispatcher();
            } else {
              eventDispatcher = reactContext
                .getNativeModule(UIManagerModule.class).getEventDispatcher();
            }
            eventDispatcher.dispatchEvent(new ReactCheckBoxEvent(buttonView.getId(), isChecked));
          } catch (NullPointerException | IllegalStateException e) {
            android.util.Log.e("ReactCheckBoxManager", "Error dispatching checkbox event", e);
          }