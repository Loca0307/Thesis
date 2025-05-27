 * A ScreenComponent defines a rectangular area where user interfaces can be constructed. Screens
 * can either be 2D (screen space) or 3D (world space) - see {@link screenSpace}. It is possible to
 * create an {@link Entity} hierarchy underneath an Entity with a ScreenComponent to create complex
 * user interfaces using the following components:
 *
 * - {@link ButtonComponent}
 * - {@link ElementComponent}
 * - {@link LayoutChildComponent}
 * - {@link LayoutGroupComponent}
 * - {@link ScrollbarComponent}
 * - {@link ScrollViewComponent}
 *
 * You should never need to use the ScreenComponent constructor directly. To add a ScreenComponent
 * to an {@link Entity}, use {@link Entity#addComponent}:
 *
 * ```javascript
 * const entity = new pc.Entity();
 * entity.addComponent('screen', {
 *     referenceResolution: new pc.Vec2(1280, 720),
 *     screenSpace: false
 * });
 * ```
 *
 * Once the ScreenComponent is added to the entity, you can access it via the {@link Entity#screen}
 * property:
 *
 * ```javascript
 * entity.screen.scaleBlend = 0.6; // Set the screen's scale blend to 0.6
 *
 * console.log(entity.screen.scaleBlend); // Get the screen's scale blend and print it
 * ```
 *
 * Relevant Engine API examples:
 *
 * - [Screen Space Screen](https://playcanvas.github.io/#/user-interface/text)
 * - [World Space Screen](https://playcanvas.github.io/#/user-interface/world-ui)