//go:embed assets
var assetsFS embed.FS

func get_img(filepath string, console *widget.Entry, assetsFS embed.FS) (image.Image, error) {
	imgData, err := assetsFS.ReadFile(filepath)
	if err != nil {
		console.SetText(console.Text + "Error loading image: " + err.Error() + "\n")
		fmt.Println("in 1: " + err.Error())
		return nil, err
	}

	img, _, err := image.Decode(bytes.NewReader(imgData))
	if err != nil {
		console.SetText(console.Text + "Error loading image: " + err.Error() + "\n")
		fmt.Println("in 2: " + err.Error())
		return nil, err
	}

	return img, nil
}
