
    private static boolean isPlayerInRiptideAnimation(PlayerEntity player) {
        return player.getActiveItem().getItem().toString().contains("riptide");
    }

    private static boolean isInNether(PlayerEntity player) {
        // Check if the player is in the Nether based on dimension ID
        return player.getWorld().getRegistryKey().getValue().equals(new Identifier("minecraft", "nether"));
    }

    private static boolean isInVehicle(PlayerEntity player) {
        return player.getVehicle() != null && 
               (player.getVehicle() instanceof net.minecraft.entity.vehicle.BoatEntity ||
                player.getVehicle() instanceof net.minecraft.entity.vehicle.MinecartEntity);
    }

    private static boolean isSneaking(PlayerEntity player) {
        return player.isSneaking();
    }
