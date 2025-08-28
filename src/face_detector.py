import cv2
import numpy
import matplotlib.pyplot as plt

class FaceDetector:
    
    def __init__(self) -> None:
        self.cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # type: ignore
    
    def get_img_meta(self, image: numpy.ndarray):
        """
        Return metadata for the image image
        
        Args:
            **image** - Image file as a numpy ndarray 
        """
        cv2_img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        if image is None or cv2_img is None:
            return None
        
        im_shape = cv2_img.shape
        
        return {
            "height": im_shape[0],
            "width": im_shape[1] if len(im_shape) > 1 else 1,
            "channels": im_shape[2] if len(im_shape) > 2 else 1,
            "compressed_size_bytes": len(image),
            "uncompressed_size_bytes": cv2_img.nbytes,
            "aspect_ratio": (im_shape[1] / im_shape[0]) if len(im_shape) > 1 and im_shape[0] != 0 else None,
        }
        