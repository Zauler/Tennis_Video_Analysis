# Tennis_Video_Analysis

This project focuses on developing an AI-powered system to track tennis players and the ball on the court. Leveraging advanced technologies such as YOLO for object detection, OpenCV for computer vision tasks, and PyTorch for deep learning models, this system provides comprehensive analysis and visualization for tennis matches.

## Features

### Video Input
- Reads input videos of tennis matches for processing and analysis.

### Player and Ball Detection
- **Player Detection:** Utilizes a pre-trained YOLOv8x model to detect players in each frame of the video.
- **Ball Detection:** Employs a model specifically trained to detect the tennis ball.
- **Interpolation:** Interpolates ball positions to maintain smooth tracking even when the ball is not visible in some frames.

### Court Line Detection
- Detects court lines and key points using a custom-trained model, providing essential reference points for accurate tracking.

### Mini-Court Visualization
- Converts the positions of players and the ball to a simplified 2D mini-court representation for clear visualization.

### Statistics Calculation
- Computes various statistics, including:
  - Shot speed for each player
  - Player movement speed
  - Number of shots made by each player

### Visualization
- Draws bounding boxes around players and the ball.
- Displays court keypoints on the video.
- Shows player and ball positions on a mini-court.
- Annotates the video with player statistics and frame numbers.

## Technologies Used
- **YOLO**: For player and ball detection.
- **OpenCV**: For computer vision tasks.
- **PyTorch**: For implementing deep learning models.
- **Pandas**: For managing and processing player statistics.
