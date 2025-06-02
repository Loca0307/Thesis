import numpy as np
import time
import json

# Create a class for the donut
class SpinningDonut:
    """
    A class representing a spinning 3D donut.
    """

    # Initialize the donut
    def __init__(self, screen_size=40, theta_spacing=0.07, phi_spacing=0.02, delay=0.01):
        """
        Initialize the donut with certain parameters.

        Parameters:
        screen_size (int): The size of the screen.
        theta_spacing (float): The spacing between thetas.
        phi_spacing (float): The spacing between phis.
        delay (float): The delay between frames.
        """
        # Set the variables
        # screen_size: The size of the screen
        self.screen_size = screen_size
        # theta_spacing: The spacing between thetas
        self.theta_spacing = theta_spacing
        # phi_spacing: The spacing between phis
        self.phi_spacing = phi_spacing
        # illumination: The illumination of the donut
        self.illumination = np.fromiter(".,-~:;=!*#$@", dtype="<U1")
        self.A = 1
        self.B = 1
        self.R1 = 1
        self.R2 = 2
        self.K2 = 5
        self.K1 = self.screen_size * self.K2 * 3 / (8 * (self.R1 + self.R2))
        # delay: The delay between frames
        self.delay = delay

    # Get the frame to render
    def get_render_frame(self):
        """
        Calculate the frame to render.

        Returns:
        output (np.array): The frame to render.
        """
        # Get the cos and sin of A and B
        cos_A = np.cos(self.A)
        sin_A = np.sin(self.A)
        cos_B = np.cos(self.B)
        sin_B = np.sin(self.B)
        # Create the output and zbuffer
        output = np.full((self.screen_size, self.screen_size), " ")
        # zbuffer: The zbuffer of the donut
        zbuffer = np.zeros((self.screen_size, self.screen_size))
        # Get the cos and sin of phi and theta
        cos_phi = np.cos(phi := np.arange(0, 2 * np.pi, self.phi_spacing))
        # sin_phi: The sin of phi
        sin_phi = np.sin(phi)
        # Get the cos and sin of theta
        cos_theta = np.cos(theta := np.arange(0, 2 * np.pi, self.theta_spacing))
        # sin_theta: The sin of theta
        sin_theta = np.sin(theta)
        # Get the circle x and y
        circle_x = self.R2 + self.R1 * cos_theta
        # circle_y: The y of the circle
        circle_y = self.R1 * sin_theta

        # Get the x, y, and z
        x = (np.outer(cos_B * cos_phi + sin_A * sin_B * sin_phi, circle_x) - circle_y * cos_A * sin_B).T
        y = (np.outer(sin_B * cos_phi - sin_A * cos_B * sin_phi, circle_x) + circle_y * cos_A * cos_B).T
        z = ((self.K2 + cos_A * np.outer(sin_phi, circle_x)) + circle_y * sin_A).T
        # ooz: The reciprocal of z
        ooz = np.reciprocal(z)
        # xp: The x position
        xp = (self.screen_size / 2 + self.K1 * ooz * x).astype(int)
        # yp: The y position
        yp = (self.screen_size / 2 - self.K1 * ooz * y).astype(int)
        L1 = (((np.outer(cos_phi, cos_theta) * sin_B) - cos_A * np.outer(sin_phi, cos_theta)) - sin_A * sin_theta)
        L2 = cos_B * (cos_A * sin_theta - np.outer(sin_phi, cos_theta * sin_A))
        L = np.around(((L1 + L2) * 8)).astype(int).T
        mask_L = L >= 0
        # chars: The characters to use
        chars = self.illumination[L]

        # Render the frame
        for i in range(90):
            # mask: The mask
            mask = mask_L[i] & (ooz[i] > zbuffer[xp[i], yp[i]])
            # zbuffer: The zbuffer
            zbuffer[xp[i], yp[i]] = np.where(mask, ooz[i], zbuffer[xp[i], yp[i]])
            # output: The output
            output[xp[i], yp[i]] = np.where(mask, chars[i], output[xp[i], yp[i]])

        return output

    # Render the frame
    def render(self, array):
        """
        Render the frame on the console.

        Parameters:
        array (np.array): The frame to render.
        """
        # Print the array
        print(*[" ".join(row) for row in array], sep="\n")
        # Sleep
        time.sleep(self.delay)

    def save_frames_to_json(self, filename):
        """
        Save the frames to a JSON file.

        Parameters:
        filename (str): The name of the file to save.
        """
        frames = []
        for _ in range(self.screen_size * self.screen_size):
            self.A += self.theta_spacing
            self.B += self.phi_spacing
            frame = self.get_render_frame()
            # Convert the entire frame to a single string with "\n" as line separators
            frame_string = "\n".join("".join(row) for row in frame)
            frames.append(frame_string)

        # Save the frames to a JSON file
        with open(filename, 'w') as f:
            json.dump(frames, f)

    # Run the donut
    def run(self):
        """
        Run the donut animation. This method loops indefinitely.
        """
        # Run the donut
        for _ in range(self.screen_size * self.screen_size):
            # Increment A and B
            self.A += self.theta_spacing
            self.B += self.phi_spacing
            # Clear the screen
            print("\x1b[H")
            self.render(self.get_render_frame())
           
# If the file is run directly:
if __name__ == "__main__":
    # Create the donut
    donut = SpinningDonut()
    # Run the donut
    # donut.run()
    donut.save_frames_to_json("donut.json")
    print("done")