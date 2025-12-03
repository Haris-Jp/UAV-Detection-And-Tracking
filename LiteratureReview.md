# UAV-Detection-Literature-Review


This markdown contains the **literature review references and supporting materials** for the semester project:  
 **“Real-Time Drone-to-Drone Detection and Tracking using YOLOv9-M.”**  
*Course:* **Computer Vision (CS-477)**  


##  Project Summary

This study explores state-of-the-art deep learning approaches for real-time drone-to-drone detection and tracking on embedded edge devices.  
The review focuses on **YOLO-based and transformer-based** detectors optimized for **UAV vision tasks**, covering research between **2016–2025**.  

All papers are cited according to IEEE format and linked below.  
---
# Brief Summary of Each Paper

### 1. Redmon et al., 2016 — YOLO (CVPR)
Introduced the first unified end-to-end real-time object detector, performing localization and classification in a single CNN forward pass. Achieved 45 FPS, establishing the foundation for all modern YOLO variants.  
**Key Point:** First real-time one-stage detector.

---

### 2. Du et al., 2018 — UAVDT Benchmark (ECCV)
Created the UAVDT dataset containing over 80k frames for aerial detection and tracking under challenging conditions such as weather, scale variation, and camera motion.  
**Key Point:** Standard dataset for UAV detection & tracking evaluation.

---

### 3. Lyu et al., 2023 — Tiny UAV Detection (CVPRW Anti-UAV)
Proposed a lightweight convolutional detector optimized for tiny UAVs at long distances, achieving high FPS while maintaining accuracy through multi-scale feature fusion.  
**Key Point:** Fast tiny-object detection for embedded systems.

---

### 4. Yu et al., 2023 — Transformer-Based Anti-UAV Tracker (CVPRW)
Introduced a transformer-based tracker with multi-head attention for improved UAV tracking robustness during rapid motion and occlusion.  
**Key Point:** Transformer architecture for stable aerial tracking.

---

### 5. Munir et al., 2024 — UAV Detection in Complex Backgrounds (WACV)
Analyzed UAV detection performance under cluttered scenes, poor lighting, and occlusions, proposing augmentation and preprocessing strategies for robustness.  
**Key Point:** Environmental robustness analysis for UAV detection.

---

### 6. Liu et al., 2022 — MOT Meets Moving UAV (CVPR)
Enhanced multi-object tracking (MOT) to handle continuously moving UAV viewpoints by integrating trajectory modeling and temporal association techniques.  
**Key Point:** Tracking pipelines optimized for aerial camera motion.

---

### 7. Zhu et al., 2019 — VisDrone-DET2019 (ICCV Workshop)
Released a large-scale UAV dataset with 10k+ images and standardized evaluation metrics for aerial detection challenges.  
**Key Point:** Widely-used dataset for aerial object detection benchmarks.

---

### 8. Xu et al., 2023 — Survey of YOLO Series (IEEE Access)
Comprehensively reviewed YOLOv1–YOLOv9, covering architectural evolution, backbone improvements, feature aggregation, quantization, and real-time deployment challenges.  
**Key Point:** Full technical survey of all YOLO generations.

---

### 9. Tang et al., 2023 — UAV Detection Survey (Remote Sensing)
Surveyed over 150 UAV detection approaches, examining model design, dataset variety, edge-device constraints, and aerial vision challenges.  
**Key Point:** Deep UAV-focused survey highlighting embedded AI issues.

---

### 10. Hakani & Rawat, 2024 — YOLOv9 on Jetson Nano (Drones)
Implemented YOLOv9 on Jetson Nano using TensorRT, pruning, and quantization, achieving 95.7% mAP and real-time 24 FPS performance.  
**Key Point:** Real-world validation of YOLOv9 on Jetson Nano.

---

### 11. Rey et al., 2025 — YOLO on Edge Devices (Electronics)
Benchmarked YOLOv5–YOLOv8 models on edge devices, analyzing accuracy–FPS–power trade-offs and proposing configurations optimized for constrained GPU platforms.  
**Key Point:** Performance comparison of YOLO models on embedded hardware.

##  Literature Review Papers 

| # | Paper Title | Authors / Year | Venue | Link |
|:-:|--------------|----------------|--------|------|
| **1** | You Only Look Once: Unified, Real-Time Object Detection | J. Redmon, S. Divvala, R. Girshick, A. Farhadi (2016) | CVPR | [PDF](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf) |
| **2** | The Unmanned Aerial Vehicle Benchmark: Object Detection and Tracking | D. Du et al. (2018) | ECCV | [PDF](https://openaccess.thecvf.com/content_ECCV_2018/papers/Dawei_Du_The_Unmanned_Aerial_ECCV_2018_paper.pdf) |
| **3** | A Real-Time and Lightweight Method for Tiny Airborne Object Detection | Y. Lyu et al. (2023) | CVPR Workshop (Anti-UAV) | [PDF](https://openaccess.thecvf.com/content/CVPR2023W/Anti-UAV/papers/Lyu_A_Real-Time_and_Lightweight_Method_for_Tiny_Airborne_Object_Detection_CVPRW_2023_paper.pdf) |
| **4** | A Unified Transformer Based Tracker for Anti-UAV Tracking | Q. Yu et al. (2023) | CVPR Workshop (Anti-UAV) | [PDF](https://openaccess.thecvf.com/content/CVPR2023W/Anti-UAV/papers/Yu_A_Unified_Transformer_Based_Tracker_for_Anti-UAV_Tracking_CVPRW_2023_paper.pdf) |
| **5** | Investigation of UAV Detection in Images With Complex Backgrounds | A. Munir et al. (2024) | WACV | [PDF](https://arxiv.org/abs/2305.16450) |
| **6** | Multi-Object Tracking Meets Moving UAV | J. Liu et al. (2022) | CVPR | [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Liu_Multi-Object_Tracking_Meets_Moving_UAV_CVPR_2022_paper.pdf) |
| **7** | VisDrone-DET2019: The Vision Meets Drone Object Detection Challenge | Z. Zhu et al. (2019) | ICCV Workshop (VisDrone) | [PDF](https://openaccess.thecvf.com/content_ICCVW_2019/papers/VISDrone/Du_VisDrone-DET2019_The_Vision_Meets_Drone_Object_Detection_in_Image_Challenge_ICCVW_2019_paper.pdf) |
| **8** | A Survey of the YOLO Series of Object Detection Algorithms | J.-H. Xu, J.-P. Li, Z.-R. Zhou, Q. Lv, J. Luo (2023) | IEEE Access | [IEEE Link](https://ieeexplore.ieee.org/document/10235612) |
| **9** | A Survey of Object Detection for UAVs Based on Deep Learning | L. Tang et al. (2023) | Remote Sensing | [PDF](https://www.mdpi.com/2072-4292/16/1/149) |
| **10** | Edge Computing-Driven Real-Time Drone Detection Using YOLOv9 and Jetson Nano | R. Hakani, A. Rawat (2024) | Drones | [PDF](https://www.mdpi.com/2504-446X/8/11/680) |
| **11** | Performance Analysis of YOLO Models for Constrained Edge Devices in Drone Applications | L. Rey et al. (2025) | Electronics | [PDF](https://www.mdpi.com/2079-9292/14/3/638) |


