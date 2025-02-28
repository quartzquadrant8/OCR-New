import unittest
from google.auth.exceptions import DefaultCredentialsError
from google.cloud import vision

class TestGoogleVisionAPI(unittest.TestCase):

    def test_key_access_permissions(self):
    
        try:
            client = vision.ImageAnnotatorClient()
          
            with open('image.jpg', 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)

            response = client.text_detection(image=image)
            self.assertIsNotNone(response, "Failed to authenticate with Google Cloud Vision API.")
            print("API key access permissions confirmed.")
        except DefaultCredentialsError:
            self.fail("Failed to authenticate with Google Cloud Vision API. Check your credentials.")
        except Exception as e:
            self.fail(f"Unexpected error during authentication: {e}")

    def test_google_vision_access(self):
        """Test to confirm access mechanism to Google Vision API is functional."""
        try:
            client = vision.ImageAnnotatorClient()
           
            with open('image.jpg', 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = client.text_detection(image=image)
            self.assertIsNotNone(response, "Google Vision API request failed.")
            print("Google Vision API request access confirmed.")
        except Exception as e:
            self.fail(f"Google Vision API access failed: {e}")

if __name__ == '__main__':
    unittest.main()
