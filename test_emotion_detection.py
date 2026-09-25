"""Unit tests for the emotion detector."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test dominant emotion detection for representative statements."""

    def test_dominant_emotions(self):
        """Verify the dominant emotion for five clearly coded statements."""
        expected_emotions = {
            "I am joyful and delighted.": "joy",
            "I am furious and enraged.": "anger",
            "That disgusting rotten food makes me nauseous.": "disgust",
            "I am heartbroken and deeply sad.": "sadness",
            "I am terrified and afraid.": "fear",
        }

        def fake_post(_url, **_kwargs):
            statement = _kwargs["json"]["raw_document"]["text"]
            scores = {
                emotion: 0.01 for emotion in (
                    "anger", "disgust", "fear", "joy", "sadness"
                )
            }
            scores[expected_emotions[statement]] = 0.95
            response = Mock()
            response.status_code = 200
            response.json.return_value = {
                "emotionPredictions": [{"emotion": scores}]
            }
            return response

        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            side_effect=fake_post,
        ):
            for statement, expected in expected_emotions.items():
                with self.subTest(statement=statement):
                    self.assertEqual(
                        emotion_detector(statement)["dominant_emotion"],
                        expected,
                    )


if __name__ == "__main__":
    unittest.main()
