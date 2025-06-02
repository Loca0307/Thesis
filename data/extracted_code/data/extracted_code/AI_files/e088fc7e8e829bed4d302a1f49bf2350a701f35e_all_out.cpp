    // determine whether or not to handle packet
    if ((requestEthLayer->getSourceMac() == device->getMacAddress() ||
         requestEthLayer->getSourceMac() ==
             allOutArpPoisoningCookie->attackerMacAddress) ||
        requestArpLayer->getTargetIpAddr() != device->getIPv4Address()) {
        return;
    }
