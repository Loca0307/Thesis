    /**
     * Returns animator that controls depth/blur of the background.
     */
private ObjectAnimator getBackgroundAnimator() {
    boolean allowBlurringLauncher = mLauncher.getStateManager().getState() != OVERVIEW
            && BlurUtils.supportsBlursOnWindows();

    LaunchDepthController depthController = new LaunchDepthController(mLauncher);
    ObjectAnimator backgroundRadiusAnim = ObjectAnimator.ofFloat(depthController.stateDepth,
                    MULTI_PROPERTY_VALUE, BACKGROUND_APP.getDepth(mLauncher))
            .setDuration(APP_LAUNCH_DURATION);

    if (allowBlurringLauncher) {
        View rootView = mLauncher.getDragLayer();

        // Create a composite SurfaceControl layer for everything behind the app animation
        ViewRootImpl viewRootImpl = rootView.getViewRootImpl();
        SurfaceControl parentSurface = viewRootImpl != null ? viewRootImpl.getSurfaceControl() : null;

        if (parentSurface != null) {
            SurfaceControl blurLayer = new SurfaceControl.Builder()
                    .setName("Blur Layer")
                    .setParent(parentSurface)