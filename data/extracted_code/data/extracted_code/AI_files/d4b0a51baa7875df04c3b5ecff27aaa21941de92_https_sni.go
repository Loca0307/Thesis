// isValidFQDN validates if the given hostname is a valid FQDN
func isValidFQDN(hostname string) bool {
	// Regular expression to match a valid FQDN
	var fqdnRegex = regexp.MustCompile(`^(?i:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,})$`)
	return fqdnRegex.MatchString(hostname)
}
