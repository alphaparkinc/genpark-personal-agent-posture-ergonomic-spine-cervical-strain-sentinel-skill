# -*- coding: utf-8 -*-
"""Posture Ergonomic Cervical Spine Strain Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class PostureErgonomicCervicalStrainSentinel:
    @staticmethod
    def calculate_cervical_spine_load(forward_tilt_angle_degrees: float, head_weight_lbs: float = 12.0) -> Dict[str, Any]:
        # Hansraj biomechanical spine model: 0 deg = 12 lbs, 15 deg = 27 lbs, 30 deg = 40 lbs, 45 deg = 49 lbs, 60 deg = 60 lbs
        angle = min(60.0, max(0.0, forward_tilt_angle_degrees))
        effective_load_lbs = round(head_weight_lbs + (48.0 * (angle / 60.0) ** 1.15), 1)
        strain_multiplier = round(effective_load_lbs / head_weight_lbs, 1)
        return {"forward_tilt_deg": angle, "effective_cervical_load_lbs": effective_load_lbs, "strain_multiplier": strain_multiplier, "risk_tier": "HIGH_COMPRESSIVE_FATIGUE" if angle >= 30 else "OPTIMAL_ALIGNMENT"}

    @staticmethod
    def generate_cervical_micro_reset_routine(hours_seated_continuous: float) -> Dict[str, Any]:
        return {"hours_seated": hours_seated_continuous, "routine": ["Cervical Retraction (Chin Tucks) 10 reps holding 3s", "Thoracic Spine Extension over chair backrest", "Scapular Retraction and Wall Angels 15 reps"], "advisory": "Raise monitor top edge to eyebrow height to zero out forward cervical pitch."}
