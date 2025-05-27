	defer syscall.Close(fd)

	// ソケットをインターフェースにバインド
	addr := syscall.SockaddrLinklayer{
		Protocol: syscall.ETH_P_ALL,
		Ifindex:  iface.Index,
	}
	if err := syscall.Bind(fd, &addr); err != nil {
		log.Fatalf("Failed to bind raw socket: %v", err)
	}