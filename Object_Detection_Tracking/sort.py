from filterpy.kalman import KalmanFilter
import numpy as np

class Sort:
    def __init__(self):
        self.trackers = []
        self.track_id = 0

    def update(self, detections):
        results = []
        for det in detections:
            x1, y1, x2, y2 = det
            results.append([x1, y1, x2, y2, self.track_id])
            self.track_id += 1
        return results
