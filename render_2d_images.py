import os
     import torch
     import numpy as np
     from PIL import Image
     from nerf.utils import Trainer, render_image
     from nerf.provider import NeRFProvider

     def render_2d_views(workspace, num_views=8):
         # Load trained model
         provider = NeRFProvider()
         trainer = Trainer('ngp', provider, opt=None)
         checkpoint = os.path.join(workspace, 'checkpoints', 'df.pth')
         trainer.load_checkpoint(checkpoint)

         # Define camera angles
         angles = np.linspace(0, 360, num_views, endpoint=False)
         os.makedirs(os.path.join(workspace, 'renders'), exist_ok=True)

         for i, angle in enumerate(angles):
             # Set camera pose (azimuth angle)
             pose = np.array([
                 [np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle)), 0, 0],
                 [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle)), 0, 0],
                 [0, 0, 1, 2.0],
                 [0, 0, 0, 1]
             ])
             image = render_image(trainer.model, pose, H=800, W=800)
             image = (image * 255).astype(np.uint8)
             Image.fromarray(image).save(os.path.join(workspace, 'renders', f'view_{i}.png'))

     if __name__ == "__main__":
         render_2d_views('trial')